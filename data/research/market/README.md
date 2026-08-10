# GLOU 시장조사 종합 보고서 (Master Synthesis)

> 모두의 창업 프로젝트(2026, 중앙대) R1 — GLOU: 외국인 대상 서울 K-뷰티 라이프 큐레이션
> 조사 방식: 10개 병렬 리서치(WebSearch 130회+), 모든 수치 출처 표기, [사실]/[추정] 구분
> 최종 정리: 2026-07-01 · 상세는 각 절의 링크 파일 참조

---

## 0. TL;DR — 한 장 결론

1. **시장은 진짜다.** 방한 외국인 **쇼핑 1위 = 향수·화장품 71.8%**, 외국인 뷰티 지출 8,433억(+38%)·의료관광 2.08조(+65%). [02·04·06]
2. **타겟은 "유럽"이 아니라 "영어권 서구(미국 주도 + 영국 + 영어권 유럽/오세아니아)".** 멘토님의 "중국 레드오션/서구 블루오션"은 옳지만, 유럽 단독은 볼륨이 1/8.6로 너무 작다. **미국 단독(132만)만으로 서유럽 4국 합(53.3만)의 2.5배**, 게다가 **미국이 2026 Q1 K-뷰티 수출 1위로 중국 추월**. [05·09]
3. **핵심 페인 3종**: ①한국번호/ARC 없으면 예약·결제 차단 ②협찬으로 신뢰 붕괴된 추천 ③바가지·업셀·시술실패 공포. [02·08]
4. **단, 진입장벽이 이번 달 변했다.** 2026-06-09 **네이버 여권 인증** 시행 → "외국인은 예약 불가"가 부분 완화. **"예약 가능"만으론 차별화 불가, "큐레이션·신뢰·코스"가 해자.** [07]
5. **경쟁 빈틈 = 통합 흐름.** Seoul Sister는 추천만, Creatrip은 예약만 한다. **AI 성분·효과 진단 → 로컬 매장 예약 → 동네·테마 코스**를 하나로 잇는 영어권 서비스는 없다. [04]
6. **결제 정답 = Stripe Connect** (게스트 체크아웃 + 매장 자동 정산 + 수수료 분리) + 노쇼 pre-auth hold. day1은 Trazy식 경량 컨시어지(payment link)로 검증. [07]
7. **듀얼 트랙 검토**: GLOU(B2C 유저 획득) + B2B(ReactionLens/SkinMatch = 보유 Kbeauty RAG 직결, 피칭 데모 즉시 + 수익·해자). [10]

---

## 1. 프로그램 맥락 & 평가 → [01_program_competition.md](01_program_competition.md)
- 2026년 **1기(첫 회차)**. 총 5,000명(테크 4,000 + 로컬 1,000), 비수도권 70%↑. 중앙대 18팀.
- 깔때기 N→4,000→500→200→100→**TOP 10**. 우승 상금 5억 + 투자 5억(검토) + CES. (가중치 25/25/50·TOP10은 **OT 공식 슬라이드로 확정** → [program-summary.md](../../../docs/program/program-summary.md))
- **심사 가점**: 트랙션(달성 성과) 최우선 > 아이디어. 콘텐츠/큐레이션형 흔한 감점 = "BM 약함·예약 전환 트랙션 부재·확장성 의문".
- **K-스타트업 2025 최상위는 딥테크(의료초음파)** — 콘텐츠형은 최상위 수상 드묾 → GLOU는 **검증된 시장+트랙션+팀 화력+대국민 호소**로 승부.

## 2. 시장 규모 & 수요 근거 → [04](04_competitors_korea.md)·[05](05_target_segment.md)·[06](06_references_papers.md)
| 지표 | 수치 | 출처 |
|---|---|---|
| 방한객 쇼핑 1위 | 향수·화장품 **71.8%** | 외래관광객조사 2025 |
| 외국인 뷰티 지출 | **8,433억(+38%)** | 머니투데이 '케어케이션' |
| 의료관광 시장 | **2.08조(+65%)**, 외국인환자 117만(+2배), 피부과 56.6%(+194.9%) | 보건복지부 2024 |
| 의료관광 재방문율 | **38.6%**, 1인 $2,408, 피부·성형 77.3% | 야놀자리서치 Vol.33 |
| 올리브영 외국인 매출 | **2025 1조 돌파**(2022比 26배), 유럽 +180~250% | CJ올리브영 |
| K-뷰티 수출 2025 | **$114.18억 세계 2위**, 미국 첫 1위 $21.84억(19.1%), 무역흑자 첫 $100억 | 식약처 [08] |
| 글로벌 K-뷰티 시장 | 2025 $147억 → 2034 $305억 (CAGR 8.43%) | Straits Research |

