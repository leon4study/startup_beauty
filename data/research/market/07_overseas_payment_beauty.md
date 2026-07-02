# 07. 해외 결제·예약 시스템 & 해외 뷰티/생활정보 서비스 벤치마크

> 조사일: 2026-06-30 | 프로젝트: GLOU (외국인 대상 서울 라이프+K-뷰티 큐레이션·예약·결제 플랫폼)
> 핵심 페인포인트: 외국인은 ARC·한국 전화번호가 없어 네이버예약/캐치테이블/카카오 결제가 아예 안 된다.
> [사실] = 출처로 확인된 사실 / [추정] = 조사자 해석·추론

---

## A. 해외 결제·예약 시스템

### A-1. 마켓플레이스 결제·정산 인프라

#### Stripe Connect (마켓플레이스 표준)
- [사실] Stripe Connect는 플랫폼이 연결된 매장(connected account) 대신 결제를 처리하고 정산 시 자금을 분배하는 마켓플레이스 인프라. 46개국·135개+ 통화 지원. 출처: https://stripe.com/connect , https://docs.stripe.com/connect
- [사실] `application_fee`로 플랫폼 수수료를 분리 차감 가능. 전체 금액을 매장에 보내는 대신 일부를 플랫폼 수수료로 떼고, Stripe 수수료는 플랫폼이 부담하므로 매장이 보는 것은 application_fee뿐. 출처: https://docs.stripe.com/connect/marketplace/tasks/app-fees
- [사실] charge 모델 2종 — direct charge / destination charge. 결제마다 split 비율을 설정 가능(상품·매장·모델별 차등 가능), payout 스케줄(롤링/주기) 커스터마이즈 가능. 출처: https://docs.stripe.com/connect/charges
- [사실] **사전승인(pre-auth, place a hold)**: 결제수단에 hold를 걸어 자금을 예약했다가 나중에 capture. 호텔이 체크인 전 전액 승인 후 체크아웃 시 capture하는 방식과 동일 → 예약 보증금/노쇼 방지에 그대로 적용 가능. 온라인 카드결제 표준 승인 유효기간 7일, **extended authorization 최대 30일**(Visa/MC/Amex/Discover 한정). 출처: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method , https://docs.stripe.com/payments/extended-authorization

#### Adyen for Platforms (엔터프라이즈)
- [사실] split_items 배열에 BalanceAccount/Commission/VAT 등 타입별 할당. 수동/자동 룰 기반 split, delayed payout, delayed capture 지원. 출처: https://www.sharetribe.com/academy/marketplace-payments/adyen-for-platforms-overview/
- [추정] 연 $10M+ 고볼륨 마켓플레이스용. 엔터프라이즈 최소 약정·복잡한 연동으로 초기 스타트업엔 부적합 → **GLOU MVP는 Adyen 부적합, Stripe Connect 권장**. 출처: https://dodopayments.com/blogs/stripe-connect-alternatives
- [사실] Adyen 2025년 Intelligent Money Movement(money-in/관리/money-out 통합 레이어) 출시. 출처: https://www.airwallex.com/en-us/blog/stripe-vs-adyen-comparison

#### 게스트 체크아웃 / 노쇼 방지
- [사실] Stripe로 계정 없이 카드만으로 게스트 결제 가능. hold(사전승인)로 보증금 확보 후 노쇼 시 capture, 정상 방문 시 release/부분 capture(나머지는 즉시 환불). 출처: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method

### A-2. 지갑·간편결제·멀티통화·BNPL

#### BNPL (Klarna / Afterpay)
- [사실] BNPL 핵심: **매장은 전액을 선지급(upfront) 받고**, BNPL사가 소비자에게서 분할로 회수 → 매장 현금흐름 안정. Klarna: Pay in 4 / 30일 후납 / 최대 24개월 할부. Afterpay: 6주 4회(보통 25% 선납). 출처: https://www.shopify.com/blog/what-is-klarna
- [사실] 매장 수수료 — Klarna 3.29~5.99% + $0.30, Afterpay 4~6% + $0.30. Afterpay는 매장 지급에 최대 영업일 5일 소요. 출처: https://www.hulkapps.com/blogs/ecommerce-hub/how-does-klarna-make-money-klarna-business-model-in-a-nutshell
- [추정] GLOU의 외국인 고객(특히 미국/호주/유럽)에게 Klarna/Afterpay는 익숙 → 고가 시술(피부과/헤어) 전환율 제고에 유효. 단 한국 매장 정산은 Stripe Connect로, BNPL은 소비자측 결제수단으로만 노출하는 게 현실적.

