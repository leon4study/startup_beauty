# 03. 해외 서비스 벤치마킹 + as-is→to-be 인풋

> 작성일: 2026-06-30 · 프로젝트: GLOU (외국인 대상 서울 라이프 + K-뷰티 큐레이션·예약 플랫폼)
> 목적: 해외에서 외국인/여행자/현지인이 쓰는 서비스를 분석해 "한국에 없는/약한 기능"을 정리하고, GLOU가 그대로 '얹을' 글로벌 표준 UX를 도출.
> 표기: [사실] = 출처로 직접 확인 / [추정] = 출처 기반 합리적 추론(미확정). 모든 주장에 출처 URL.

---

## 0. 카테고리별 핵심 요약 (한눈에)

| 카테고리 | 대표 서비스 | 글로벌 표준 UX | 한국 현실(외국인 입장) |
|---|---|---|---|
| 살롱/뷰티 예약 | Treatwell, StyleSeat, Booksy, Fresha, Vagaro | 실시간 빈 시간 → 3클릭 즉시 100% 확정, 카드 선결제/보증금, 디자이너 포트폴리오·영상 | 전화/카톡 수동, 워크인, 외국어 미지원, 선결제·확정 개념 약함 |
| 메디컬뷰티 리뷰 | RealSelf | 보정 없는 전후 사진 + 실지불 금액 + 다운타임 + "Worth It" 투표 | 병원 광고성 후기·블로그, 실가격·다운타임 비공개 |
| 다이닝/로컬 | Yelp, Google/Naver Map, Resy, OpenTable, TheFork | 식이 필터(비건/할랄/글루텐프리/코셔) + 지도→예약→결제 원스톱 | 식이 필터 부재, 예약 앱 분절, 외국어 메뉴/예약 약함 |
| 여행/체험 | Klook, GetYourGuide, Viator, Airbnb Exp/Services | 외국인 대상 다국어 액티비티 즉시 예약, 명확한 취소·미팅포인트, 모바일 바우처 | 로컬 액티비티는 한국어 전용 플랫폼에 잠겨 있음 |
| 잉여/딜·소셜 | Too Good To Go, Timeleft | 잉여 음식 50~75% 할인 픽업 / 낯선 사람 매칭 디너 | 외국인이 쉽게 못 찾음(한국어 앱 위주) |
| 성분·발견 | Yuka, INCI Decoder, Think Dirty, Supergreat | 바코드 스캔 → 성분 점수·기능 설명, 커뮤니티 리뷰/라이브 | 한글 성분표 해독 불가, K-뷰티 영문 성분 DB 빈약 |

---

## 1. 뷰티/살롱 예약 (Treatwell · StyleSeat · Booksy · Fresha · Vagaro)

### 1-1. Treatwell (유럽)
- [사실] 2025년 초 기준 **13개국 60,000+ 파트너 살롱, 연 1억+ 예약 처리**. 유럽 뷰티 예약 마켓플레이스 1위. 출처: https://businessmodelcanvastemplate.com/blogs/how-it-works/treatwell-how-it-works
- [사실] **"discovery → confirmation까지 3클릭"**, 예약 확정은 이메일·고객계정으로 **즉시 발송**. 실시간 availability 확인 후 몇 클릭으로 예약. 출처: 동상 + https://www.visa.co.uk/small-business-toolkit/tools/online-booking/treatwell.html
- [사실] **선결제(pre-paid)로 노쇼 방지**, 온라인 선불 시 2%+VAT 소액 수수료. 노쇼율 ~50% 감소. 출처: https://www.treatwell.co.uk/partners/solutions/payments/
- [사실] 마지막/비수기 시간대 **스마트 프라이싱(할인)** + 예약마다 포인트 적립(리워드). 출처: https://www.treatwell.co.uk/
- **잘하는 것**: 발견(discovery) + 실시간 예약 + 결제를 한 흐름으로. 마켓플레이스로 신규 고객 유입.
- **차별점**: 비수기 동적 할인 + 리워드 포인트로 수요 평탄화.
- **GLOU 차용**: 빈 시간(비수기) 동적 할인을 "외국인 라스트미닛 딜"로 재포장(외국인 일정은 유연 → 빈 슬롯 채우기에 최적).

