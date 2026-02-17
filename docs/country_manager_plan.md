# 컨트리 매니저 구조 최종안

## 확정된 구조: 9개 컨트리 매니저

```
세일즈 디렉터 (sales_director)
├── CM Korea (cm_korea)              ← 한국 단독
├── CM Japan (cm_japan)              ← 일본 단독
├── CM India (cm_india)              ← 인도 단독
├── CM Indonesia (cm_indonesia)      ← 인도네시아 단독
├── CM Vietnam (cm_vietnam)          ← 베트남 단독
├── CM Philippines (cm_philippines)  ← 필리핀 단독
├── CM Singapore (cm_singapore)      ← 싱가포르 단독 (HQ 집중)
├── CM SEA Emerging (cm_sea_emerging)← 태국+말레이시아 묶음
├── CM ANZ (cm_anz)                  ← 호주+뉴질랜드 묶음
├── 메시지 쓰기_한글 (message_writer_ko)
└── 메시지 쓰기_영어 (message_writer_en)
```

---

## 시장 분류 근거

### Tier 1: 고성장 개도국 (판매 확률 높음)

| CM | 시장 | 규모 | 성장률 | 단독 사유 |
|----|------|------|--------|----------|
| CM Indonesia | 인도네시아 | $94.5B | 고성장 | SEA 최대, Tokopedia/Bukalapak |
| CM Vietnam | 베트남 | - | 고성장 | Tiki/Sendo, 베트남어 |
| CM Philippines | 필리핀 | $17.6B | **16.7%** | SEA 최고 성장률 |

### Tier 2: 전략 시장 (고계약단가 / 네트워크)

| CM | 시장 | 규모 | 성장률 | 단독 사유 |
|----|------|------|--------|----------|
| CM Korea | 한국 | - | 안정 | 홈마켓, 한국어, 네트워크 |
| CM Japan | 일본 | 지역 4.5% | 안정 | 아시아 2위, 일본어 필수 |
| CM Singapore | 싱가포르 | $10B+ | 11% | **지역 HQ**, 고계약단가 |

### Tier 3: 잠재/보조 시장

| CM | 시장 | 규모 | 성장률 | 묶음/단독 사유 |
|----|------|------|--------|---------------|
| CM India | 인도 | 5% 침투 | 급성장 | 14억 인구, 잠재력 최대 |
| CM SEA Emerging | 태국+말레이 | 중간 | 중간 | 영어 통용, 보조 시장 |
| CM ANZ | 호주+뉴질랜드 | $81B | 8.2% | 영어권, 동일 문화 |

---

## 일일 타깃 배분 (20명)

| CM | 담당 시장 | 타깃 | 비율 | 우선순위 |
|----|----------|-----|------|---------|
| CM Indonesia | 인도네시아 | 3명 | 15% | ⭐⭐⭐ |
| CM Vietnam | 베트남 | 3명 | 15% | ⭐⭐⭐ |
| CM Korea | 한국 | 3명 | 15% | ⭐⭐⭐ |
| CM Japan | 일본 | 3명 | 15% | ⭐⭐⭐ |
| CM Singapore | 싱가포르 | 2명 | 10% | ⭐⭐ |
| CM Philippines | 필리핀 | 2명 | 10% | ⭐⭐ |
| CM India | 인도 | 2명 | 10% | ⭐⭐ |
| CM SEA Emerging | 태국+말레이시아 | 1명 | 5% | ⭐ |
| CM ANZ | 호주+뉴질랜드 | 1명 | 5% | ⭐ |

**리소스 집중도**:
- 고성장 + 전략 시장: 18명/일 (90%)
- 보조 시장: 2명/일 (10%)

---

## 컨트리 매니저 공통 역할

### 1. 프리세일즈 지휘

```yaml
책임:
  - 담당 시장 리드 타깃 선정 기준 수립
  - 리드 품질 검수 (A/B/C급 분류)
  - 초기 접촉 메시지 톤/내용 승인
  - 응답률 모니터링 및 전략 조정

산출물:
  - workspace/leads/lead_db_YYYYMMDD_[country].md
  - workspace/messages/daily_target_YYYYMMDD_[country].md
```

