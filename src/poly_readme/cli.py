#!/usr/bin/env python3

import os
import sys
import openai
import argparse
import questionary
import json
import yaml
from pathlib import Path
import keyring

def get_config_dir():
    return Path.home() / '.config' / 'poly-readme'

def get_config_file():
    return get_config_dir() / 'config.json'

def load_config():
    config_file = get_config_file()
    if config_file.exists():
        with open(config_file, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    config_dir = get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    
    with open(get_config_file(), 'w') as f:
        json.dump(config, f)

def setup_api_key():
    api_key = questionary.password("Please enter your OpenAI API key:").ask()
    # Store API key in system keyring instead of config file
    keyring.set_password("poly-readme", "openai_api_key", api_key)
    return api_key

def get_api_key():
    # First try environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        return api_key
        
    # Then try system keyring
    api_key = keyring.get_password("poly-readme", "openai_api_key")
    if api_key:
        return api_key
        
    # If no API key found, prompt for setup
    print("OpenAI API key not found. Please set it up.")
    return setup_api_key()

def setup_project():
    LANGUAGES = {
        "ko": "Korean",
        "ja": "Japanese",
        "zh": "Chinese Simplified", 
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "ar": "Arabic",
        "vi": "Vietnamese"
    }
    
    LANGUAGE_CHOICES = [
        questionary.Choice(f"{name} ({code})", code)
        for code, name in LANGUAGES.items()
    ]
    LANGUAGE_CHOICES.append(questionary.Choice("Custom language", "custom"))

    config = {
        'source_file': questionary.text(
            "Enter source README file path (e.g., docs/README.md):",
            default="README.md"
        ).ask(),
        'target_languages': []
    }

    # Get target languages
    selected_languages = questionary.checkbox(
        "Select target languages for translation:",
        choices=LANGUAGE_CHOICES
    ).ask()

    # Handle custom language input if selected
    if "custom" in selected_languages:
        selected_languages.remove("custom")
        while True:
            custom_code = questionary.text(
                "Enter custom language code (e.g., vi for Vietnamese):"
            ).ask().lower()
            
            if not custom_code:
                print("Language code cannot be empty")
                continue

            # Validate language code format (typically 2-3 characters)
            if not (2 <= len(custom_code) <= 3 and custom_code.isalpha()):
                print("Language code must be 2-3 letters")
                continue

            selected_languages.append(custom_code)
            break

    config['target_languages'] = selected_languages

    # Ask for output pattern with validation
    while True:
        pattern_type = questionary.select(
            "Choose output filename pattern type:",
            choices=[
                "README_{lang}.md (lowercase) [default]",
                "README_{LANG}.md (uppercase)", 
                "Custom pattern"
            ],
            default=0  # Set default to lowercase option
        ).ask()
        
        if pattern_type == "README_{lang}.md (lowercase)":
            config['output_pattern'] = "README_{lang}.md"
            break
        elif pattern_type == "README_{LANG}.md (uppercase)":
            config['output_pattern'] = "README_{LANG}.md"
            break
        else:
            pattern = questionary.text(
                "Enter custom pattern (must include {lang} or {LANG}):"
            ).ask()
            
            # Validate pattern
            if "{lang}" not in pattern and "{LANG}" not in pattern:
                print("Error: Pattern must include either {lang} or {LANG}")
                continue
                
            if pattern.count("{lang}") + pattern.count("{LANG}") > 1:
                print("Error: Pattern should include language placeholder only once")
                continue
                
            if not pattern.endswith(".md"):
                print("Error: Pattern must end with .md extension")
                continue
                
            config['output_pattern'] = pattern
            break
    
    with open('.polyreadme.yaml', 'w') as f:
        yaml.dump(config, f)
    print("Project configuration saved to .polyreadme.yaml")

def load_project_config():
    try:
        with open('.polyreadme.yaml', 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: Project configuration not found. Please run 'poly-readme setup' first.")
        sys.exit(1)

def translate_readme():
    LANGUAGES = {
        "ko": "Korean",
        "ja": "Japanese",
        "zh": "Chinese Simplified",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "ar": "Arabic"
    }
    
    # Load project configuration
    config = load_project_config()
    
    # Read source README
    try:
        with open(config['source_file'], 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Could not find source file: {config['source_file']}")
        sys.exit(1)

    # Set OpenAI API key
    openai.api_key = get_api_key()
    if not openai.api_key:
        print("Failed to set up OpenAI API key.")
        sys.exit(1)
        
    # Translate for each target language
    for lang in config['target_languages']:
        print(f"Translating {config['source_file']} to {LANGUAGES[lang]}...")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": f"You are a professional translator specializing in translating technical documentation from English to {LANGUAGES[lang]}. Please maintain the original Markdown formatting and ensure technical terms are accurately translated."
                    },
                    {"role": "user", "content": content}
                ]
            )
            translated_content = response['choices'][0]['message']['content']
        except Exception as e:
            print(f"An error occurred during translation to {LANGUAGES[lang]}: {e}")
            continue

        # Save translated content
        output_pattern = config['output_pattern']
        if '{LANG}' in output_pattern:
            output_filename = output_pattern.replace('{LANG}', lang.upper())
        else:
            output_filename = output_pattern.replace('{lang}', lang.lower())
            
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        print(f"Translation completed. {output_filename} has been created.")