## 3. 타겟 세그먼트 확정 → [05](05_target_segment.md)·[09](09_europe_vs_china.md)
**1차 = 영어권 서구(미국 주도 + 영국 + 영어권 유럽/오세아니아), 20–30대 여성, 6–14일 중장기 여행객.**
**2차 = 서울 거주 유학생(생활 밀착).** 중국은 의도적 후순위.

| 후보 | 매력도 | 근거 |
|---|---|---|
| **영어권 서구 ★★★★★** | 1차 | 미국 K-뷰티 수출 1위 추월(2026Q1 $620M), 체류 12–14일, 1인 고지출(프 $2,988/영 £1,056), 올영 컨설팅 80%·핸즈온 93%가 외국인, **영어 단일 콘텐츠로 미국+영국+호주+영어권 유럽 동시 커버** |
| 중국 ★★★ | 보류(레드오션) | 규모는 최대(460만)지만 샤오홍슈/디엔핑/위챗·따이궁으로 **이미 포화**, 코로나前 60%만 회복, 저가·면세 규제 대상 |
| 유럽 단독 ★★★ | 2차 풀 | 수요 급증(점유율 3%→11%)이나 **볼륨 1/8.6**·다국어 분산 |
| 동남아 ★★★ | 2차 | 고성장(인니 +28%)이나 구매력 후순위 |
| 일본 ★★★ | — | 안정적이나 단기체류·저지출 |

> **멘토 가설 판정**: 방향(중국 회피·서구 공략)은 맞다. 단 **"유럽"을 "영어권 서구(미국 포함)"로 교정**해야 볼륨이 산다.

## 4. 페인포인트 (as-is) → [02](02_painpoints_community.md)·[08](08_recovered_findings.md)
1. **"외국인은 그냥 안 되는 예약·결제"** — ARC/한국번호 없으면 네이버예약·캐치테이블·카카오 인증 실패(차단 원인은 카드가 아니라 통신사 DB 본인인증). *전 영역 공통 1순위.*
2. **신뢰할 추천 부재** — 네이버 리뷰 **"절반 이상이 협찬"**(원문 인용 확보), 비건/할랄/글루텐프리 식이필터 파편화.
3. **바가지·업셀·시술실패 공포** — 피부과 '외국인 프리미엄'·미끼가격 업셀, 서양 모질/곱슬 시술 실패, 다국어 가격표 부재.
4. **K-뷰티 선택 마비** — 올리브영 과다 선택 + 한글 성분표를 Papago/CosDNA로 매번 수동 해독.
5. **정보 휘발** — 진짜 정보는 페북그룹뿐, 검색 최악·같은 질문 무한반복.

## 5. as-is → to-be → [03](03_overseas_services.md)·[07](07_overseas_payment_beauty.md)
| 영역 | As-is (외국인 현실) | To-be (GLOU + 글로벌 표준 차용) |
|---|---|---|
| 예약 | 인스타 DM·번역기, ARC 인증벽 | **No-contact 즉시 확정**(Treatwell) + 여권·이메일만 |
| 결제 | 한국 PG 본인인증 실패 | **Stripe Connect 게스트 체크아웃** + Apple/Google Pay |
| 노쇼/신뢰 | 매장이 외국인 예약 기피 | **pre-auth hold·부분 선결제**(Vagaro/StyleSeat) |
| 매장 선택 | 간판만 보고 도박 | **원장 개인 포트폴리오(전후·영상)+전문태그**(StyleSeat/Booksy, 곱슬 전용 카테고리 확인) |
| 시술 신뢰 | 가격·다운타임 불투명 | **실지불액+다운타임+보정없는 전후+Worth It**(RealSelf) |
| 다이닝 | 협찬 리뷰·필터 없음 | **식이필터(비건/할랄/글루텐프리)+그룹 교집합 필터**(빈틈) |
| 제품 | 한글 성분표 수동 해독 | **AI 성분→효과→피부타입 매칭** + AI 스킨분석 임베드(Perfect Corp/Haut.AI, 자체개발 불필요) |

## 6. 경쟁 지형 & 포지셔닝 → [04](04_competitors_korea.md)·[07](07_overseas_payment_beauty.md)
- **Creatrip (직접 최대)**: MAU 160–170만, 14개 언어, 거래액 51%가 뷰티·의료(+71%), 제휴 2,000, 투자 160억. → 예약·콘텐츠 강하나 **개인화 성분 진단·라이프 코스는 약함**.
- **Seoul Sister**: AI 성분 추천($24.99/월), **예약 기능 없음**.
- **화해 Global**(성분추천, 앱 한국어 전용) / **강남언니 UNNI**(의료 강세 13언어, 라이프 큐레이션 없음) / **Trazy**(Beauty Concierge=payment link 컨시어지) / **Klook·KKday**(뷰티 카테고리 흡수, 헤드스파 +230%, UNNI 제휴) / **South of Seoul**(외국인 Go Local 커뮤니티, 인접) / 글로우픽·언니의파우치·파우더룸(**한국어 전용**).
- **빈틈**: AI 성분·효과 진단 ↔ 로컬 오프라인 예약 ↔ 동네·테마 코스(뷰티+카페+맛집+웰니스)를 **하나의 개인화 흐름**으로 잇는 영어권 플레이어 부재.
- **포지셔닝 한 줄**: *"추천만 하는 Seoul Sister와 예약만 하는 Creatrip 사이에서, AI 성분·효과 진단을 서울 로컬 예약 + 동네·테마 코스로 잇는 '추천→예약→경험' 단일 흐름의 영어권 K-뷰티 라이프 큐레이션."*

