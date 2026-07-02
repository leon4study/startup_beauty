# 발산적 창업 아이디어 + 아이디어 발굴 리소스/방법론 (10)

> 작성일: 2026-07-01 | 프로젝트: 모두의 창업 프로젝트(2026, 중앙대) R1 / 현재 아이디어 = GLOU
> 목적: (A) 이종 산업까지 포괄하는 아이디어 발굴 사이트·방법론 큐레이션 + (B) 이 팀이 이길 수 있는 발산 아이디어 15개 생성 + (C) 재실행 가능한 발굴 절차
> 표기: [사실] = 출처 기반, [추정] = 본 보고서 해석. 모두의창업 6대 산업 태그 = A(AI·빅데이터)/B(Bio-Health)/C(Contents·Culture)/D(DT·딥테크)/E(Energy·ESG)/F(Food-Tech)
> 팀 자산(지렛대): ①글로벌 라이프스타일 인플루언서(SNS·마케팅 데이터 분석, 팔로워 1만/조회수 100만+, 180개국 외국인 네트워크) ②데이터·개발 + K-뷰티 리뷰(아마존·틱톡) 분석 + RAG(GraphRAG/LightRAG) 파이프라인 + 화학·약학 이해 ③뷰티 인플루언서. 공통: 콘텐츠 제작력 + 외국인 인사이트 + 데이터/AI

---

## 0. 한 줄 결론

- 이 팀의 진짜 해자는 "GLOU라는 특정 서비스"가 아니라 **세 가지 재사용 자산(글로벌 외국인 네트워크 + K-뷰티 리뷰 RAG 파이프라인 + 콘텐츠 제작력)**이다. 따라서 발산은 이 3자산을 다른 조합으로 재배치하는 방향으로 한다.
- 발산 결과 **베스트 5**는 GLOU와 인접하거나 GLOU를 더 강하게 만드는 B2B/데이터 레버리지에 몰려 있다(아래 3장).
- 모두의창업 심사·피칭 관점에서는 "이미 가진 데이터 자산(리뷰 RAG)"을 제품화하는 아이디어가 **증거 기반 차별화**가 가장 쉽다.

---

## 1. 미션 A — 아이디어 발굴 리소스·방법론

### 1-A. 글로벌 사이트 (이종 산업 아이디어 소스)

| # | 이름 | 링크 | 한 줄 용도 |
|---|---|---|---|
| 1 | Y Combinator Request for Startups (RFS) | https://www.ycombinator.com/rfs | YC가 "이거 만들어라"고 공개한 분기별 테마 리스트. 2026 RFS는 AI를 'feature가 아닌 foundation'으로 전제 — 거시 방향 캘리브레이션용 |
| 2 | IdeaBrowser (Greg Isenberg) | https://www.ideabrowser.com/ | Reddit·구글트렌드·유튜브 신호를 긁어 매일 1개씩 검증된 아이디어를 점수(검색량/성장%/페인레벨/실현성/창업자적합도/수익)와 함께 제공 |
| 3 | Exploding Topics | https://explodingtopics.com/ | 폭발 직전 검색 트렌드·신생 시장 조기 탐지 — '아직 안 붐빈' 수직 시장 찾기 |
| 4 | Starter Story | https://www.starterstory.com/ | 2,800+ 실제 수익 사업의 창업 스토리 DB — "어떻게 시작·성장했나" 분해 |
| 5 | Failory (Graveyard) | https://www.failory.com/graveyard | 실패한 스타트업 200+ 분석 — "왜 죽었나"로 역설계, 우리 아이디어 사망 시나리오 점검 |
| 6 | Indie Hackers | https://www.indiehackers.com/ | 1인·소규모 창업자 실전 스토리·매출 공개·아이디어 프레임워크 게시판 |
| 7 | Product Hunt | https://www.producthunt.com/ | 매일 신규 런칭 — 인접 카테고리에서 누가 무엇을 만드는지 트렌드 스캔 |
| 8 | BetaList | https://betalist.com/ | 베타 단계 스타트업 디렉토리 — '아직 정식 출시 전' 초기 경쟁/공백 파악 |
| 9 | CB Insights | https://www.cbinsights.com/ | 시장지도·유니콘·투자 테마 리포트 — 톱다운 시장 사이즈·경쟁 구도 |
| 10 | a16z / Sequoia 마켓 테제 | https://a16z.com/ / https://www.sequoiacap.com/ | 톱티어 VC의 시장 논문(market thesis) — 어디에 자본이 모이는지 |
| 11 | r/startups · r/SideProject · r/Entrepreneur | https://reddit.com/r/startups | 창업자·사용자 불만 1차 텍스트. Painstorming 원천(아래 방법론) |
| 12 | Trends.vc | https://trends.vc/ | 압축된 시장 트렌드 리포트(번들/언번들·플레이북). 거시 테마를 빠르게 흡수 |

