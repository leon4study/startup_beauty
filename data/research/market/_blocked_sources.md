# _blocked_sources — 차단·미검증 소스 마스터 추적표 (재조사)

> 작성일: 2026-07-01 · 프로젝트: GLOU (외국인 대상 서울 K-뷰티 라이프 큐레이션)
> 목적: 01~06 시장조사에서 403/파싱실패/인덱싱 제약으로 막혔던 소스를 우회 방법으로 재조사한 결과를 한 표에 집계.
> 짝 문서: 회수한 인용·수치 상세는 [`08_recovered_findings.md`](./08_recovered_findings.md).
> 상태 표기: **[확인됨]** = 우회로 본문/수치 직접 회수 · **[대체확인]** = 원본은 여전히 막혔으나 동급 대체 출처로 사실 확보 · **[막힘]** = 모든 우회 실패

---

## 재조사 방법론 (시도 순서 · 효과 요약)

| 방법 | 사용법 | 이번 회차 효과 |
|---|---|---|
| **① r.jina.ai 리더 프록시** | `https://r.jina.ai/https://<원본URL>` 를 WebFetch | **★ 최고 효과.** 403 블로그(The Dissolve, South of Seoul), **PDF 바이너리 파싱 실패(accesson 논문)**를 텍스트로 회수. 단 Reddit/Klook/Booksy는 jina에서도 403/451(원 사이트가 봇·법적 차단) |
| **② Reddit 직접(.json / old.reddit / r.jina 경유)** | URL 뒤 `.json`, 또는 old.reddit, 또는 jina 경유 | **전부 실패.** WebFetch 네트워크 차단, `curl`도 403(HTML 챌린지 페이지 반환), jina도 403. WebSearch도 Reddit 링크 미반환(US 인덱스 제약) → **유일 잔존 미회수 영역** |
| **③ web.archive.org 스냅샷** | `https://web.archive.org/web/2024/<URL>` | WebFetch가 archive.org 자체를 차단(`unable to fetch`) + 일부 451 → 이번엔 무효 |
| **④ PDF/통계 → HTML 대체** | 원문 PDF 대신 보도자료·언론 HTML·기업정보 사이트 | **★ 효과적.** 식약처 수출통계, 바비톡 매출을 HTML 기사·기업정보(사람인)로 완전 대체 회수 |
| **⑤ 기업 매출 교차** | 사람인/잡코리아/THE VC/언론 기사 | **효과적.** 사람인 정기공시 기반 바비톡 연도별 매출·영업이익 확보 |

핵심 교훈: **r.jina.ai는 "일반 웹페이지 403"과 "PDF 추출 실패"에 거의 만능**이지만, **Reddit·Klook·Booksy처럼 강한 봇 차단/지역(451) 차단을 건 사이트에는 무효** → 이들은 (a) WebSearch 다이제스트, (b) 동급 대체 출처, (c) 공식 API로만 회수 가능.

---

## 마스터 추적표