## 7. 결제·예약 아키텍처 권고 → [07](07_overseas_payment_beauty.md)
1. **Stripe Checkout/Payment Links + Connect(destination charge)** — application_fee 수수료 분리, 매장 payout, 게스트 체크아웃, Apple/Google Pay. (한국 본인인증·폰번호 우회)
2. **노쇼 방지** = pre-auth hold(7–30일) 또는 부분 선결제(고가 시술 전액/부분).
3. **신뢰 장치** = 명확한 환불정책 + 정산주기 공개 + 다국어 영수증(Trazy 모델).
4. **인바운드 폭** = 1차 글로벌카드, 2차 Alipay+/WeChat Pay(중화권), 통합 PG로 KOMOJU 고려.
5. **하이브리드** = day1 Trazy식 경량 컨시어지 → 수요 검증 후 Stripe Connect 자동 정산.
> ⚠️ **리스크**: 2026-06-09 네이버 여권 인증 시행으로 대형 플랫폼이 예약 진입로를 여는 중. GLOU는 "예약 가능"이 아니라 **큐레이션·신뢰·코스**가 본질이어야 함. 일본 HotPepper Beauty(일본어 전용)·태국 GoWabi가 다국어 빈틈/직접 벤치마크.

## 8. 발산 아이디어 & 듀얼 트랙 → [10_divergent_ideas.md](10_divergent_ideas.md)

> 📣 **팀 공유용 단일 카탈로그(서비스 76개 + 수익구조 + 점수·추천)** = [docs/business/서비스_아이디어_카탈로그.md](../../../docs/business/서비스_아이디어_카탈로그.md). 아이디어 원본 8종(A~H) = [data/research/ideas/](../ideas/).
**Best 5** (팀 자산: 글로벌 콘텐츠 인플루언서 + 데이터/개발 + 뷰티 인플루언서 + Kbeauty RAG):
1. **ReactionLens** — 외국인 반응 인사이트 SaaS. 보유 리뷰 RAG 직결, **피칭 데모 즉시**. (A: AI&빅데이터)
2. **UGC Bridge** — K-브랜드 ↔ 글로벌 마이크로 인플루언서. 팀이 곧 공급, 콜드스타트 없음. (C)
3. **SkinMatch API** — 성분·효과 매칭 B2B. 화학/약학+GraphRAG 정체성 일치, GLOU와 엔진 공유. (A/B)
4. **SeoulPlate** — 식이필터 다이닝. GLOU 최근접 비뷰티 확장. (F: Food-Tech)
5. **Landing.kr** — 외국인 정착 온보딩 OS(휴대폰·집·행정·배달). (C/DT)
> 권고: **GLOU(B2C로 유저·데이터 확보) + B2B(ReactionLens/SkinMatch로 수익·해자) 듀얼 트랙** — 셋이 같은 엔진을 공유.

**6축 점수화 결과** → [12_idea_scoring.md](12_idea_scoring.md): ReactionLens(43) · SkinMatch(40.5) · UGC Bridge(38.5) · GLOU(38). B2B 데이터 라인이 위 — *팀자산 직결 + 데모 즉시 + 규제리스크 낮음*. (정성 추정이므로 상위 3개는 실수요 인터뷰로 Gate 확정 필요.)

**해외 K-뷰티 아이템 조사**(product-research 방법론 적용) → [11_overseas_item_research.md](11_overseas_item_research.md): Top3 = 리들샷·마이크로니들(효자) · 딥톤/셰이드갭 색조(브랜드) · PDRN(미끼→효자). ⚠️ **규제가 단일 최대 함정** — 美 선크림=OTC 의약품(K-선크림 D2C 불가), de minimis $800 면세폐지(2025-08-29)+15% 관세, MoCRA/EU CPNP. → **day1 BM은 소싱이 아니라 규제 부담 없는 "큐레이션·송객".**

