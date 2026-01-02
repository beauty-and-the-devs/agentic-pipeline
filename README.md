# agentic-pipeline

AI 에이전트를 구성하고 실행하기 위한 파이프라인을 관리하는 프로젝트입니다.

## 폴더 구조

- `resources/`
  - `prompt/`
    - 각 agent의 Prompt(프롬프트)들이 저장되어 있습니다.
    - 실행 시 필요한 prompt를 이 폴더에서 불러와(agent가 참조할 프롬프트를 로드하여) 각 agent의 task(업무/역할)를 정의합니다.
    - 세 개의 process들이 폴더로 구분되어 있고, 해당하는 프로세스의 각 Agent들의 task가 정의되어 있습니다.

## logs
- [2026.01.02. Fri] - yonghwan.lee: AI Agent의 resources/prompt 각 prompt 정의
- [2026.01.02. Fri] - yonghwan.lee: AI Agent의 resources/prompt default files 생성

## VERSION
- 버전 정보는 VERSION 파일에 정의되어 있습니다.
- 버전 정의는 아래와 같습니다.(예: 1.0.0.1)
    - 첫 번째 숫자: 전체 기획 변경 시, 1 up (단, 기본적으로 1부터 시작)
    - 두 번째 숫자: 주요 기능 변경 시, 1 up
    - 세 번째 숫자: 일상적 기능 변경 시, 1 up
    - 네 번째 숫자: hot-fix 변경 시, 1 up (단, 기본적으로 1부터 시작)
    - dev: 이슈 넘버가 가장 처음 등장(#1 -> 1), 그 후에는 0001부터 시작
        - 제일 처음에는 dev10001과 같이 정의
        - commit 마다 dev10002, dev10003으로 정의
        - 새로운 feature가 열리면 이슈 넘버 증가 -> dev20001 등으로 정의