#### 지갑·멀티통화
- [추정·일반] Apple Pay/Google Pay는 Stripe Checkout에서 토글로 활성화 가능 → 외국인 카드를 Wallet에 넣어 쓰는 흐름이 한국 로컬앱 대비 마찰이 적음.
- [사실] Alipay+/WeChat Pay = 중국·홍콩·동남아 인바운드 핵심(아래 A-4 한국 현실 참조).

### A-3. 글로벌 예약 플랫폼의 결제 처리 (벤치마크)

| 플랫폼 | 신규고객 수수료 | 결제처리 | 매장 정산/payout | 노쇼·보증금 |
|---|---|---|---|---|
| **Fresha** | 마켓플레이스 신규고객 20%(최소 $6), 재방문/직접링크 0% | 카드 2.19%+$0.20(+추가 1%대 가능) | 카드 on file, 선결제 deposit 지원 | 노쇼/지각취소 수수료를 저장 카드에 청구 |
| **Treatwell** | 신규고객 첫 예약 ~20~35%(최대 35%), 재방문/위젯은 저율 | 온라인 2.5%+VAT | SaaS 구독(€29~100+/월) + 거래 커미션 혼합 | 예약 시 부분/전액 선결제 → 시술 후 차감 |
| **Booksy** | 구독제(£40/월 또는 $29.99/mo), 마켓플레이스 커미션 낮음 | Tap to Pay 0.99%+20p+VAT | 구독+결제수수료 | deposit과 cancellation fee 구분 운영 |
| **Klook** | 매장 커미션 15~25%(협상·일부는 도매매입 후 리셀) | 20개+ 언어·40개+ 통화·글로벌 결제수단, 시장별 로컬결제 | 플랫폼이 고객 결제 수금 후 매장에 정산 | 플랫폼 선결제(prepaid) 모델 |
| **GetYourGuide** | 국가별 20~30%(표준 시작 ~30%) | 플랫폼이 전액 수금, 매장은 고객 돈 안 만짐 | 월정산(격주 5·20일은 +2% 추가) | 예약시 선결제 |
| **Viator** | 보통 20~25% | 플랫폼이 예약시점 수금, 매장 결제 미관여 | 여행 월 종료 후 21영업일 내(은행/PayPal) | 예약시 선결제 |

- [사실] Fresha 출처: https://www.fresha.com/pricing , https://www.fresha.com/help-center/knowledge-base/payments/617-charge-no-show-and-cancellation-fees
- [사실] Treatwell 출처: https://businessmodelcanvastemplate.com/blogs/how-it-works/treatwell-how-it-works , https://partnercare.treatwell.com/s/article/How-does-Treatwell-s-commission-work
- [사실] Booksy 출처: https://support.booksy.com/hc/en-us/articles/16465247608594 , https://glossgenius.com/blog/booksy-price
- [사실] Klook 출처: https://businessmodelhub.in/klook-business-model-how-klook-makes-money/ , https://arival.travel/article/inside-klook-and-asias-ascendant-tours-activities-sector/
- [사실] GetYourGuide/Viator 출처: https://automate.travel/blog/viator-vs-getyourguide-for-operators/ , https://www.sambahq.com/ota-supplier-guide/ota-commission-rates
- **공통 구조 [사실/추정]**: OTA가 소매가로 고객에게서 선수금 → 커미션 차감 → 매장에 net 정산. **매장은 고객 카드를 직접 만지지 않음** = 외국인 카드·환불·정산을 OTA가 전부 흡수. 이것이 GLOU가 복제해야 할 핵심 패턴.