### 1-2. StyleSeat (미국)
- [사실] **부킹 프로필에 영상(video) 추가가 가능한 유일 플랫폼** — 디자이너가 자기 작업을 시각적으로 포트폴리오화. 출처: https://www.styleseat.com/join/hairstylists
- [사실] 고객은 서비스 메뉴·설명·가격을 보고 **24/7 셀프 예약 + 카드 온파일**. 출처: 동상
- [사실] **보증금(flat fee 또는 %)·노쇼 보호** → 예약 완료율 최대 **25% 개선**. 출처: https://www.styleseat.com/blog/styleseat-deposits/ , https://www.styleseat.com/join/deposits
- [사실/주의] 마켓플레이스가 데려온 신규 고객 매출의 **약 30% 수수료**(공격적). 출처: https://glossgenius.com/blog/styleseat-vs-booksy
- **잘하는 것**: "사람(디자이너) 중심" 발견. 살롱이 아니라 개인 스타일리스트를 팔로우/예약.
- **차별점**: 영상 포트폴리오 + 개인 단위 신뢰.
- **GLOU 차용**: 매장이 아닌 **개인 디자이너/원장 포트폴리오(전후 사진·영상) 기반 선택** UX. 외국인은 매장명보다 "이 사람이 내 모발/피부를 다룰 수 있나"를 본다.

### 1-3. Booksy
- [사실] **5,000만+ 고객**. 실시간 availability + 검증 리뷰 + **포트폴리오 브라우징**으로 매칭. 출처: https://booksy.com/en-us/ , https://blog.booksy.com/us/beauty/find-your-forever-stylist/
- [사실] 자동 노쇼 방지(미결제 차단), 안전 카드결제, 상세 고객 프로필. 출처: https://biz.booksy.com/en-us/blog/booksy-alternatives-for-salons
- [추정] 텍스처/전문 분야(예: Black hair, 곱슬) 전용 필터의 명시적 존재는 이번 검색으로 확정 못 함 → 서비스명 검색(예: "curly", "silk press")으로 우회 탐색하는 구조로 보임. (확정 필요) 출처: https://booksy.com/en-us/s/hair-salon
- **GLOU 차용**: "포에버 스타일리스트(단골 만들기)" 내러티브 — 외국인 재방문/체류 락인.

### 1-4. Fresha
- [사실] 2025년 4월부터 **스태프 캘린더당 월 £9.95** 구독형으로 가격 모델 변경(저비용 진입). 마켓플레이스 병행. 출처: https://www.fresha.com/for-business/salon/best-salon-software , https://glossgenius.com/blog/fresha-vs-vagaro
- **차별점**: 저수수료/구독형으로 공급자(살롱) 온보딩 마찰이 낮음 → 공급 측 확장에 유리.
- **GLOU 시사**: 공급자(로컬 매장) 확보 시 수수료 구조 설계의 벤치마크.

### 1-5. Vagaro
- [사실] **카드 온파일 필수화** 후 예약 가능(노쇼 시 수수료 자동 청구). 온라인 예약 시 **보증금(deposit) 요구** 옵션. 출처: https://support.vagaro.com/hc/en-us/articles/17733255316763-Require-a-Credit-Card-on-File-to-Book , https://support.vagaro.com/hc/en-us/articles/17733255383707-Require-a-Customer-Deposit-for-Online-Booking
- **차별점**: 노쇼/취소/리스케줄 정책을 세밀하게 룰화.
- **GLOU 차용**: "카드 온파일 + 보증금"을 **노쇼 리스크가 큰 외국인 예약의 신뢰 장치**로 표준 탑재.

> **살롱 카테고리 공통 표준 UX**: ① 실시간 빈 슬롯 → 즉시 100% 확정(No-contact, 전화 불필요) ② 카드 선결제/보증금으로 노쇼 방지 ③ 개인(디자이너) 포트폴리오·영상 ④ 서비스 극세분(메뉴 단위) ⑤ 마켓플레이스 발견.

---

## 2. 메디컬뷰티 리뷰 (RealSelf)

- [사실] 실제 환자가 공유한 **30만+ 리뷰**, 전후 사진 + "Worth It" 평점 + **평균 비용** 공개. 예: 가슴확대 95% Worth It(6,902리뷰, 평균 $7,865), 눈성형 93%($6,304). 출처: https://www.realself.com/ , https://www.realself.com/reviews
- [사실] 시술별 **다운타임/회복 정보**까지 구조화(예: Emface는 다운타임 없음). 출처: https://www.realself.com/news/emface-before-and-after-results
- **잘하는 것**: "이 시술 할까 말까"를 **실가격 + 보정 없는 전후 + 다운타임 + 집단 투표(Worth It)**로 의사결정.
- **차별점**: 광고가 아니라 **환자 1인칭 경험 + 문제 해결 중심 검색**("never again" 경고담까지).
- **GLOU 차용**: K-뷰티 시술(스킨부스터·레이저·리프팅 등) 리뷰를 **① 실지불 금액 ② 다운타임 ③ 보정 없는 전후 ④ Worth It 투표**로 표준화. 한국 클리닉은 이 셋이 모두 불투명 → GLOU의 핵심 신뢰 무기.

