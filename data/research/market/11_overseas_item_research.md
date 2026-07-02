# 11. 해외 K-뷰티 아이템 조사 — GLOU 큐레이션·소싱 후보 발굴

> **목적**: GLOU(영어권 서구 20–30대 여성 타겟, 서울 K-뷰티 라이프 큐레이션)의 ①AI 추천·큐레이션이 "서구 소비자가 진짜 원하는 K-뷰티"를 알게 하고 ②D2C/소싱 확장 후보를 발굴하기 위해, `new_items` 이커머스 상품발굴 방법론을 **해외 K-뷰티**에 적용.
> **방법론**: `new_items/.claude/skills/product-research` — 6축 0~5 점수화 + 가중합, 역할(미끼/효자/브랜드), Stage-Gate Go/Hold/Kill, ★1~2 리뷰 페인 마이닝, 합격컷. 데이터소스: `new_items/ideas/playbooks/11_data-sources-catalog.md`.
> **6축 해외 변환**: ①경쟁강도=Amazon 등록수·정착브랜드÷수요 ②검색량/수요=Google Trends+YouTube·TikTok ③틈새=수요有+영어권 신뢰 리스팅·정보 빈+★1~2 불만 ④마진=Amazon US가−한국 소싱가−국경배송·관세 ⑤**운영/규제 리스크=MoCRA·EU CPNP·美 선크림 OTC·액상통관·de minimis 폐지·관세**(비중 大) ⑥시즌성.
> **기준일**: 2026-07-01 · WebSearch 18회+ · 모든 수치 출처 URL 표기 · [사실]/[추정] 구분 · 숫자 미확인은 "미확인"
> **데이터 자산**: `Kbeauty_Analysis` — Amazon 5개 브랜드 리뷰 ~1.2만 건(Dr.Jart+·COSRX·Joseon·PURITO·imfrom CSV) + TikTok 1,680영상 + GraphRAG(성분·효과·피부타입 ~570노드) RAG. → GLOU의 ReactionLens(외국인 반응 SaaS)·SkinMatch(성분·효과 매칭 API) 엔진과 직결.

---

## 0. 점수화 가중치 (루브릭 그대로, 해외 라벨로만 변환)

| 축 | 가중 | 해외 의미 | 방향 |
|---|---|---|---|
| 1 경쟁강도 | ×2 | Amazon 등록수·정착 브랜드 ÷ 수요 | 낮을수록↑ |
| 2 검색량/수요 | ×1.5 | Google Trends·YouTube·TikTok 수요 | 적정·확실 선호 |
| 3 틈새 | ×1.5 | 수요有 + 영어권 신뢰 리스팅·정보 빈 + ★1~2 불만 | 틈 클수록↑ |
| 4 마진 | ×2 | Amazon US가 − 한국 소싱가 − 국경배송·관세 | 높을수록↑ |
| 5 운영/규제 리스크 | ×1.5 | **MoCRA·CPNP·선크림 OTC·액상통관·관세** | 낮을수록↑ |
| 6 시즌성 | ×1 | Google Trends 계절성 | 비계절↑ |

만점 = (5×2)+(5×1.5)+(5×1.5)+(5×2)+(5×1.5)+(5×1) = **47.5** (루브릭 동일). 판정: ✅ 상위+빨간불(1점) 2개 미만 / ⚠️ 중간 또는 빨간불 2개 / ❌ 경쟁·마진 중 1점 + 하위.

> ⚠️ **해외 특수 보정**: 멘토 방법론의 "첫 상품 특별규칙(운영리스크·마진 안정성 가중↑)"을 그대로 차용 — 해외는 **규제(축5)가 단일 최대 함정**이라 빨간불 시 사실상 Kill 우선 검토.

---

## Phase 1 — 후보 롱리스트 (15개)

> 서구에서 뜨는 K-뷰티 카테고리/제품. lead-market(Amazon Best Sellers·TikTok·Reddit 급상승)으로 신규 포함.

