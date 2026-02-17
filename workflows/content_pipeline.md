# 콘텐츠 파이프라인 워크플로우

## 개요

인바운드 콘텐츠 마케팅을 위한 6단계 파이프라인.

## 파이프라인 일정

```
[조사] → [팩트체크] → [구조화] → [작성] → [검수] → [발행]
 D+0      D+1         D+2       D+3      D+4      D+5
```

## 단계별 상세

### 1. 심층 조사 (D+0)

**담당**: researcher_region1, researcher_region2, researcher_region3

**입력**:
- 총괄 실장/콘텐츠 디렉터의 조사 주제 지시

**산출물**:
- `workspace/research/research_report_YYYYMMDD_[topic]_[country].md`

**병렬 실행**:
```
Task (researcher_region1) ─┐
Task (researcher_region2) ─┼─→ [병렬 조사]
Task (researcher_region3) ─┘
```

**품질 기준**:
- 출처 URL 100% 기재
- 뉴스 포함 기준 충족 (조회수 2,000+ / 댓글 5+ / Tier 1 매체)
- 신뢰도 평가 포함

---

### 2. 팩트체크 (D+1)

**담당**: fact_checker

**입력**:
- `workspace/research/research_report_*.md`

**산출물**:
- `workspace/verified/verified_report_YYYYMMDD_[topic].md`
- 또는 `workspace/verified/recheck_request_YYYYMMDD_[topic].md`

**품질 기준**:
- 모든 데이터 포인트 검증 상태 태깅
- 직접 접근 가능한 URL 확인
- 검증 출처: `knowledge/fact_check_sources.md` 기준

**판정 기준**:
| 승인율 | 판정 | 다음 단계 |
|--------|------|----------|
| 90% 이상 | ✅ 승인 | 구조화로 진행 |
| 70-89% | ⚠️ 조건부 승인 | 미검증 항목 표시 후 진행 |
| 70% 미만 | ❌ 반려 | 조사원에게 재조사 요청 |

---

### 3. 자료 구조화 (D+2)

**담당**: content_structurer

**입력**:
- `workspace/verified/verified_report_YYYYMMDD_[topic].md`

**산출물**:
- `workspace/outlines/content_outline_YYYYMMDD_[topic]_ko.md`
- `workspace/outlines/content_outline_YYYYMMDD_[topic]_en.md`

**포맷별 구조**:
| 플랫폼 | 분량 | 구조 |
|--------|------|------|
| LinkedIn | 1,000자 | 넘버링, 인사이트 3개 |
| X/Twitter | 280자 | 팩트 + 인사이트 |
| Substack | 1,200자 | LinkedIn + 심층 분석 |

**인사이트 필수 관점**:
1. 리테일 기업 관점
2. 물류 기업 관점
3. 제조/D2C 기업 관점

---

### 4. 콘텐츠 작성 (D+3)

**담당**: content_editor

**입력**:
- `workspace/outlines/content_outline_YYYYMMDD_[topic]_ko.md`
- `workspace/outlines/content_outline_YYYYMMDD_[topic]_en.md`

**산출물**:
- `workspace/drafts/final_content_YYYYMMDD_[topic]_linkedin_ko.md`
- `workspace/drafts/final_content_YYYYMMDD_[topic]_linkedin_en.md`
- `workspace/drafts/final_content_YYYYMMDD_[topic]_x_ko.md`
- `workspace/drafts/final_content_YYYYMMDD_[topic]_x_en.md`
- `workspace/drafts/final_content_YYYYMMDD_[topic]_substack_ko.md`
- `workspace/drafts/final_content_YYYYMMDD_[topic]_substack_en.md`
- `workspace/drafts/visual_YYYYMMDD_[topic]_[type].png`

**병렬 실행**:
```
Task (content_editor) [한글] ─┐
                              ├─→ [병렬 작성]
Task (content_editor) [영어] ─┘
```

**문체 가이드**:
- 한국어: `knowledge/style_guide_ko.md` (김훈 스타일)
- 영어: `knowledge/style_guide_en.md` (Justin Welsh 스타일)

---

### 5. 검수 (D+4)

**담당**: content_director

**입력**:
- `workspace/drafts/final_content_*.md`
- `workspace/drafts/visual_*.png`

**검수 항목**:

| 영역 | 체크 항목 |
|-----|----------|
| 내용 | 팩트체크된 데이터만 사용 |
| 문체 | 플랫폼별 가이드 준수 |
| 분량 | 플랫폼별 기준 충족 |
| 비주얼 | 수치 정확성, 요소 오버랩 없음 |

**판정**:
- ✅ 통과 → 발행 진행
- 🔄 수정 필요 → content_editor에게 피드백

---

### 6. 발행 (D+5)

**담당**: content_director (또는 사용자 직접)

**산출물 이동**:
```
workspace/drafts/final_content_*  →  outputs/linkedin/
                                  →  outputs/x/
                                  →  outputs/substack/
```

**발행 채널**:
| 채널 | 발행 시간 | 빈도 |
|-----|----------|------|
| LinkedIn | 09:00 KST | 주 3회 |
| X | 수시 | 주 5회 |
| Substack | 금요일 09:00 | 주 1회 |

---

## 파이프라인 상태 관리

### state/pipeline_state.json

```json
{
  "current_topic": "vietnam_ecommerce",
  "start_date": "2026-02-17",
  "stages": {
    "research": "completed",
    "fact_check": "in_progress",
    "structure": "pending",
    "writing": "pending",
    "review": "pending",
    "publish": "pending"
  },
  "files": {
    "research": ["workspace/research/research_report_20260217_vietnam_region1.md"],
    "verified": [],
    "outlines": [],
    "drafts": [],
    "published": []
  },
  "issues": []
}
```

---

## 예외 처리

### 재조사 요청 시

```
fact_checker → recheck_request → researcher_region* → 재조사 → fact_checker
```

### 긴급 콘텐츠 (단축 파이프라인)

```
[조사+팩트체크] → [구조화+작성] → [검수+발행]
    D+0              D+1              D+2
```
