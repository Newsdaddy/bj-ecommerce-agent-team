# CLAUDE.md

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
│   ├── [컨트리 매니저 9개]
│   │   ├── CM Korea (cm_korea)                     ← 한국 (3명/일)
│   │   ├── CM Japan (cm_japan)                     ← 일본 (3명/일)
│   │   ├── CM Indonesia (cm_indonesia)             ← 인도네시아 (3명/일) ⭐고성장
│   │   ├── CM Vietnam (cm_vietnam)                 ← 베트남 (3명/일) ⭐고성장
│   │   ├── CM Philippines (cm_philippines)         ← 필리핀 (2명/일) ⭐최고성장률
│   │   ├── CM Singapore (cm_singapore)             ← 싱가포르 (2명/일) HQ집중
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
    └── 조사원3 (researcher_region3)

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
│   ├── sales/                   ← 세일즈 (CM 9개 + 메시지 쓰기 2개)
│   │   ├── sales_director.md
│   │   ├── cm_korea.md
│   │   ├── cm_japan.md
│   │   ├── cm_indonesia.md
│   │   ├── cm_vietnam.md
│   │   ├── cm_philippines.md
│   │   ├── cm_singapore.md
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
│       └── researcher_region3.md
├── knowledge/                   ← 공유 지식
│   ├── regions.md               ← 권역 정의
│   ├── ecdb_product.md          ← SaaS 제품
│   ├── style_guide_ko.md        ← 김훈 문체
│   ├── style_guide_en.md        ← Justin Welsh 문체
│   └── fact_check_sources.md    ← 검증 출처 100+
├── workflows/                   ← 파이프라인 정의
│   ├── content_pipeline.md
│   ├── sales_pipeline.md
│   ├── handoff_rules.md
│   └── content_sales_collaboration.md  ← CM-콘텐츠 협업
├── docs/                        ← 문서
│   └── country_manager_plan.md  ← CM 구조 계획
├── outputs/                     ← 최종 산출물
│   ├── linkedin/
│   ├── x/
│   ├── substack/
│   ├── sales/
│   ├── reports/
│   └── scripts/
├── workspace/                   ← 작업 중 파일
│   ├── research/
│   ├── verified/
│   ├── outlines/
│   ├── drafts/
│   ├── leads/
│   └── messages/
├── state/                       ← 파이프라인 상태
│   └── pipeline_state.json
└── src/                         ← 자동화 코드
    └── content_auto/            ← LangGraph 시스템
```

## 컨트리 매니저 (CM) 체계

### 일일 타깃 배분 (20명)

| CM | 시장 | 타깃 | 비율 | 특성 |
|----|------|-----|------|------|
| CM Indonesia | 인도네시아 | 3명 | 15% | SEA 최대 $94.5B |
| CM Vietnam | 베트남 | 3명 | 15% | 고성장, Tiki/Sendo |
| CM Korea | 한국 | 3명 | 15% | 홈마켓 |
| CM Japan | 일본 | 3명 | 15% | 아시아 2위, 고단가 |
| CM Singapore | 싱가포르 | 2명 | 10% | 지역 HQ 집중 |
| CM Philippines | 필리핀 | 2명 | 10% | 16.7% CAGR |
| CM India | 인도 | 2명 | 10% | 14억 잠재력 |
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
| CM, 팩트체커, 조사원, 메시지 쓰기 | `claude-sonnet-4-5-20250929` | 실무 작업 |

## MCP 서버 도구

| MCP 서버 | 용도 |
|---------|------|
| `playwright` | 웹 브라우저 자동화 |
| `nano-banana` | 이미지 생성/편집 |
| `slack` | Slack 메시지 관리 |
| `notion` | Notion 연동 |

## 빠른 시작

### 콘텐츠 자동 생성

```bash
cd src/content_auto
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py --run-now
```

### 비주얼 에이드 생성

```python
plt.style.use('dark_background')
# 컬러: #00D4FF (시안), #FF6B6B (코랄), #4ECDC4 (민트)
```

## 참조 문서

- CM 구조 계획: `docs/country_manager_plan.md`
- 권역 정의: `knowledge/regions.md`
- 제품 정보: `knowledge/ecdb_product.md`
- 문체 가이드: `knowledge/style_guide_ko.md`, `knowledge/style_guide_en.md`
- 검증 출처: `knowledge/fact_check_sources.md`
- 워크플로우: `workflows/`