### A-4. ★한국의 외국인 결제 현실 (가장 중요)

#### 왜 막히나: 본인인증(本人認證) 장벽
- [사실] 한국 온라인 결제 대부분은 카드 입력 직후 **본인인증(이름·전화번호·생년월일·통신사 가입정보를 국가 DB와 대조)**을 요구. 카드번호 자체가 아니라 그 다음 단계에서 외국 카드가 막힘. 출처: https://klifechoice.com/paying-in-korea-as-a-foreigner/
- [사실] 필요 조건: 본인 명의 한국 전화번호(SMS 인증), ARC, 한국은행 계좌·인증서(RRN 기반). 외국 번호는 한국 시스템이 받는 형식의 인증 SMS를 못 받는 경우 多. 출처: https://klifechoice.com/paying-in-korea-as-a-foreigner/
- [사실] PG사(KG이니시스, NHN KCP, 토스페이먼츠 등)가 e커머스 트래픽을 라우팅하며 도메스틱 카드 중심으로 인증. 외국 카드 수용은 별도 셋업이 필요해 소규모 매장은 대부분 생략. 출처: https://klifechoice.com/paying-in-korea-as-a-foreigner/ , https://klifechoice.com/coupang-checkout-foreigners-korea/
- [사실] 외국 카드 차단 서비스: 쿠팡·배민 등 배달앱, 한국 e커머스, KTX(코레일)·공공결제·구독 → 본인인증 단계에서 "결제 수단을 확인해주세요"로 실패. 출처: https://klifechoice.com/ktx-booking-for-foreigners/

#### 앱별 외국인 정책
- [사실] **카카오페이**: 한국 전화번호(010) 필수, 관광 SIM/외국 번호 불가. 2020년경부터 ARC 번호는 수용하나 ARC 이름과 은행 등록 이름이 정확히 일치해야 함(사소한 차이도 실패). 출처: https://onboardkorea.com/kakao-pay-for-foreigners/
- [사실] **네이버페이(과거)**: 검증된 네이버 계정 + 한국 은행계좌 + 한국 통신사 번호 필요 → 단기 방문객은 사실상 불가. 출처: https://10mag.com/verify-naver-account-and-set-up-naver-pay-for-foreigners/
- [사실] **★네이버 여권 인증(2026-06-09 발표, 6월 시행)**: 한국 외 발급 여권으로 스마트폰에서 직접 본인인증 → 한국 휴대폰 번호 없이 네이버 지도 식당 예약·주문·결제(Npay Connect 단말) 가능. 한국어 리뷰 영/중/일 자동번역. 출처: https://www.koreatimes.co.kr/business/companies/20260609/... , https://www.navercorp.com/en/media/pressReleasesDetail?seq=10034413
  - [추정] **이것은 GLOU에 양날의 검**: (1) "외국인이 네이버예약 못 쓴다"는 핵심 페인포인트가 2026년 들어 부분 완화되기 시작 → 순수 결제대행만으론 해자가 약해짐. (2) 다만 시행 초기·서비스 범위 제한적(지도/식당 중심, 헤어/피부과/소형 살롱 미커버 다수)·신뢰/큐레이션/언어 컨시어지 가치는 유효 → GLOU는 결제 뚫기 자체보다 **큐레이션+신뢰+컨시어지+멀티버티컬 코스**로 포지셔닝해야 함.
- [사실] **토스뱅크**: 한국 인터넷은행 최초로 외국인이 ARC로 비대면 온라인 계좌 개설 가능(2025-03-21부터 모바일 ARC 수용). 단 계좌 개설 = 체류 외국인(ARC 보유)용이지 단기 관광객용은 아님. 출처: https://www.koreaherald.com/article/2856358 , https://toss.im/tossfeed/article/korealifehacks-7-en