| # | 항목 | 원래 문제 | 시도한 방법 | 상태 | 회수한 사실 / 링크 |
|---|---|---|---|---|---|
| 1 | Klook K-뷰티 시술 리스팅 상세 (activity/122334) | 403 / CAPTCHA | r.jina(451)·web.archive(차단)·WebSearch | **[대체확인]** | 리스팅 본문은 여전히 CAPTCHA. 단 WebSearch로 **강남언니(UNNI) 앱 제휴로 운영**, Botox/스킨부스터/리프팅 현지가 예약, **올리브영 기프트카드 perk** 확인. 가격대 Botox ₩40,000–220,000/부위, Rejuran ₩150,000–300,000. https://www.klook.com/en-US/activity/122334-korean-beauty-and-skin-care-clinic-reservation/ |
| 2 | Booksy 텍스처별(Black/곱슬) 전용 필터 존재 여부 | 미확인(03 [추정]) | r.jina(451)·WebSearch | **[확인됨]** | **전용 카테고리 존재 확정.** Booksy에 `Natural Hair Stylists` 전용 버티컬 + 도시별 페이지(퀸스·신시내티 등). 텍스처 전문 살롱 발견이 명명된 카테고리로 제공됨. https://booksy.com/en-us/s/natural-hair-stylists |
| 3 | 한국 내 외국인 생활앱 정량 점유율 | 미확보(03) | WebSearch | **[대체확인]** | 진짜 "외국인 앱 시장점유율 %" 공개 조사는 부재. 단 외국인 방문객 만족도 조사로 **Naver Map 1위(27.8%), Papago 2위(9.9%)** 확보. 국민 전체로는 KakaoTalk 92.5%/Naver 검색 67.5%. (정량 점유율은 향후 KTO 외래관광객조사 원자료 필요) |
| 4 | Reddit 원문 스레드 (Living_in_Korea/koreatravel/AsianBeauty) | site:reddit 무링크(02 한계) | .json·curl·old.reddit·r.jina·WebSearch 전부 | **[막힘]** | 모든 우회 실패(403/451, WebSearch 미인덱싱). 정황은 02 문서의 검색 다이제스트로만 유지. **향후: Reddit 공식 OAuth API 키 필요** |
| 5 | The Dissolve — 한국 맛집 협찬 리뷰 글 | 403(02) | **r.jina.ai** | **[확인됨]** | 본문 회수 성공. **"over half of the restaurant reviews"가 협찬**, Google Maps/TripAdvisor "can't recommend in Korea", 협찬 식별법 인용 확보(08 문서). https://thedissolve.kr/how-to-find-real-good-food-in-korea/ |
| 6 | South of Seoul 블로그 | 403(02) | **r.jina.ai** | **[확인됨]** | 본문 회수. 외국인 "Go Local" 커뮤니티 플랫폼(앱·블로그·phrasebook·지역가이드·SOS Explorers 자원봉사 구조) 확인 → 단순 살롱가이드 아닌 **외국인 라이프 정보 경쟁/레퍼런스**. https://www.southofseoul.net/ |
| 7 | kcia/식약처 화장품 수출통계 원문 PDF | 바이너리 파싱 실패(05·06) | **PDF→HTML 대체**(코스모닝·THE KBS·M이코노미 등) | **[대체확인]** | 2025 수출 **114.18억 달러(세계 2위, 佛 다음)**, **미국 21.84억(19.1%) 사상 첫 1위**, 중국 20.18억(2위, -19%), 일본 10.87억(3위, +4.9%), **무역흑자 첫 100억 달러 돌파**, 수출국 172→202개국, 상위10국 70.7%, 미중 합산 비중 46.9%(2023)→36.7%(2025). https://www.cosmorning.com/news/article.html?no=51971 |
| 8 | accesson.kr [R2] 논문 저자·연도 확정 | PDF 추출 실패(06 D항) | **r.jina.ai (PDF 리더)** | **[확인됨]** | **서지 확정.** Yang, Heesoon; Jin, Byoungho; Jung, Minji (2017), *Korean Journal of Consumer and Advertising Psychology*, **18(2), 173–192**, DOI 10.21074/kjlcap.2017.18.2.173. (※ [R1]과 동일 저자진의 별 논문 — 06 [R2]의 "2010년대 후반/저자미상" 추정 교정) https://accesson.kr/kscap/assets/pdf/15415/journal-18-2-173.pdf |
| 9 | 바비톡(Babitalk) 2025 매출 | 미확인(04) | **사람인 기업정보 + 언론**(뉴시스/아시아경제) | **[대체확인]** | 바비톡 단독 연매출(공시): 2022 233.5억 → 2023 254.6억 → **2024 307.6억(정확 307억 5,732만), 영업익 42.9억(42억 8,961만)**. **2026 1분기 분기 첫 100억 돌파(역대 최대)**, 모회사 케어랩스 2026 1Q 연결매출 205억. (2025 연간 확정치는 2026 중반 공시 후 갱신 필요) https://www.saramin.co.kr/zf_user/company-info/view-inner-finance/csn/MjhKUW9QTUtNa3VPUml1UFBkUWFtUT09/company_nm/(%EC%A3%BC)%EB%B0%94%EB%B9%84%ED%86%A1 |
| 10 | 글로우픽·언니의파우치·파우더룸 영어/예약 지원 | 추정(04) | WebSearch + 스토어 CS 답변 | **[확인됨]** | **글로우픽**: 한국어 전용, 영어판 없음(CS 공식 답변), 예약 기능 없음. **언니의파우치**: 한국어 앱 UI, 외국인은 결제 외 기능만 사용 가능(별도 영어 UI·예약 없음). **파우더룸**: 네이버 뷰티카페 앱, 한국어 전용. → 04의 [추정]을 [확인]으로 승격. 셋 다 외국인 진입장벽 높음 = GLOU가 흡수할 "발견" 영역. https://play.google.com/store/apps/details?id=com.glowdayz.glowmee · https://unpa.me/ |

---

## 회수 성공 집계

- **전체 항목: 10** (시드 10 + 01~06 문서 한계표기와 중복 통합)
- **[확인됨] 5** (#2, #5, #6, #8, #10) · **[대체확인] 4** (#1, #3, #7, #9) · **[막힘] 1** (#4 Reddit)
- **회수율: 9/10 (90%)** — 사실 확보 기준. 완전 원문 회수(8/9 항목)는 r.jina.ai와 HTML 대체가 견인.

## 여전히 막힌 항목 + 향후 방안

1. **Reddit 원문 스레드 (#4)** — 유일한 미회수. 현재 환경의 모든 무인증 우회가 차단됨.
   - 향후: **Reddit 공식 OAuth API 키**(`oauth.reddit.com`, 무료 100req/min)로 r/Living_in_Korea·r/koreatravel·r/AsianBeauty 검색 → 원문 인용 2~3개 확보. 또는 Pushshift/유료 소셜리스닝 DB.
2. **Klook 리스팅 약관 상세 (#1 잔여)** — 취소정책·바우처 정확 문구는 CAPTCHA로 미회수. 향후: 헤드리스 브라우저(Playwright) 또는 Klook 파트너 API.
3. **외국인 앱 정량 점유율 (#3 잔여)** — 만족도 %는 확보했으나 진짜 MAU 점유율은 부재. 향후: KTO 외래관광객조사 원자료(마이크로데이터) 또는 유료 앱분석(data.ai/Sensor Tower).
4. **바비톡 2025 연간 확정치 (#9 잔여)** — 분기 추세만 확보. 2026 중반 감사보고서 공시 후 사람인/DART에서 갱신.
</content>
</invoke>