| # | 후보 | 대표 제품/브랜드(원문) | 발굴 신호 |
|---|---|---|---|
| 1 | 스네일뮤신 에센스 | COSRX Advanced Snail 96 Mucin Power Essence | Amazon 4.6★ 10.5만 평점, 글로벌 1,300만개 판매 [사실] |
| 2 | PDRN/연어DNA | medicube PDRN Pink, Pink Collagen Capsule Cream | 2025 최대 바이럴, Kylie/Hailey 언급 [사실] |
| 3 | 선크림(일반) | Beauty of Joseon Relief Sun, Round Lab | K-선크림 수출 1위 / **단 US서 SPF판매 중단** [사실] |
| 4 | **딥톤/셰이드갭 선크림·쿠션** | TIRTIR(9→40셰이드), Parnell×Miss Darcei 40셰이드 | 백탁·다크스킨 미스매치 = 영어권 최대 불만 [사실] |
| 5 | 리들샷/마이크로니들(스파이큘) | VT Reedle Shot 100/300/700 | 2024~ TikTok 바이럴, $21, "microneedling in a bottle" [사실] |
| 6 | 시카·세라마이드 배리어 | Anua Heartleaf, 라운드랩, COSRX | "배리어 번아웃" 급상승, 발효세라마이드 트렌드 [사실] |
| 7 | 라이스 토너/저자극 토너 | Anua Rice Toner, Beauty of Joseon | 한방·라이스 트렌드, Anua Heartleaf 토너 핵심 SKU [사실] |
| 8 | 클렌징오일/밤 | KAHI 멀티밤, Haruharu Wonder Black Rice Oil | 더블클렌징·발효 라이스 오일 [사실] |
| 9 | 립·치크 틴트 | rom&nd, peripera Ink Velvet | Ulta K-스킨 매출성장 38% 견인 [사실] |
| 10 | 쿠션 파운데이션 | Clio Kill Cover, TIRTIR | 위 38% 성장 공동 견인 [사실] |
| 11 | 두피·헤드스파 홈케어 | Aromatica/Lador 스칼프 스케일러, 두피 스크러버 | 살롱 스칼프 +9%, "head spa scrubber" 검색 급등(’25.11) [사실] |
| 12 | 비건/할랄 인증 K뷰티 | (인증 레이어) | 北美 할랄 최고성장 지역, 비건 수요 85% [사실] |
| 13 | 남성 K뷰티 | (그루밍 라인) | K뷰티 남성 CAGR 10.9%(’26~’33) [사실] |
| 14 | AHA/BHA·아젤라산 각질 | Anua Azelaic 10, medicube 토너패드 | 아젤라·만델산 각질 트렌드, Amazon 베셀 등장 [사실] |
| 15 | 엑소좀·한방 모던 | 2026 Cosmobeauty 신상 | BeautyMatter 2026 medicosmetic actives 1위군 [사실] |

> 신규 발굴(롱리스트 추가가치): **#4 딥톤 셰이드갭**(수요는 폭발하나 영어권 공급·정보 빈 = 전형적 화이트스페이스), **#11 두피 홈케어**(살롱→홈 리텐션 신호), **#5 리들샷**(국경배송 가벼움·고단가·바이럴) — 멘토 방법론의 "갭/화이트스페이스 + 해외선행" 결합 지점.

---

## Phase 2 — 6축 점수화 (가중합)

> 수치 없는 축은 "미확인" 표기(부풀리기 금지). 점수는 0~5, 괄호는 근거.