#### 한국에서 작동하는 우회 / 외국인 친화 결제
- [사실] **Alipay+ / WeChat Pay 가맹**: 표준 QR로 해외 17개 모바일 결제(Alipay·WeChat 등) 연결 → 외국 관광객이 본국 앱으로 한국에서 결제. 2025년 한국 내 Alipay+ QR 거래 +18%, 결제액 +16%(중국 본토 Alipay > 홍콩 AlipayHK 순). 일본 PayPay도 2025-09 말부터 Alipay+로 한국 200만+ 가맹점 수용. 출처: https://www.koreatimes.co.kr/business/companies/20251209/... , https://thedigitalbanker.com/paypay-is-now-accepted-in-south-korea-via-ant-internationals-alipay/
- [사실] **KOMOJU**(일본계 PG): 한국 시장 대상으로 국제카드(VISA/MASTER/JCB/DINERS/AMEX) + 로컬카드(삼성·롯데·현대·하나·BC·NH·신한·KB) + 네이버페이/토스 + 외국인용 QR(본국 앱)까지 지원. 가입비·월비·숨은비용 없이 거래수수료만. → 외국인 친화 한국 결제를 한 통합 PG로 깔 수 있는 현실적 옵션. 출처: https://en.komoju.com/payment-methods/korea/ , https://en.komoju.com/payment-methods/korea/international-credit-cards/
- [사실] **Apple Pay 한국**: 2023년 현대카드 독점 출시. 현대카드 American Express 계열만 등록 가능, 2024년 현대카드 해외사용 +81%. Shinhan·KB로 확대 협의 중이나 **여전히 한국 발급 현대카드 필요 → 외국인 본국 카드는 Apple Pay로 한국 가맹점 결제 불가**. 출처: https://www.koreaherald.com/article/10407575 , https://www.koreatimes.co.kr/www/biz/2024/12/602_364062.html
- [사실] **서울 교통 오픈루프**: 2025년부터 신규 키오스크에서 해외 카드로 교통카드 충전, T-money를 Apple Pay(iPhone)에 등록(2025-07-22~). 출처: https://english.seoul.go.kr/seoul-implements-open-loop-payments-for-international-tourists/

#### 외국인 친화 한국 예약·결제 서비스 사례 (= GLOU 직접 경쟁/벤치마크)
- [사실] **Creatrip**: 정부 인증 의료미용 에이전시. 피부과/병원 예약, 스킨케어 클리닉 예약 시 현장결제 총액의 **10% 캐시백(Creatrip 포인트)**, Creatrip Buddy(개인 어시스턴트) 14일 무료. 출처: https://creatrip.com/en/blog/14800
- [사실] **Trazy Beauty Concierge**: 외국인이 원하는 살롱(상호/인스타 링크·서비스·희망일시)을 요청하면 한국어 팀이 살롱에 직접 연락·예약 확정. **선결제 필요 시 secure payment link 발송**, 현장결제면 금액 사전 안내. 헤어/네일/메이크업/헤드스파/왁싱, 서울·부산. 요청 살롱 불가 시 전액 환불, 확정 후 변심 취소는 환불 불가. → **컨시어지+payment link = GLOU MVP가 그대로 채택 가능한 경량 모델**. 출처: https://www.trazy.com/experience/detail/korea-beauty-concierge-hair-nail-waxing-salon-reservation
  - [추정] Creatrip·Trazy는 결제를 "secure link / 현장결제 / 캐시백"으로 우회하고 살롱 정산은 사람이 개입(컨시어지). GLOU 차별점 = AI 성분·효과 추천 + 멀티버티컬 코스 + 자동화된 Stripe Connect 정산.

---

## B. 해외 뷰티 서비스 심화 (agent 03 미커버 영역)

> (커머스·발견·로열티 / 가상메이크업·AI피부분석 / 아시아 예약 벤치마크)

