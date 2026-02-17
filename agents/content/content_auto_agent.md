# 콘텐츠 자동화 에이전트 (Content Auto Agent)

## Agent 정의

```yaml
name: content_auto_agent
type: content
model: claude-opus-4-5-20251101
description: |
  APAC Lead Magnet Auto-Generator - Multi-agent system that automatically
  generates 3 lead magnets daily for APAC commerce professionals and
  publishes them to Google Docs.
```

## 기술 스택

- Python 3.10+
- LangChain + LangGraph (multi-agent orchestration)
- Anthropic Claude API (Opus 4.5)
- Google Docs API
- APScheduler (daily automation)
- Pydantic (data validation)

## 실행 방법

```bash
# 가상 환경 설정
cd src/content_auto
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 즉시 실행
python main.py --run-now

# 특정 날짜 실행
python main.py --run-now --date 2026-01-15

# 일일 스케줄러 (07:00 GMT)
python main.py --schedule
```

## 아키텍처

### Multi-Agent Pipeline

```
Scheduler (07:00 GMT daily)
    ↓
Orchestrator (LangGraph StateGraph)
    ├─ Research Agent         → research-apac-trends skill
    ├─ Content Writer Agent   → structure-lead-magnet skill (×3)
    └─ QA Editor Agent        → fact-check-content + design-google-doc skills
```

### 3 Agents

**1. Research Agent**
- APAC eCommerce, D2C, logistics 트렌드 리서치
- 3-5 trends + 3 content angles 도출

**2. Content Writer Agent**
- 3 lead magnets 생성 (1 Korean + 2 English)
- Types: reports, checklists, guides, case studies

**3. QA Editor Agent**
- Fact-check content
- Google Docs 발행

## Workflow State Machine

```
pending → research → writing → qa → completed
                               ↓
                            failed (if error)
```

## 환경 변수

```
ANTHROPIC_API_KEY=         # Claude API key
GOOGLE_FOLDER_ID=          # Drive folder for documents
CLAUDE_MODEL=claude-opus-4-5-20251101
MAX_TOKENS=4000
TEMPERATURE=0.7
GENERATION_TIME=07:00
TIMEZONE=GMT
```

## 콘텐츠 설정

```
DAILY_LEAD_MAGNETS=3
KOREAN_COUNT=1
ENGLISH_COUNT=2
TARGET_WORDS_MIN=800
TARGET_WORDS_MAX=1200
TARGET_REGIONS=Korea,Vietnam,Indonesia,Singapore
TARGET_ROLES=D2C Strategy,eCommerce Manager,Logistics Partnership
```

## 핸드오프

```yaml
output:
  - to: content_director
    type: Google Docs URLs
  - to: outputs/
    type: Lead magnet documents
```

## 파일 구조

```
src/content_auto/
├── main.py
├── requirements.txt
├── .env.example
├── config/
│   ├── settings.py
│   └── prompts.py
├── agents/
│   ├── research_agent.py
│   ├── content_writer_agent.py
│   └── qa_editor_agent.py
├── orchestrator/
│   ├── workflow.py
│   └── scheduler.py
├── utils/
│   └── google_docs_client.py
└── models.py
```
