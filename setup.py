from setuptools import setup, find_packages

setup(
    name='poly-readme',  # 패키지 이름
    version='0.1.0',  # 패키지 버전
    description='Automatically translate README.md into multiple languages using LLMs.',  # 패키지 설명
    author='Chad Lee',  # 작성자 이름
    author_email='think.bicycle@gmail.com',  # 작성자 이메일
    url='https://github.com/drllr/poly-readme',  # GitHub URL
    packages=find_packages(where="src"),  # src 디렉토리 내에서 패키지 찾기
    package_dir={"": "src"},  # src 디렉토리를 패키지 루트로 지정
    install_requires=[
        'openai>=1.0.0',
        'questionary>=1.10.0',
        'keyring>=24.0.0',
        'PyYAML>=6.0.0',
    ],
    entry_points={
        'console_scripts': [
            'poly-readme=poly_readme.cli:main',  # CLI 명령어와 엔트리 포인트 매핑
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # 최소 Python 버전
)
