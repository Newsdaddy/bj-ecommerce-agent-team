# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

BJ 이커머스 사단 - Claude Code 멀티 에이전트 워크스페이스

## 개요

이커머스 데이터 SaaS(ECDB)의 B2B 세일즈를 위한 병렬 에이전트 시스템.

- **최종 목표**: €15,000 상당의 연간 계약 체결
- **작업 언어**: 한국어 (별도 지시 없는 한)
- **최종 산출물**: `outputs/`에 저장

## 에이전트 구조

```
총괄 실장 (general_manager)                          ← Task 기반 오케스트레이션
│
├── 세일즈 디렉터 (sales_director)                   ← 아웃바운드 파이프라인
│   │
│   ├── [컨트리 매니저 8개]
│   │   ├── CM Korea (cm_korea)                     ← 한국 (3명/일)
│   │   ├── CM Japan (cm_japan)                     ← 일본 (3명/일)
│   │   ├── CM Indonesia (cm_indonesia)             ← 인도네시아 (3명/일) ⭐고성장
│   │   ├── CM Vietnam (cm_vietnam)                 ← 베트남 (3명/일) ⭐고성장
│   │   ├── CM Philippines (cm_philippines)         ← 필리핀 (2명/일) ⭐최고성장률
│   │   ├── CM India (cm_india)                     ← 인도 (2명/일)
│   │   ├── CM SEA Emerging (cm_sea_emerging)       ← 태국+말레이 (1명/일)
│   │   └── CM ANZ (cm_anz)                         ← 호주+뉴질랜드 (1명/일)
│   │
│   ├── 메시지 쓰기_한글 (message_writer_ko)
│   └── 메시지 쓰기_영어 (message_writer_en)
│
└── 콘텐츠 디렉터 (content_director)                 ← 인바운드 콘텐츠 + CM 협업
    ├── 콘텐츠 자동화 (content_auto_agent)           ← LangGraph 시스템
    ├── 콘텐츠 에디터 (content_editor)               ← 김훈/Justin Welsh 문체
    ├── 콘텐츠 구조화 (content_structurer)
    ├── 팩트체커 (fact_checker)
    ├── 조사원1 (researcher_region1)
    ├── 조사원2 (researcher_region2)
    ├── 조사원3 (researcher_region3)
    ├── 레이아웃 디자이너 (layout_designer)          ← 카드뉴스 레이아웃 🆕
    └── 테마 디자이너 (theme_designer)               ← 카드뉴스 디자인 시스템 🆕

사외 이사 (outside_director)                         ← 전략 자문, 비판적 관점
```

## 디렉토리 구조

```
BJ 이커머스 사단/
├── CLAUDE.md                    ← 마스터 (현재 파일)
├── agents/                      ← 에이전트 역할 정의
│   ├── strategic/               ← 전략급
│   │   ├── outside_director.md
│   │   └── general_manager.md
│   ├── sales/                   ← 세일즈 (CM 8개 + 메시지 쓰기 2개)
│   │   ├── sales_director.md
│   │   ├── cm_korea.md
│   │   ├── cm_japan.md
│   │   ├── cm_indonesia.md
│   │   ├── cm_vietnam.md
│   │   ├── cm_philippines.md
│   │   ├── cm_india.md
│   │   ├── cm_sea_emerging.md
│   │   ├── cm_anz.md
│   │   ├── message_writer_ko.md
│   │   └── message_writer_en.md
│   └── content/                 ← 콘텐츠
│       ├── content_director.md
│       ├── content_auto_agent.md
│       ├── content_editor.md
│       ├── content_structurer.md
│       ├── fact_checker.md
│       ├── researcher_region1.md
│       ├── researcher_region2.md
│       ├── researcher_region3.md
│       ├── layout_designer.md   ← 카드뉴스 레이아웃 🆕
│       └── theme_designer.md    ← 카드뉴스 테마 🆕
├── knowledge/                   ← 공유 지식
│   ├── regions.md               ← 권역 정의
│   ├── ecdb_product.md          ← SaaS 제품
│   ├── style_guide_ko.md        ← 김훈 문체
│   ├── style_guide_en.md        ← Justin Welsh 문체
│   ├── thread_writing_templates_josh.md  ← 스레드 글쓰기 11 템플릿
│   └── fact_check_sources.md    ← 검증 출처 100+
├── workflows/                   ← 파이프라인 정의
│   ├── content_pipeline.md
│   ├── sales_pipeline.md
│   ├── handoff_rules.md
│   ├── content_sales_collaboration.md  ← CM-콘텐츠 협업
│   └── cardnews_pipeline.md     ← 카드뉴스 제작 🆕
├── docs/                        ← 문서
│   └── country_manager_plan.md  ← CM 구조 계획
├── outputs/                     ← 최종 산출물
│   ├── linkedin/
│   ├── x/
│   ├── substack/
│   ├── sales/
│   ├── reports/
│   ├── scripts/
│   └── cardnews/                ← 카드뉴스 PNG 🆕
├── workspace/                   ← 작업 중 파일
│   ├── research/
│   ├── verified/
│   ├── outlines/
│   ├── drafts/
│   ├── leads/
│   ├── messages/
│   └── cardnews/                ← 카드뉴스 작업 🆕
│       ├── themes/              ← 테마 YAML/CSS
│       └── html/                ← HTML 임시 파일
├── state/                       ← 파이프라인 상태
│   └── pipeline_state.json
└── src/                         ← 자동화 코드
    └── content_auto/            ← LangGraph 시스템
```

