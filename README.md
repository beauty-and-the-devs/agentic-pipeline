# agentic-pipeline

AI 에이전트를 구성하고 실행하기 위한 파이프라인을 관리하는 프로젝트입니다.

## run
```bash
conda activate amore-agent
cd ./agentic-pipeline
python3 -m src.app

```

## environments
- Ubuntu 24.02 LTS
- Python 3.12(conda)

### Library
- requirements.txt 참고
  ```
  langgraph>=0.2.0
  langchain>=0.2.0
  langchain-core>=0.2.0
  langchain-openai>=0.2.0
  pyyaml>=6.0.1
  python-dotenv>=1.0.1
  requests>=2.32.0
  ```

## 폴더 구조

- `output/`
  - 파이프라인 실행 결과(산출물/로그)가 저장됩니다.
  - 기본적으로 실행 시점 기준 run id로 하위 폴더가 생성됩니다. (예: `output/run_20260102_235959/`)
  - 생성 파일 예시:
    - `run.log`: 실행 로그
    - `input_data.json`: 이번 실행에 사용된 입력 데이터 스냅샷
    - `insight_report.md`
    - `product_report.md`
    - `product_review.json`
    - `plot_report.md`
    - `marketing_videos.json`
    - `final_state.json`: 파이프라인 최종 state
  - `RUN_ID` 환경변수로 폴더명을 고정할 수 있습니다.

- `resources/`
  - `test/`
    - `input_data.json`: 테스트용 더미 입력 데이터(수집 데이터)
  - `prompt/`
    - 각 agent의 Prompt(프롬프트)들이 저장되어 있습니다.
    - 실행 시 필요한 prompt를 이 폴더에서 불러와(agent가 참조할 프롬프트를 로드하여) 각 agent의 task(업무/역할)를 정의합니다.
    - 세 개의 process들이 폴더로 구분되어 있고, 해당하는 프로세스의 각 Agent들의 task가 정의되어 있습니다.
    - `insight_process/`: 인사이트 도출 단계(DataExtractAgent → InsightGeneratorAgent)
    - `product_develop/`: 제품 기획/개발 보고서 단계(ProductDevelopAgent → ProductReviewAgent)
    - `marketing_contents/`: 마케팅 콘텐츠 단계(PlotGeneratorAgent → MarketingVideoGeneratorAgent)

  - `spec/`
    - 모델 스펙(LLM 설정) YAML이 저장됩니다.
    - `model_spec.yml`: `text_gen`, `video_gen`로 구분하여 모델/temperature 등의 설정을 관리합니다.

- `src/`
  - 파이프라인 실행 코드 및 agent 구현이 위치합니다.
  - `app.py`: 전체 파이프라인을 순차 실행하는 엔트리 포인트(샘플 입력 포함)
  - `pipelines.py`: 프로세스별 실행 함수와 상태(state) 정의
    - insight_process, product_develop(+review loop), marketing_contents 단계 함수 포함
  - `pipelines_graph.py`: LangGraph(StateGraph) 기반으로 동일 순서의 앱 그래프 구성
  - `agent/`: 개별 agent 구현
    - `_base.py`: prompt/model spec 로딩 및 LLM(OpenRouter) 생성 공통 유틸
    - `*Agent.py`: 각 prompt YAML(=`resources/prompt/**`)을 로드해 실행하는 agent 클래스

- `tests/`
  - 간단한 호출/연동 테스트가 위치합니다.

## logs
- [2026.01.03. Sat] - yonghwan.lee: 전체 파이프라인의 기본 베이스 테스트
- [2026.01.03. Sat] - yonghwan.lee: 전체 파이프라인의 기본 베이스 정의
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