# 미션 H — 수익모델 벤치마크 라이브러리

> 작성일 2026-07-01 / GLOU 팀(외국인 × K-뷰티 × 서울) 수익구조 근거 라이브러리
> 표기 규칙: [사실] = 출처에 명시된 수치 / [추정] = 출처 기반 추론 또는 범위 추정
> 주의: 비공개 가격(SaaS 다수)은 3자 추정치이므로 협상 실제값과 다를 수 있음. 환율·시점 차이 유의.

---

## 1) 예약/마켓플레이스 take-rate

| 회사 | 수익구조 | take-rate / 수수료 | 근거 |
|---|---|---|---|
| **Treatwell** (유럽) | 신규고객 송객 수수료 + SaaS + 결제수수료 | 신규고객 첫 예약 **35% (+VAT)**, 재방문(365일 내) **0%**, 선결제 거래 **2%** | [사실] |
| **Fresha** (글로벌) | 신규고객 수수료 + 저가 구독 + 결제수수료 | 마켓플레이스 신규고객 **20% (1회, 최소 $6)**, 재방문 0%, 온라인 결제 2.79%+$0.20, 구독 $19.95~/월~ | [사실] |
| **Booksy** (글로벌) | Boost(성과형) 신규고객 수수료 + $29.99/월 구독 | Boost 신규고객 첫 방문 **30%** (최소 $10, 최대 $100), 재방문 0% | [사실] |
| **StyleSeat** (미국) | New Client Connection 수수료 + 구독 | 신규고객 **30%** (Basic, 최대 $50) / **20%** (Premium), 재방문 0% | [사실] |
| **GoWabi** (태국, 뷰티 특화) | 예약 건당 커미션 (가입·월비 무료) | 정확한 % 미공개. "예약 발생 시에만 커미션" 모델 | [사실](% 비공개) |
| **Klook** (아시아 OTA) | 머천드 커미션 + 1P 인벤토리 + B2B 솔루션 | 카테고리별 **15~25%** (보고 범위 10~35%), **블렌디드 take-rate ~18%** (IPO S-1) | [사실] |
| **Creatrip** (한국, 외국인 관광) | 어필리에이트 + 직접 예약 커미션 | 어필리에이트 파트너 **최대 8%** 수익배분 (직접 파트너는 최대 40% 언급). 2025년 뷰티·의료가 거래액 **51%**(피부과 36%) | [사실] |
| **강남언니(힐링페이퍼)** (한국) | **광고 모델**(송객 수수료 폐지) | 2019년부터 송객 수수료 X → 성과형 광고 + 배너 + 크로스보더. 2023 매출 **417억원**, 영업이익 **122억원**(첫 흑자전환) | [사실] |

**언제 돈이 되나:** 송객형(Treatwell/Fresha/Booksy/StyleSeat)은 *신규고객 한 번에 20~35%를 떼되 재방문은 0%* → 플랫폼이 "신규 유입 채널" 역할을 할 때만 정당화됨. 단가 높은 시술(피부·성형)일수록 1건 커미션 절대액이 커져 유리.

**GLOU 적용 주의:** 한국은 **의료광고·의료법 규제**로 시술 송객 수수료 자체가 위법 소지(강남언니가 2015~2018 송객 모델로 형사처벌 후 광고 모델 전환). 의료/시술 영역은 **광고비 모델**로, 비의료 뷰티 서비스(헤어·네일·메이크업·체험)는 송객 커미션이 가능. 외국인 타깃이면 Creatrip식 **어필리에이트(~8%)** + 직접예약 커미션 혼합이 규제·진입 측면에서 현실적.

---

## 2) B2B SaaS / 데이터 (리뷰·소비자 인텔리전스)

| 회사 | 수익구조 | 구독가 / 단가 | 근거 |
|---|---|---|---|
| **Revuze** | 연 구독 (소비자 인사이트 AI) | **$30,000/년~**, 커스텀 | [사실] |
| **Brandwatch** | 연 계약 (소셜 리스닝), 비공개 | 중소 $1k~15k, 미드 **$20k~45k**, 엔터프라이즈 **$60k~150k+/년** + 도입비 $5k~20k | [추정](3자 견적) |
| **Talkwalker** | 데이터량 기반 연 구독, 비공개 | 엔터프라이즈 **$13k~100k/년** (중앙값 ~$27k), Core ~$500/월 | [추정](3자 견적) |
| **Yuka** (B2C 스캐너) | **순수 프리미엄 구독**(광고·데이터판매 X) | 연 **$10~20** 자율 가격, 2024 구독매출 $7.17M = 매출의 **98.1%**, 누적 7천만+ 다운로드 | [사실] |

**언제 돈이 되나:** B2B 인텔리전스는 *연 $20k~150k 고가 연단위 계약* → Fortune500·브랜드 본사가 "VoC/디지털셸프 최적화"에 예산을 쓸 때 성립. ACV가 크므로 소수 고객으로도 수익. Yuka형 B2C는 *대규모 무료 사용자 → 1~5% 유료전환*으로만 성립(70M 다운로드 규모 필요).