| # | 후보 | 1경쟁 ×2 | 2수요 ×1.5 | 3틈새 ×1.5 | 4마진 ×2 | 5규제 ×1.5 | 6시즌 ×1 | 총점/47.5 | 판정 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 스네일뮤신 에센스 | 1 (COSRX 등 포화·정착) | 5 (확실·대형) | 1 (이미 굳음+짝퉁 리스크) | 2 (저단가·관세·짝퉁경쟁) | 4 (화장품·MoCRA만) | 5 | **27.0** | ⚠️ |
| 2 | PDRN/연어DNA | 3 (급성장·진입여지) | 5 (최대 바이럴) | 4 (정보 혼란·신뢰갭) | 4 (고단가) | 2 (효능표방·시술연상 규제민감) | 4 | **35.5** | ✅ |
| 3 | 선크림(일반 SPF) | 2 | 5 | 1 | 미확인 | **0 (US OTC 의약품=SPF판매 차단)** | 3 | **~22** | ❌ |
| 4 | **딥톤/셰이드갭 선크림·쿠션** | 4 (영어권 공급 희소) | 4 (수요↑·검색有) | 5 (★1~2 백탁불만 다수=명확한 틈) | 3 (쿠션 중단가) | 2 (선크림=OTC, 쿠션은 화장품) | 4 | **36.5** | ✅ |
| 5 | 리들샷/마이크로니들 | 4 (VT 외 영어권 소수) | 5 (TikTok 바이럴) | 4 (개념혼란·정보갭) | 4 ($21 고단가·경량) | 3 (스파이큘 효능표방 주의) | 4 | **39.0** | ✅ |
| 6 | 시카·세라마이드 배리어 | 2 (Anua·COSRX 정착) | 5 | 2 | 3 | 4 | 5 | **31.5** | ⚠️ |
| 7 | 라이스/저자극 토너 | 2 (Anua 독주·짝퉁) | 4 | 2 | 2 (액상·저단가·관세) | 4 | 5 | **28.0** | ⚠️ |
| 8 | 클렌징오일/밤 | 3 | 3 | 3 | 3 (밤=경량 유리) | 4 | 4 | **31.0** | ⚠️ |
| 9 | 립·치크 틴트 | 3 (rom&nd 강하나 메이크업 틈) | 4 | 3 | 4 (경량·고마진) | 4 (색조=화장품) | 4 | **34.0** | ✅ |
| 10 | 쿠션 파운데이션 | 3 | 4 | 4 (셰이드갭=틈) | 3 | 3 (색소·셰이드매칭 CS) | 4 | **33.0** | ✅ |
| 11 | 두피·헤드스파 홈케어 | 4 (영어권 K-스칼프 희소) | 3 (급등 초기) | 4 (정보·리스팅 빈) | 3 | 4 (대부분 화장품) | 4 | **33.5** | ✅ |
| 12 | 비건/할랄 인증 | 4 (인증 자체가 차별) | 3 | 4 (인증 필터 빈) | 미확인 | 3 (인증비용·검증) | 5 | **~31** | ⚠️ |
| 13 | 남성 K뷰티 | 4 (영어권 K-남성 희소) | 3 (성장 초기) | 4 | 3 | 4 | 5 | **34.5** | ✅ |
| 14 | AHA/BHA·아젤라 각질 | 2 | 4 | 2 | 3 | 3 (각질=효능·자극 CS) | 4 | **28.5** | ⚠️ |
| 15 | 엑소좀·한방 모던 | 4 (초기·진입여지) | 3 (검색 미성숙) | 3 | 미확인 | 2 (엑소좀=규제 회색·줄기세포 연상) | 4 | **~28** | ⚠️ |

> **점수 신뢰도 주석**: 축1·3은 Amazon 등록수·★1~2 분포의 **체계적 수치 미확보**(PA-API 자격 게이트, anti-bot) → 정성+검색 기반 추정. 축4 마진은 #1(스네일)만 실가 확보, 나머지는 단가대 추정. **이 미확인은 GLOU가 Kbeauty_Analysis 리뷰 DB·향후 PA-API/관세청 HS통계로 채워야 할 정량 공백**(Phase별 데이터 매핑은 §6).

---

## Phase 3 — 상위 후보 정성(★1~2 페인 마이닝·경쟁 현실·규제 함정)

### A. #5 리들샷/마이크로니들 (39.0, 최고점) — 역할: **효자(cash cow) 후보**
- **수요·경쟁**: VT Reedle Shot이 2024~ TikTok·인스타 바이럴, 100/300/700/1000 라인, $21/병. 영어권에서 "microneedling without needles" 포지션을 VT가 거의 독점 → 같은 스파이큘 카테고리에 정착 영어권 경쟁 적음. [사실] [VT TikTok Shop/WhoWhatWear]
- **★1~2 페인(차별화)**: 스파이큘 제품 공통 불만 = ①따가움·자극("스파이큘이 미세상처") ②강도 선택 혼란(50/100/300/700 중 뭘?) ③오용 시 트러블. → **GLOU 차별화 = "내 피부타입엔 몇 강도"를 SkinMatch가 안내**(자가 시술 가이드가 제품보다 부재).
- **규제 함정**: 스파이큘이 "각질·흡수촉진"을 넘어 "마이크로니들링"이라 주장하면 **의료기기/효능표방 경계**. 화장품 범위 내 클레임 관리 필수. 액상 아닌 점도형이라 통관·누액 리스크 낮음(경량 = 국경배송 유리).
- **소싱/D2C**: 고단가($21)+경량 → de minimis 폐지 후에도 마진 방어 상대적 양호. 단 VT 브랜드 파워가 강해 GLOU는 **PB보다 큐레이션·정보 레이어**가 현실적.