---

## 3. 다이닝/로컬 (Yelp · Google/Naver Map · Resy · OpenTable · TheFork)

- [사실] **Yelp 식이 필터**: gluten-free, halal, keto, kosher, pescatarian, vegan, vegetarian 옵션 보유 여부를 검색결과에서 자동 하이라이트(메뉴 사진 안 뒤져도 됨). 출처: https://blog.yelp.com/news/yelp-is-releasing-a-new-personalized-app-experience/
- [사실] **OpenTable** 65,000+ 식당, 날짜·시간·위치 + **식이제한 필터** 검색. 출처: https://www.opentable.com/
- [사실] **Resy**(Amex 소유)는 프리미엄/큐레이션 가이드 중심, 다이너 네트워크는 OpenTable·TheFork보다 작음. **TheFork**는 유럽·중남미·호주 강세. 출처: https://www.theforkmanager.com/en/blog/best-restaurant-booking-systemst-restaurant-booking-systems-in-2025
- [사실] **미충족 영역**: 그룹 단위(여러 명의 겹치는 식이제한) 교집합 필터는 현재 Yelp·Google에도 없음 → 빈틈. 출처: https://github.com/muaddibco/RealWorldProblems/issues/1054
- [사실] 한국: 외국인은 Google Maps가 약해 **Naver Map(다국어 영/일/중) + Kakao Map**을 병행. 단 이들도 비건/할랄 등 **식이 필터는 부재**. 출처: https://klifechoice.com/naver-map-vs-kakao-map-korea/ , https://visit.seoul.kr/en/articles/seoul-navigation-apps-guide-2026
- **GLOU 차용**: ① **식이/라이프스타일 필터**(비건/할랄/글루텐프리/알레르기)를 한국 맛집·카페에 입혀 외국인 1차 페인 해소 ② 발견→예약→결제 **원스톱**(한국은 지도/예약/결제가 분절).

---

## 4. 여행/체험·로컬 가이드 (Klook · GetYourGuide · Viator · Airbnb Experiences/Services)

- [사실] 2025년 체험 예약 3강: **Viator**(미주·TripAdvisor계), **Klook**(아·태 + 티켓/교통/유틸리티 올인원), **GetYourGuide**(유럽 시티투어·박물관). 출처: https://www.cheshirepeopleandplaces.com/picks/best-tour-booking-sites/
- [사실] GetYourGuide는 **미팅포인트·언어 옵션·취소 라벨·모바일 티켓·리뷰**를 스캔하기 쉽게 제시(외국인 친화 정보 구조). 출처: https://adventureglimpse.com/getyourguide-klook-or-viator-comparing-the-top-3-experience-booking-platforms/
- [사실] **Klook 한국 K-뷰티 수요 폭증**: 2025년 헤드스파 트래픽 **+230%**, 보톡스·스킨부스터·리프팅을 **현지 가격으로** 예약 가능. 출처: https://www.klook.com/en-US/activity/122334-korean-beauty-and-skin-care-clinic-reservation/ , https://www.kedglobal.com/retail/newsView/ked202512280003
- [사실/핵심] **Airbnb Services(2025 여름 출시)**: chefs, **massage, spa treatments, personal training, hair, makeup, nails** 등 10개 카테고리 × 260개 도시. 호스트는 신원검증 + **라이선스·자격증 제출**. Experiences는 650개 도시 재론칭, **숙박 안 해도 로컬 체험 예약 가능**. 출처: https://news.airbnb.com/airbnb-2025-summer-release/ , https://arival.travel/article/inside-airbnb-experiences-relaunch/
- **잘하는 것**: 외국인 대상 **다국어 + 즉시 예약 + 명확한 취소/미팅포인트/바우처**.
- **차별점(Klook)**: 한국에서 외국인에게 **시술까지** 현지가로 연결(GLOU의 직접 인접 경쟁자이자 모델).
- **GLOU 차용**: ① 다국어 + **명확한 취소 정책/미팅포인트/모바일 바우처** 표준 ② Airbnb Services형 **자격증·라이선스 검증된 로컬 매장** 신뢰 레이어 ③ "숙박 무관, 로컬 발견" 포지션(GLOU도 여행자뿐 아니라 체류 외국인 타깃).

