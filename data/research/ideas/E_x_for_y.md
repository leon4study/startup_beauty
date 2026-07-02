# 미션 E — "X for Y" 글로벌 검증모델 이식 (외국인 × 서울)

> 작성일: 2026-07-01 · 팀: GLOU · 트랙: 모두의창업 2026 R1
> 방식: 검증된 해외 서비스의 **실제 수익모델**을 조사 → 그대로 '외국인×서울' 맥락에 이식.
> 표기: [사실] = 출처 직접 확인 / [추정] = 출처 기반 합리적 추론.
> 팀자산: ① 글로벌 인플루언서(180개국 외국인 네트워크) ② 데이터/개발 ③ 리뷰 RAG ④ 화학·약학 ⑤ 뷰티 인플루언서.
> 1차 타겟: 영어권 서구 20–30대 여성 + 서울 거주 외국인. 핵심 페인: 예약·결제 차단 / 협찬리뷰 불신 / 바가지 / 식이필터 부재 / 정착 마찰.

## 시장 그라운딩 (공통 근거)
- [사실] 한국 외국인 주민 2025-10 기준 **283만 명**(전체 인구의 5.3%), 서울 거주 외국인 약 **45만 명**. 출처: https://www.koreantopik.com/2025/11/koreas-foreign-resident-population.html , https://www.koreaherald.com/article/10690931
- [사실] 2025년 방한 외국인 **1,850만 명**(코로나 이전 회복, 2030년 3,000만 목표). 출처: https://www.travelandtourworld.com/news/article/south-korea-surpasses-pre-pandemic-records-with-18-5-million-tourists-in-2025-aiming-for-30-million-by-2030-a-look-at-the-growing-appeal-of-seoul-incheon-and-beyond/
- [사실] 2025년 외국인 의료관광(주로 피부과) 지출 **2.08조 원**(+65.3% YoY), 의료기관 거래 +58%, 약국·드럭스토어 외국인 지출 +63%. 출처: https://www.kedglobal.com/retail/newsView/ked202512280003
- [사실] 외국인 페인 확정: 바가지(외국인 차등가격), 언어장벽, 입소문·한국 SNS 의존, 협찬리뷰 불신. 출처: https://www.gangnamskintreatment.com/blog/foreigner-pricing-in-korean-skin-clinics
- [사실] 2025-12 의료·미용 택스리펀드(TAX FREE) 제도 종료 → 가격 투명성·환급 안내 수요 증가. 출처: https://blog.yeoshin.co.kr/en/korea-beauty-tax-refund-2026-policy-change/

> tier 정의: T1=핵심(즉시 추진) · T2=확장(검증 후) · T3=옵션(선택).
> 거리 = 팀자산 적합도 0–5(높을수록 우리가 잘함).

---

## E1. Treatwell/Fresha for 서울 살롱(외국인) — "Seoulwell"
- **한줄**: 서울 헤어·네일·왁싱·피부관리 살롱을 영어 실시간 예약·선결제로 100% 확정해주는 외국인 전용 뷰티 예약 마켓플레이스.
- **타겟**: 서울 거주 외국인 + 체류 1주+ 여행자(영어권 20–30 여성 1순위).
- **페인**: 전화/카톡 수동 예약·외국어 미지원·확정 불확실·노쇼 리스크로 매장이 외국인 기피.
- **차별화(팀자산)**: ②개발로 실시간 빈슬롯→3클릭 확정·카드선결제 UX, ⑤뷰티 인플루언서가 살롱 포트폴리오(전후·영상) 시딩, ①180개국 네트워크로 초기 수요 풀.
- **수익구조(원본 적용)**: [사실] Treatwell=신규고객 첫예약 **35% 커미션**+월구독 €29~49+선결제 2.9%; Fresha=신규고객 마켓플레이스 예약 **약 20% 커미션**+캘린더당 월 £9.95. 출처: https://businessmodelcanvastemplate.com/blogs/how-it-works/treatwell-how-it-works , https://www.fresha.com/pricing → **우리 버전**: 신규 외국인 첫예약 **20% 커미션**(재방문 0%)+살롱 월구독 ₩30,000(영문 프로필·다국어 캘린더)+선결제 PG 2.9%. 살롱 외국인 객단가 ₩60,000×월 30건×20%=**살롱당 월 ₩36만 커미션**, 살롱 500곳 시 월 ₩1.8억+구독 ₩1,500만.
- **태그**: #예약 #결제 #핵심페인 #마켓플레이스
- **거리**: 5 · **tier**: T1