### 아시아권 예약 벤치마크 (직접 조사)
- [사실] **HotPepper Beauty (일본·Recruit)**: 일본 최대 뷰티 예약 플랫폼, 15만+ 살롱·25만+ 스타일리스트·연 1.8억 예약. **선결제 없음 — 현장 현금/일본카드 결제**, 국제 휴대폰 번호로 SMS 확인 수용, 일본어 프로필은 "Request Translation" AI 번역(정확도 ~92%). → 외국인 마찰이 한국보다 낮은 이유: 선결제·본인인증을 강제하지 않음. 출처: https://www.moshimoshitraveljapan.com/p/getting-haircut-japan-using-hot-pepper-beauty , https://tokyopast3.com/how-to-create-a-hot-pepper-beauty-account/
- [사실] **GoWabi (태국)**: 5,000+ 뷰티/스파/클리닉, VISA/MC/AMEX 온라인 결제로 외국 카드 수용, 인도네시아 확장. 소비자 추가 플랫폼 수수료 없음(매장측 커미션 모델 추정). 할인·캐시백 중심. 출처: https://www.gowabi.com/customer_faq/ , https://www.gowabi.com/en
### B-1. 커머스·디스커버리·로열티
- [사실] **Sephora Beauty Insider**: 무료 가입 3티어(Insider / VIB $350+/년 / Rouge $1,000+/년), 전 티어 $1=1pt, 500pt=$10. 2025말 회원 ~4,600만(5년간 +75%). 2023 도입 게이미피케이션 "Beauty Insider Challenges"에 회원 ~30% 참여. 포인트는 Rewards Bazaar에서 샘플·세트·정품 교환. 앱 Virtual Artist(ModiFace 기반 AR), Color IQ, Smart Skin Scan. 출처: https://www.sephora.com/beauty/loyalty-program , https://www.forbes.com/sites/shelleykohan/2026/02/09/...
- [사실] **Ulta Beauty Rewards**(2024-01 리브랜딩): 활성회원 ~4,400만. **적립률 차등**(Member 1pt / Platinum $500/년 1.25pt / Diamond $1,200/년 1.5pt). 100pt=$3 ~ 2,000pt=$125. → Sephora=교환 차등, Ulta=적립률 차등 (로열티 설계 2모델). 출처: https://www.rivo.io/blog/ulta-rewards-program-a-complete-breakdown
- [사실] **Soko Glam / Then I Met You**(2012, Charlotte Cho): 수천 제품 직접 테스트·핸드셀렉트(큐레이션 수개월~수년), 북미에 "10-Step K-skincare" 도입, 번들 10~15% 내장 할인. **The Klog** 에디토리얼 허브가 트렌드를 빠르게 전달·커머스로 트래픽 유도. → "느린 전문가 큐레이션 + 빠른 에디토리얼 + 번들"이 외국인 신뢰 공식. 출처: https://sokoglam.com/pages/our-story , https://yoyofumedia.com/why-klog-content-marketing-works/
- [사실] **크로스보더 K-뷰티 커머스 결제 폭**: YesStyle = Visa/MC/Amex/JCB/PayPal/Apple Pay/Google Wallet(Alipay 미지원). **iHerb = 180+국·80+통화·40+결제수단**(+ Klarna/Alipay/UnionPay/일본 Konbini), 한국 물류센터 직배송. [추정] 외국인 커머스 차별점 = 현지화 결제수단 폭(iHerb 최강) + 관세 투명성. 출처: https://information.iherb.com/hc/en-us/articles/360051735232-Available-Payment-Methods , https://www.logisticsff.com/yesstyle-shipping/
- [사실] **구독박스 Birchbox/Ipsy**: 뷰티 프로필 퀴즈 매칭으로 샘플 발송 → 박스 내 할인카드로 자사몰 정품 풀사이즈 구매 유도(sample-to-purchase 퍼널). → [추정] "샘플(저위험 체험)→정품 전환" 퍼널을 "K-뷰티 발견→서비스 예약→전환"으로 변형 적용 가능. 출처: https://www.mysubscriptionaddiction.com/ipsy-vs-birchbox-which-beauty-subscription-box-offers-the-best-value