> **경쟁 경고**: Klook가 이미 외국인에게 K-뷰티 시술을 팔고 있고, Airbnb Services가 hair/spa/nails로 진입. GLOU는 **성분·효과 기반 AI 추천 + 지역·테마 코스 큐레이션**으로 차별화해야 함(단순 예약 중개는 레드오션).

---

## 5. 잉여/딜 + 소셜 ('TimeLeft' 정체 확인)

- [사실/중요] **TimeLeft ≠ Too Good To Go.** 둘은 전혀 다른 서비스.
  - **Too Good To Go**: 매장 마감 시간대 잉여 음식을 **"Surprise Bag"**으로 원가의 **50~75% 할인** 픽업. 봉투당 ~2.7kg CO2e 절감. 출처: https://www.toogoodtogo.com/en-us/how-does-the-app-work
  - **Timeleft**: **낯선 사람 5명과 매칭 디너**(연령·성격·**언어 선호** 기반 매칭). 3M+ 유저, 160+ 도시(서울 포함), 48개국. 결제는 현장 음식값. 출처: https://timeleft.com/ , https://help.timeleft.com/hc/en-150/articles/14235814215452-Locations-Dinner-time
  - → 외국인이 "한국에서 쓰는 Time Left"는 **소셜 디너 매칭 앱**이지 잉여음식 앱이 아님. (질문의 가설은 오답으로 확정)
