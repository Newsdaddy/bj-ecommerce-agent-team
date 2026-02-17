# 핸드오프 규칙

## 파일명 규칙

### 기본 패턴

```
[산출물유형]_YYYYMMDD_[주제]_[추가구분].md
```

### 산출물 유형별 패턴

| 유형 | 패턴 | 예시 |
|-----|------|------|
| 조사 보고서 | `research_report_YYYYMMDD_[topic]_[country].md` | `research_report_20260217_vietnam_region1.md` |
| 검증 보고서 | `verified_report_YYYYMMDD_[topic].md` | `verified_report_20260217_vietnam.md` |
| 재조사 요청 | `recheck_request_YYYYMMDD_[topic].md` | `recheck_request_20260217_vietnam.md` |
| 콘텐츠 개요 | `content_outline_YYYYMMDD_[topic]_[lang].md` | `content_outline_20260217_vietnam_ko.md` |
| 최종 콘텐츠 | `final_content_YYYYMMDD_[topic]_[platform]_[lang].md` | `final_content_20260217_vietnam_linkedin_ko.md` |
| 비주얼 에이드 | `visual_YYYYMMDD_[topic]_[type].png` | `visual_20260217_vietnam_bar.png` |
| 리드 DB | `lead_db_YYYYMMDD_[region]_[source].md` | `lead_db_20260217_region1_exhibition.md` |
| 일일 타깃 | `daily_target_YYYYMMDD.md` | `daily_target_20260217.md` |
| 메시지 구조 | `message_structure_YYYYMMDD_NNN.md` | `message_structure_20260217_001.md` |
| 메시지 초안 | `message_[lang]_YYYYMMDD_[campaign]_[batch].md` | `message_ko_20260217_vietnam_01.md` |
| 발송 기록 | `sending_log_[lang]_YYYYMMDD_[campaign].md` | `sending_log_ko_20260217_vietnam.md` |

---

## 저장 위치 규칙

### workspace/ (작업 중)

| 디렉토리 | 용도 | 담당 에이전트 |
|---------|------|--------------|
| `workspace/research/` | 조사 보고서 | researcher_region1/2/3 |
| `workspace/verified/` | 검증 보고서, 재조사 요청 | fact_checker |
| `workspace/outlines/` | 콘텐츠 개요 | content_structurer |
| `workspace/drafts/` | 콘텐츠 초안, 비주얼 에이드 | content_editor |
| `workspace/leads/` | 리드 DB | presales_region1/2/3 |
| `workspace/messages/` | 타깃 리스트, 메시지 구조, 메시지 초안 | message_structurer, message_writer_* |

### outputs/ (최종)

| 디렉토리 | 용도 |
|---------|------|
| `outputs/linkedin/` | LinkedIn 발행 콘텐츠 |
| `outputs/x/` | X 발행 콘텐츠 |
| `outputs/substack/` | Substack 뉴스레터 |
| `outputs/sales/` | 세일즈 보고서 |
| `outputs/reports/` | 분석 리포트 |
| `outputs/scripts/` | 비주얼 에이드 Python 스크립트 |

---

## 핸드오프 맵

### 콘텐츠 파이프라인

```
researcher_region1/2/3
    │
    └─→ workspace/research/research_report_*.md
           │
           └─→ fact_checker
                  │
                  ├─→ workspace/verified/verified_report_*.md
                  │      │
                  │      └─→ content_structurer
                  │             │
                  │             └─→ workspace/outlines/content_outline_*_ko.md
                  │             └─→ workspace/outlines/content_outline_*_en.md
                  │                    │
                  │                    └─→ content_editor
                  │                           │
                  │                           └─→ workspace/drafts/final_content_*.md
                  │                                  │
                  │                                  └─→ content_director (검수)
                  │                                         │
                  │                                         └─→ outputs/linkedin/
                  │                                         └─→ outputs/x/
                  │                                         └─→ outputs/substack/
                  │
                  └─→ workspace/verified/recheck_request_*.md
                         │
                         └─→ researcher_region1/2/3 (재조사)
```

### 세일즈 파이프라인

```
presales_region1/2/3
    │
    └─→ workspace/leads/lead_db_*.md
           │
           └─→ message_structurer
                  │
                  ├─→ workspace/messages/daily_target_*.md
                  └─→ workspace/messages/message_structure_*.md
                         │
                         ├─→ message_writer_ko
                         │      │
                         │      └─→ workspace/messages/message_ko_*.md
                         │             │
                         │             └─→ workspace/messages/sending_log_ko_*.md
                         │
                         └─→ message_writer_en
                                │
                                └─→ workspace/messages/message_en_*.md
                                       │
                                       └─→ workspace/messages/sending_log_en_*.md
```

---

## 핸드오프 트리거 조건

### 자동 트리거

| 산출물 완료 | 다음 에이전트 | 트리거 |
|-----------|-------------|--------|
| research_report 완료 | fact_checker | 조사원 → 팩트체커 |
| verified_report 완료 | content_structurer | 팩트체커 → 구조화 |
| content_outline 완료 | content_editor | 구조화 → 에디터 |
| lead_db 완료 | message_structurer | 프리세일즈 → 구조화 |
| message_structure 완료 | message_writer_* | 구조화 → 작성 |

### 수동 트리거

| 상황 | 트리거 주체 |
|-----|-----------|
| 검수 완료 후 발행 | content_director |
| 팔로업 메시지 | sales_director |
| 긴급 콘텐츠 | general_manager |

---

## 상태 파일 업데이트

### 핸드오프 시 필수 업데이트

산출물 생성 후 `state/pipeline_state.json` 업데이트:

```json
{
  "files": {
    "research": ["workspace/research/research_report_20260217_vietnam_region1.md"],
    "verified": [],  // 팩트체커 완료 시 추가
    "outlines": [],  // 구조화 완료 시 추가
    "drafts": [],    // 에디터 완료 시 추가
    "published": []  // 발행 완료 시 추가
  },
  "stages": {
    "research": "completed",
    "fact_check": "in_progress",  // 현재 단계 표시
    "structure": "pending",
    "writing": "pending",
    "review": "pending",
    "publish": "pending"
  }
}
```

---

## 핸드오프 메시지 템플릿

### 핸드오프 알림

```markdown
## 핸드오프 알림

- **보낸 에이전트**: [에이전트명]
- **받는 에이전트**: [에이전트명]
- **산출물**: [파일 경로]
- **완료 시간**: YYYY-MM-DD HH:MM
- **다음 단계**: [작업 내용]
- **참조 문서**: [관련 knowledge/ 또는 agents/ 파일]
```

### 재조사 요청

```markdown
## 재조사 요청

- **요청 에이전트**: fact_checker
- **대상 에이전트**: researcher_region[N]
- **원본 보고서**: [파일 경로]
- **재조사 필요 항목**:
  1. [항목 1] - 사유: [사유]
  2. [항목 2] - 사유: [사유]
- **기한**: YYYY-MM-DD
```