**GLOU 적용 주의:** 데이터/API 모델은 **신뢰 가능한 K-뷰티 리뷰·성분 데이터셋**이라는 독점 자산이 선결 조건. 초기엔 엔터프라이즈 영업 사이클(6~12개월)이 길어 현금흐름 부담 → 리포트 단발 판매(PDF·시트)로 캐시 브리지를 깔고, 정착 후 연구독 전환 권장.

---

## 3) 크리에이터 마켓플레이스

| 회사 | 수익구조 | 수수료 / 구독 | 근거 |
|---|---|---|---|
| **Collabstr** | 거래 수수료 (브랜드+크리에이터 양면) + 구독 | 브랜드 **10%**(Free/Pro) → **5%**(Premium), 크리에이터 **15%** payout, 구독 $299~399/월 | [사실] |
| **Insense** | 구독(SaaS) | $450/월(분기) → 연납 $350/월, Advanced $1,300→$1,000/월 | [사실] |
| **Aspire** | 구독(엔터프라이즈) | **$1,000~2,000/월~** (연약정), 커스텀 | [추정](3자) |

**언제 돈이 되나:** Collabstr형 *양면 take(브랜드 10% + 크리에이터 15% = 합산 ~25%)*는 거래가 에스크로로 묶여 결제 안전성이 확보될 때. Insense/Aspire형 *순수 구독*은 브랜드가 캠페인을 반복 운영(월 수십 건)할 때 ROI가 나서 이탈 안 함.

**GLOU 적용 주의:** 한국 K-뷰티 크리에이터 × 해외 브랜드 매칭이면 **양면 take 모델**이 유리(외국 브랜드는 단발 협업도 결제). 다만 거래 신뢰(에스크로·환불·콘텐츠 라이선스) 인프라가 수수료 정당화의 핵심. 초기 GMV가 작으면 구독 단독은 어려움.

---

## 4) 구독박스 · 미디어

| 회사 | 수익구조 | ARPU / 가격 / 이탈 | 근거 |
|---|---|---|---|
| **Ipsy** | 월 구독 박스 | $14/월(Original), 글로벌 매출 추정 폭 넓음($215M~$500M+ 보고 상이), 구독자 300만~400만 | [사실](수치 출처별 상이) |
| **Birchbox** | 월 구독 박스 | $10~15/월, 구독자 ~25만(피크 후 감소), 월 이탈 추정 ~8~12% | [추정](과거 데이터) |
| **Substack** | 크리에이터 구독 매출 take | **10%** + Stripe(실효 13~16%) | [사실] |
| **Patreon** | 크리에이터 구독 매출 take | **10%**(2025.8~ 신규 전원), 실효 12~15%, iOS는 Apple 30% 추가 | [사실] |

**언제 돈이 되나:** 구독박스는 *월 이탈 8~12%를 LTV가 견딜 때*만 성립 → 박스 원가(샘플은 브랜드 협찬으로 원가↓) + 재구매로 메움. 콘텐츠 플랫폼(Substack/Patreon)은 *take 10%* 단순 모델이라 크리에이터가 큰 매출을 올려줄 때만 절대 수익 확보(롱테일).

**GLOU 적용 주의:** 뷰티 구독박스는 **월 8~12% 이탈**이 구조적 → CAC 회수에 보통 6~10개월. 외국인 대상이면 *국제배송비*가 ARPU를 잠식하므로 디지털(콘텐츠/큐레이션) 구독 또는 한국 내 수령형 모델로 물류비를 회피하는 설계가 안전.

---

## 5) 어필리에이트 · 리드젠

| 유형 | 대표 수치 | 근거 |
|---|---|---|
| 뷰티 어필리에이트 커미션 | **Sephora 5~10%**, Ulta ~2%, 일반 뷰티 프로그램 평균 5~10% (쿠키 24h~30일) | [사실] |
| 의료·에스테틱 **리드젠 CPL** | Meta Ads **$5~10/리드**, Google Search **$45~120/리드**, Google LSA **$20~40/리드** (미국 기준) | [사실] |

**언제 돈이 되나:** 어필리에이트는 *트래픽 볼륨 × 전환율*이 충분할 때(평균 5~10% 커미션은 박해서 대량 필요). 리드젠은 *리드당 단가 < 고객 LTV × 전환율*일 때 → 시술 단가 높은 의료/에스테틱이 CPL $45~120도 감당 가능.

**GLOU 적용 주의:** 외국인×K-뷰티 트래픽은 어필리에이트 커미션(5~10%)으로 초기 수익화가 빠르나 절대액이 작음. 의료 리드젠은 *클리닉이 외국인 환자 1명 LTV를 크게 보므로* 한국 시장에서 CPL 단가를 더 높게 받을 여지(단, 의료광고법 검토 필수).

---

## 6) 인바운드 관광 OTA (한국 사례 우선)