## E2. RealSelf for 한국 미용의료(투명후기) — "WorthIt Korea"
- **한줄**: 한국 피부과·미용시술의 실지불 금액·다운타임·보정없는 전후·"Worth It" 투표를 영문으로 표준화한 투명 리뷰 플랫폼.
- **타겟**: 시술 고민하는 외국인(의료관광객+거주 외국인).
- **페인**: 광고성 블로그·실가격/다운타임 비공개·외국인 차등가격(바가지). 택스리펀드 종료로 실가격 정보 수요↑.
- **차별화(팀자산)**: ③리뷰 RAG로 분산된 후기 정규화·신뢰 스코어링, ④화학·약학으로 시술 성분/다운타임 검증, ①네트워크로 1인칭 영문 후기 시딩.
- **수익구조(원본 적용)**: [사실] RealSelf=양면 수익(의사 유료 프로필 구독+브랜드/제휴 광고). 무료 프로필+유료 업그레이드(검색 상위·인스타 연동·타깃광고·분석). 2025년 제휴 매출 한 달 +373%(쇼퍼블 섹션). 출처: https://www.forbes.com/sites/tanyabenedictoklich/2025/09/08/inside-realselfs-rebrand-as-the-zocdoc-for-aesthetics/ , https://beautymatter.com/articles/real-selfs-new-omnichannel-content-flywheel-is-quickly-paying-off → **우리 버전**: 클리닉 유료 프로필 구독 월 ₩30~80만(검색상위·영문 코디네이터 연동·분석)+제휴/예약 리드젠(클리닉 송객 1건 ₩2~5만)+K뷰티 브랜드 쇼퍼블 제휴. 클리닉 200곳×월 ₩50만 구독=**월 ₩1억**+리드젠.
- **태그**: #신뢰후기 #투명가격 #의료관광 #리드젠
- **거리**: 5 · **tier**: T1

## E3. Yelp/TheFork for 외국인 다이닝 — "ForkSeoul"
- **한줄**: 비건·할랄·글루텐프리·알레르기 필터로 서울 맛집을 발견하고 영문 원스톱 예약하는 외국인 다이닝 가이드.
- **타겟**: 식이제한 있는 외국인(채식·종교·알레르기) + 서구 여성 여행자.
- **페인**: Naver/Kakao에도 식이 필터 부재·메뉴 외국어 약함·예약 분절. 그룹 교집합 식이필터는 글로벌에도 빈틈.
- **차별화(팀자산)**: ②개발로 식이 태깅·교집합 필터(여러 명 식이 동시), ④화학·약학으로 알레르겐 정확도, ①다국어 리뷰 풀.
- **수익구조(원본 적용)**: [사실] Yelp=CPC 광고(클릭당 $2~10, 식당 <$1)로 2025 광고매출 $1.39B; TheFork=예약당 커미션+프리미엄 구독(상위노출·마케팅·분석); OpenTable=월 $149+ 네트워크 커버당 ~$1.50. 출처: https://www.sec.gov/Archives/edgar/data/0001345016/000134501625000067/yelpq32025ex992lettertos.htm , https://vizologi.com/business-strategy-canvas/thefork-business-model-canvas/ , https://www.opentable.com/restaurant-solutions/plans/ → **우리 버전**: 예약 네트워크 커버당 ₩1,000~2,000(TheFork형)+식당 프리미엄 구독 월 ₩50,000(식이인증 뱃지·상위노출)+CPC 광고. 식당 1,000곳×월 40커버×₩1,500=**월 ₩6,000만**+구독.
- **태그**: #식이필터 #다이닝 #예약 #발견
- **거리**: 4 · **tier**: T2