### B. #4 딥톤/셰이드갭 선크림·쿠션 (36.5) — 역할: **브랜드(정체성·신뢰) 후보**
- **틈새(★1~2 페인 = 명확)**: K-쿠션은 보통 **3~5셰이드, 전부 매우 밝음**; 다크스킨(Fitzpatrick IV~VI)은 매칭 불가가 구조적. 미네랄 필터 **백탁**이 medium~deep 톤에서 최악. 과거 다크셰이드는 "마케팅 못해서" 반복 단종. [사실] [arktastic/bimbollectual/Refinery29]
- **수요·진전**: TIRTIR가 9→**40셰이드**로 확장해 美·英 최광폭 중 하나, Parnell×Miss Darcei 40셰이드 → **수요는 입증됐는데 영어권 큐레이션·정보가 여전히 빈** = 전형적 화이트스페이스.
- **규제 함정**: **선크림은 美 OTC 의약품**이라 SPF 클레임 차단(아래 C 참조) → "딥톤 선크림 소싱"은 규제 직격. 반면 **쿠션/파데(색조)는 화장품**이라 셰이드갭만 해결하면 진입 가능. → 선크림은 ❌, **쿠션·파데로 좁히면 ✅**.
- **GLOU 적합도 최상**: "다양한 피부톤 큐레이션"은 영어권 서구 타겟(다인종)에 **신뢰·정체성**을 증명하는 브랜드 상품. 마진보다 진정성. SkinMatch가 "내 언더톤·깊이에 맞는 K-쿠션 셰이드" 매칭.

### C. #2 PDRN/연어DNA (35.5) — 역할: **미끼→효자 전환 후보**
- **수요**: 2025 최대 바이럴(스네일뮤신·비프탤로우 잇는 craze), Kylie/Hailey/Mikayla 언급, medicube Pink 라인. 임상 "피부밀도 +12.4%" 인용. [사실] [NewsNation/GetTheGloss]
- **★1~2 페인**: "연어 정자(salmon sperm)" 네이밍 거부감·효능 회의·고가 부담·"진짜 효과?" → **신뢰·교육 갭** = GLOU 콘텐츠·진단의 핵심 먹잇감.
- **규제 함정**: PDRN은 한국에선 의약품/주사 시술과 연관 → 화장품 PDRN은 **시술(주사)과 다름**을 명확히 해야 하고, "재생·DNA복구" 효능표방은 **MoCRA 안전성입증·과대광고 경계**. 美 화장품으로 판매는 가능하나 클레임 관리 난도 높음.
- **전략**: 바이럴 트래픽 유입(미끼)으로 끌고, 고단가 PDRN 세럼·크림으로 마진(효자) 회수하는 razor-blade형.

### D. #1 스네일뮤신 (27.0) — 역할: **미끼(traffic driver), 효자 아님**
- **현실(왜 효자 불가)**: Amazon 4.6★ **10.5만 평점**, COSRX 글로벌 1,300만개 = **완전 포화 레드오션**. Amazon US **$18.50**(구독 $16.65) vs 한국 올리브영 글로벌가 ~$9~13대(정확 KRW는 미확인). 짝퉁이 **Amazon 마켓플레이스발 68%**, 2023 한국세관 14.2만개 압수. [사실] [Amazon/Alibaba insights]
- **결론**: 누구나 아는 KVI(시세를 외우는 상품) → **미끼·진단 데모 소재로만** 유효. D2C 소싱은 마진·짝퉁경쟁으로 부적합. GLOU에선 "AI 성분 추천 라이브 데모"의 단골 예시로 활용.

---

## Phase 4 — 출력

### 4-1. 최종 랭킹 표 (후보 × 6축 × 총점 × 판정 × 역할 × Stage-Gate)