### 2. 세일즈 마케팅 콘텐츠 기획/검수

```yaml
책임:
  - 담당 시장 특화 콘텐츠 주제 기획
  - 현지 트렌드/뉴스 반영 지시
  - 언어/톤 적합성 검수
  - 현지 사례/데이터 정확성 확인

콘텐츠팀 협업:
  - 현장 인사이트 공유 (잠재 고객 관심사)
  - 세일즈 마케팅 퍼널용 콘텐츠 요청
  - 콘텐츠 성과 피드백
```

### 3. 세일즈 디렉터 직속 보고

```yaml
보고 내용:
  - 주간 시장별 파이프라인 현황
  - 리드 품질 및 응답률 분석
  - 시장 인사이트 및 기회 보고
  - 이슈/블로커 에스컬레이션
```

---

## 콘텐츠팀 - 세일즈팀 협업 구조

### 협업 원칙

```
"현장에서 체득한 정보를 공유하고,
 그걸 바탕으로 세일즈 마케팅 퍼널용 콘텐츠를 만든다"
```

### 협업 흐름

```
[CM/세일즈팀]                      [콘텐츠팀]
     │                                 │
     │  ① 현장 인사이트 공유            │
     │  "인니 물류업체들이 cross-border  │
     │   fulfillment 데이터에 관심 많음" │
     ├────────────────────────────────→│
     │                                 │
     │  ② 콘텐츠 기획/제작              │
     │                                 │
     │  ③ 세일즈 퍼널용 콘텐츠 제공      │
     │←────────────────────────────────┤
     │  "인도네시아 크로스보더 물류 현황" │
     │  LinkedIn 글 + Lead Magnet PDF   │
     │                                 │
     │  ④ 콘텐츠 활용 후 피드백          │
     │  "오픈율 45%, 미팅 전환 2건"      │
     ├────────────────────────────────→│
     │                                 │
     │  ⑤ 콘텐츠 개선                   │
     │←────────────────────────────────┤
```

### 인사이트 공유 항목

| 공유 항목 | 예시 |
|----------|------|
| 잠재 고객 관심 주제 | "일본 리테일러들이 SEA 진출 데이터 필요" |
| 자주 받는 질문 | "마켓플레이스별 수수료 비교 있나요?" |
| 반응 좋았던 메시지 | "OO 데이터 언급하니 응답률 높았음" |
| 경쟁사 언급 | "Similar Web 쓴다고 했는데 불만족" |
| 구매 장벽 | "가격보다 데이터 정확도가 관건" |

### 콘텐츠팀 협업 의무

```yaml
콘텐츠 디렉터:
  - CM/세일즈팀 콘텐츠 요청 시 우선 대응
  - 시장별 특화 콘텐츠 기획 협의
  - 세일즈 퍼널 단계별 콘텐츠 제공

콘텐츠 에디터:
  - CM 검수 요청 시 수정 반영
  - 시장별 톤/표현 조정
  - 세일즈용 숏폼 콘텐츠 제작

조사원:
  - CM 요청 시장 우선 조사
  - 현장 인사이트 기반 데이터 수집
  - 리드 대상 기업 정보 조사 지원
```

---

## 새로운 전체 조직 구조