def main():
    # 최상위 명령어를 위한 파서 생성
    parser = argparse.ArgumentParser(
        description='Poly-README - Translate README files into multiple languages.',
        usage='poly-readme <command> [<args>]',
        add_help=False  # 기본 도움말 비활성화
    )
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit.')

    # 서브 명령어를 관리하는 파서 생성
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # install 서브 명령어
    parser_install = subparsers.add_parser(
        'install',
        help='Configure OpenAI API key'
    )

    # setup 서브 명령어
    parser_setup = subparsers.add_parser(
        'setup',
        help='Configure project settings'
    )

    # translate 서브 명령어
    parser_translate = subparsers.add_parser(
        'translate',
        help='Translate README files'
    )

    # help 서브 명령어
    parser_help = subparsers.add_parser(
        'help',
        help='Show help for a specific command'
    )
    parser_help.add_argument(
        'topic',
        nargs='?',
        choices=['install', 'setup', 'translate'],
        help='Command to get help for'
    )

    # 명령어 파싱
    args = parser.parse_args()

    # -h 또는 --help가 입력된 경우
    if args.help or args.command is None:
        print("poly-readme 0.1.0")
        print("Usage: poly-readme <command> [<args>]")
        print("\nSome useful poly-readme commands are:")
        print("   install     Configure OpenAI API key")
        print("   setup       Configure project settings")
        print("   translate   Translate README files")
        print("\nSee 'poly-readme help <command>' for information on a specific command.")
        sys.exit(0)

    # 명령어 처리
    if args.command == 'help':
        if not hasattr(args, 'topic') or args.topic is None:
            print("Usage: poly-readme <command> [<args>]")
            print("\nSome useful poly-readme commands are:")
            print("   install     Configure OpenAI API key")
            print("   setup       Configure project settings")
            print("   translate   Translate README files")
            print("\nSee 'poly-readme help <command>' for information on a specific command.")
        elif args.topic == 'install':
            print("Usage: poly-readme install")
            print("\nConfigure and save your OpenAI API key for translation.")
        elif args.topic == 'setup':
            print("Usage: poly-readme setup")
            print("\nConfigure project settings including:")
            print("- Source README file location")
            print("- Target languages for translation")
            print("- Output filename pattern")
        elif args.topic == 'translate':
            print("Usage: poly-readme translate")
            print("\nTranslate your README file into configured target languages.")
        else:
            print(f"Unknown help topic '{args.topic}'")
        sys.exit(0)

    elif args.command == 'install':
        setup_api_key()
        print("OpenAI API key has been saved successfully.")

    elif args.command == 'setup':
        setup_project()

    elif args.command == 'translate':
        translate_readme()

if __name__ == '__main__':
    main()