## E4. Too Good To Go for 한국(잉여 K뷰티·베이커리) — "Seoul Surprise Bag"
- **한줄**: 마감 임박 베이커리·카페·유통기한 임박 K뷰티 재고를 50~75% 할인 서프라이즈백으로 외국인에게 픽업 판매.
- **타겟**: 가성비 민감 외국인(학생·디지털노마드·예산 여행자).
- **페인**: TGTG는 한국어 앱 위주로 외국인 접근난·잉여 K뷰티 유통 경로 부재·바가지 반대편의 초저가 발견.
- **차별화(팀자산)**: ⑤뷰티 인플루언서로 한정 K뷰티 서프라이즈백 화제성, ②개발로 위치·픽업 슬롯, ①외국인 채널 직접 도달.
- **수익구조(원본 적용)**: [사실] TGTG=봉투당 커미션 **€1.09**+가맹점 연회비(미국 $89/년)+B2B 폐기물 분석. 2024 매출 €725M, 봉투 1.16억 개. 출처: https://www.untaylored.com/post/how-too-good-to-go-makes-money-the-business-and-revenue-model-explained → **우리 버전**: 백당 커미션 **₩1,500**+가맹점 연회비 ₩99,000. 베이커리/뷰티 매장 1,000곳×월 60백×₩1,500=**월 ₩9,000만**+연회비 ₩9,900만/년. K뷰티 잉여백은 단가↑ → 백당 ₩3,000.
- **태그**: #잉여딜 #초저가 #픽업 #ESG
- **거리**: 3 · **tier**: T3

## E5. TimeLeft for 서울 외국인 소셜디너 — "Seoul Table"
- **한줄**: 언어 선호·성향 기반으로 낯선 외국인↔로컬 5인을 매칭해 매주 서울 식당에서 소셜디너를 여는 외로움 해소 앱.
- **타겟**: 정착 초기 외국인·디지털노마드·교환학생(외로움·네트워크 페인).
- **페인**: 정착 마찰·고립감·로컬 커뮤니티 진입난. TimeLeft 서울 진출했으나 외국인×K뷰티 맥락 결합 부재.
- **차별화(팀자산)**: ①180개국 네트워크가 곧 매칭 풀, ⑤인플루언서 호스팅, ②매칭 알고리즘. 디너 후 "함께 K뷰티 클래스/시술" 코스 연계(E11·E12와 번들).
- **수익구조(원본 적용)**: [사실] TimeLeft=일회 티켓(미국 $16, 프랑스 €12.99) 또는 구독(6개월 $86, 월 €14.99). 음식값은 현장 별도. 출처: https://timeleft.com/ , https://www.tastingtable.com/1859085/dinner-parties-with-strangers-timeleft/ → **우리 버전**: 디너 1회 ₩18,000 또는 월구독 ₩19,000(주 1회)+식당 송객 제휴(커버당 ₩2,000). 참가 월 2,000명×₩18,000=**월 ₩3,600만**+식당 제휴.
- **태그**: #소셜 #정착 #커뮤니티 #구독
- **거리**: 5 · **tier**: T2

## E6. HotPepper Beauty/GoWabi 다국어 예약 이식 — "K-Salon Pass"
- **한줄**: 일본 HotPepper Beauty(월 고정 게재료)·태국 GoWabi(할인딜+커미션) 모델을 합쳐 서울 살롱을 다국어 예약+할인딜로 묶은 공급자 SaaS형 마켓플레이스.
- **타겟**: 외국인 고객 + 외국인 객 늘리려는 서울 살롱/스파.
- **페인**: 매장은 외국인 예약관리·노쇼·언어 부담. HotPepper/GoWabi 같은 강력한 로컬 예약 인프라가 한국엔 외국인용으로 없음.
- **차별화(팀자산)**: ②개발로 살롱보드형 무료 예약관리+POS 제공(락인), ③리뷰 RAG, ⑤인플루언서 할인딜 큐레이션.
- **수익구조(원본 적용)**: [사실] HotPepper Beauty=월 고정 **게재료(라이트 약 ¥3~5만 ~ 플래티넘 수십만 엔)**+예약매출 2% 수수료, 살롱 예약의 60~70% 차지; GoWabi=예약 커미션(가입 무료)+SaaS/CRM 연구독+디지털마케팅. 출처: https://salon-knowledge.com/htb/hotpepper-keisairyokin-plan/ , https://www.gowabi.com/en/partner → **우리 버전**: 살롱 월 게재료 ₩50,000~300,000(플랜별, 무료 예약관리 SaaS 포함)+예약매출 2% 수수료+할인딜 커미션 15%. 살롱 700곳×평균 월 ₩120,000=**월 ₩8,400만**+수수료/딜.
- **태그**: #예약 #SaaS #공급자락인 #할인딜
- **거리**: 4 · **tier**: T1