## 컨트리 매니저 (CM) 체계

### 일일 타깃 배분 (18명)

| CM | 시장 | 타깃 | 비율 | 특성 |
|----|------|-----|------|------|
| CM Indonesia | 인도네시아 | 3명 | 17% | SEA 최대 $94.5B |
| CM Vietnam | 베트남 | 3명 | 17% | 고성장, Tiki/Sendo |
| CM Korea | 한국 | 3명 | 17% | 홈마켓 |
| CM Japan | 일본 | 3명 | 17% | 아시아 2위, 고단가 |
| CM Philippines | 필리핀 | 2명 | 11% | 16.7% CAGR |
| CM India | 인도 | 2명 | 11% | 14억 잠재력 |
| CM SEA Emerging | 태국+말레이 | 1명 | 5% | 보조 시장 |
| CM ANZ | 호주+뉴질랜드 | 1명 | 5% | 고단가 |

### CM 역할

1. **프리세일즈 지휘**: 리드 DB 발굴, 초기 접촉
2. **세일즈 마케팅 콘텐츠 기획/검수**: 시장 특화 콘텐츠
3. **세일즈 디렉터 직속 보고**: 파이프라인 현황

## 콘텐츠-세일즈 협업

```
CM/세일즈팀 ──→ 현장 인사이트 공유 ──→ 콘텐츠팀
                                          │
              세일즈 퍼널용 콘텐츠 ←────────┘
```

- **CM → 콘텐츠팀**: 잠재 고객 관심사, 자주 받는 질문, 반응 좋은 표현
- **콘텐츠팀 → CM**: Lead Magnet, 비교 분석, 트렌드 리포트, 이메일 Hook

상세: `workflows/content_sales_collaboration.md`

## 파이프라인

### 콘텐츠 (인바운드)

```
심층 조사 → 팩트체킹 → 자료 구조화 → 콘텐츠 작성 → 검수 → 발행
 (D+0)       (D+1)      (D+2)        (D+3)       (D+4)   (D+5)
```

### 세일즈 (아웃바운드)

```
CM별 리드 발굴 → 타깃 선정 (20명/일) → 메시지 작성 → 발송 → 응답 추적
```

### 카드뉴스 (비주얼 콘텐츠) 🆕

```
브리핑 → 콘텐츠 준비 → LOCK → 테마/레이아웃 → HTML → 프리뷰 → PNG
                      ⚠️승인            ⚠️승인         🔄피드백
```

상세: `workflows/cardnews_pipeline.md`

| 단계 | 담당 |
|------|------|
| 1-4. 콘텐츠 | 조사원 → 팩트체커 → 콘텐츠 에디터 |
| 5. 테마 | 테마 디자이너 |
| 6. 레이아웃 | 레이아웃 디자이너 |
| 7-9. 제작 | `frontend-design` 스킬 + `playwright` MCP |

## 핵심 규칙

### 문체 가이드

