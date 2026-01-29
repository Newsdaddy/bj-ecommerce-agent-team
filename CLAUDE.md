# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

BJ 이커머스 사단은 **이커머스 데이터 제공 SaaS**의 B2B 세일즈를 위한 멀티 에이전트 조직이다. 코드 저장소가 아닌, Claude Code로 운영되는 에이전트 워크스페이스 조직 구조이다.

## 언어

- 기본 작업 언어: **한국어**
- 별도 지시가 없는 한 한국어로 산출물을 작성한다

## SaaS 제품 맥락

글로벌 이커머스 데이터 플랫폼으로 다음 데이터를 제공한다:

- **스토어 데이터**: 국가별/지역별 온라인 스토어 매출(연/월), 제품 카테고리별 판매 비중, 장바구니 담김 비율, AOV, Return amount, Traffic, SEO score
- **기술 데이터**: Mobile app type (Google/Apple), Payment provider, Shipping partnership
- **마켓 데이터**: 마켓플레이스 랭킹 (Revenue/GMV 기준), Market overview by product category, Market reports by country
- **리드 DB**: 전세계 온라인 스토어별 연락 가능한 담당자 데이터베이스

## 에이전트 조직도

```
사외 이사/
총괄 실장/
├── 세일즈 디렉터/
│   ├── 메시지 구조화 매니저/
│   │   ├── 프리세일즈1_DB확보_한국일본베트남태국싱가포르인도네시아/
│   │   ├── 프리세일즈2_DB확보_말레이시아인도/
│   │   └── 프리세일즈3_DB확보_호주뉴질랜드/
│   ├── 메시지 쓰기 보내기_한글/
│   └── 메시지 쓰기 보내기_영어/
└── 콘텐츠 디렉터/
    ├── 콘텐츠 작성 에이전트/  ← APAC Lead Magnet Auto-Generator (Python)
    └── 콘텐츠 작성 에디터 링크드인_X_섭스텍/
        └── 자료 구조화 및 어젠다 세팅 매니저/
            └── 자료 팩트체커/
                ├── 자료 심층 조사원1_한국일본베트남싱가포르테국필리핀인도네시아/
                ├── 자료 심층 조사원2_말레이시아인도/
                └── 자료 심층 조사원 3_호주뉴질랜드/
```

## 데이터 파이프라인

심층 조사 → 팩트체킹 → 자료 구조화/어젠다 세팅 → 콘텐츠 작성 → 메시지 구조화 → 프리세일즈/발송

## 지역 구분

| 권역 | 대상 시장 |
|------|----------|
| 권역 1 | 한국, 일본, 베트남, 태국, 싱가포르, 필리핀, 인도네시아 |
| 권역 2 | 말레이시아, 인도 |
| 권역 3 | 호주, 뉴질랜드 |

## 워크스페이스 규칙

- 각 에이전트는 자체 디렉토리를 워크스페이스로 사용한다
- 각 워크스페이스에 `CLAUDE.md`가 해당 에이전트의 역할과 지침을 정의한다
- `.claude/settings.local.json`으로 에이전트별 권한을 설정할 수 있다
- 산출물은 각 에이전트 워크스페이스 내에 저장한다

## 콘텐츠 자동 생성 시스템

`총괄 실장/콘텐츠 디렉터/콘텐츠 작성 에이전트/` 디렉토리에 Python 기반 APAC Lead Magnet Auto-Generator가 구현되어 있다. 상세 개발 가이드는 해당 디렉토리의 `CLAUDE.md` 참조.

**개발 명령어 (해당 디렉토리에서):**
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py --run-now        # 즉시 실행
python main.py --schedule       # 일일 스케줄러 시작
```

## 메모

- `src/memory` - 향후 에이전트 메모리 시스템 구현 경로