## E7. Cara/Reddit for 외국인 커뮤니티(협찬 없는 신뢰후기) — "GLOU Threads"
- **한줄**: 협찬·광고 없이 서울 거주/방문 외국인이 K뷰티 제품·시술·살롱을 1인칭으로 검증하는 신뢰 커뮤니티(서브레딧형).
- **타겟**: 협찬리뷰에 지친 영어권 여성(정보 신뢰 페인).
- **페인**: 협찬리뷰 불신·한국 SNS/블로그 광고성·영문 진짜 후기 부재.
- **차별화(팀자산)**: ③리뷰 RAG로 신뢰도 스코어+요약, ④화학·약학 전문가 답변 배지, ①네트워크로 초기 커뮤니티 시딩.
- **수익구조(원본 적용)**: [사실] Reddit=광고(2025 분기 광고 $690M)+**AI 데이터 라이선싱**(Google ~$60M/년)+프리미엄 구독 월 $6; Cara=구독+잡리스팅+엄선광고(협찬 의존 회피, 신뢰 우선). 출처: https://phemex.com/academy/reddit-stock-2026 , https://blog.cara.app/blog/finances-and-future-of-cara → **우리 버전**: 비협찬 원칙 유지+① 광고 아닌 프리미엄 구독 월 ₩4,900(광고제거·전문가 Q&A)+② **정제된 영문 K뷰티 후기 데이터셋 라이선싱**(브랜드/연구기관 B2B, 우리 RAG의 차별 자산)+③ 잡/정착 리스팅. 후기 데이터 라이선싱이 협찬 없이 신뢰를 지키는 핵심 수익. MAU 10만×구독전환 3%×₩4,900=월 ₩1,470만+데이터 라이선싱.
- **태그**: #커뮤니티 #신뢰후기 #데이터라이선싱 #비협찬
- **거리**: 5 · **tier**: T1

## E8. ClassPass for K뷰티·웰니스 패스 — "GLOU Pass"
- **한줄**: 크레딧 한 장으로 서울 헤어스파·네일·요가·필라테스·마사지를 골라 쓰는 외국인 K뷰티·웰니스 구독 패스.
- **타겟**: 다양하게 체험하고픈 거주 외국인·장기 여행자.
- **페인**: 매장마다 따로 예약·결제·언어장벽. 빈 슬롯 채우고 싶은 매장과 다양성 원하는 외국인의 미스매치.
- **차별화(팀자산)**: ②개발로 크레딧 가치 동적 산정(시간·인기·위치), ⑤인플루언서 큐레이션, ①수요 풀. Treatwell 비수기 동적할인과 결합.
- **수익구조(원본 적용)**: [사실] ClassPass=월 구독(플랜 $15~199)으로 크레딧 지급, 매장은 수수료 0 — **ClassPass가 회원 크레딧가와 매장 정산액 사이 스프레드로 수익**. 2025 GMV $700M+, 매출 구독 60%/B2B 20%/PPU·제휴 20%. 매장은 6개월 후 평균 매출 +29%. 출처: https://productmint.com/the-classpass-business-model-how-does-classpass-work-make-money/ , https://fourweekmba.com/classpass-business-model/ → **우리 버전**: 외국인 월 구독 ₩59,000(크레딧 30)~₩149,000(크레딧 90)+B2B(기업·코리빙 복지 패키지). **스프레드 수익**: 크레딧당 회원과금 ₩2,000, 매장 정산 ₩1,400 → 마진 ₩600/크레딧. 구독자 3,000명×평균 40크레딧×₩600=**월 ₩7,200만**.
- **태그**: #구독 #패스 #웰니스 #스프레드
- **거리**: 4 · **tier**: T2