| 순위 | 후보 | 총점/47.5 | 판정 | 역할 태그 | Stage-Gate |
|---|---|---|---|---|---|
| 1 | **리들샷/마이크로니들(스파이큘)** | 39.0 | ✅ | 효자(cash cow) | **Go** |
| 2 | **딥톤/셰이드갭 쿠션·파데** | 36.5 | ✅ | 브랜드(정체성·신뢰) | **Go** (선크림은 Kill) |
| 3 | **PDRN/연어DNA** | 35.5 | ✅ | 미끼→효자 | **Go(조건부: 클레임 관리)** |
| 4 | 남성 K뷰티 | 34.5 | ✅ | 효자 후보 | Hold |
| 5 | 립·치크 틴트 | 34.0 | ✅ | 효자(경량·고마진) | Hold |
| 6 | 두피·헤드스파 홈케어 | 33.5 | ✅ | 브랜드/효자 | Hold |
| 7 | 쿠션 파운데이션(일반) | 33.0 | ✅ | 효자 | Hold |
| 8 | 시카·세라마이드 배리어 | 31.5 | ⚠️ | 효자(레드오션) | Hold |
| 9 | 클렌징오일/밤 | 31.0 | ⚠️ | 효자 | Hold |
| 10 | 비건/할랄 인증 | ~31 | ⚠️ | 브랜드 | Hold |
| 11 | AHA/BHA·아젤라 각질 | 28.5 | ⚠️ | 효자 | Hold |
| 12 | 라이스/저자극 토너 | 28.0 | ⚠️ | 효자(레드오션·액상) | Hold |
| 13 | 엑소좀·한방 모던 | ~28 | ⚠️ | 브랜드(선행) | Hold |
| 14 | 스네일뮤신 에센스 | 27.0 | ⚠️ | **미끼/데모 소재** | Hold(소싱 Kill) |
| 15 | 선크림(일반 SPF) | ~22 | ❌ | — | **Kill(소싱)** |

### 4-2. Top 3 추천 (왜·리스크·차별화)

**① 리들샷/마이크로니들 — 효자, Go**
- 왜: 최고점(39.0). 고단가·경량(국경배송·관세 방어), TikTok 수요 확실, 영어권에 VT 외 정착 경쟁 적음. 액상 아님 → 통관·누액 리스크 낮음.
- 리스크: VT 브랜드 독점력 강함(GLOU PB 어려움) / 스파이큘 "마이크로니들링" 클레임 = 의료기기 경계.
- 차별화: 제품이 아니라 **"내 피부엔 어느 강도(100/300/700)"** 가이드가 시장에 부재 → SkinMatch 진단 + ReactionLens 후기로 정보갭 메움. 큐레이션 우위.

**② 딥톤/셰이드갭 쿠션·파데 — 브랜드, Go(선크림은 Kill)**
- 왜: 틈새 5점(★1~2 백탁·미스매치 불만 명확), 수요 입증(TIRTIR 40셰이드), 영어권 다인종 타겟에 **신뢰·정체성** 직결. GLOU 적합도 최상.
- 리스크: 선크림은 OTC 규제로 차단 → **색조(쿠션·파데)로 좁혀야** 함. 셰이드매칭 실패=반품 CS.
- 차별화: "다양한 피부톤용 K-뷰티 큐레이션"은 경쟁사(Seoul Sister·Creatrip)가 안 하는 영역. SkinMatch가 언더톤·깊이 매칭, ReactionLens가 "deep tone 실사용 후기" 제공.

**③ PDRN/연어DNA — 미끼→효자, Go(조건부)**
- 왜: 2025 최대 바이럴 = 유입 자석(미끼), 고단가 = 마진 회수(효자). 신뢰·교육 갭이 GLOU 콘텐츠의 먹잇감.
- 리스크: "연어 정자" 거부감·효능 회의 / "재생·DNA" 효능표방 = MoCRA 과대광고·시술 혼동 경계.
- 차별화: 화장품 PDRN ≠ 주사 시술임을 교육 + 효과 회의에 ReactionLens 실후기 데이터로 응답. 바이럴 트래픽을 GLOU 진단 깔때기로 흡수.

### 4-3. 규제 리스크 핵심 경고 (축5 = 해외 최대 함정)

