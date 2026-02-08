# Plan: AI 코딩 도구 시장 경쟁사 분석

> **Feature ID**: ai-coding-tools-competitor-analysis
> **Created**: 2026-02-05
> **Status**: Draft
> **Output Format**: PPT 슬라이드용 Markdown

---

## 1. 목적 (Objective)

AI 코딩 도구 시장의 주요 경쟁사(Cursor, Augment Code, Claude Code)를 비교 분석하여 PPT 프레젠테이션용 슬라이드 콘텐츠를 제작한다.

### 1.1 비즈니스 목표
- ECDB 영업 시 AI 도구 시장 인사이트 제공
- 기술 트렌드 이해를 통한 고객 신뢰 구축
- 내부 도구 선택 의사결정 지원

### 1.2 산출물
- `docs/02-design/features/ai-coding-tools-competitor-analysis.design.md`
- PPT 슬라이드용 구조화된 Markdown (10-15 슬라이드)

---

## 2. 범위 (Scope)

### 2.1 분석 대상
| 도구 | 개발사 | 카테고리 |
|------|--------|----------|
| **Cursor** | Anysphere | AI-first IDE |
| **Augment Code** | Augment | AI 코딩 어시스턴트 |
| **Claude Code** | Anthropic | CLI 기반 AI 에이전트 |

### 2.2 비교 항목
1. **제품 개요**: 출시일, 기반 기술, 핵심 컨셉
2. **기능 비교**: 코드 생성, 자동완성, 멀티파일 편집, 에이전트 기능
3. **가격 정책**: 무료/유료 플랜, 월/연 요금
4. **기술 스택**: 사용 LLM, IDE 통합, 지원 언어
5. **시장 포지셔닝**: 타겟 유저, 차별화 전략
6. **장단점 요약**: SWOT 스타일 분석

### 2.3 Out of Scope
- GitHub Copilot (별도 분석 필요)
- 오픈소스 대안 (Cody, Continue 등)
- 상세 벤치마크 테스트

---

## 3. 요구사항 (Requirements)

### 3.1 슬라이드 구성 요구사항

| 슬라이드 # | 제목 | 내용 |
|-----------|------|------|
| 1 | 표지 | 제목, 날짜, 발표자 |
| 2 | 목차 | 전체 흐름 안내 |
| 3 | 시장 개요 | AI 코딩 도구 시장 규모, 성장률 |
| 4-6 | 제품별 소개 | Cursor, Augment, Claude Code 각 1장 |
| 7 | 기능 비교표 | 핵심 기능 매트릭스 |
| 8 | 가격 비교표 | 플랜별 가격 비교 |
| 9 | 기술 스택 비교 | LLM, 아키텍처 |
| 10 | 포지셔닝 맵 | 2x2 매트릭스 |
| 11 | 장단점 요약 | 3사 SWOT |
| 12 | 시사점 | 우리에게 주는 의미 |
| 13 | Q&A | 질의응답 |

### 3.2 디자인 요구사항
- 각 슬라이드는 **핵심 메시지 1개**에 집중
- 데이터는 **표 또는 차트**로 시각화
- 텍스트 최소화, 불릿포인트 사용

---

## 4. 일정 (Timeline)

| 단계 | 작업 | 예상 |
|------|------|------|
| Plan | 문서 작성 (현재) | ✅ 완료 |
| Design | 슬라이드별 상세 콘텐츠 설계 | 다음 단계 |
| Do | (해당 없음 - 문서 산출물) | - |
| Check | 팩트체크 및 리뷰 | Design 후 |

---

## 5. 리소스 (Resources)

### 5.1 참고 자료 (조사 필요)
- [ ] Cursor 공식 사이트 (cursor.com)
- [ ] Augment Code 공식 사이트 (augmentcode.com)
- [ ] Claude Code 문서 (docs.anthropic.com)
- [ ] 시장 리포트 (Gartner, Forrester 등)

### 5.2 도구
- WebSearch: 최신 정보 수집
- WebFetch: 공식 사이트 데이터 추출

---

## 6. 리스크 (Risks)

| 리스크 | 영향도 | 대응 |
|--------|--------|------|
| 최신 정보 부재 | 중 | 공식 사이트 직접 확인 |
| 가격 정보 변동 | 중 | 조회 일자 명시 |
| 비공개 기능 정보 | 저 | 공개 정보만 활용 |

---

## 7. 다음 단계

**→ `/pdca design ai-coding-tools-competitor-analysis`** 실행하여 Design 문서 작성

Design 단계에서:
1. 각 슬라이드별 상세 콘텐츠 작성
2. 비교표 데이터 수집 및 정리
3. 시각화 가이드 포함

---

## Appendix: 용어 정의

| 용어 | 정의 |
|------|------|
| AI-first IDE | AI 기능을 핵심으로 설계된 통합개발환경 |
| 에이전트 | 자율적으로 작업을 수행하는 AI 시스템 |
| 멀티파일 편집 | 여러 파일을 동시에 수정하는 기능 |