| 회사 | GMV / 거래액 | 수수료(take) | 근거 |
|---|---|---|---|
| **MyRealTrip** (한국) | 2025 거래액 **2.3조원**(YoY +45%), 매출 **1,100억원+** 전망, 국내 1호 OTA IPO 준비 | OTA 통상 **15~30%/건**(MRT 자체 % 미공개) | [사실]+[추정] |
| **Klook** | GTV ~$3B, 2024 매출 $417.1M | 블렌디드 **~18%** (15~25% 카테고리별) | [사실] |
| **Trazy** (한국) | 미공개 | K-뷰티 트리트먼트·K-pop·체험 판매, OTA 통상 15~30% | [추정] |
| **Creatrip** (한국) | MAU 160만, 뷰티·의료 거래 비중 **51%**, YoY +71% | 어필리에이트 ~8% + 직접예약 커미션 | [사실] |

**언제 돈이 되나:** 인바운드 OTA는 *GMV 규모 × take 15~30%* → 거래액이 조 단위로 커져야 의미. 단, K-뷰티/의료처럼 **객단가 높은 카테고리**는 같은 GMV로도 커미션 절대액이 커 수익 효율 우수(Creatrip이 의료·뷰티에 집중하는 이유).

**GLOU 적용 주의:** 한국 인바운드 시장은 MyRealTrip(2.3조)·Creatrip(MAU 160만) 등 강한 선점자 존재 → *수평 OTA 경쟁은 비현실적*. GLOU는 "외국인 × K-뷰티 × 서울"의 **버티컬 깊이**(예: 시술 예약+통역+사후관리)로 단가·재방문을 높여 take를 정당화하는 전략이 적합. 의료 영역은 강남언니 선례대로 **수수료가 아닌 광고/구독** 모델로 우회.

---

## 출처 (원문 링크 유지)

- Fresha: https://www.fresha.com/help-center/knowledge-base/billing-and-fees/188-marketplace-new-client-fees , https://www.fresha.com/pricing
- Treatwell: https://www.treatwell.co.uk/partners/pricing/ , https://partners.treatwell.com/hc/en-gb/articles/360015011760-How-does-Treatwell-s-commission-work-
- Booksy: https://support.booksy.com/hc/en-us/articles/16486248108946-How-does-Boost-pricing-work , https://biz.booksy.com/en-us/pricing
- StyleSeat: https://styleseat.freshdesk.com/support/solutions/articles/69000837158-how-new-client-connection-works-for-each-plan , https://pabau.com/blog/styleseat-pricing/
- GoWabi: https://www.gowabi.com/en/partner , https://www.gowabi.com/customer_faq/?m=guide
- Klook: https://www.mostlymetrics.com/p/klook-ipo-s1-breakdown , https://www.sambahq.com/ota-supplier-guide/ota-commission-rates , https://getlatka.com/companies/klook
- Creatrip: https://affiliate.creatrip.com/en , https://en.sedaily.com/technology/2026/02/11/travel-platform-with-16-million-foreign-users-bets-big-on-k
- 강남언니/힐링페이퍼: https://dealsite.co.kr/articles/124815 , https://www.news2day.co.kr/article/20240315500244 , https://thevc.kr/healingpaper
- Revuze: https://www.capterra.com/p/179229/Revuze/ , https://www.getapp.com/marketing-software/a/revuze/
- Brandwatch: https://checkthat.ai/brands/brandwatch/pricing , https://www.vendr.com/marketplace/brandwatch
- Talkwalker: https://checkthat.ai/brands/talkwalker/pricing , https://prowly.com/magazine/talkwalker-pricing/
- Yuka: https://breakevenpointcalculator.com/how-does-yuka-make-money-revenue-model-explained/ , https://yuka.io/en/premium-member/ , https://yuka.io/en/independence/
- Collabstr: https://collabstr.com/pricing , https://www.creatorstackclub.com/software/collabstr
- Insense/Aspire: https://insense.pro/pricing , https://insense.pro/blog/insense-vs-aspire-io , https://www.ugcroster.com/blog/brands/aspire-influencer-platform-pricing-roi-breakdown
- Ipsy/Birchbox: https://fourweekmba.com/how-does-ipsy-make-money/ , https://www.mysubscriptionaddiction.com/ipsy-vs-birchbox-which-beauty-subscription-box-offers-the-best-value , https://sell.cratejoy.com/blog/what-is-birchboxs-monthly-churn-rate/
- Substack/Patreon: https://www.ruzuku.com/learn/articles/substack-pricing , https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview , https://paprika.bot/blog/substack-fees/
- 뷰티 어필리에이트: https://www.creator-hero.com/blog/sephora-affiliate-program-in-depth-review-pros-and-cons , https://www.authorityhacker.com/beauty-affiliate-programs/
- 의료 리드젠 CPL: https://beautybrandbuilders.co/cost-per-lead-benchmarks-for-med-spas-explained/
- MyRealTrip: https://koreatechdesk.com/koreas-first-ota-ipo-myrealtrip-mirae-asset-travel-tech , https://www.cbinsights.com/company/myrealtrip
- Trazy: https://stayfi.com/vrm-insider/2025/11/04/ota-fees/