```
총괄 실장 (general_manager)
│
├── 세일즈 디렉터 (sales_director)
│   │
│   ├── [컨트리 매니저 9명]
│   │   ├── CM Korea ─────→ 프리세일즈 업무 직접 수행
│   │   ├── CM Japan ─────→ 프리세일즈 업무 직접 수행
│   │   ├── CM India ─────→ 프리세일즈 업무 직접 수행
│   │   ├── CM Indonesia ─→ 프리세일즈 업무 직접 수행
│   │   ├── CM Vietnam ───→ 프리세일즈 업무 직접 수행
│   │   ├── CM Philippines → 프리세일즈 업무 직접 수행
│   │   ├── CM Singapore ─→ 프리세일즈 업무 직접 수행
│   │   ├── CM SEA Emerging → 프리세일즈 업무 직접 수행
│   │   └── CM ANZ ───────→ 프리세일즈 업무 직접 수행
│   │
│   ├── 메시지 쓰기_한글 (message_writer_ko)
│   └── 메시지 쓰기_영어 (message_writer_en)
│
└── 콘텐츠 디렉터 (content_director)
    │
    ├── 콘텐츠 자동화 (content_auto_agent)
    ├── 콘텐츠 에디터 (content_editor)
    ├── 콘텐츠 구조화 (content_structurer)
    ├── 팩트체커 (fact_checker)
    ├── 조사원1 (researcher_region1)
    ├── 조사원2 (researcher_region2)
    └── 조사원3 (researcher_region3)

사외 이사 (outside_director) ← 전략 자문
```

**변경 사항**:
- 기존 `presales_region1/2/3` → CM이 프리세일즈 업무 직접 수행
- 기존 `message_structurer` → CM별 타깃 선정으로 분산
- 콘텐츠팀 ↔ 세일즈팀 협업 라인 신설

---

## 기존 구조와 비교

| 항목 | 기존 (권역 3개) | 신규 (CM 9개) |
|-----|----------------|--------------|
| 단위 | 지리적 권역 | 시장 특성 기반 |
| 프리세일즈 | 별도 에이전트 3개 | CM이 직접 수행 |
| 언어 | 혼재 | CM별 명확 |
| 콘텐츠 협업 | 없음 | **양방향 협업** |
| 책임 | 분산 | CM에 집중 |
| 전문성 | 낮음 (권역1에 7개국) | 높음 (최대 2개국) |

---

## 에이전트 파일 구조

```
agents/
├── strategic/
│   ├── outside_director.md
│   └── general_manager.md
├── sales/
│   ├── sales_director.md
│   ├── cm_korea.md          ← 신규
│   ├── cm_japan.md          ← 신규
│   ├── cm_india.md          ← 신규
│   ├── cm_indonesia.md      ← 신규
│   ├── cm_vietnam.md        ← 신규
│   ├── cm_philippines.md    ← 신규
│   ├── cm_singapore.md      ← 신규
│   ├── cm_sea_emerging.md   ← 신규
│   ├── cm_anz.md            ← 신규
│   ├── message_writer_ko.md
│   └── message_writer_en.md
└── content/
    ├── content_director.md   ← 협업 의무 추가
    ├── content_editor.md     ← 협업 의무 추가
    ├── content_structurer.md
    ├── fact_checker.md
    ├── researcher_region1.md ← 협업 의무 추가
    ├── researcher_region2.md
    └── researcher_region3.md
```

**삭제 대상**:
- `agents/sales/message_structurer.md` (CM으로 분산)
- `agents/sales/presales_region1.md` (CM으로 통합)
- `agents/sales/presales_region2.md` (CM으로 통합)
- `agents/sales/presales_region3.md` (CM으로 통합)

---

## 구현 순서

### Phase 1: CM 에이전트 생성

1. [ ] CM Korea 역할 정의
2. [ ] CM Japan 역할 정의
3. [ ] CM Indonesia 역할 정의
4. [ ] CM Vietnam 역할 정의
5. [ ] CM Philippines 역할 정의
6. [ ] CM Singapore 역할 정의
7. [ ] CM India 역할 정의
8. [ ] CM SEA Emerging 역할 정의
9. [ ] CM ANZ 역할 정의

### Phase 2: 협업 워크플로우

1. [ ] workflows/content_sales_collaboration.md 생성
2. [ ] content_director.md 협업 의무 추가
3. [ ] content_editor.md 협업 의무 추가
4. [ ] researcher_region1/2/3.md 협업 의무 추가

### Phase 3: 기존 구조 정리

1. [ ] 기존 presales_region1/2/3.md 삭제
2. [ ] 기존 message_structurer.md 삭제
3. [ ] CLAUDE.md 업데이트
4. [ ] sales_director.md 업데이트 (CM 관리 추가)