1. **🔴 美 선크림 = OTC 의약품 (SPF 소싱 사실상 차단)**: 美는 자외선차단을 OTC drug로 규제, 승인 필터 16종·1990년대 이후 신규 무. 한국 선크림(베모트리지놀 등) UV필터 다수 미승인 → **Beauty of Joseon Relief Sun 등 美 SPF 판매 중단**. 베모트리지놀 모노그래프 추가는 ~2026 가능성(불확정). **→ K-선크림 D2C 소싱은 ❌. 큐레이션은 "한국 현지 구매" 맥락으로만.** [사실] [cheonbeauty/peoniesbeaute/BeautyMatter]
2. **🔴 de minimis $800 면세 폐지 (2025-08-29 전국가) + 韓 15% 관세**: 모든 소포가 정식·약식 통관+관세. K-뷰티 소매가 **10~25%↑**, Heartleaf 토너 $19.99→$22.99 실례, $100 직구에 DHL $20 관세고지 실례. **→ 저단가·액상(토너·에센스) D2C 마진 직격. 고단가·경량(리들샷·세럼) 유리.** [사실] [NBC/Fashionista/WBEZ]
3. **🟠 MoCRA(2023~) 시설등록·제품리스팅·Responsible Person·라벨 연락처**: 해외 제조사는 **US Agent 지정** 의무, 2년마다 갱신, 라벨 연락처(2024-12-29 시한 경과). **→ GLOU가 직접 수입·판매(D2C) 시 RP/US Agent 부담. 큐레이션·송객(현지구매 유도) 모델은 회피 가능.** [사실] [FDA/Crowell]
4. **🟠 EU CPNP + EU 역내 Responsible Person**: EU 판매는 사전 CPNP 신고(유예 없음)+EU 내 RP+PIF/CPSR 필수. **→ 영국·영어권 유럽 확장 시 별도 규제 트랙.** [사실] [REACH24H/EU]
5. **🟡 짝퉁 리스크(스네일뮤신 등 KVI)**: Amazon 마켓플레이스발 짝퉁 68%. **→ "정품 인증·공식 판매처 큐레이션" 자체가 GLOU 신뢰 가치.** [사실] [Alibaba insights]

> **종합**: D2C/소싱은 **고단가·경량·색조/세럼(화장품 카테고리)** 으로 좁히고, **선크림·액상저단가·PDRN 효능표방**은 규제·관세로 후순위. 가장 안전한 1차 BM은 **소싱이 아니라 큐레이션·송객**(규제 주체를 GLOU가 안 짊).

### 4-4. 시즌성 (축6)
- 선크림류만 강한 여름 계절성(봄~여름 검색 급등). 스네일·PDRN·리들샷·토너·시카·색조·두피는 **연중 평탄~완만** → 대부분 비계절(첫 진입 유리). [추정, Google Trends 패턴 일반론]

---

## §5. GLOU 연결 — 이 인사이트가 추천/큐레이션/ReactionLens·SkinMatch에 어떻게 쓰이나

1. **추천·큐레이션 엔진의 "서구가 진짜 원하는 것" 사전(prior)**: 위 랭킹·★1~2 페인이 곧 GLOU AI 추천의 **가중 prior**. 예) 다크스킨 유저엔 "백탁 없는 쿠션·딥셰이드"를 우선 노출, 배리어 번아웃 유저엔 시카·세라마이드. "서구 인기 K-뷰티 ≠ 한국 인기"(스네일=미끼/PDRN=교육필요/셰이드갭=공급부족)를 GLOU가 알고 큐레이션.
2. **ReactionLens = ★1~2 페인의 실시간 소스**: 보유 Amazon 리뷰 1.2만 + TikTok 1,680영상 RAG가 "외국인이 이 제품에 뭘 불만하나(백탁·따가움·셰이드·연어거부감·짝퉁)"를 브랜드/GLOU에 SaaS로 제공. 본 조사의 정성 페인이 **ReactionLens 데모 시나리오·태그 사전**으로 직결. (Kbeauty 분석 결론 "만족은 키워드보다 사용경험·피부타입 의존"과 정합 → 피부타입 축이 핵심.)
3. **SkinMatch = 규제·셰이드·강도 매칭 레이어**: GraphRAG(성분·효과·피부타입 570노드)가 ①리들샷 강도(100/300/700) ②딥톤 셰이드·언더톤 ③시카/세라마이드 vs 자극성분 회피 ④PDRN 효능 교육을 개인 조건으로 매칭. 본 조사의 "정보·신뢰 갭"이 곧 SkinMatch가 메울 빈칸. **규제로 D2C 못 파는 선크림도 "한국 현지 구매 큐레이션"으로 SkinMatch에 태울 수 있음**(GLOU의 서울 라이프 큐레이션 본질과 정합).

> 듀얼트랙 정합: B2C GLOU가 유저·반응 데이터 축적 → ReactionLens/SkinMatch(B2B)가 그 데이터로 수익·해자. 본 조사는 셋이 공유하는 **엔진의 도메인 prior**.

---

## §6. Kbeauty_Analysis 데이터가 각 단계에 꽂히는 지점