- **한국어**: `knowledge/style_guide_ko.md` (김훈 스타일)
- **영어**: `knowledge/style_guide_en.md` (Justin Welsh 스타일)

### 팩트체킹

- 모든 데이터는 **직접 접근 가능한 URL** 필수
- 검증 상태: `✅ VERIFIED`, `⚠️ PARTIALLY_VERIFIED`, `❌ UNVERIFIED`, `🔄 RECHECK_NEEDED`
- 검증 출처: `knowledge/fact_check_sources.md` 참조

### 핸드오프 규칙

파일명 패턴:
```
[산출물유형]_YYYYMMDD_[주제]_[언어].md

예시:
- lead_db_20260217_indonesia.md
- insight_20260217_korea.md
- final_content_20260217_vietnam_linkedin_en.md
```

## 에이전트 모델 권장 사양

| 역할 | 권장 모델 | 용도 |
|-----|----------|------|
| 사외 이사, 총괄 실장, 디렉터급 | `claude-opus-4-5-20251101` | 전략적 판단 |
| 테마 디자이너 | `claude-opus-4-5-20251101` | 디자인 시스템 설계 |
| CM, 팩트체커, 조사원, 메시지 쓰기 | `claude-sonnet-4-5-20250929` | 실무 작업 |
| 레이아웃 디자이너 | `claude-sonnet-4-5-20250929` | 레이아웃 명세 |

## MCP 서버 도구

| MCP 서버 | 용도 |
|---------|------|
| `playwright` | 웹 브라우저 자동화 |
| `nano-banana` | 이미지 생성/편집 |
| `slack` | Slack 메시지 관리 |
| `notion` | Notion 연동 |

## 개발 명령어

### 콘텐츠 자동 생성 (LangGraph)

```bash
# 설치
cd src/content_auto
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 실행
python main.py --run-now              # 즉시 1회 실행
python main.py --run-now --date 2025-01-15  # 특정 날짜
python main.py --schedule             # 일일 스케줄러 (07:00 GMT)
```

### X(트위터) 자동 포스팅

```bash
cd src/x_auto_post
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 랜딩 페이지 (React + Vite)

```bash
cd landing
npm install
npm run dev    # 개발 서버
npm run build  # 프로덕션 빌드
```

### 비주얼 에이드 생성

```python
plt.style.use('dark_background')
# 컬러: #00D4FF (시안), #FF6B6B (코랄), #4ECDC4 (민트)
```

## 자동화 시스템 아키텍처

### 콘텐츠 자동 생성 (src/content_auto/)

LangGraph StateGraph 기반 3-에이전트 파이프라인:

```
Research Agent → Content Writer Agent → QA Editor Agent
                                              ↓
                                       Google Docs 발행
```

- **상태 흐름**: pending → research → writing → qa → completed
- **환경 변수**: `.env` (ANTHROPIC_API_KEY, GOOGLE_FOLDER_ID 필수)
- **인증**: 최초 실행 시 Google OAuth 인증 필요 (credentials.json)

### X 자동 포스팅 (src/x_auto_post/)

```
generate_post.py → post_queue.py → scheduler.py → x_client.py
```

- **의존성**: tweepy, schedule, python-dotenv

## 참조 문서

- CM 구조 계획: `docs/country_manager_plan.md`
- 권역 정의: `knowledge/regions.md`
- 제품 정보: `knowledge/ecdb_product.md`
- 문체 가이드: `knowledge/style_guide_ko.md`, `knowledge/style_guide_en.md`
- **스레드 글쓰기 템플릿**: `knowledge/thread_writing_templates_josh.md` (by Josh)
- 검증 출처: `knowledge/fact_check_sources.md`
- **카드뉴스 파이프라인**: `workflows/cardnews_pipeline.md`
- 워크플로우: `workflows/`
- 콘텐츠 자동화 상세: `src/content_auto/CLAUDE.md`

## 사용 가능한 Claude Code 스킬

콘텐츠 제작 시 관련 스킬 활용:
- `/cardnews` - 10장 카드뉴스 제작 파이프라인
- `/create-linkedin`, `/create-thread` - SNS 콘텐츠 생성
- `/broadcast-*` - 콘텐츠 방송/배포 워크플로우
- `/frontend-design` - HTML/CSS 비주얼 제작