- [사실] 외국인 한국 생활 필수앱: **Naver Map / Kakao Map**(다국어), **Papago**(번역, Citymapper(서울 한정, 영어). 출처: https://visit.seoul.kr/en/articles/seoul-navigation-apps-guide-2026 , https://www.digitalnomadskorea.com/post/korea-7-must-have-apps-for-digital-nomads
- **GLOU 차용**: ① Timeleft의 **언어 선호 기반 그룹 매칭** → 외국인↔로컬 "테마 코스 동행" 매칭 ② Too Good To Go의 **라스트미닛 잉여 슬롯 딜** → 살롱/카페 빈 시간을 외국인용 surprise 딜로.

---

## 6. 뷰티 발견/성분 앱 (Yuka · INCI Decoder · Think Dirty · Supergreat)

- [사실] **Yuka**: 바코드 스캔 → 식품 1.5M·화장품 500K DB에서 **0~100 점수**(내분비교란·발암·알레르기·자극·오염 위험도). 무료 + 유료 $10~20/년, **브랜드 후원 불가(중립성)**. 출처: https://yuka.io/en/ , https://www.glossy.co/beauty/yuka-beauty-wellness-product-scanning-app/
- [사실] **Think Dirty**: 1~10 점수(1=깨끗). **INCI Decoder**: 안전성보다 **성분 기능 교육**에 초점. 출처: https://suvarna.co.uk/blogs/news/the-think-dirty-app-vs-inci-beauty-yuka-and-more-your-insider-guide-to-clean-beauty-tech
- [사실/한계] 이 앱들은 **농도 무시**(성분 존재만으로 감점) → 화장품 화학자들이 "오해 소지" 비판. 출처: https://www.newbeauty.com/view/beauty-ingredient-apps , https://amperna.com/blogs/news/barcode-scanning-apps-yuka-thinkdirty-helpful-harmful
- [사실] **Supergreat**: Gen-Z 뷰티 **커뮤니티 + 라이브스트림 리뷰**(월 100만 라이브), Supercoins 리워드. Series A $6.5M. 출처: https://supergreat.com/ , https://beautymatter.com/articles/beauty-community-app-supergreat-raises-65-million-in-series-a
- **GLOU 차용**: ① **성분 기능 설명(INCI Decoder형) + 효과 기반 추천**을 외국인 영문으로 — 한글 성분표를 못 읽는 외국인의 핵심 페인 ② 점수의 농도 한계를 피해 **"성분→효과→피부타입 적합도"** 추천(공포 마케팅 대신 큐레이션) ③ Supergreat형 커뮤니티 리뷰로 신뢰 누적.

---

## 7. 글로벌 표준 UX vs 한국 현실(외국인 입장) — as-is → to-be

| 영역 | 한국 현실 as-is (외국인 입장) | 글로벌 표준 UX | GLOU to-be |
|---|---|---|---|
| 살롱 예약 | 전화/카톡 수동·워크인, 외국어 불가, 확정 불확실 | 실시간 빈 슬롯 → 3클릭 100% 확정(No-contact) | 영문 실시간 예약 + 즉시 확정 + 카드 선결제/보증금 |
| 디자이너 선택 | 매장 단위, 누가 시술할지 모름 | 개인 포트폴리오·영상(StyleSeat) | 원장/디자이너 전후·영상 + "곱슬/시술 전문" 태그 |
| 식당 발견 | 비건/할랄/알레르기 필터 부재, 메뉴 외국어 약함 | 식이 필터 + 지도→예약→결제 원스톱(Yelp/OpenTable) | 식이·알레르기 필터 + 영문 메뉴 + 원스톱 예약 |
| 시술 리뷰 | 광고성 블로그, 실가격·다운타임 비공개 | 보정 없는 전후 + 실지불액 + 다운타임 + Worth It(RealSelf) | 실가격·다운타임·전후·투표 표준화(영문) |
| 성분 이해 | 한글 성분표 해독 불가 | 스캔→성분 점수·기능(Yuka/INCI) | 영문 성분→효과→피부타입 적합 AI 추천 |
| 로컬 체험 | 한국어 전용 플랫폼에 잠김 | 다국어 즉시 예약 + 취소·미팅포인트·바우처(Klook/GYG) | 다국어 코스 큐레이션 + 명확 취소·바우처 |
| 노쇼/신뢰 | 외국인 노쇼 리스크로 매장이 꺼림 | 카드 온파일 + 보증금(Vagaro/StyleSeat) | 카드 온파일/보증금으로 매장-외국인 양방향 신뢰 |

---

## 8. GLOU가 글로벌 표준에서 그대로 '얹을' UX (핵심)

1. **No-contact 즉시 확정 예약** (Treatwell·Fresha): 실시간 빈 슬롯 → 3클릭 → 100% 확정. 한국 외국인 예약의 1번 페인(전화/카톡/언어)을 한 번에 제거.
2. **카드 온파일 + 보증금 노쇼 방지** (Vagaro·StyleSeat): 매장이 외국인 예약을 안심하고 받게 하는 신뢰 장치. 공급(매장) 온보딩의 핵심.
3. **개인 디자이너/원장 포트폴리오(전후·영상) 기반 선택** (StyleSeat·Booksy): 매장명이 아니라 "이 사람이 내 모발/피부를 다룰 수 있나"로 선택 + 전문 태그(곱슬/특정 시술).
4. **식이·라이프스타일 필터** (Yelp·OpenTable): 비건/할랄/글루텐프리/알레르기 필터를 한국 맛집·카페·웰니스에 입힘. 그룹 교집합 필터는 글로벌에도 빈틈 → 차별화 기회.
5. **시술 신뢰 3종 세트: 실지불액 + 다운타임 + 보정 없는 전후 + Worth It 투표** (RealSelf): 한국 클리닉이 모두 불투명한 지점을 영문 표준으로.

---

## 출처 (상위)
1. Treatwell 동작 원리/규모: https://businessmodelcanvastemplate.com/blogs/how-it-works/treatwell-how-it-works
2. StyleSeat 영상 포트폴리오·보증금: https://www.styleseat.com/join/hairstylists , https://www.styleseat.com/blog/styleseat-deposits/
3. RealSelf 전후·실가격·Worth It: https://www.realself.com/ , https://www.realself.com/reviews
4. Yelp 식이 필터: https://blog.yelp.com/news/yelp-is-releasing-a-new-personalized-app-experience/
5. Klook 한국 K-뷰티 시술(헤드스파 +230%): https://www.kedglobal.com/retail/newsView/ked202512280003
6. Airbnb 2025 Services/Experiences(hair·spa·nails): https://news.airbnb.com/airbnb-2025-summer-release/
7. Timeleft(소셜 디너 ≠ TGTG): https://timeleft.com/ · Too Good To Go: https://www.toogoodtogo.com/en-us/how-does-the-app-work
8. Yuka 성분 스캔·중립성: https://yuka.io/en/ , https://www.glossy.co/beauty/yuka-beauty-wellness-product-scanning-app/

> 미확정/후속 확인 필요: ① Booksy의 텍스처별(Black hair/곱슬) 전용 필터 명시 존재 여부 ② Klook K-뷰티 리스팅의 다국어/가격 투명도 상세(페이지 403으로 직접 fetch 실패) ③ 한국 내 외국인 사용 생활앱의 정량 점유율.