### B-2. 버추얼 메이크업·AI 피부분석
- [사실] **Perfect Corp (YouCam)**: 누적 다운로드 11억+, 800+ 브랜드 파트너. B2B SaaS = AR try-on(AgileFace®) + AI Skin Analysis(7만+ 의료급 이미지 학습). 파트너 성과 장바구니 +40%·전환율 2.5배·반품 -8%. 2025-11 YouCam AI Beauty Agent 출시. 출처: https://www.perfectcorp.com/ , https://www.businesswire.com/news/home/20250627047159/en/
- [사실] **ModiFace(L'Oréal 2018 인수)**: 로레알 전 브랜드 AR try-on·피부진단·헤어컬러. **Sephora Virtual Artist도 ModiFace 기반**. AI 진단 = 임상 6,000장+셀피 4,500장 학습, 20+ 임상 신호 식별. 출처: https://www.loreal.com/en/news/research-innovation/loreal-and-modiface-an-artificial-intelligencepowered-skin-diagnostic/
- [사실] **Haut.AI**(에스토니아): 300만+ 이미지 학습, 150+ 피부 파라미터. **API + 노코드 SaaS(iframe 임베드)** 제공, 파트너 Beiersdorf/Ulta/Grupo Boticário. 출처: https://haut.ai/product/ai-skin-analysis
- [추정] GLOU 적용: 자체 개발 대신 Perfect Corp/Haut.AI **B2B API 임베드**로 "스킨 분석→큐레이션 추천→예약" 진입점을 빠르게 구현.

### B-3. 아시아 뷰티 예약 벤치마크 (외국인 처리)
- [사실] **HotPepper Beauty(일본·Recruit)**: 일본 최대, 15.2만+ 살롱, 연 ~1.6억 예약, GMV ~1.1조엔. **선결제 없음(현장 현금/일본카드)**, 국제 번호 SMS 수용. **서비스는 일본어 전용·영어 번역 옵션 사실상 부재** → 영어권 관광객 큰 장벽. 수익=광고비+거래수수료+살롱 SaaS(SALON BOARD). 출처: https://recruit-holdings.com/en/blog/post_20240625_0001/ , https://www.moshimoshitraveljapan.com/p/getting-haircut-japan-using-hot-pepper-beauty
  - [추정] **GLOU 최대 기회 = "아시아 1위 뷰티 예약앱이 자국어 전용"이라는 공백.** 한국 외국인 대상 다국어 예약·결제는 명백한 미충족 수요.
- [사실] **GoWabi(태국·1위)**: 5,000+ 매장, 플래시세일 최대 80%. 관광객·외국인 거주자 타깃, 영어 사전예약, 앱 내 결제로 현장 가격 모호성 제거. 결제수단 = Visa/MC/Amex + TrueMoney/ShopeePay/Rabbit LINE Pay/**Alipay**/Google Pay/PromptPay + ฿3,000+ 시 0% 할부. **커미션 = 가입 무료·회비 없음·예약 발생 시에만 성과형 수수료**(7일 리포트·15일 정산, 수수료율 비공개, [추정] 업계 통상 15~30%). 출처: https://www.gowabi.com/en/partner , https://www.gowabi.com/customer_faq/?m=guide
  - [추정] **GoWabi = GLOU와 가장 유사한 직접 벤치마크**(외국인 타깃 + 다양한 현지/국제 결제 + 선결제 앱예약 신뢰 + 무료가입·성과형 수수료).
- [사실] **Vaniday(싱가포르·1위)**: 예약+e커머스+콘텐츠(VaniZine)+로열티 통합형. 단 수익성 부진으로 인수·재론칭 → [추정] 단일시장 통합모델 지속의 어려움 = GLOU는 "외국인/관광객" 니치로 차별화 필요. 출처: https://www.vaniday.com/ , https://vulcanpost.com/705609/

---

## C. 해외 외국인 대상 생활·여행 정보 서비스

### C-1. 외국인 정착(onboarding) / 도시 가이드
- [사실] **Monito**: 100+ 송금·환전 서비스 실시간 비교 "이주민 허브". 해외 계좌 개설·생활정보 안내, 누적 절감 7,500만 달러+. 출처: https://www.monito.com/en/how-it-works
- [사실] **Wise / Revolut**: 도착 *전* 해외에서 멀티커런시 계좌 개설. Wise = 여권+비현지 주소+10초 셀피로 도착 전 IBAN 발급(현지 폰/주소/세금ID 불필요). Revolut는 현지 세금ID 필요해 문턱 높음. → 정착 첫 병목인 "계좌가 있어야 결제, 계좌엔 현지 주소·등록 필요"라는 닭-달걀을 Wise는 도착 전 개설로 해소. 출처: https://www.findenglish.de/blog/n26-vs-wise-vs-revolut-expats-germany-2026
- [사실] **Onboard Expat(싱가포르)**: 비자·보험·이사·주거·공항픽업 + **은행계좌+SIM 셋업**을 한 업체가 번들 처리하는 정착 컨시어지. 출처: https://onboardexpat.com/
- [사실] **Sakura Mobile(일본)**: 신규 입국자용 SIM. 주소등록(재류카드 도장) 없이 **여권+입국 비자만으로** 가입 → 외국인 타임라인에 맞춘 KYC 완화. 출처: https://www.sakuramobile.jp/blog/plan-guides/...

### C-2. eSIM + 신원/온보딩
- [사실] **Airalo**: 200+ 국가 eSIM 마켓플레이스. 이메일+신용카드만으로 구매, **여권/셀피/정부ID 업로드 기본 無**(eKYC는 UAE·몰디브 정도만 예외) → 신원확인 마찰 제로로 매장방문·물리SIM·로밍 전부 제거. 출처: https://www.airalo.com/blog/faq-about-esims
- [사실] **Holafly**: 일수 기준 무제한 데이터 eSIM(유럽 7일 ~$27). 단 다수 요금제 테더링 불가. 출처: https://esim.holafly.com/reviews/holafly-vs-airalo/
- [원리] eSIM의 가치 = "출발 전, 자국에서, 카드 한 장으로, 신원확인 없이" 데이터 확보. 한국의 "실명 한국번호 SMS 인증" 구조와 정반대로 **현지 폰번호 자체를 우회**.

### C-3. 마찰 없는 관광객 예약·결제 (한국 대비용)
- [사실] **Klook**: Visa/MC/JCB/Amex/UnionPay/Korean Local Card + PayPal/**Apple Pay/Google Pay**/e-wallet 수용, 핸들링 수수료 없음. 영어로 한국어 사이트·본인인증 우회 예약. 2025 Klook–Korail 제휴로 한국 철도 실시간 예약 직접 처리. → 제3자 플랫폼이 ₩1,000~5,000 수수료로 "본인인증 마찰 제거"를 상품화. 출처: https://www.klook.com/en-US/faq/category-2-question-133/ , https://www.thetraveler.org/klook-korail-tie-up-brings-real-time-rail-booking-to-korea/
- [사실] **GetYourGuide / Viator**: 게스트 체크아웃(계정 강제 X), 카드 결제, 24h 무료 취소. GYG는 투어 2일 전까지 미청구, Viator는 "Reserve Now & Pay Later". 외국 카드+이메일만으로 예약, 현지 머천트는 플랫폼 통해 정산. 출처: https://www.getyourguide.com/
- [사실] **일본의 예외(한국과 유사 구조)**: 일본 비접촉결제 다수가 FeliCa(IC칩) 기반이라 해외 Apple/Google Pay가 안 먹히는 경우 有. 단 **Alipay+/WeChat Pay QR가 폭넓게 수용**되어 외국인 우회로 존재 → 한국보다 마찰 낮음. 출처: https://www.japan.travel/en/plan/cashless-payments-in-japan/

### C-4. ★한국이 외국인에게 유독 마찰이 큰 지점 (대비 결론)
1. [사실] 본인인증이 결제의 필수 관문 — 카드가 아니라 *그 다음 단계*에서 실패. (klifechoice)
2. [사실] 실명 등록 한국 통신사 번호로만 SMS 인증 통과 — 관광 SIM·본국 번호 불가. (klifechoice/ktx)
3. [사실] 주민등록번호 요구 — 고액 거래 등에서 외국인 1차 차단. (klifechoice/ktx)
4. [사실] 쿠팡·배민·KTX 등 핵심 생활/예약 앱이 외국 카드·외국인 사실상 배제. (klifechoice/coupang, KoreaTimes)
5. [사실] 실패 오류 메시지 불친절 — 어느 단계가 막혔는지 안내 없음. (KoreaTimes)
6. [사실] 교통·오프라인 결제도 폐쇄적 — 국제카드 비호환, 원화 전용 T-money 강제, 일부 상점 외국카드 의도적 차단. (KoreaTimes)
- 출처: https://www.koreatimes.co.kr/economy/others/20250423/why-koreas-payment-systems-leave-tourists-frustrated
- **[추정] 대비 결론**: 일본·EU·태국은 외국인이 본국 카드/이메일/eSIM/QR페이로 우회로를 갖지만, 한국은 **본인인증+한국 실명 폰번호+주민번호 3중 관문**이 결제 자체에 박혀 우회로가 없음. → GLOU 기회 = Klook/GetYourGuide식 "마찰 흡수 레이어"를 K-뷰티/서울 라이프에 특화.

---

## D. ★GLOU MVP day1 결제·예약 아키텍처 권고 (종합)

> 핵심 원리(글로벌 OTA 공통): **GLOU가 외국 카드로 고객에게서 선수금 → 커미션 차감 → 한국 매장에 정산.** 매장은 고객 카드·본인인증·외국인 결제를 일절 만지지 않음. 이것이 한국 결제 마찰을 통째로 흡수하는 구조.

1. **결제 처리 = Stripe Checkout/Payment Links + Connect(destination charge)** [권고]
   - 외국인은 게스트 체크아웃(계정 없이 카드만) + Apple Pay/Google Pay. application_fee로 GLOU 수수료 자동 분리, 매장은 connected account로 payout. Adyen은 초기 부적합(엔터프라이즈). → 한국 본인인증·한국 폰번호 요구 없이 외국 카드 결제 성립.
2. **노쇼 방지 = 사전승인(pre-auth hold) 또는 부분 선결제(deposit)** [권고]
   - Stripe place-a-hold로 보증금 hold(7일, extended 30일) → 정상 방문 시 release, 노쇼 시 capture. 고가 시술(피부과/헤어)은 Fresha/Treatwell처럼 부분/전액 선결제. → 매장 신뢰 확보 + 외국인 노쇼 리스크 제어.
3. **정산·환불 신뢰 장치** [권고]
   - Viator/GetYourGuide식 명확한 환불정책(예약 X일 전 무료취소) + 매장 정산 주기 명시(월/격주). 요청 살롱 불가 시 전액 환불(Trazy 모델). 다국어 영수증·예약확정 메일.
4. **인바운드 결제수단 폭** [권고]
   - 1차: Stripe 글로벌카드 + Apple/Google Pay. 2차: 중국·홍콩·동남아 인바운드용 **Alipay+/WeChat Pay**(한국 가맹 활발, 2025 거래 +18%). 미·호주·유럽 고가 시술엔 Klarna/Afterpay(매장 선지급) 검토. 통합 PG로 **KOMOJU** 고려(국제카드+로컬+네이버페이/토스+외국인 QR을 한 번에).
5. **컨시어지 → 자동화 하이브리드(MVP)** [권고]
   - day1은 Trazy식 경량 모델(요청→한국어팀 살롱 컨택→secure payment link)로 빠르게 검증 → 수요 확인 후 Stripe Connect 자동 정산으로 전환. **차별점 = AI 성분·효과 추천 + 멀티버티컬(뷰티/헤어/피부과/카페/맛집/웰니스) 코스 + 자동 정산.**

### 전략적 경보 [추정]
- **2026-06 네이버 여권 인증 시행**으로 "외국인이 네이버예약 못 쓴다"는 핵심 페인포인트가 부분 완화 시작 → 순수 "결제 뚫기"만으론 해자가 약화. GLOU는 **큐레이션+신뢰+다국어 컨시어지+멀티버티컬 코스+로열티(Sephora/Ulta 모델)**로 포지셔닝을 이동해야 함. 네이버 커버리지(지도/식당 중심)가 닿지 않는 소형 살롱·헤어·피부과·웰니스가 단기 진입 지점.

---