## E9. Klook 모델의 K뷰티 시술 큐레이션 — "GLOU Clinic Deals"
- **한줄**: 헤드스파·스킨부스터·레이저·리프팅을 외국인에게 현지 가격·다국어·모바일 바우처로 즉시 예약 판매하는 K뷰티 시술 큐레이션 마켓.
- **타겟**: 의료관광객 + 시술 원하는 거주 외국인. (Klook가 이미 진입한 영역 → 큐레이션·신뢰로 차별화)
- **페인**: 바가지·다운타임 불투명·예약 언어장벽. Klook 헤드스파 트래픽 2025 +230%로 수요 입증.
- **차별화(팀자산)**: ④화학·약학으로 시술·성분 검증 큐레이션, ③리뷰 RAG로 신뢰, ⑤인플루언서 코스. E2(WorthIt)와 후기↔예약 연계.
- **수익구조(원본 적용)**: [사실] Klook=공급자 커미션 **take rate 약 15~25%**(평균 17.8%, 매출의 85%)+리테일미디어 광고(2025 +78%)+Klook Pass 번들(브레이키지 ~9%)+B2B/1P. 출처: https://www.mostlymetrics.com/p/klook-ipo-s1-breakdown , https://www.sambahq.com/ota-supplier-guide/ota-commission-rates → **우리 버전**: 시술 예약 커미션 **15~20%**+클리닉 상위노출 광고+시술 번들패스(예: 스킨부스터 3회 묶음, 마진↑). 시술 객단가 ₩200,000×월 1,000건×17%=**월 ₩3,400만**+광고/번들.
- **태그**: #시술 #큐레이션 #바우처 #커미션
- **거리**: 5 · **tier**: T1

## E10. INCI/Yuka for 한글 성분 스캔 — "K-Scan"
- **한줄**: K뷰티 제품 바코드·한글 성분표를 스캔하면 영문 성분 점수·기능·피부타입 적합도를 알려주는 외국인용 성분 해독 앱.
- **타겟**: 한글 성분표 못 읽는 외국인(올리브영·드럭스토어 쇼퍼).
- **페인**: 한글 성분 해독 불가·K뷰티 영문 성분 DB 빈약. 외국인 약국·드럭스토어 지출 2025 +63%.
- **차별화(팀자산)**: ④화학·약학으로 농도 한계 보완(존재만 감점 X → 효과·적합도 추천), ②OCR/RAG로 한글성분 영문화, ⑤인플루언서 추천 큐레이션.
- **수익구조(원본 적용)**: [사실] Yuka=**프리미엄 구독이 주수익**(약 $10/월 또는 $10~50/년 "원하는 만큼"), **광고·브랜드후원·데이터판매 일절 없음**(중립성). 매출 $20.3M, VC 0. 출처: https://yuka.io/en/independence/ , https://getlatka.com/companies/yuka.io → **우리 버전(중립성 유지)**: 프리미엄 구독 월 ₩4,900(스캔없이 검색·알림·피부타입 매칭). 브랜드 광고 대신 **중립 큐레이션**으로 신뢰. 부가: K뷰티 제품 영문 성분 데이터셋 B2B 라이선싱. MAU 20만×구독전환 4%×₩4,900=**월 ₩3,920만**.
- **태그**: #성분스캔 #중립성 #구독 #화학자산
- **거리**: 5 · **tier**: T1

## E11. Airbnb Experiences for K뷰티 클래스 — "GLOU Experiences"
- **한줄**: 자격검증된 로컬 전문가가 여는 K뷰티 메이크업·스킨케어·헤어 클래스를 외국인이 다국어로 예약하는 체험 마켓.
- **타겟**: 체험 원하는 외국인(여행자+거주자), 클래스 호스팅하려는 K뷰티 전문가·인플루언서.
- **페인**: 로컬 체험이 한국어 플랫폼에 잠김. Airbnb Services가 hair/spa/nails 진입 중 → 선점 필요.
- **차별화(팀자산)**: ⑤뷰티 인플루언서가 곧 호스트 풀, ④화학·약학 클래스 콘텐츠 신뢰, ①180개국 게스트 수요. E5 소셜디너→클래스 번들.
- **수익구조(원본 적용)**: [사실] Airbnb Experiences=호스트 **서비스 수수료 20%**(자동 차감), Services는 15%+최소 $6. 호스트 신원검증+라이선스·자격증 제출. 출처: https://www.airbnb.com/help/article/3164 , https://news.airbnb.com/airbnb-2025-summer-release/ → **우리 버전**: 호스트 수수료 **15~20%**+게스트 서비스 수수료 별도. 클래스 객단가 ₩60,000×월 800건×18%=**월 ₩864만**+게스트 수수료. 인플루언서 호스트 화제성으로 고단가 프리미엄 클래스(₩150,000+) 가능.
- **태그**: #체험 #클래스 #호스트수수료 #인플루언서
- **거리**: 5 · **tier**: T2

