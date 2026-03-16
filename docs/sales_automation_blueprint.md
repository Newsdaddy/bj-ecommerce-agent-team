# 세일즈 자동화 블루프린트

> 2026-03-15 세션에서 도출된 핵심 전략
> 다른 머신의 에이전트 팀에 이 문서를 학습시켜 동일한 시스템 구축 가능

---

## 1. 핵심 발견: Cowork + Sales Navigator 통합

### Cowork란?
- Claude Desktop의 **브라우저 자동화 기능**
- 크롬에 띄운 웹사이트를 직접 조종 (클릭, 입력, 읽기)
- MCP 없이도 브라우저 제어 가능

### Sales Navigator 자동화 가능 작업
| 작업 | 가능 여부 | 방법 |
|------|---------|------|
| 리드 검색/필터링 | ✅ | Cowork 브라우저 조종 |
| 프로필 정보 추출 | ✅ | Cowork |
| **InMail 발송** | ✅ | Cowork (핵심 기능) |
| 연결 요청 | ✅ | Cowork (주 200개 제한) |
| 1촌 메시지 | ⏸️ | 수동 처리 예정 |

### InMail의 전략적 가치
- 2촌 이상 잠재 고객에게 직접 접근
- 이메일보다 높은 오픈율 (LinkedIn 내 알림)
- Sales Navigator 플랜에 월 50개 포함

---

## 2. Salesforce MCP 연동

### 사용 가능한 MCP 서버
| 옵션 | URL | 특징 |
|------|-----|------|
| Salesforce CLI MCP | https://github.com/salesforcecli/mcp | 공식 |
| Community MCP | https://github.com/tsmztech/mcp-server-salesforce | 안정 |
| Composio | https://composio.dev/toolkits/salesforce/framework/claude-code | 통합 |

### Salesforce 연동 시 가능한 자동화
- 리드 자동 생성/업데이트
- 연락처 관리
- Opportunity 추적
- 캠페인 성과 기록
- Task 자동 생성

---

## 3. 통합 세일즈 파이프라인

```
┌─────────────────────────────────────────────────────────────────┐
│                    COWORK + SALES NAVIGATOR                      │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │ 리드 검색   │ → │ 프로필 추출  │ → │ InMail 발송 │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       AGENT TEAM                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │ CM 에이전트 │ → │ 메시지 작성  │ → │ 리드 DB 정제│          │
│  │ (9개 시장)  │    │ (ko/en)     │    │             │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      SALESFORCE MCP                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │ Lead 등록   │ → │ Opportunity │ → │ 파이프라인   │          │
│  │             │    │ 전환        │    │ 대시보드    │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. 현재 연결 가능한 도구

| 도구 | 역할 | 연결 방식 | 상태 |
|------|------|---------|------|
| Sales Navigator | 리드 발굴 + InMail | Cowork 브라우저 | 테스트 예정 |
| Salesforce | CRM 관리 | MCP 서버 | 설정 필요 |
| Gmail | 이메일 | MCP | ✅ 설정됨 |
| Slack | 내부 알림 | MCP | ✅ 설정됨 |
| Notion | 문서 관리 | MCP | ✅ 설정됨 |

---

## 5. 에이전트 팀 구조 (복제용)

### 디렉토리 구조
```
BJ 이커머스 사단/
├── CLAUDE.md                    ← 마스터 설정 (필수)
├── agents/
│   ├── strategic/               ← 전략급 (2명)
│   │   ├── outside_director.md
│   │   └── general_manager.md
│   ├── sales/                   ← 세일즈팀 (11명)
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
│   └── content/                 ← 콘텐츠팀 (10명)
│       ├── content_director.md
│       ├── content_editor.md
│       ├── fact_checker.md
│       ├── researcher_region1.md
│       ├── researcher_region2.md
│       ├── researcher_region3.md
│       └── ...
├── knowledge/                   ← 공유 지식
├── workflows/                   ← 파이프라인 정의
└── docs/                        ← 문서 (이 파일 포함)
```

### 일일 타깃 배분 (18명)
| CM | 시장 | 타깃 | 우선순위 |
|----|------|-----|---------|
| CM Indonesia | 인도네시아 | 3명 | ⭐⭐⭐ 고성장 |
| CM Vietnam | 베트남 | 3명 | ⭐⭐⭐ 고성장 |
| CM Korea | 한국 | 3명 | ⭐⭐⭐ 홈마켓 |
| CM Japan | 일본 | 3명 | ⭐⭐⭐ 고단가 |
| CM Philippines | 필리핀 | 2명 | ⭐⭐ 최고성장률 |
| CM India | 인도 | 2명 | ⭐⭐ 잠재력 |
| CM SEA Emerging | 태국+말레이 | 1명 | ⭐ 보조 |
| CM ANZ | 호주+뉴질랜드 | 1명 | ⭐ 고단가 |

---

## 6. 다른 머신에 복제하는 방법

### Step 1: Git Clone
```bash
git clone [repository-url] "BJ 이커머스 사단"
cd "BJ 이커머스 사단"
```

### Step 2: MCP 서버 설정
```bash
# Gmail, Slack, Notion은 이미 설정되어 있다면 스킵
# Salesforce MCP 추가 (선택)
claude mcp add salesforce
```

### Step 3: Claude Code에서 CLAUDE.md 인식 확인
```bash
claude
# "총괄 실장, 에이전트 팀 스탠바이 상태 보고해" 입력
# 24개 에이전트 인식되면 성공
```

### Step 4: Cowork 설정 (Sales Navigator용)
1. Claude Desktop 열기
2. Cowork 탭 활성화
3. Chrome에서 Sales Navigator 로그인
4. Cowork에서 브라우저 연결

---

## 7. 다음 단계 (TODO)

- [ ] InMail 테스트 (1건)
- [ ] Salesforce MCP 설정
- [ ] 한국 시장 파일럿 (CM Korea)
- [ ] 메시지 템플릿 A/B 테스트
- [ ] 응답률 트래킹 체계 구축

---

## 8. 참고 자료

- Salesforce CLI MCP: https://github.com/salesforcecli/mcp
- Salesforce MCP Setup Guide: https://www.jitendrazaa.com/blog/salesforce/salesforce-mcp-server-for-claude-code-mcp-clients-setup/
- Composio Salesforce: https://composio.dev/toolkits/salesforce/framework/claude-code

---

*이 문서를 다른 Claude Code 인스턴스의 프로젝트 폴더에 포함시키면, 해당 에이전트가 동일한 맥락을 학습합니다.*