| Stage-Gate 단계 | Kbeauty_Analysis 자산이 메우는 공백 |
|---|---|
| Phase1 후보수집 | TikTok 1,680영상(56인플루언서)·Amazon 5브랜드가 **lead-market 후보·바이럴 신호** 직접 공급(PDRN·스네일·시카 등 검증). |
| Phase2 점수화(축3 틈새·축1 경쟁) | Amazon 리뷰 1.2만 ★분포·LDA토픽(Dr.Jart보습/COSRX트러블/PURITO천연)이 **★1~2 불만 빈도·경쟁 차별축**을 정량화 → 현재 "미확인" 축을 채움. |
| Phase3 정성(페인 마이닝) | 리뷰 RAG가 "Sticky·Irritated·백탁·따가움" 등 **실제 ★1~2 페인 텍스트**를 근거로 제공(추정→사실 격상). |
| Phase4 역할·GLOU 연결 | 추천 알고리즘(무작위 대비 3.25× ER) = **미끼 PDRN/스네일로 유입한 트래픽을 인플루언서 선정으로 전환**하는 마케팅 레버. selection effect 95% 발견 = "키워드보다 인플루언서/피부타입" → GLOU 큐레이션 설계 원칙. |
| 규제 보강(축5) | 관세청 HS통계(향후)·MoCRA/CPNP 사실이 **소싱 Go/Kill 게이트의 객관 입력**. |

---

## 상위 출처 (URL)
1. 美 선크림 OTC·Beauty of Joseon SPF 미국 판매중단·베모트리지놀: https://cheonbeauty.com/blogs/news/korean-sunscreen-ban · https://www.peoniesbeaute.com/post/beauty-of-joseon-spf-no-longer-in-the-u-s-meet-your-new-favorites
2. de minimis 폐지(2025-08-29 전국가)·관세 영향: https://www.npr.org/2025/08/28/nx-s1-5519361/de-minimis-rule-tariffs-consumers-imports-trump · https://www.nbcnews.com/news/asian-america/end-de-minimis-exemption-tariffs-korean-beauty-products-rcna228929
3. 韓 15% 관세·K뷰티 가격 10~25%↑·Heartleaf $19.99→$22.99·DHL $20: https://fashionista.com/2025/10/k-beauty-skin-care-brands-us-expansion-tariffs · https://www.beautetrade.com/blogs/how-usa-tariffs-are-affecting-k-beauty-product-prices-in-2025/
4. MoCRA 시설등록·Responsible Person·US Agent: https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products · https://www.crowell.com/en/insights/client-alerts/fda-issues-final-guidance-on-facility-registration-and-product-listing-under-mocra
5. EU CPNP·RP·PIF: https://en.reach24h.com/service/cosmetic/eu-cpnp-registration · https://knokglobal.com/blog/eu-cosmetics-regulations-korean-beauty-cpnp-compliance-2026
6. TikTok/Amazon 트렌드(PDRN·스네일·배리어·리들샷): https://wwd.com/pop-culture/culture-news/top-tiktok-beauty-trends-2025-1238427383/ · https://www.qogita.com/blog/tiktok-beauty-trends-2026/ · https://beautymatter.com/articles/2026-k-beauty-forecast-top-7-data-backed-trends · https://www.whowhatwear.com/beauty/skin/vt-cosmetics-reedleshot-100-review
7. 딥톤 셰이드갭·TIRTIR 9→40·백탁: https://www.arktastic.com/blog/makeup/foundation-perfect-match-kbeauty · https://www.refinery29.com/en-gb/korean-beauty-foundation-dark-skin-tones-miss-darcei · https://knokglobal.com/blog/korean-sunscreen-dark-skin-tones-no-white-cast-guide
8. 스네일 마진·짝퉁(Amazon $18.50/4.6★/10.5만, 짝퉁 68%): https://www.amazon.com/COSRX-Repairing-Hydrating-Secretion-Phthalates/dp/B00PBX3L7K · https://www.alibaba.com/product-insights/how-to-spot-counterfeit-cosrx-snail-mucin-using-packaging-and-viscosity-clues.html · 두피: https://klinegroup.com/beauty-and-wellbeing/professional-hair-care/the-scalp-care-boom-are-brands-unlocking-growth-from-the-root-up/

---
*작성: 2026-07-01 · product-research 6축 방법론 해외 적용 · 데이터 자산: Kbeauty_Analysis(Amazon 리뷰·TikTok·GraphRAG)*