## E12. (보너스) GoWabi/Booksy "Forever Stylist" — "MyStylist Seoul"
- **한줄**: 매장이 아닌 개인 디자이너/원장 포트폴리오(전후·영상·곱슬/텍스처 전문 태그)로 외국인이 "내 모발/피부 맞는 사람"을 찾아 단골로 락인하는 예약 앱.
- **타겟**: 곱슬·다양한 텍스처·민감성 피부 외국인(한국 매장이 다루기 어려워하는 모발).
- **페인**: 매장 단위 발견으로 "누가 내 곱슬을 다룰 줄 아나" 모름. 서구 여성 텍스처 전문 디자이너 매칭 부재.
- **차별화(팀자산)**: ⑤인플루언서·디자이너 영상 포트폴리오, ②전문 태그 매칭(curly/silk press/민감성), ①네트워크 수요.
- **수익구조(원본 적용)**: [사실] StyleSeat/Booksy=마켓플레이스 신규고객 매출 커미션(StyleSeat 약 30%)+보증금/카드온파일 노쇼방지, 예약완료율 +25%. 출처: https://glossgenius.com/blog/styleseat-vs-booksy , https://www.styleseat.com/blog/styleseat-deposits/ → **우리 버전**: 신규 외국인 첫예약 **20% 커미션**(재방문 0%로 단골 락인)+보증금/카드온파일. 디자이너 단위라 객단가↑(텍스처 전문 ₩100,000+). 디자이너 300명×월 신규 8건×₩100,000×20%=**월 ₩4,800만**.
- **태그**: #디자이너중심 #텍스처전문 #단골락인 #커미션
- **거리**: 4 · **tier**: T2

---

## 출처 (수익모델 핵심)
1. Treatwell/Fresha 커미션·구독: https://businessmodelcanvastemplate.com/blogs/how-it-works/treatwell-how-it-works , https://www.fresha.com/pricing
2. RealSelf 양면 수익·제휴: https://www.forbes.com/sites/tanyabenedictoklich/2025/09/08/inside-realselfs-rebrand-as-the-zocdoc-for-aesthetics/
3. Yelp CPC·TheFork·OpenTable: https://www.sec.gov/Archives/edgar/data/0001345016/000134501625000067/yelpq32025ex992lettertos.htm , https://vizologi.com/business-strategy-canvas/thefork-business-model-canvas/ , https://www.opentable.com/restaurant-solutions/plans/
4. Too Good To Go 봉투당 €1.09+연회비: https://www.untaylored.com/post/how-too-good-to-go-makes-money-the-business-and-revenue-model-explained
5. TimeLeft 티켓·구독: https://timeleft.com/ , https://www.tastingtable.com/1859085/dinner-parties-with-strangers-timeleft/
6. HotPepper Beauty 게재료+2%·GoWabi 커미션: https://salon-knowledge.com/htb/hotpepper-keisairyokin-plan/ , https://www.gowabi.com/en/partner
7. Reddit 광고+데이터라이선싱·Cara: https://phemex.com/academy/reddit-stock-2026 , https://blog.cara.app/blog/finances-and-future-of-cara
8. ClassPass 스프레드 모델: https://productmint.com/the-classpass-business-model-how-does-classpass-work-make-money/
9. Klook take rate 17.8%: https://www.mostlymetrics.com/p/klook-ipo-s1-breakdown
10. Yuka 구독·중립성: https://yuka.io/en/independence/ , https://getlatka.com/companies/yuka.io
11. Airbnb Experiences 20% 수수료: https://www.airbnb.com/help/article/3164
12. StyleSeat/Booksy 커미션·보증금: https://glossgenius.com/blog/styleseat-vs-booksy
13. 시장 그라운딩(외국인 283만·시술지출 2.08조): https://www.kedglobal.com/retail/newsView/ked202512280003 , https://www.koreantopik.com/2025/11/koreas-foreign-resident-population.html