> 보조: GummySearch(Reddit 페인 마이닝 도구, https://gummysearch.com/)는 **2025년 11월 종료**([사실], Reddit API 가격정책 여파). 대체로 PainOnSocial(https://painonsocial.com/), Reddily(https://reddily.io/) 등이 동일 역할.

### 1-B. 한국 사이트 (생태계·데이터·공고)

| # | 이름 | 링크 | 한 줄 용도 |
|---|---|---|---|
| 1 | 디스콰이엇(Disquiet) | https://disquiet.io/ | 한국 메이커 SNS — 프로덕트 공유·투표·피드백으로 아이디어 검증·초기유저 확보(2025.10 픽셀릭/릴레잇 인수) |
| 2 | 혁신의숲(InnoForest) | https://www.innoforest.co.kr/ | 8,500+ 국내 스타트업의 트래픽·고용·투자·소비자거래 데이터(상당수 무료) — 인접 경쟁/시장 규모 |
| 3 | 로켓펀치(RocketPunch) | https://www.rocketpunch.com/ | 스타트업 인물·채용·기업 DB — 누가 어디서 뭘 하는지 |
| 4 | EO / EO planet | https://eopla.net/ | 미래기술·창업가 영상 미디어·커뮤니티 — 창업가 인터뷰에서 페인·실행 디테일 |
| 5 | 폴인(folin) | https://www.folin.co/ | 업계 현장 인사이트·라이프스타일 창업 케이스(유료) |
| 6 | 아웃스탠딩(outstanding) | https://outstanding.kr/ | IT·스타트업 심층 분석 미디어 |
| 7 | 벤처스퀘어 | https://www.venturesquare.net/ | 국내 스타트업 뉴스·투자·트렌드 |
| 8 | 플래텀(Platum) | https://platum.kr/ | 스타트업 뉴스 + 중화권/글로벌 진출 정보 |
| 9 | 와이즈앱·리테일·굿즈 | https://www.wiseapp.co.kr/ | 앱·소비 데이터(MAU·결제액) — 인접 서비스 실사용 규모 검증 |
| 10 | 아이지에이웍스(IGAWorks) 데이터 | https://www.igaworks.com/ | 모바일인덱스 등 앱 트렌드 데이터 |
| 11 | K-Startup (창업진흥원) | https://www.k-startup.go.kr/ | 2026 예비/초기창업패키지 등 공고·RFP — 정부가 원하는 테마 = 자금이 붙는 방향 |
| 12 | 비즈인포(bizinfo) 통합공고 | https://www.bizinfo.go.kr/ | 2026 중앙부처·지자체 창업지원 통합공고(글로벌 진출/딥테크/Food-Tech 등 유형 확인) |

### 1-C. 방법론 (어떻게 쓰는가)

| 방법론 | 한 줄 + 쓰는 법 |
|---|---|
| **Jobs-to-be-Done (JTBD)** | 사용자가 "고용하는 일"을 정량적으로 정의. Outcome-Driven: '결과 기대치 - 충족도'가 가장 큰 unmet 영역을 찾아 그걸 더 잘 해결(Ulwick). 우리 식: 외국인이 "K-뷰티/한국생활에서 끝내고 싶은 일"을 인터뷰→점수화 |
| **언번들링(Unbundling)** | 비대한 제품(예: Creatrip, Reddit, 네이버지도)에서 한 직무만 떼어내 압도적으로 잘 만든다. 조건: (a) JTBD 편차가 뚜렷 (b) 그 니치가 충분히 큼/성장 중. 우리 식: Creatrip의 '뷰티 예약'만, 네이버지도의 '식이필터'만 |
| **Idea Maze** | 아이디어 = 점이 아니라 미로. History/Analogy/Theory/Direct-experience 4소스로 미로 지도를 먼저 그린 뒤 진입(cdixon). 우리 식: 경쟁사 실패(Seoul Sister 예약없음)·과거 시도를 지도화 |
| **Painstorming** | 커뮤니티(Reddit·디시·블라인드·외국인 카페) 불만을 긁어 빈도순 클러스터링. Zapier+LLM로 자동 리포트화. 빈도=기회 강도. 우리 식: r/korea, r/Living_in_Korea, 외국인 페북그룹 마이닝 |
| **"X for Y" 아비트라지** | 검증된 모델(X)을 새 수직/지역(Y)에 이식. "Collabstr for K-beauty", "GummySearch for 외국인 페인". Insight Arbitrage = 시장이 아직 모르는 통찰의 델타 |
| **밸류 마이그레이션(Value Migration)** | 가치가 빠져나가는 채널(면세·따이궁)→유입되는 채널(틱톡샵·UGC)을 식별해 흐름이 모이는 쪽에 베팅. 우리 식: 중국 면세 채널 쇠퇴 → 서구 D2C·틱톡샵 부상 |
| **틈새 수직화(Verticalization)** | 폭 대신 깊이. 한 산업/세그먼트에 전문화해 높은 마진·진입장벽 구축(nfx '버티컬라이제이션'). Vertical AI = 일반 LLM 위에 도메인 데이터·워크플로 얹기. 우리 식: 'K-뷰티 전용' RAG |

---

## 2. 미션 B — 발산 아이디어 15개 (근접 피벗 → 이종 산업)

> 각 항목: 컨셉 / 타겟 / 팀이 이기는 이유 / 수익 / 모두의창업 적합도(★1~5) / GLOU와의 거리(가까움→멈/태그)

### 근접 (외국인 대상 비뷰티 버티컬)

**1. SeoulPlate — 외국인용 식이필터 다이닝 내비** `[F·A]`
- 컨셉: 할랄/비건/글루텐프리/알러지 필터 + 영어 메뉴·예약을 하나로. 컨셉 1줄: "네이버지도의 식이필터만 언번들링."
- 타겟: 무슬림·비건·알러지 보유 방한 서구·동남아 20~30대.
- 이기는 이유: 외국인 네트워크로 검증 리뷰 확보 + RAG로 메뉴 성분 자동 라벨링(이미 성분 마이닝 역량 보유). 기존 Halal Haseyo/VegeFeed는 단일 종교/식단에 한정.
- 수익: 식당 예약 수수료 + 프리미엄 큐레이션 + 광고. 적합도 ★★★★ (Food-Tech). GLOU와의 거리: **가까움**.

**2. Landing.kr — 외국인 정착 온보딩 OS** `[A·D]`
- 컨셉: 휴대폰 개통(ARC 전 eSIM→010)·집계약·행정(HiKorea)·배달 가입을 단계별 체크리스트+대행으로. 1줄: "외국인 정착의 마찰 전부를 한 앱에."
- 타겟: 신규 거주 유학생·주재원·디지털노마드.
- 이기는 이유: 우리가 이미 정리한 정착 마찰 인사이트(07/02 보고서) + 180개국 네트워크로 다국어 콘텐츠 즉시 제작. 경쟁(Seoulstart 등)은 정보 나열, 우리는 실행 대행.
- 수익: 통신·부동산·금융 제휴 수수료(CPA) + 구독. 적합도 ★★★★ (AI·DT). GLOU와의 거리: **가까움**.

**3. ClinicPass — 외국인 의료·피부과 내비게이션** `[B·A]`
- 컨셉: 영어 가능 클리닉(피부·미용) 투명가격·통역예약·후기. 1줄: "바가지·업셀 공포 없는 미용의료 예약."
- 타겟: 시술 목적 방한 여성, 의료관광객.
- 이기는 이유: '협찬 리뷰 불신'을 검증 후기로 해소(인플루언서 자산) + 성분/시술 RAG로 신뢰 설명. 기존 KRACE·Himedi는 에이전시형(불투명). 단, 의료광고법 규제 주의 [추정].
- 수익: 예약 알선·통역 패키지. 적합도 ★★★★ (Bio-Health). GLOU와의 거리: **가까움-중간**.

### 인접 (크리에이터·브랜드 경제)

**4. UGC Bridge — 한국 브랜드 ↔ 글로벌 마이크로 인플루언서 마켓플레이스** `[C·A]`
- 컨셉: K-뷰티/라이프 브랜드가 180개국 마이크로 크리에이터에게 UGC·캠페인을 셀프서브로 발주. 1줄: "Collabstr for K-beauty(외국인 크리에이터 풀)."
- 타겟: 해외진출 원하는 한국 인디 브랜드 + 해외 마이크로 크리에이터.
- 이기는 이유: 우리 자체가 인플루언서 + 180개국 네트워크 = 공급측을 콜드스타트 없이 시딩. Collabstr/Insense는 K-brand↔외국인 연결 특화가 약함.
- 수익: 거래 수수료(10~20%) + 구독. 적합도 ★★★★★ (Contents). GLOU와의 거리: **중간**.

**5. ReactionLens — 브랜드용 '외국인 반응' 인사이트 SaaS** `[A·C]`
- 컨셉: 한국 브랜드의 아마존·틱톡·유튜브 해외 리뷰/댓글을 RAG로 마이닝해 "서구 소비자가 뭘 좋아/싫어하나"를 대시보드로. 1줄: "Revuze의 K-뷰티 특화 + 외국인 정성 인사이트."
- 타겟: 글로벌 진출 K-뷰티 브랜드 마케팅팀.
- 이기는 이유: **이미 보유한 아마존·틱톡 리뷰 RAG 파이프라인을 그대로 제품화**(자산 직결). 성분/약학 이해로 클레임 검증까지.
- 수익: B2B SaaS 시트/리포트 구독. 적합도 ★★★★★ (AI·빅데이터). GLOU와의 거리: **중간**.

**6. SkinMatch API — 성분·효과·피부타입 매칭 엔진(B2B)** `[A·B]`
- 컨셉: '성분-효과-피부타입-리뷰근거'를 매핑한 API/임베드 위젯. 1줄: "K-뷰티 전용 Skincare API + RAG 추천."
- 타겟: 커머스·브랜드몰·뷰티앱(추천 위젯 필요).
- 이기는 이유: GraphRAG로 성분-효과 그래프 구축 = 단순 키워드 API(skincareapi.dev) 대비 설명가능·근거제시. 화학/약학 역량이 데이터 신뢰의 핵심.
- 수익: API 호출 과금 + 화이트라벨. 적합도 ★★★★★ (AI·Bio). GLOU와의 거리: **중간**.

**7. K-Launch — K-뷰티/라이프 브랜드 해외진출 대행** `[C·A]`
- 컨셉: 틱톡샵 우선(MBX식 'TikTok-first') → 아마존 확장의 풀퍼널 진출 대행(콘텐츠+크리에이터+반응분석). 1줄: "THG식 진출 대행의 K-뷰티 부티크 버전."
- 타겟: 진출 자원 부족한 중소 K-브랜드.
- 이기는 이유: 인플루언서의 핵심 역량(콘텐츠+네트워크) + 데이터(반응분석)를 한 팀이 묶음 제공. 서비스→데이터→SaaS로 진화 가능.
- 수익: 리테이너 + 매출 쉐어. 적합도 ★★★★ (Contents). GLOU와의 거리: **중간**.

### 데이터 (K-beauty RAG 제품화)

**8. ReviewMine — K-뷰티 리뷰 마이닝 인사이트 툴** `[A]`
- 컨셉: "이 성분/제품에 대해 서구·동남아 소비자가 실제로 한 말"을 질문형(자연어)으로 답하는 리서치 코파일럿. 1줄: "VOC AI의 K-뷰티·다국어 특화."
- 타겟: 브랜드 R&D·상품기획·해외MD.
- 이기는 이유: 리뷰 RAG 자산 + 다국어(180개국) 코퍼스 정규화 노하우.
- 수익: SaaS 구독. 적합도 ★★★★ (AI·빅데이터). GLOU와의 거리: **중간-멈**.

**9. DermaGraph — 성분-효과-피부타입 지식그래프(소비자용)** `[B·A]`
- 컨셉: 6번의 소비자향 버전. 사진/설문→피부타입→근거기반 루틴 추천. 1줄: "설명가능한 K-뷰티 추천 + 약학 검증."
- 타겟: 외국인+내국인 스킨케어 입문자.
- 이기는 이유: 단순 ML 추천(Kaggle류) 대비 근거·성분상호작용까지 RAG로 설명.
- 수익: 프리미엄 구독 + 제품 어필리에이트. 적합도 ★★★★ (Bio·AI). GLOU와의 거리: **중간**.

### 아웃바운드 (해외진출 지원)

**10. CrossBorder Beauty Index — 글로벌 K-뷰티 트렌드 데이터 구독** `[A·C]`
- 컨셉: 시장별(미국/서유럽/동남아) 떠오르는 성분·포맷·클레임을 틱톡·아마존 신호로 주간 리포트. 1줄: "Exploding Topics의 K-뷰티 버티컬."
- 타겟: 브랜드·OEM/ODM·투자자.
- 이기는 이유: 외국인 네트워크가 정성 신호를, RAG가 정량 신호를 결합.
- 수익: 리포트 구독(B2B). 적합도 ★★★★ (AI). GLOU와의 거리: **중간-멈**.

### 이종 (콘텐츠+데이터의 다른 산업)

**11. HallyuLingua — K-뷰티/라이프로 배우는 한국어** `[C·A]`
- 컨셉: 화장품 성분·뷰티 루틴·카페 주문 등 '실제 라이프 상황'으로 한국어 학습(쉐도잉+OCR 메뉴 스캔). 1줄: "TTMIK/Koko의 K-뷰티·라이프 테마판."
- 타겟: K-콘텐츠로 한국에 빠진 서구 20~30대 여성(우리 핵심 타겟과 동일!).
- 이기는 이유: 동일 타겟·동일 콘텐츠 자산 재활용. 인플루언서가 학습 콘텐츠를 직접 제작. 적합도 ★★★ (Contents·AI). GLOU와의 거리: **멈**.

**12. PersonaK — AI K-뷰티 인플루언서/페르소나 스튜디오** `[C·A·D]`
- 컨셉: 브랜드용 다국어 AI 인플루언서(성분지식 RAG로 '말이 되는' 멘트) 생성·운영. 1줄: "할루시네이션 없는 뷰티 버추얼 휴먼."
- 타겟: 24/7 다국어 콘텐츠가 필요한 브랜드.
- 이기는 이유: 콘텐츠 감각 + 성분 RAG로 '틀린 말 안 하는' 페르소나(일반 AI인플루언서 약점 보완). 과감한 베팅. 적합도 ★★★ (Contents·DT). GLOU와의 거리: **멈**.

**13. GreenRoutine — 친환경/클린뷰티 검증·탄소 라벨** `[E·A·B]`
- 컨셉: 성분·패키징의 ESG/클린뷰티 주장을 RAG로 검증하고 '그린워싱 점수' 제공. 1줄: "뷰티판 클린 라벨 검증기."
- 타겟: 가치소비 서구 소비자 + ESG 압박받는 브랜드.
- 이기는 이유: 약학·성분 역량 = 클레임 진위 판별의 핵심. Energy·ESG 산업군 커버(모두의창업 6대 중 E는 경쟁 적음 [추정]). 적합도 ★★★ (ESG·Bio). GLOU와의 거리: **멈**.

**14. SilverGlow — 시니어 대상 안전 스킨케어 코치** `[B·A]`
- 컨셉: 약물-화장품 상호작용·민감피부 고려한 시니어 맞춤 루틴(RAG 약학 검증). 1줄: "복용약과 안 부딪치는 스킨케어."
- 타겟: 한국/해외 시니어(고성장·미개척).
- 이기는 이유: 약학 이해가 안전성 차별화. 이종 세그먼트로 확장. 적합도 ★★★ (Bio·AI). GLOU와의 거리: **멈**(이종).

**15. ScanTrust — 글로벌 성분 안전 스캐너(다국가 규제 매핑)** `[B·A·F]`
- 컨셉: 제품 바코드/성분 스캔→해당국(EU/US/한국) 규제·알러지·금지성분 즉시 판정. 1줄: "TagHalal의 화장품+식품 규제 통합판."
- 타겟: 국경 넘는 소비자·해외직구족·역직구 브랜드.
- 이기는 이유: 다국가 성분 규제 RAG = 외국인 인사이트 + 약학 + 데이터의 교집합. 적합도 ★★★★ (Bio·Food). GLOU와의 거리: **멈**.

---

## 3. 미션 B 결론 — 베스트 5 추천

> 기준: ①팀 자산 직결도(콜드스타트 회피) ②모두의창업 증거 기반 차별화 ③수익화 명료성 ④GLOU와의 시너지(둘 다 살릴 수 있는가)

1. **#5 ReactionLens (브랜드용 외국인 반응 SaaS)** — **이미 가진 리뷰 RAG를 그대로 제품화**. 데모를 당장 만들 수 있어 피칭에서 "증거"가 가장 강함. B2B라 수익 명료. `A·C` ★★★★★
2. **#4 UGC Bridge (K-brand↔글로벌 마이크로 인플루언서 마켓)** — 팀이 곧 공급(인플루언서)이라 공급측 콜드스타트가 없음. 180개국 네트워크가 그대로 해자. `C·A` ★★★★★
3. **#6 SkinMatch API (성분·효과 매칭 B2B)** — 화학/약학 + GraphRAG의 정체성과 가장 일치. GLOU의 추천 엔진으로도 재사용 가능(자산 공유). `A·B` ★★★★★
4. **#1 SeoulPlate (식이필터 다이닝)** — GLOU와 가장 가까운 비뷰티 확장. 외국인 페인(식이필터 부재)이 검증돼 있고 Food-Tech 태그 확보. GLOU 번들의 한 모듈로 흡수 가능. `F·A` ★★★★
5. **#2 Landing.kr (정착 온보딩 OS)** — 정착 마찰 인사이트(07/02 보고서)와 직결, 시장 큼. GLOU와 동일 사용자 풀을 공유해 교차판매. `A·D` ★★★★

> 전략적 함의 [추정]: 1~3위는 **B2B·데이터 레버리지(가진 자산 직결)**, 4~5위는 **GLOU의 모듈/확장**이다. 즉 GLOU를 버리지 않고도, 같은 자산으로 더 방어 가능한 B2B 라인(ReactionLens·SkinMatch)을 '듀얼 트랙'으로 검토할 만하다. GLOU=B2C 학습/유저획득, B2B=수익·해자.

---

## 4. 미션 C — 재실행 가능한 아이디어 발굴 절차 (반복 루프)

> 주기: 2주 1사이클 권장. 산출물은 항상 '스코어카드 1장'.

1. **소스 수집(Source)** — 위 1-A/1-B 사이트에서 신호 수집. 고정 루틴: ①YC RFS·a16z 테제(거시 방향) ②Exploding Topics·Trends.vc(트렌드) ③K-Startup/bizinfo 공고(자금 방향) ④혁신의숲(인접 경쟁 규모).
2. **페인 마이닝(Mine)** — Painstorming: r/korea·r/Living_in_Korea·외국인 페북그룹·디스콰이엇 + 우리 보유 아마존/틱톡 리뷰를 RAG로 질의("외국인이 가장 자주 막히는 일은?"). 빈도순 클러스터링 → unmet 후보 리스트.
3. **프레이밍(Frame)** — 각 후보를 JTBD로 재진술("__하려는데 __가 막힌다"). 언번들링 렌즈로 "어떤 비대 제품의 한 직무인가?" / "X for Y"로 "검증된 모델 X를 우리 Y에 이식하면?" 적용. Idea Maze로 과거 시도·실패(Failory류) 점검.
4. **팀 자산 매칭(Match)** — 후보별로 3자산(외국인 네트워크 / 리뷰 RAG·약학 / 콘텐츠) 중 몇 개를 쓰는지 표시. **2개 이상 쓰면 통과**(콜드스타트·차별화 동시 해결).
5. **스코어링(Score)** — 6축 1~5점: ①페인 강도(빈도) ②팀 자산 적합도 ③시장 규모·성장(밸류 마이그레이션 방향인가) ④경쟁 공백 ⑤수익화 명료성 ⑥모두의창업 6대 산업 태그·증거 데모 가능성. 합산 상위 + "당장 데모 가능"한 것 우선.
6. **킬 기준(Kill)** — 한국번호/규제(의료·금융 광고)로 막히는지, 거대경쟁(Creatrip)이 1주면 복제 가능한지 체크. 막히면 폐기 또는 언번들 더 좁히기.

> 자동화 팁 [추정]: 2단계는 Zapier/스크립트 + LLM으로 주간 페인 리포트 자동 생성, 5단계는 스프레드시트 스코어카드로 표준화하면 매 사이클 30분 내 1라운드 가능.

---

## 5. 저장 경로

`/Users/jun/GitStudy/startup_beauty/data/research/market/10_divergent_ideas.md`

### 주요 출처(원문 유지)
- YC RFS https://www.ycombinator.com/rfs / YC S26 RFS 정리 https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas
- IdeaBrowser https://www.ideabrowser.com/ / https://www.gregisenberg.com/blog/find-winning-startup-ideas-from-ai-and-data
- Unbundling Reddit (Isenberg) https://latecheckout.substack.com/p/the-ultimate-guide-to-unbundling / Painstorming https://www.newline.co/@kchan/conducting-painstorming-on-reddit-with-zapier-and-chatgpt--d0d5564f
- Idea Maze (cdixon) https://cdixon.org/2013/08/04/the-idea-maze/ / JTBD https://strategyn.com/jobs-to-be-done/ / Verticalization https://www.nfx.com/post/verticalization-of-everything
- Disquiet https://disquiet.io/ / 혁신의숲 https://www.innoforest.co.kr/ / K-Startup https://www.k-startup.go.kr/ / bizinfo 통합공고 https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/view.do?pblancId=PBLN_000000000116904
- Collabstr https://collabstr.com/ / Insense https://insense.pro/ / Nuri Lounge(K-beauty 크리에이터) / Skincare API https://skincareapi.dev/ / Revuze https://www.revuze.it/ / VOC AI
- TikTok-first 진출(MBX) https://digiday.com/marketing/how-3-brands-are-using-tiktok-shop-to-expand-abroad/ / Beauty of Joseon UK TikTok(THG) https://retailtechinnovationhub.com/
- 정착: Kimchi Mobile(ARC/MVNO) https://www.kimchimobile.com/guides/korea-mvno-for-foreigners/ / Seoulstart https://seoulstart.com/guides/top-websites-for-foreigners-in-korea / HiKorea
- 의료: KRACE https://krace.kr/book-clinic-korea-foreigner/ / Himedi https://himedi.com/ / K-MedLinker https://www.k-medlinker.com/
- 식이: Halal Haseyo / VegeFeed / TagHalal https://apps.apple.com/us/app/taghalal-halal-food-scanner/id1626990007
- 한국어 학습: TTMIK / Koko https://apps.apple.com/us/app/koko-learn-korean-with-ai/id6751234829 / HeyKorea
