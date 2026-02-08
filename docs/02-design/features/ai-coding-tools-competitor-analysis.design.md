# Design: AI 코딩 도구 시장 경쟁사 분석 - PPT 슬라이드 콘텐츠

> **Feature ID**: ai-coding-tools-competitor-analysis
> **Created**: 2026-02-05
> **Plan Reference**: `docs/01-plan/features/ai-coding-tools-competitor-analysis.plan.md`
> **Output Format**: PPT 슬라이드용 Markdown (총 13 슬라이드)

---

# SLIDE 1: 표지

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│           AI 코딩 도구 시장 경쟁사 분석                     │
│                                                             │
│        Cursor vs Augment Code vs Claude Code                │
│                                                             │
│                      2026.02.05                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**발표자 노트**:
- AI 코딩 도구가 개발자 생산성의 필수 인프라로 자리잡은 2026년 현재, 주요 3사 비교 분석

---

# SLIDE 2: 목차

## 오늘의 안건

1. **시장 개요** - AI 코딩 도구 시장 규모와 성장률
2. **주요 플레이어** - Cursor, Augment Code, Claude Code
3. **비교 분석** - 기능, 가격, 기술 스택
4. **포지셔닝** - 차별화 전략과 타겟 유저
5. **시사점** - 우리에게 주는 의미

---

# SLIDE 3: 시장 개요

## AI 코딩 도구 시장, 폭발적 성장

| 지표 | 수치 |
|------|------|
| **2025년 시장 규모** | $47억 ~ $74억 |
| **2030년 예상 규모** | $240억 ~ $979억 |
| **연평균 성장률 (CAGR)** | 15% ~ 27% |

### 핵심 성장 동력

- LLM 정확도 향상 (HumanEval 90%+ 달성)
- IDE 플러그인 보편화
- 기업의 '필수 생산성 인프라'로 인식 전환

### 지역별 점유율

```
북미        ████████████████████ 42%
아시아태평양 ████████████ 27% (최고 성장률)
유럽        ████████ 20%
기타        ████ 11%
```

