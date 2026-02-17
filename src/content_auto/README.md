# APAC Lead Magnet Auto-Generator

AI 기반 멀티 에이전트 시스템으로 매일 자동으로 APAC 커머스/물류 전문가를 위한 리드 마그넷 3개를 생성하여 Google Docs로 전달합니다.

## 주요 기능

- **자동 스케줄링**: 매일 오전 7시 GMT에 자동 실행
- **멀티 에이전트**: Research → Content Writing → QA/Publishing 파이프라인
- **다국어 지원**: 한글 1개 + 영어 2개 자동 생성
- **Google Docs 통합**: 완성된 리드 마그넷을 Google Docs로 자동 업로드
- **Claude 스킬 시스템**: 재사용 가능한 4개 스킬 활용

## 타겟 오디언스

- **지역**: APAC (한국, 베트남, 인도네시아, 싱가포르 등)
- **산업**: 이커머스, D2C, 물류, 크로스보더 커머스
- **직무**: 전략 담당자, 임원, 파트너십 세일즈

## 설치

```bash
# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate    # Windows

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일에 API 키 입력
```

## Google Docs API 설정

1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 새 프로젝트 생성
3. Google Docs API 활성화
4. OAuth 2.0 클라이언트 ID 생성
5. `credentials.json` 다운로드하여 프로젝트 루트에 저장

## 실행

### 수동 실행 (테스트용)
```bash
python main.py --run-now
```

### 스케줄러 실행 (매일 자동)
```bash
python main.py --schedule
```

### 특정 날짜에 생성
```bash
python main.py --run-now --date 2025-01-15
```

## 아키텍처

```
Scheduler → Orchestrator (LangGraph)
              ├─ Research Agent (리서치)
              ├─ Content Writer Agent (콘텐츠 작성)
              └─ QA Editor Agent (검수 + 퍼블리싱)
```

### 3개 에이전트

1. **Research Agent**: APAC 커머스/물류 트렌드 리서치
2. **Content Writer Agent**: 3개 리드 마그넷 작성 (한글 1, 영어 2)
3. **QA Editor Agent**: 팩트 체크 및 Google Docs 퍼블리싱

### 4개 Claude 스킬

- `research-apac-trends`: 트렌드 리서치
- `structure-lead-magnet`: 콘텐츠 구조화
- `fact-check-content`: 팩트 체크
- `design-google-doc`: Google Docs 서식 적용

## 프로젝트 구조

```
.
├── .claude/skills/          # Claude 스킬
├── agents/                  # 3개 에이전트
├── orchestrator/            # LangGraph 워크플로우
├── config/                  # 설정
├── utils/                   # 유틸리티
├── main.py                  # 메인 스크립트
└── CLAUDE.md               # Claude Code 가이드
```

## 라이선스

MIT
