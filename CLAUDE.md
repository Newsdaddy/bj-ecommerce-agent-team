# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 개요

BJ 이커머스 사단은 이커머스 데이터 SaaS(ECDB)의 B2B 세일즈를 위한 멀티 에이전트 조직이다. 코드 저장소가 아닌, Claude Code로 운영되는 에이전트 워크스페이스다.

- **최종 목표**: €15,000 상당의 연간 계약 체결
- **작업 언어**: 한국어 (별도 지시 없는 한)
- **최종 산출물**: `총괄 실장/final_outputs/`에 저장

## 빠른 시작

### 콘텐츠 자동 생성 (Python)

```bash
cd "총괄 실장/콘텐츠 디렉터/콘텐츠 작성 에이전트"
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py --run-now              # 즉시 실행
python main.py --schedule             # 일일 스케줄러 (07:00 GMT)
python main.py --run-now --date 2025-01-15  # 특정 날짜
```

### 비주얼 에이드 생성 (matplotlib)

```python
plt.style.use('dark_background')
# 컬러: #00D4FF (시안), #FF6B6B (코랄), #4ECDC4 (민트)
```

생성 후 nano-banana로 스타일 보정 가능. 최종본은 `총괄 실장/final_outputs/scripts/`에 저장.

## 에이전트 구조

```
사외 이사/                                    ← 전략 자문, 비판적 관점 (Opus 4.5)
총괄 실장/                                    ← 업무 분배, 일일 점검 (Opus 4.5)
├── 세일즈 디렉터/                            ← 아웃바운드 파이프라인
│   ├── 메시지 구조화 매니저/                 ← 일일 20명 타깃 선정
│   │   ├── 프리세일즈1_DB확보_한국일본베트남태국싱가포르인도네시아/
│   │   ├── 프리세일즈2_DB확보_말레이시아인도/
│   │   └── 프리세일즈3_DB확보_호주뉴질랜드/
│   ├── 메시지 쓰기 보내기_한글/
│   └── 메시지 쓰기 보내기_영어/
└── 콘텐츠 디렉터/                            ← 인바운드 콘텐츠 전략 (Opus 4.5)
    ├── 콘텐츠 작성 에이전트/                 ← LangGraph 자동화 시스템
    └── 콘텐츠 작성 에디터 링크드인_X_섭스텍/ ← 김훈/Justin Welsh 문체
        └── 자료 구조화 및 어젠다 세팅 매니저/
            └── 자료 팩트체커/                ← 직접 링크 검증 (Sonnet 4)
                ├── 자료 심층 조사원1_한국일본베트남싱가포르테국필리핀인도네시아/
                ├── 자료 심층 조사원2_말레이시아인도/
                └── 자료 심층 조사원 3_호주뉴질랜드/
```

## 지역 구분

| 권역 | 대상 시장 |
|------|----------|
| 권역 1 | 한국, 일본, 베트남, 태국, 싱가포르, 필리핀, 인도네시아 |
| 권역 2 | 말레이시아, 인도 |
| 권역 3 | 호주, 뉴질랜드 |

## 파이프라인

### 콘텐츠 (인바운드)
```
심층 조사 → 팩트체킹 → 자료 구조화 → 콘텐츠 작성 → 검수 → 발행
 (D+0)       (D+1)      (D+2)        (D+3)       (D+4)   (D+5)
```

### 세일즈 (아웃바운드)
```
DB 확보 → 메시지 구조화 (20명/일) → 메시지 작성 → 발송 → 응답 추적
```

## 핵심 규칙

### 워크스페이스
- 각 에이전트 디렉토리 = 워크스페이스
- 각 워크스페이스의 `CLAUDE.md`가 해당 에이전트의 역할 정의
- `.claude/settings.local.json`으로 에이전트별 권한 설정

### 문체 가이드
- **한국어 (김훈)**: 단문, 명사형 종결, 건조함, 수식어 최소화
- **영어 (Justin Welsh)**: Hook → Context → Numbered List → CTA

### 팩트체킹
- 모든 데이터는 **직접 접근 가능한 URL** 필수
- 검증 상태: `✅ VERIFIED`, `⚠️ PARTIALLY_VERIFIED`, `❌ UNVERIFIED`, `🔄 RECHECK_NEEDED`

## SaaS 제품 (ECDB) 데이터

- **스토어**: 매출, 카테고리 비중, AOV, Traffic, SEO score
- **기술**: Mobile app, Payment provider, Shipping partnership
- **마켓**: 마켓플레이스 랭킹, Market overview, Market reports
- **리드 DB**: 온라인 스토어별 담당자 연락처

## 산출물 구조

```
총괄 실장/final_outputs/
├── linkedin/      ← LinkedIn 콘텐츠
├── x/             ← X(Twitter) 콘텐츠
├── substack/      ← Substack 뉴스레터
├── sales/         ← 세일즈 캠페인 리포트
├── reports/       ← 분석 리포트
└── scripts/       ← 비주얼 에이드 Python 스크립트
```

## 에이전트 워크스페이스 운영

### 에이전트 호출 방법

특정 에이전트 워크스페이스로 이동하여 Claude Code 실행:
```bash
cd "총괄 실장/콘텐츠 디렉터"
claude   # 해당 에이전트의 CLAUDE.md 컨텍스트로 작동
```

### MCP 서버 도구

| MCP 서버 | 용도 |
|---------|------|
| `playwright` | 웹 브라우저 자동화 (콘텐츠 발행 확인, 리드 조사) |
| `nano-banana` | 이미지 생성/편집 (비주얼 에이드 스타일 보정) |
| `slack` | Slack 메시지/채널 관리 |
| `notion` | Notion 페이지/데이터베이스 연동 |
| `vercel` | 배포 및 프로젝트 관리 |
| `figma` | Figma 디자인 연동 |

### 핸드오프 패턴

에이전트 간 산출물 전달 시 파일명 규칙:
```
[산출물유형]_YYYYMMDD_[주제]_[언어].md

예시:
- research_report_20260204_korea_ecommerce_ko.md
- content_outline_20260204_korea_ecommerce_en.md
- final_content_20260204_korea_ecommerce_linkedin_ko.md
```

### 일일 운영 체크

```bash
# 콘텐츠 파이프라인 산출물 확인
ls "총괄 실장/final_outputs/linkedin/"
ls "총괄 실장/final_outputs/x/"
ls "총괄 실장/final_outputs/substack/"

# 세일즈 파이프라인 확인
ls "총괄 실장/세일즈 디렉터/reports/"
```

## 향후 계획

- `src/memory` - 에이전트 메모리 시스템 구현 예정
