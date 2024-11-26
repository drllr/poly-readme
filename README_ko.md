# Poly-README

Poly-README는 OpenAI의 GPT-4 모델을 사용하여 README.md 파일을 여러 언어로 자동 번역하는 커맨드라인 도구입니다.

## 기능

- README.md 파일의 자동 번역
- 여러 대상 언어 지원
- 간단한 커맨드라인 인터페이스
- 마크다운 포맷 유지
- OpenAI의 GPT-4를 사용한 고품질 번역
- 시스템 키링을 통한 안전한 API 키 관리
- YAML을 통한 프로젝트 수준 구성
- 번역 중 진행 상황 표시
- 사용자 지정 출력 파일명 패턴 지원

## 설치

```bash
pip install poly-readme
```

## 필수 조건

Poly-README를 사용하기 전에, 다음이 필요합니다:

1. OpenAI API 키를 보유
2. 다음 중 하나를 수행:
   - OpenAI API 키를 환경 변수로 설정:
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - 또는 CLI를 사용하여 안전하게 설치:
     ```bash
     poly-readme install
     ```

## 사용법

### 초기 설정

프로젝트 설정을 구성하세요:

```bash
poly-readme setup
```

이 과정에서는 다음을 안내합니다:

- 소스 README 파일 위치 설정
- 번역 대상 언어 선택
- 출력 파일명 패턴 구성

### 번역

프로젝트 구성에 따라 README를 번역합니다:

```bash
poly-readme translate
```

### 사용 가능한 언어 코드

- `ko`: 한국어
- `ja`: 일본어
- `zh`: 중국어 (간체)
- `es`: 스페인어
- `fr`: 프랑스어
- `de`: 독일어
- `it`: 이탈리아어
- `pt`: 포르투갈어
- `ru`: 러시아어
- `ar`: 아랍어
- `vi`: 베트남어

번역된 파일은 설정된 패턴에 따라 저장됩니다 (기본 값: `README_{lang}.md`).

## 명령어

- `poly-readme install` - OpenAI API 키 설정
- `poly-readme setup` - 프로젝트 설정 구성
- `poly-readme translate` - README 파일 번역
- `poly-readme help [command]` - 도움말 정보 표시

## 기여

기여는 환영합니다! Pull Request를 제출해 주세요.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다 - 자세한 내용은 LICENSE 파일을 참조하세요.

## 저자

- Chad Lee
- 이메일: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## 감사의 말

- 이 도구는 OpenAI의 GPT-4 모델을 사용하여 번역을 수행합니다.