**출처**: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/generative-ai-coding-assistants-market-report), [SNS Insider](https://www.globenewswire.com/news-release/2026/01/05/3212882/0/en/AI-Code-Assistant-Market-Set-to-Hit-USD-14-62-Billion-by-2033.html)

---

# SLIDE 4: Cursor 소개

## Cursor - AI-First IDE의 선두주자

### 기본 정보
| 항목 | 내용 |
|------|------|
| **개발사** | Anysphere |
| **제품 유형** | AI 네이티브 IDE (VS Code 기반) |
| **2025년 ARR** | $5억 (기업가치 $100억) |

### 핵심 컨셉
> "VS Code에 AI를 추가한 게 아니라, AI를 중심으로 에디터를 다시 만들었다"

### 주요 기능
- **Tab 자동완성**: 다음 편집 위치 예측
- **Background Agents**: 병렬 자율 코딩 (v0.50)
- **멀티모델 지원**: GPT-4.1, Claude Opus 4, Gemini 2.5 Pro

### 경쟁 우위
- 풀 IDE 경험 (플러그인 X)
- 에이전트 워크플로우 내장
- 개발자 커뮤니티 가장 활성화

**출처**: [Cursor Pricing](https://cursor.com/pricing), [Cursor Changelog 2026](https://blog.promptlayer.com/cursor-changelog-whats-coming-next-in-2026/)

---

# SLIDE 5: Augment Code 소개

## Augment Code - 엔터프라이즈 코드베이스 전문가

### 기본 정보
| 항목 | 내용 |
|------|------|
| **개발사** | Augment (Eric Schmidt 투자) |
| **제품 유형** | IDE 플러그인 + CLI |
| **누적 투자** | $2.52억 |

### 핵심 컨셉
> "대규모 코드베이스 전체를 이해하는 Context Engine"

### 주요 기능
- **Context Engine**: 200K 토큰 컨텍스트, 전체 스택 이해
- **AI Code Review**: GitHub PR 자동 리뷰 (업계 최고 정확도 주장)
- **100+ 네이티브 도구**: MCP 지원
- **Auggie CLI**: 터미널 기반 에이전트

### 경쟁 우위
- ISO 42001 인증 (AI 관리 표준 최초)
- SOC 2 Type II 보안
- 엔터프라이즈 특화

**출처**: [Augment Code](https://www.augmentcode.com), [Augment Pricing](https://www.augmentcode.com/pricing)

---

# SLIDE 6: Claude Code 소개

## Claude Code - 터미널에 사는 개발자

### 기본 정보
| 항목 | 내용 |
|------|------|
| **개발사** | Anthropic |
| **제품 유형** | CLI 기반 에이전트 |
| **최신 버전** | v2.1.0 (2026.01.07) |

### 핵심 컨셉
> "전체 코드베이스를 읽은 숙련된 개발자가 터미널에 상주"

### 주요 기능
- **에이전틱 코딩**: 파일 읽기/쓰기, 테스트, Git 커밋
- **백그라운드 에이전트**: 병렬 작업 수행
- **Skill 시스템**: 확장 가능한 명령어
- **MCP 서버 통합**: 외부 도구 연동

### 경쟁 우위
- Claude Opus 4.5 (SWE-bench 80%+ 최초 달성)
- 100만 토큰 컨텍스트 윈도우
- 에이전트 자율성 최고 수준

**출처**: [Claude Pricing](https://claude.com/pricing), [Claude Code Review 2026](https://aitoolanalysis.com/claude-code/)

---

# SLIDE 7: 기능 비교표

## 핵심 기능 매트릭스

| 기능 | Cursor | Augment Code | Claude Code |
|------|:------:|:------------:|:-----------:|
| **자동완성** | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| **채팅/Q&A** | ★★★★★ | ★★★★★ | ★★★★★ |
| **멀티파일 편집** | ★★★★★ | ★★★★☆ | ★★★★★ |
| **에이전트 모드** | ★★★★★ | ★★★★☆ | ★★★★★ |
| **코드 리뷰** | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| **컨텍스트 이해** | ★★★★☆ | ★★★★★ | ★★★★★ |
| **터미널 통합** | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| **IDE 통합** | ★★★★★ | ★★★★☆ | ★★★☆☆ |

### 차별화 포인트
- **Cursor**: 올인원 IDE 경험
- **Augment**: 엔터프라이즈 코드베이스 + 보안
- **Claude Code**: 터미널 네이티브 + 에이전트 자율성

---

# SLIDE 8: 가격 비교표

## 가격 정책 비교 (2026년 2월 기준)

### 개인/소규모 팀

| 플랜 | Cursor | Augment Code | Claude Code |
|------|--------|--------------|-------------|
| **무료** | Hobby (제한적) | - | Free (일일 한도) |
| **기본** | Pro $20/월 | Indie $20/월 | Pro $20/월 |
| **프로** | Pro+ $60/월 | Developer $50/월 | Max $100/월 |
| **울트라** | Ultra $200/월 | - | Max $200/월 |

### 팀/엔터프라이즈

| 플랜 | Cursor | Augment Code | Claude Code |
|------|--------|--------------|-------------|
| **팀** | $40/유저/월 | $50+/유저/월 | API 기반 |
| **엔터프라이즈** | 커스텀 | 커스텀 | 커스텀 |

### 가격 특징
- **Cursor**: 2025.06 크레딧 기반 전환, 연간 20% 할인
- **Augment**: 2025.10 크레딧 기반 전환, 팀 크레딧 풀링
- **Claude Code**: API 사용량 기반 (Opus 4.5: $5/$25 per MTok)

---

# SLIDE 9: 기술 스택 비교

## 기술 아키텍처

| 항목 | Cursor | Augment Code | Claude Code |
|------|--------|--------------|-------------|
| **기반** | VS Code Fork | IDE 플러그인 | CLI Native |
| **지원 IDE** | Cursor 전용 | VS Code, JetBrains, Vim | 터미널 (IDE 확장) |
| **기본 LLM** | 멀티모델 선택 | Claude Sonnet 4.5 | Claude 모델군 |
| **컨텍스트** | 가변 | 200K 토큰 | 100만 토큰 |

### LLM 지원 현황

```
Cursor:      GPT-4.1 | Claude Opus 4 | Gemini 2.5 Pro | 기타
Augment:     Claude Sonnet 4.5 (기본) | 멀티모델 라우팅
Claude Code: Claude Opus 4.5 | Sonnet 4.5 | Haiku 4.5
```

### 아키텍처 철학
- **Cursor**: "IDE 자체를 AI로 재설계"
- **Augment**: "멀티모델 라우팅으로 최적 선택"
- **Claude Code**: "터미널이 곧 에이전트"

---

# SLIDE 10: 포지셔닝 맵

## 시장 포지셔닝 2x2 매트릭스

```
                    엔터프라이즈 중심
                          │
                          │    ┌─────────────┐
                          │    │   Augment   │
                          │    │    Code     │
                          │    └─────────────┘
                          │
   IDE 통합 ──────────────┼────────────────── CLI/터미널
                          │
        ┌─────────────┐   │         ┌─────────────┐
        │   Cursor    │   │         │ Claude Code │
        └─────────────┘   │         └─────────────┘
                          │
                    개발자 중심
```

### 타겟 유저 프로필

| 제품 | 1차 타겟 | 2차 타겟 |
|------|----------|----------|
| **Cursor** | 프론트엔드/풀스택 개발자 | 스타트업 팀 |
| **Augment** | 엔터프라이즈 엔지니어 | 대규모 레거시 코드베이스 |
| **Claude Code** | 시니어 개발자, DevOps | 터미널 파워유저 |

---

# SLIDE 11: SWOT 요약

## 3사 장단점 비교

### Cursor
| 강점 | 약점 |
|------|------|
| 통합 IDE 경험 | GitHub Copilot 대비 2배 가격 |
| 가장 큰 사용자 기반 | 독자 IDE 종속 |
| 활발한 업데이트 | 대규모 코드베이스 한계 |

### Augment Code
| 강점 | 약점 |
|------|------|
| 엔터프라이즈 보안 인증 | 개인 개발자에게 비쌈 |
| 코드 리뷰 최고 정확도 | 신생 브랜드 인지도 |
| 대규모 코드베이스 특화 | 무료 플랜 없음 |

### Claude Code
| 강점 | 약점 |
|------|------|
| 최강 LLM (Opus 4.5) | GUI 부재 |
| 100만 토큰 컨텍스트 | 학습 곡선 |
| 에이전트 자율성 | 사용량 예측 어려움 |

---

# SLIDE 12: 시사점

## 우리에게 주는 의미

### 1. 시장 트렌드
- AI 코딩 도구는 "선택"이 아닌 "필수"로 전환
- 크레딧 기반 과금이 업계 표준으로 정착
- 에이전트(자율 코딩)가 다음 경쟁 축

### 2. 도구 선택 기준

| 상황 | 추천 도구 |
|------|-----------|
| 빠른 프로토타이핑, 1인 개발 | Cursor Pro |
| 대규모 레거시 코드베이스 | Augment Code |
| 복잡한 멀티파일 리팩토링 | Claude Code |
| 보안/컴플라이언스 필수 | Augment Code |
| 예산 최소화 | Cursor Hobby + Claude Free |

### 3. 비용 최적화 전략
- 개발 단계별 도구 혼용 (프로토타입: Cursor / 코드리뷰: Augment)
- 연간 결제로 20% 절감
- 팀 크레딧 풀링 활용

---

# SLIDE 13: Q&A

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                        Q & A                                │
│                                                             │
│                    질문 있으시면?                           │
│                                                             │
│                                                             │
│           "AI 코딩 도구, 어떤 것을 선택해야 할까?"         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 추가 참고 자료
- [Cursor Pricing](https://cursor.com/pricing)
- [Augment Code](https://www.augmentcode.com)
- [Claude Pricing](https://claude.com/pricing)
- [AI Coding Assistant Pricing 2025](https://getdx.com/blog/ai-coding-assistant-pricing/)

---

# Appendix A: 상세 가격표

## Cursor 상세 가격 (2025.06 이후)

| 플랜 | 월 요금 | 포함 내용 |
|------|---------|-----------|
| Hobby | 무료 | 제한된 완성/요청 |
| Pro | $20 | $20 상당 크레딧 풀 |
| Pro+ | $60 | 더 많은 크레딧 |
| Ultra | $200 | 20x 사용량 + 우선 기능 |
| Teams | $40/유저 | 팀 협업 기능 |
| Enterprise | 커스텀 | SSO, 감사 로그 |

## Augment Code 상세 가격 (2025.10 이후)

| 플랜 | 월 요금 | 크레딧 |
|------|---------|--------|
| Indie | $20 | 기본 크레딧 |
| Developer | $50 | 130,000 크레딧/유저 |
| Standard Team | $50+/유저 | 팀 크레딧 풀링 |
| Enterprise | 커스텀 | 무제한 + 보안 |

## Claude API 가격

| 모델 | 입력 (MTok) | 출력 (MTok) |
|------|-------------|-------------|
| Haiku 4.5 | $1 | $5 |
| Sonnet 4.5 | $3 | $15 |
| Opus 4.5 | $5 | $25 |
| Sonnet (200K+ 컨텍스트) | $6 | $22.50 |

---

# Appendix B: 용어 정의

| 용어 | 정의 |
|------|------|
| **AI-first IDE** | AI를 핵심으로 설계된 통합개발환경 |
| **에이전트** | 자율적으로 코딩 작업을 수행하는 AI |
| **Context Engine** | 코드베이스 전체를 이해하는 시스템 |
| **크레딧 풀** | 사용량 기반 과금 단위 |
| **MCP** | Model Context Protocol (도구 연동 표준) |
| **SWE-bench** | 실제 GitHub 버그 수정 벤치마크 |

---

**Document Version**: 1.0
**Last Updated**: 2026-02-05
**Next Step**: `/pdca analyze ai-coding-tools-competitor-analysis` (팩트체크)