**아이디어 발굴 리소스(재실행용)**: YC RFS · IdeaBrowser · Exploding Topics · Starter Story · Failory · Indie Hackers · Product Hunt · BetaList · CB Insights · Trends.vc / 한국: 디스콰이엇·혁신의숲·EO·폴인·아웃스탠딩·벤처스퀘어·플래텀. 방법론: JTBD·언번들링·Idea Maze·Painstorming·"X for Y". (⚠️ GummySearch는 2025.11 종료)

## 9. 킬러 레퍼런스 (발표 인용) → [06](06_references_papers.md)·[08](08_recovered_findings.md)
1. **외래관광객조사 2025** — 방한 쇼핑 1위 = 향수·화장품 **71.8%** (시장 헤드라인)
2. **야놀자리서치 Vol.33** — 의료관광 77.3% 피부·성형, **재방문율 38.6%, 1인 $2,408** (LTV·리텐션)
3. **Yang·Jin·Jung (2017), KJCAP 18(2)** + Wang&Lee(2021) — **일반인 인플루언서 > 셀럽**(4.06 vs 3.77) (GLOU의 로컬 큐레이터 모델 정당화)
4. **식약처 2025** — 미국이 K-뷰티 수출 1위 추월 (타겟 근거)

## 10. 9월 지역오디션(10분) 발표 전략 → [01](01_program_competition.md)
1. **트랙션을 두괄식 숫자로** — 팔로워 아닌 신청폼/예약 성사/제휴 매장/첫 수수료 매출.
2. **Creatrip 정면 차별화 비교표** — "추천+예약+코스 풀퍼널 + 인플루언서 3인 CAC 무기".
3. **수익모델 = 단가 × 전환 × 월예약 = GMV** 구체화.
4. **대국민 호소(투표 25%)** — 외국인 1인칭 페인 영상 + 30초 라이브 데모(AI 성분 추천/코스).
5. **약점 선제 인정 + MVP 자동화 로드맵** — 네이버 여권인증 리스크 선제 대응 서사 포함.

## 11. 리스크 & 오픈 이슈
- 네이버 여권인증(2026-06)이 진입장벽 완화 → 차별화 압박 ↑.
- 영어권에도 선점자(Creatrip·K-Beauty Concierge·BeautyHopper) 존재 → "무주공산" 아님.
- 볼륨(서구 절대수 적음) ↔ 블루오션 트레이드오프.
- O2O 공급(매장 제휴) 확보 난이도 = 실행의 핵심.
- **Reddit 원문 미확보**(OAuth API 키 필요) → [_blocked_sources.md](_blocked_sources.md).

## 12. 파일 인덱스
| # | 파일 | 내용 |
|---|---|---|
| 01 | [01_program_competition.md](01_program_competition.md) | 프로그램·경쟁구도·심사 |
| 02 | [02_painpoints_community.md](02_painpoints_community.md) | 외국인 페인포인트(커뮤니티) |
| 03 | [03_overseas_services.md](03_overseas_services.md) | 해외 벤치마크·as-is→to-be |
| 04 | [04_competitors_korea.md](04_competitors_korea.md) | 한국 경쟁사 매핑 |
| 05 | [05_target_segment.md](05_target_segment.md) | 타겟 통계 근거 |
| 06 | [06_references_papers.md](06_references_papers.md) | 논문·시장 보고서 |
| 07 | [07_overseas_payment_beauty.md](07_overseas_payment_beauty.md) | 해외 결제·뷰티 심화 |
| 08 | [08_recovered_findings.md](08_recovered_findings.md) | 차단소스 회수 결과 |
| 09 | [09_europe_vs_china.md](09_europe_vs_china.md) | 유럽 vs 중국 팩트체크 |
| 10 | [10_divergent_ideas.md](10_divergent_ideas.md) | 발산 아이디어·발굴법 |
| 11 | [11_overseas_item_research.md](11_overseas_item_research.md) | 해외 K-뷰티 아이템 6축 점수화(product-research 방법론 적용) |
| 12 | [12_idea_scoring.md](12_idea_scoring.md) | 발산 아이디어 6축 점수화 → 듀얼트랙 우선순위 |
| 13 | [13_review_integrity.md](13_review_integrity.md) | 리뷰 신뢰 설계(타베로그·Yelp) → GLOU "외국인 신뢰 리뷰" 시사점 (07/05 멘토링) |
| 14 | [14_ux_competitor_review.md](14_ux_competitor_review.md) | Yelp UX 벤치 + 외국인이 한국 앱 불편한 이유 + O/X 비교표 (프로토타입 리디자인 기준) |
| 15 | [15_business_plan_research.md](15_business_plan_research.md) | ⭐ 사업계획서용 자료조사(시장·정책·경쟁·수익·심사기법·리스크) — 전 항목 출처 링크+코멘트 |
| — | [_blocked_sources.md](_blocked_sources.md) | 차단·미검증 추적표 |
| — | [_data_sources.md](_data_sources.md) | 합법·안정 데이터소스 카탈로그(GLOU용) |
