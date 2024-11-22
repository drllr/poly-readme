# Poly-README

Poly-README is a command-line tool that automatically translates your README.md files into multiple languages using OpenAI's GPT-3.5-turbo model.

## Features

- Automatic translation of README.md files
- Support for multiple target languages
- Simple command-line interface
- Maintains markdown formatting
- Uses OpenAI's GPT-3.5-turbo for high-quality translations

## Installation

```bash
pip install poly-readme
```

## Prerequisites

Before using Poly-README, you need to:

1. Have an OpenAI API key
2. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Basic usage to translate your README.md:

```bash
poly-readme translate --lang ko  # Translates to Korean
```

Available language codes:

- `ko`: Korean
- `ja`: Japanese
- `zh`: Chinese
- And more...

The translated file will be saved as `README_{LANG}.md` in your current directory.

## Example

If you run:

```bash
poly-readme translate --lang ko
```

Your `README.md` will be translated to Korean and saved as `README_KO.md`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Chad Lee
- Email: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Acknowledgments

- This tool uses OpenAI's GPT-3.5-turbo model for translations
