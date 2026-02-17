# 세일즈 파이프라인 워크플로우

## 개요

아웃바운드 B2B 세일즈를 위한 5단계 파이프라인.

## 파이프라인 흐름

```
[DB 확보] → [메시지 구조화] → [메시지 작성] → [발송] → [응답 추적]
```

## 일일 목표

- **타깃 선정**: 20명/일
- **메시지 발송**: 20건/일
- **응답률 목표**: 5%
- **미팅 전환**: 1건/주

## 단계별 상세

### 1. DB 확보

**담당**: presales_region1, presales_region2, presales_region3

**병렬 실행**:
```
Task (presales_region1) ─┐
Task (presales_region2) ─┼─→ [병렬 DB 수집]
Task (presales_region3) ─┘
```

**리드 소스**:
| 우선순위 | 소스 | 기대 품질 |
|---------|------|----------|
| 1 | 전시회/박람회 연사 | Very High |
| 2 | 전시회/박람회 참석자 | High |
| 3 | 정부/공공기관 담당자 | High |
| 4 | 기업 보도자료 인용 인물 | Medium-High |
| 5 | 기업 홈페이지 담당자 | Medium |

**산출물**:
- `workspace/leads/lead_db_YYYYMMDD_region1_[source].md`
- `workspace/leads/lead_db_YYYYMMDD_region2_[source].md`
- `workspace/leads/lead_db_YYYYMMDD_region3_[source].md`

**품질 기준**:
- **A급**: 이메일 확인됨 + 의사결정권자
- **B급**: 이메일 확인됨 + 실무자
- **C급**: 이메일 미확인 / 추정

---

### 2. 메시지 구조화

**담당**: message_structurer

**입력**:
- `workspace/leads/lead_db_*.md`

**산출물**:
- `workspace/messages/daily_target_YYYYMMDD.md` (일일 20명 리스트)
- `workspace/messages/message_structure_YYYYMMDD_NNN.md` (개별 구조)

**일일 타깃 선정 기준**:

| 우선순위 | 기준 | 가중치 |
|---------|------|--------|
| 1 | 리드 품질 (A급 우선) | 30% |
| 2 | 최근 활동 (뉴스/발표) | 25% |
| 3 | 의사결정권 (C-level 우선) | 20% |
| 4 | 업종 적합성 (ECDB fit) | 15% |
| 5 | 지역 분산 | 10% |

**권역별 배분**:
| 권역 | 인원 | 비율 |
|-----|------|------|
| 권역 1 | 10명 | 50% |
| 권역 2 | 5명 | 25% |
| 권역 3 | 5명 | 25% |

**메시지 구조 설계**:
```markdown
## 이메일 구조
- Hook (관심 끌기)
- Pain Point (공감)
- Solution (ECDB 가치 제안)
- CTA (행동 유도)

## LinkedIn 구조 (300자)
- 인사 + 연결 감사
- 공통점/연결고리
- 1줄 가치 제안
- 소프트 CTA
```

---

### 3. 메시지 작성

**담당**: message_writer_ko, message_writer_en

**병렬 실행**:
```
Task (message_writer_ko) [한글 타깃] ─┐
                                      ├─→ [병렬 작성]
Task (message_writer_en) [영어 타깃] ─┘
```

**입력**:
- `workspace/messages/message_structure_YYYYMMDD_NNN.md`

**산출물**:
- `workspace/messages/message_ko_YYYYMMDD_[campaign]_[batch].md`
- `workspace/messages/message_en_YYYYMMDD_[campaign]_[batch].md`

**필수 체크**:
- [ ] 이름/직함 정확성
- [ ] 회사명 오타 없음
- [ ] 시제 표현 정확
- [ ] 수치/통계 출처 확인
- [ ] 문화권별 톤 적용

---

### 4. 발송

**담당**: message_writer_ko, message_writer_en

**채널**:
| 채널 | 도구 | 발송 시간 |
|-----|------|----------|
| 이메일 | 스크립트/Gmail | 업무 시간 (현지) |
| LinkedIn | Playwright | 업무 시간 (현지) |

**발송 순서**:
1. 이메일 발송
2. LinkedIn 연결 요청
3. (수락 후) LinkedIn 메시지

---

### 5. 응답 추적

**담당**: sales_director

**산출물**:
- `workspace/messages/sending_log_ko_YYYYMMDD_[campaign].md`
- `workspace/messages/sending_log_en_YYYYMMDD_[campaign].md`

**추적 지표**:
| 지표 | 측정 방법 |
|-----|----------|
| 발송 성공 | 발송 로그 |
| 오픈율 | 이메일 트래킹 |
| 응답률 | 응답 기록 |
| 미팅 전환 | CRM 기록 |

---

## 주간 보고

**담당**: sales_director → general_manager

**산출물**:
- `outputs/sales/weekly_sales_report_YYYYMMDD.md`

**포함 항목**:
| 지표 | 목표 | 실적 | 달성률 |
|-----|------|------|--------|
| 신규 리드 | 100건 | | |
| 메시지 발송 | 100건 | | |
| 오픈율 | 30% | | |
| 응답률 | 5% | | |
| 미팅 전환 | 5건 | | |

---

## 파이프라인 상태 관리

### state/sales_pipeline_state.json

```json
{
  "date": "2026-02-17",
  "daily_target": {
    "total": 20,
    "region1": 10,
    "region2": 5,
    "region3": 5
  },
  "status": {
    "leads_collected": 150,
    "targets_selected": 20,
    "messages_drafted": 20,
    "messages_sent": 18,
    "responses": 2
  },
  "files": {
    "leads": [],
    "structures": [],
    "messages": [],
    "logs": []
  }
}
```

---

## 팔로업 프로세스

### 팔로업 타이밍

| 단계 | 시점 | 내용 |
|-----|------|------|
| 1차 | D+3 | 미응답 시 간단한 리마인더 |
| 2차 | D+7 | 추가 가치 제안 또는 인사이트 |
| 3차 | D+14 | 마지막 시도 (옵트아웃 제안) |

### 응답 처리

| 응답 유형 | 처리 |
|----------|------|
| 긍정 (관심) | 미팅 세팅 |
| 질문 | 정보 제공 후 팔로업 |
| 거절 | 기록 후 3개월 후 재접촉 |
| 옵트아웃 | DB에서 제외 |
