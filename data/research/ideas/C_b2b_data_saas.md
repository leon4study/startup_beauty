# 미션 C — B2B 데이터·SaaS 라인 (Kbeauty RAG 레버리지)

> 작성일: 2026-07-01 · 프로젝트: 모두의창업 2026 R1 / 팀: GLOU
> 목적: 보유 자산(K-뷰티 리뷰 RAG + 성분·효과 지식그래프 + 인플루언서 분석 + 화학·약학 이해)을 **B2B 데이터·SaaS 제품 10개**로 제품화. 각 BM·비교사·데모 가능성·팀자산 직결도 명시.
> 듀얼트랙 전제: **같은 엔진(K-뷰티 리뷰 RAG + 성분·효과 그래프)을 B2C(GLOU)와 B2B로 동시 수익화.** ([12_idea_scoring.md](../market/12_idea_scoring.md)에서 ReactionLens·SkinMatch가 1·2위로 이미 검증됨)
> 표기: [사실] = 출처 URL로 확인 / [추정] = 출처 기반 해석. 1차 타겟 = 영어권 서구(US·EU).

---

## 0. 한 줄 결론

- 이 라인의 해자는 **"이미 돌아가는 엔진"**이다 — Kbeauty_Analysis에 ①Amazon 리뷰 1.2만 건 분석 ②성분·효과 지식그래프(570 노드: 브랜드 5 + 제품타입 46 + **성분 498** + 효과 23) ③GraphRAG/LightRAG 챗봇(safety 11배 우세 검증) ④TikTok 인플루언서 추천 알고리즘(무작위 대비 3.25배) ⑤RAG 평가 하네스(faithfulness·context precision·recall)가 **실측·재현 가능한 상태로 존재**한다. ([사실] [Kbeauty_Analysis/README.md](../../../../Kbeauty_Analysis/README.md))
- B2B가 B2C보다 모두의창업 R1에 유리한 이유: **데모를 당장 만들 수 있어** "콘텐츠형 약점(BM·기술깊이)"을 데이터로 방어한다.
- **타이밍 근거**: 미국 K-뷰티 매출 2025년 **$2B 돌파(+37% YoY)**, 미국이 한국 뷰티 수출 1위국(수출의 **28%**, 2년 전 17%), K-뷰티 매출의 **70%가 온라인**. → 브랜드들이 "영어권 리뷰·반응 데이터"에 돈 쓸 이유가 폭발 중. ([사실] [CNBC](https://www.cnbc.com/2025/11/27/k-beauty-tiktok-makeup.html), [awisee](https://awisee.com/blog/k-beauty-market-us-sales-trends/), [beautymatter](https://beautymatter.com/articles/k-beautys-export-boom-is-no-longer-a-trend-story))

### 데모 즉시 가능 vs 추가 빌드 (요약)

| 라인 | 데모 즉시? | 팀자산 직결도 | 핵심 BM |
|---|:-:|:-:|---|
| **C1 ReactionLens** (외국인 반응 대시보드) | ⭐ 즉시 | ★★★★★ | SaaS 시트 |
| **C2 SkinMatch** (성분·피부타입 매칭 API/위젯) | ⭐ 즉시 | ★★★★★ | API 호출 과금 + 위젯 화이트라벨 |
| C3 K-Beauty Trend Index (글로벌 트렌드 구독) | 🔶 거의 | ★★★★☆ | 리포트 구독 |
| C4 ReguScan (US MoCRA·EU CPNP 스캐너) | 🔶 부분 | ★★★☆☆ | SaaS + 건당 |
| C5 VOC Multilingual (다국어 번역·VOC 마이닝) | ⭐ 즉시 | ★★★★★ | API + SaaS |
| C6 CreatorMatch (인플루언서↔브랜드 매칭) | ⭐ 즉시 | ★★★★★ | SaaS + 매칭 성과 |
| C7 ClaimGuard (짝퉁·그린워싱·효능클레임 검증) | 🔶 부분 | ★★★★☆ | 건당 + SaaS |
| C8 IngredientDemand (OEM/ODM 신성분 수요예측) | 🔶 부분 | ★★★★☆ | 엔터프라이즈 구독 |
| C9 GapReport (셰이드·포맷 갭 리포트) | ⭐ 즉시 | ★★★★☆ | 리포트 단건/구독 |
| C10 GLOU Data Co-op (B2C 데이터의 B2B 환류) | 🔶 후행 | ★★★★★ | 데이터 라이선스 |

---

## 1. 비교사(벤치마크) 가격 레퍼런스 — 한눈에

이 표가 **우리 가격 설계의 기준선**이다(전부 [사실], 출처 각 행).

| 비교사 | 분류 | 가격 | 시사점 |
|---|---|---|---|
| **Revuze** | VoC/리뷰 AI 분석 | **$30,000/년~** (커스텀) | 엔터프라이즈 전용. "no predefined themes" = 자동 토픽 발견. [Capterra](https://www.capterra.com/p/179229/Revuze/) |
| **Brandwatch** | 소셜리스닝·컨슈머 인텔 | 중견 **$20K~45K/년**, 엔터 **$60K~150K+/년** | 공개가 없음, 데이터량 과금. [vendr](https://www.vendr.com/marketplace/brandwatch), [costbench](https://costbench.com/software/social-media-management/brandwatch/) |
| **Talkwalker** | 컨슈머 인텔 | 1유저 **~$9K/년**, 10유저 $15~25K, 엔터 **$150K~** | 시트 아닌 데이터 소비량 과금, 무제한 유저. [itqlick](https://www.itqlick.com/talkwalker/pricing) |
| **skincareapi.dev** | 성분 API | **$49/월**(5만콜) · **$199/월**(50만콜) · PAYG **$0.01/콜·$0.05/스캔** | 우리 SkinMatch API의 직접 비교사·가격 천장. [pricing](https://skincareapi.dev/pricing) |
| **Yuka** | 성분 스캐너(B2C) | 유저펀딩 구독, **2024 매출 $7.3M**(98%가 구독), 7,300만 유저 | "광고·데이터판매 안 함" 신뢰모델. 우리 B2C 위젯의 반례·참고. [breakeven](https://breakevenpointcalculator.com/how-does-yuka-make-money-revenue-model-explained/), [foodtimes](https://www.foodtimes.eu/consumers-and-health/yuka-app-nutrition-health-and-market-opportunities/) |
| **WGSN** | 트렌드 포캐스팅 | **$15K~50K+/년**(표준 ~$25K) | 에디토리얼. 우리 Trend Index의 가격 천장. [gravelai](https://gravelai.com/blog/wgsn-vs-beauty-streams) |
| **Spate / Trendalytics** | AI 트렌드(검색·소셜) | 데모 기반 비공개 | 검색 신호 기반 → **리뷰·반응 신호는 우리 차별점**. [gravelai](https://gravelai.com/blog/wgsn-alternatives) |
| **Aspire / Upfluence / CreatorIQ** | 인플루언서 매칭 | Aspire **~$2K/월**($24~30K/년), Upfluence ~$2K/월, CreatorIQ **$35K~200K/년** | 우리 CreatorMatch의 비교사. 단 K-뷰티·서구 매칭+ER 예측은 빈틈. [stackinfluence](https://stackinfluence.com/influencer-marketing-platform-pricing-2025/) |

> VoC 텍스트 분석 시장 자체가 큼: VoC 소프트웨어 **$16.19B(2025)→$52B(2035)**, 텍스트 분석 **$43.85B(2034, CAGR 20.4%)**, 리테일·이커머스가 최대 40% 비중. ([사실] [custommarketinsights](https://www.custommarketinsights.com/report/voice-of-customer-voc-platform-market/), [trendxinsights](https://trendxinsights.com/syndicated-market-research-reports/text-analytics-market/))

---

## 2. 라인별 상세 (10개)

각 항목 형식: **무엇 / 누가 산다 / 팀자산 직결 / BM / 비교사·빈틈 / 데모 / 리스크**.

---

### C1. ReactionLens — 브랜드용 '외국인 반응' 인사이트 대시보드 ⭐데모 즉시

- **무엇**: K-뷰티 브랜드가 자사·경쟁사 SKU를 넣으면 Amazon·TikTok 리뷰에서 **영어권 소비자가 실제로 뭐라 반응하는지**(만족·불만·피부타입별·"sticky/irritated" 같은 공통 단점)를 토픽·감성·시계열로 보여주는 대시보드.
- **누가 산다**: 미국 진출 중인 인디/중견 K-뷰티 브랜드, 그들의 ODM(Cosmax·Kolmar), 리테일 MD.
- **팀자산 직결 ★★★★★**: Kbeauty_Analysis가 **이미 경쟁사 5곳 리뷰 1.2만 건을 TF-IDF/LDA로 분석**해 "Dr.Jart+ 보습 / COSRX 트러블 / PURITO 천연성분" 차별점과 공통 단점(Sticky·Irritated)을 뽑아낸 노트북이 존재. 그대로 제품 UI만 입히면 됨. ([사실] README)
- **BM**: SaaS 시트 단가 — Starter $X/월(1브랜드·3경쟁사), Pro(다SKU·알림·API). 비교사 기준 **연 $12K~45K** 레인지가 현실적(Brandwatch 중견 구간 아래에서 K-뷰티 특화로 침투).
- **비교사·빈틈**: Revuze($30K~)·Brandwatch·Talkwalker는 범용·고가·영어권 일반 카테고리. **빈틈 = "K-뷰티 + 성분·피부타입 축 + 한국 브랜드 친화 가격·언어"**. 우리는 성분 그래프와 결합해 "왜 불만인지(어떤 성분·포맷 때문인지)"까지 내려감.
- **데모**: ⭐ **즉시** — 기존 노트북 산출물 + GraphRAG 챗봇을 1화면 대시보드로 래핑. R1 피칭의 핵심 증거물.
- **리스크**: 리뷰 데이터 재수집 ToS(아마존), 신뢰성(샘플 편향) 라벨링 필요.

---

### C2. SkinMatch — 성분·효과·피부타입 매칭 API / 임베드 위젯 ⭐데모 즉시

- **무엇**: "민감 피부 + 히알루론산 함유 + 알코올 제외" 같은 **다조건(multi-hop) 질의에 제품·성분을 매칭**해주는 API와, 브랜드 자사몰·리뷰페이지에 꽂는 임베드 위젯("이 제품이 내 피부에 맞나?").
- **누가 산다**: 브랜드 자사몰(전환율·반품률 개선), K-뷰티 편집샵/리테일러, 앱 개발사.
- **팀자산 직결 ★★★★★**: **성분 498 + 효과 23 + 제품타입 46 노드의 지식그래프**가 핵심. GraphRAG가 "알러지 회피 등 safety에서 LightRAG 대비 11배 우세"로 검증됨 → **B2B에서 'safety'는 곧 책임·전환율**. ([사실] README, [docs/rag_evaluation_results](../../../../Kbeauty_Analysis/docs/rag_evaluation_results.md))
- **BM**: **API 호출 과금** — skincareapi.dev 천장($0.01/콜, $49/$199 월정액) 참조하되, **위젯은 화이트라벨 월구독**(브랜드 로고 단 SkinMatch). 전환율 향상 = 가치 명확.
- **비교사·빈틈**: skincareapi.dev·inciapi.com·dermalytics.dev는 **성분 사전 조회**가 주력(정적 데이터). **우리 빈틈 = "성분 그래프 + 실제 리뷰 반응 결합 추천"**(정적 안전성이 아니라 "이 피부타입은 실제로 만족했나") + **K-뷰티 SKU 커버리지**.
- **데모**: ⭐ **즉시** — `cosmetic_rag_chat`을 API 엔드포인트로 노출 + 간단 위젯. fresh clone 후 인덱싱 1회(~$0.06)면 가동. ([사실] README 빠른시작)
- **리스크**: 의학적 클레임 회피 문구 필수(MoCRA/FDA), 성분 DB 최신성 유지.

---

### C3. K-Beauty Trend Index — 글로벌 트렌드 인덱스 구독 🔶거의 즉시

- **무엇**: 영어권 리뷰·TikTok·검색 신호를 종합해 **성분·포맷·클레임별 "K-뷰티 트렌드 인덱스"**(예: "snail mucin 상승 +40%", "glass skin 포화", "PDRN 급부상")를 월간 리포트·대시보드로 구독 제공.
- **누가 산다**: 브랜드 마케팅·NPD팀, ODM 기획, VC/리테일 바이어, 미디어.
- **팀자산 직결 ★★★★☆**: TikTok 1,680영상·인플루언서 분석 + 리뷰 토픽 모델 + 성분 그래프 = **"무엇이 뜨는지"를 성분·효과 노드 단위로 인덱싱** 가능. K-Premium ERV(+4.76~5.10%p) 같은 정량 지표가 인덱스 신뢰도의 차별점. ([사실] README)
- **BM**: **리포트 구독** — Lite(월간 PDF) $X/월 · Pro(대시보드+API) · 엔터프라이즈(맞춤 추적). WGSN($15~50K/년) 대비 **K-뷰티 특화·1/3~1/5 가격**으로 침투.
- **비교사·빈틈**: WGSN·Beauty Streams는 에디토리얼·고가·범용. Spate·Trendalytics는 **검색 신호 기반**(소비자가 뭘 검색하나)이지 **리뷰 반응/실제 제품 신호가 아님** → 우리 빈틈은 **"리뷰·성분 결합 + 한국 공급망 시점"**. ([사실] [gravelai](https://gravelai.com/blog/wgsn-alternatives))
- **데모**: 🔶 **거의** — 기존 데이터로 "스냅샷 인덱스 1호" 샘플 리포트 1건 생성 가능. 정기 갱신 파이프라인은 추가 빌드.
- **리스크**: 정기 데이터 수집 파이프라인 운영비, 인덱스 방법론 신뢰성 공개.

---

### C4. ReguScan — 다국가 화장품 규제 스캐너 (US MoCRA · EU CPNP) 🔶부분 데모

- **무엇**: 브랜드가 성분표(INCI)·라벨을 넣으면 **US MoCRA(시설등록·제품리스팅·금지성분)와 EU CPNP(RP·PIF·CMR·나노)** 요건 대비 **결격 사유·필요 절차를 자동 점검**하는 스캐너 + 진출 체크리스트.
- **누가 산다**: 미국·EU 진출 인디 K-뷰티 브랜드(규제팀 없음), 수출 대행사, ODM.
- **팀자산 직결 ★★★☆☆**: 성분 그래프 + 화학·약학 이해가 **금지/규제성분 매핑**에 직결. 단 규제 룰셋은 새로 구축 필요(자산 직결도 중간).
- **BM**: **SaaS(브랜드별 월구독) + 건당 스캔 과금**(제품 리스팅 1건당). 규제 컨설팅 대비 1/10 가격으로 셀프서비스화.
- **규제 사실(타이밍)**:
  - [사실] **MoCRA**: 시설등록·제품리스팅 의무, **2년마다 갱신**, "responsible person"이 제출, 소규모 면제 있으나 눈·점막 접촉·주사·체내·24h+ 변형 제품은 면제 불가. FDA "Cosmetics Direct" SPL 툴. ([FDA](https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products))
  - [사실] **EU CPNP**: 무료 포털이나 **EU 역내 RP만 통지 가능 → 비EU 기업은 EU 대리인 지정 필수**, PIF·CMR·프레임포뮬러·나노(시판 6개월 전) 통지. ([EC](https://single-market-economy.ec.europa.eu/sectors/cosmetics/cosmetic-product-notification-portal_en))
- **비교사·빈틈**: REACH24H·Cosmedesk 등은 **컨설팅 서비스**(사람). **빈틈 = "셀프서비스 SaaS + K-뷰티 인디 가격대 + 성분그래프 자동매핑"**.
- **데모**: 🔶 **부분** — 금지성분 대조 + 체크리스트 생성기 MVP는 빠르게. 전체 SPL 제출 연동은 후행.
- **리스크**: 규제 오판 = 법적 책임 → "정보 제공, 법률 자문 아님" 디스클레이머 + 룰셋 최신성 운영 부담. **가장 무거운 운영 리스크.**

---

### C5. VOC Multilingual — 리뷰 다국어 번역·VOC 마이닝 ⭐데모 즉시

- **무엇**: 한국 브랜드가 **영·일·스페인어 등 다국어 해외 리뷰를 한국어로 번역 + VOC(불만·요청·칭찬) 자동 마이닝·태깅**해주는 API/대시보드. "외국인이 뭐라 하는지 한국어로 즉시 이해".
- **누가 산다**: 한국 본사 마케팅·CS·R&D팀(영어 리뷰를 못 읽어 의사결정이 늦는 브랜드).
- **팀자산 직결 ★★★★★**: 리뷰 분석 파이프라인 + RAG가 **그대로 VOC 추출 엔진**. 평가 하네스(faithfulness·context precision)로 **"환각 없는 요약"을 보증**하는 게 차별점(q08 봇 환각 검출 경험 보유). ([사실] README RAG eval)
- **BM**: **API 호출 과금(번역·태깅 건당) + SaaS 대시보드 구독**. 리뷰 1만 건 배치 처리 패키지.
- **비교사·빈틈**: Revuze·Brandwatch는 다국어 하지만 영어권 본사 타깃·고가. **빈틈 = "한국 브랜드향(출력이 한국어) + K-뷰티 성분·피부타입 온톨로지 태깅"**. 범용 번역(DeepL)은 VOC 구조화를 안 함.
- **데모**: ⭐ **즉시** — 영어 리뷰 → 한국어 VOC 카드(불만 Top5·요청 Top5) 생성 데모를 기존 데이터로 바로.
- **리스크**: 번역 품질·뉘앙스(피부 표현), LLM 비용 관리.

---

### C6. CreatorMatch — 인플루언서↔브랜드 매칭 데이터 ⭐데모 즉시

- **무엇**: K-뷰티 브랜드에 **"실제로 매출·참여를 일으킬" 서구 인플루언서를 추천**. 단순 팔로워가 아니라 **ER%(참여율) 예측 기반** 매칭. 시드 인플루언서 2명만 넣으면 닮은꼴을 추천.
- **누가 산다**: 미국·EU 진출 K-뷰티 브랜드, 인플루언서 에이전시, ODM 마케팅.
- **팀자산 직결 ★★★★★**: **추천 알고리즘 ver.4가 무작위 대비 3.25배 ER%를 1,540조합 부트스트랩으로 검증**. 게다가 K-Premium의 95%가 **인플루언서 selection effect**라는 발견 = "키워드 말고 사람을 골라라"가 곧 제품 가치 제안. ([사실] README, [docs/refactor/14](../../../../Kbeauty_Analysis/docs/refactor/14_kpremium_number_history.md))
- **BM**: **SaaS 시트 + 매칭 성과 과금**(추천→계약 시 수수료) 하이브리드. 팀의 글로벌 인플루언서 네트워크(180개국)와 결합 시 공급측 우위.
- **비교사·빈틈**: Aspire(~$2K/월)·Upfluence·CreatorIQ($35K~200K/년)는 **검색·관리 툴**이지 **"ER% 인과 예측"이 아님**. **빈틈 = "K-뷰티 특화 + within-FE로 검증한 selection 모델 + 한국 브랜드 가격대"**. ([사실] [stackinfluence](https://stackinfluence.com/influencer-marketing-platform-pricing-2025/))
- **데모**: ⭐ **즉시** — 56명 인플루언서 풀에서 "시드 2명 → Top10 추천" 라이브 데모(이미 노트북 존재).
- **리스크**: 인플루언서 데이터 신선도, 매칭 ToS, 팀 본진(GLOU B2C)과의 자원 분산.

---

### C7. ClaimGuard — 짝퉁·그린워싱·효능클레임 검증 🔶부분 데모

- **무엇**: ①브랜드/리테일러용 **짝퉁·가짜리뷰 탐지**(리뷰 패턴·배치코드·셀러 신호) ②**그린워싱/효능클레임 검증**("clean"·"hypoallergenic"·"clinically proven"이 성분·리뷰로 뒷받침되나).
- **누가 산다**: 브랜드(자사 보호·경쟁사 모니터링), 리테일러, 규제 대응팀.
- **팀자산 직결 ★★★★☆**: 성분 그래프(클레임↔성분 검증) + 리뷰 분석(가짜 패턴) + RAG 평가 하네스의 **환각/노이즈 검출 경험**이 직결. ([사실] README)
- **BM**: **건당 검증 리포트 + SaaS 모니터링 구독**.
- **시장·규제 사실(타이밍)**:
  - [사실] 영국 Which? 조사: 온라인 마켓 화장품의 **2/3(67%)가 위조 가능성**, FDA가 2023년 Amazon·TikTok Shop 1,200+ 리스팅을 변조·미신고 스테로이드/수은/하이드로퀴논으로 적발. Amazon은 2025년 가짜 리뷰 수억 건 차단. ([forgestop](https://www.forgestop.com/blog/fake-cosmetics-nfc-smart-label-authentication), [aboutamazon](https://www.aboutamazon.com/news/policy-news-views/amazon-trustworthy-shopping-experience-report-2025))
  - [사실] **EU 그린클레임 지령(EU 2024/825) 2026년 9월 27일 시행** — "eco-friendly·biodegradable" 등 모호한 환경 클레임 금지, **제3자 검증·QR 증빙 의무화**, EU 녹색 클레임 53%가 모호·오인. → **검증 SaaS의 직접 수요 트리거**. ([greenwashing-checker](https://greenwashing-checker.com/en/blog/eu-green-claims-directive-2026-complete-guide/), [natrue](https://natrue.org/eu-directives-tackle-greenwashing/))
- **비교사·빈틈**: NFC 스마트라벨(ForgeStop 등)은 물리 인증. **우리 빈틈 = "데이터 기반(리뷰+성분) 클레임·짝퉁 검증" + K-뷰티 + 2026 그린클레임 대응 타이밍**.
- **데모**: 🔶 **부분** — "이 클레임이 성분·리뷰로 뒷받침되나" 검증 데모는 빠르게. 짝퉁 탐지 정확도는 데이터 더 필요.
- **리스크**: 오탐(브랜드 명예훼손 리스크), 짝퉁 탐지의 한계.

---

### C8. IngredientDemand — OEM/ODM용 신성분 수요예측 🔶부분 데모

- **무엇**: ODM·브랜드 NPD팀에게 **"다음에 뜰 성분·포맷"을 리뷰·트렌드 신호로 예측**. "어떤 성분 조합이 어떤 피부타입에서 만족·미충족 수요가 큰가"를 데이터로.
- **누가 산다**: Cosmax·Kolmar 같은 ODM, 브랜드 R&D/NPD, 원료사.
- **팀자산 직결 ★★★★☆**: 성분 498 노드 그래프 + 리뷰의 "미충족 불만(unmet)" 매핑 = **수요예측의 정확한 입력**. Kbeauty 본진의 "키워드<사용경험·피부타입" 인사이트가 곧 방법론. ([사실] README)
- **BM**: **엔터프라이즈 구독(ODM/원료사)** — 분기별 성분 수요 리포트 + API.
- **시장·검증 사실**: [사실] 화장품 OEM/ODM 시장 **$73.24B(2025)→$126B(2035)**, Cosmax 14~18%·Kolmar 12~15% 점유, 2023~24 신제품 41%가 바이오텍 성분, **Kolmar는 이미 AI 포뮬레이션으로 개발기간 38% 단축**(= AI 데이터 수요 입증). ([globalgrowthinsights](https://www.globalgrowthinsights.com/market-reports/cosmetics-oem-and-odm-market-103536), [futuremarketinsights](https://www.futuremarketinsights.com/reports/demand-and-trend-analysis-of-cosmetics-odm-in-korea))
- **비교사·빈틈**: WGSN·Mintel은 거시 트렌드. **빈틈 = "성분·포맷 단위 + 미충족 수요(리뷰 기반) + 피부타입 세그먼트"**. ODM이 가장 원하는 입자도.
- **데모**: 🔶 **부분** — "성분 X의 만족·미충족 맵" 1샘플은 가능. 예측 모델은 시계열 데이터 축적 필요.
- **리스크**: 예측 정확도 검증의 시간(B2B 신뢰), ODM 영업 사이클 길다.

---

### C9. GapReport — 해외 신제품 셰이드/포맷 갭 리포트 ⭐데모 즉시

- **무엇**: 브랜드에 **"영어권 시장에 비어 있는 셰이드/포맷/가격대"**를 리뷰·리뷰 미충족 신호로 리포트. 예: "deep tone 파운데이션 미충족", "민감성 + 무향 + 스틱 포맷 공백".
- **누가 산다**: 미국 진출 브랜드, ODM 기획, 리테일 바이어.
- **팀자산 직결 ★★★★☆**: 본진이 **"경쟁사 공통 단점(Sticky·Irritated) 보완으로 빈자리 찾기"**를 이미 실증 — 그 방법론을 셰이드/포맷 축으로 확장. ([사실] README)
- **BM**: **리포트 단건 판매 + 구독**(분기 갱신). 진출 의사결정 1건당 고가 가능.
- **시장 사실(수요 증거)**: [사실] **Fenty Effect** — 40셰이드 출시 후 40일 $1억 매출, "40셰이드"가 업계 표준화. 단 40개 중 30개가 light/tan에 몰리면 무의미 → **"진짜 갭"은 데이터로만 보임**(MUFE 40 중 31개가 60~90 명도). = 우리 리포트의 존재 이유. ([fashionmagazine](https://fashionmagazine.com/beauty-grooming/fenty-effect-40-foundation-shades/), [pudding.cool](https://pudding.cool/2018/06/makeup-shades/))
- **비교사·빈틈**: 범용 트렌드 리포트는 "셰이드 갭" 입자도까지 안 감. **빈틈 = "리뷰 미충족 + 셰이드·포맷·피부톤 세그먼트 결합"**.
- **데모**: ⭐ **즉시** — 기존 리뷰 데이터로 "포맷/단점 갭" 1페이지 샘플 리포트 즉시 생성.
- **리스크**: 셰이드 데이터(이미지·톤)는 추가 수집 필요할 수 있음(리뷰 텍스트 갭은 즉시).

---

### C10. GLOU Data Co-op — B2C 데이터의 B2B 환류 🔶후행

- **무엇**: GLOU(B2C)가 모은 **외국인 유저의 실제 사용·반응·피부타입 1차 데이터**를 익명·집계해 위 C1~C9 제품의 **독점 데이터 레이어**로 환류. "남의 리뷰"가 아니라 "우리 유저의 검증된 반응".
- **누가 산다**: 위 모든 B2B 라인의 데이터 공급원(내부) + 브랜드(라이선스).
- **팀자산 직결 ★★★★★**: **듀얼트랙의 심장** — GLOU가 데이터를 만들고 B2B가 수익화하는 플라이휠. [12_idea_scoring.md](../market/12_idea_scoring.md) 권고("하나의 자산을 두 방향으로")의 실체.
- **BM**: **데이터 라이선스(집계·익명)** + 내부 데이터 비용 절감.
- **데모**: 🔶 **후행** — GLOU 유저 확보 후. R1에서는 "구조 설계 + C1 데모"로 서사만.
- **리스크**: 개인정보(GDPR·동의), 콜드스타트(유저 확보 선행 필요).

---

## 3. 권고 — R1 발표용 우선순위

```
[공유 엔진]  K-뷰티 리뷰 RAG + 성분·효과 그래프(498성분) + 인플루언서 ER 모델
   │
   ├─ 데모 1순위(즉시·자산직결★★★★★): C1 ReactionLens · C2 SkinMatch · C6 CreatorMatch
   ├─ 서사 보강(타이밍 강력): C7 ClaimGuard(2026.9 EU 그린클레임) · C4 ReguScan(MoCRA)
   └─ 환류 설계: C10 Data Co-op = "GLOU(B2C)가 데이터, B2B가 수익" 플라이휠
```

- **R1 피칭 한 문장**: *"우리는 이미 돌아가는 K-뷰티 데이터 엔진(ReactionLens·SkinMatch·CreatorMatch 데모)이 있고, 그걸 외국인 큐레이션(GLOU)으로 푼다. 같은 엔진, 두 방향 수익화."*
- **데모 3종(C1·C2·C6)**은 Kbeauty_Analysis fresh clone + 인덱싱 1회(~$0.06)로 **이번 주 안에 라이브 가능**. ([사실] README 빠른시작)
- **가장 강한 타이밍 카드 = C7 ClaimGuard**(EU 그린클레임 2026-09 시행, 제3자 검증 의무) + **시장 카드 = K-뷰티 US $2B·+37%·수출 1위국**.
- **운영 리스크 최고 = C4 ReguScan**(법적 책임), **자원 분산 주의 = C6**(GLOU 본진과 경쟁).

---

## 출처 (전체)

- Kbeauty_Analysis 팀자산: [../../../../Kbeauty_Analysis/README.md](../../../../Kbeauty_Analysis/README.md), [docs/rag_evaluation_results.md](../../../../Kbeauty_Analysis/docs/rag_evaluation_results.md), [docs/refactor/14](../../../../Kbeauty_Analysis/docs/refactor/14_kpremium_number_history.md)
- 비교사 가격: Revuze [Capterra](https://www.capterra.com/p/179229/Revuze/) · Brandwatch [vendr](https://www.vendr.com/marketplace/brandwatch) [costbench](https://costbench.com/software/social-media-management/brandwatch/) · Talkwalker [itqlick](https://www.itqlick.com/talkwalker/pricing) · skincareapi [pricing](https://skincareapi.dev/pricing) · Yuka [breakeven](https://breakevenpointcalculator.com/how-does-yuka-make-money-revenue-model-explained/) [foodtimes](https://www.foodtimes.eu/consumers-and-health/yuka-app-nutrition-health-and-market-opportunities/) · WGSN/Spate/Trendalytics [gravelai](https://gravelai.com/blog/wgsn-vs-beauty-streams) [gravelai-alt](https://gravelai.com/blog/wgsn-alternatives) · 인플루언서 [stackinfluence](https://stackinfluence.com/influencer-marketing-platform-pricing-2025/)
- 규제: MoCRA [FDA](https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products) · CPNP [EC](https://single-market-economy.ec.europa.eu/sectors/cosmetics/cosmetic-product-notification-portal_en) · 그린클레임 [greenwashing-checker](https://greenwashing-checker.com/en/blog/eu-green-claims-directive-2026-complete-guide/) [natrue](https://natrue.org/eu-directives-tackle-greenwashing/)
- 시장: K-뷰티 US [CNBC](https://www.cnbc.com/2025/11/27/k-beauty-tiktok-makeup.html) [awisee](https://awisee.com/blog/k-beauty-market-us-sales-trends/) [beautymatter](https://beautymatter.com/articles/k-beautys-export-boom-is-no-longer-a-trend-story) · VoC/텍스트 [custommarketinsights](https://www.custommarketinsights.com/report/voice-of-customer-voc-platform-market/) [trendxinsights](https://trendxinsights.com/syndicated-market-research-reports/text-analytics-market/) · OEM/ODM [globalgrowthinsights](https://www.globalgrowthinsights.com/market-reports/cosmetics-oem-and-odm-market-103536) [futuremarketinsights](https://www.futuremarketinsights.com/reports/demand-and-trend-analysis-of-cosmetics-odm-in-korea) · 짝퉁 [forgestop](https://www.forgestop.com/blog/fake-cosmetics-nfc-smart-label-authentication) [aboutamazon](https://www.aboutamazon.com/news/policy-news-views/amazon-trustworthy-shopping-experience-report-2025) · 셰이드 갭 [fashionmagazine](https://fashionmagazine.com/beauty-grooming/fenty-effect-40-foundation-shades/) [pudding.cool](https://pudding.cool/2018/06/makeup-shades/)
- RAG 기술: LightRAG [arxiv](https://arxiv.org/abs/2410.05779)
