# GLOU 리서치 데이터소스 — 합법·안정 카탈로그 (서구 K-뷰티 시장 센싱용)

> 출처 베이스: `new_items/ideas/playbooks/11_data-sources-catalog.md`(2026-06-07 직접 검증) 를 **GLOU(영어권 서구 타겟)용으로 재구성** + 해외 규제 소스 추가.
> 원칙: 같은 신호를 **공식 API(백본) + 회색 엔드포인트(보강) + 공공통계(불멸 백업)** 3겹으로. robots/ToS 준수, 캐싱·rate-limit. 작성 2026-07-01.

## 1. GLOU 니즈 → 추천 소스

| GLOU가 알아야 할 것 | 추천 소스 | 접근법(합법성) | 비용 |
|---|---|---|---|
| 서구 K-뷰티 **수요·트렌드** | Google Trends(공식 API alpha / pytrends 회색), **YouTube Data API v3** | ✅공식(YouTube 무료 1만u/일) | 무료 |
| 바이럴 **선행 신호** | TikTok Creative Center, Pinterest Trends | ⚠️웹 공개(불안정) | 무료 |
| 해외 **이커머스 수요·경쟁** | **Amazon Best Sellers/Movers&Shakers**(anti-bot→`r.jina.ai` 우회), **Rakuten Ichiba API**(일본 선행, 무료 appId), Etsy API(니치 1만/일) | ⚠️Amazon 크롤 회색 / ✅Rakuten·Etsy 공식 | 무료 |
| **외국인 페인포인트**(커뮤니티) | **Reddit Data API**(r/AsianBeauty·r/SkincareAddiction·r/Living_in_Korea) | ✅공식 **OAuth 필수**(앱 사전승인) | 무료 100QPM |
| K-뷰티 **수출·거시수요** | **관세청 HS코드 수출통계**(3304 화장품), 공공데이터포털, KOSIS | ✅공식 API | 무료 |
| **성분·안전·규제(국내)** | 식약처·국표원 공개데이터 | ✅공식 | 무료 |
| **해외 화장품 규제**(필수) | US FDA **MoCRA**, EU **CPNP**, 美 선크림 OTC 모노그래프 | ✅공식 문서 | 무료 |
| 국내 경쟁·가격(보조) | 네이버 쇼핑 API, 11번가 오픈 API | ✅공식 | 무료 |
| 보유 1차 자산 | **`Kbeauty_Analysis`의 아마존·틱톡 리뷰 + RAG** | 내부 | 보유 |

## 2. ⚠️ 절대 크롤 금지 (robots/ToS — 11번 직접 확인)
- **Reddit** `Disallow:/` → **공식 Data API(OAuth)만**. (우리 02·08 보고서에서 막힌 그 지점 — `r.jina.ai`도 Reddit엔 무효. 유일한 길 = 무료 Reddit 앱 키)
- **쿠팡**(Akamai Access Denied) · **올리브영**(anti-bot) · **무신사**(미등록봇 차단, sitemap만) → 크롤 고위험, 지양.

## 3. GLOU에 "지금 붙이기 좋은" 톱5 (합법·무료·선행가치)
1. **YouTube Data API v3** — K-뷰티 하울/리뷰 영상 수·조회·게시속도 = 검색량에 안 잡힌 서구 초기 수요 선행. (무료 1만u/일)
2. **Reddit Data API(OAuth)** — r/AsianBeauty·r/Living_in_Korea 페인 원문. 발표 인용·ReactionLens 페인 사전. (무료 키 발급만 하면 됨)
3. **관세청 HS코드 3304 수출통계** — 국가별 화장품 수요 거시추세(미국↑·중국↓ 교차검증). 소셜이 다 죽어도 안 죽는 백본.
4. **Amazon Best Sellers(뷰티)** — 서구 실거래 베스트·급상승. `r.jina.ai` 경유 저속 수집 → 11번 아이템조사 정기 갱신.
5. **Rakuten Ichiba API** — 일본(한국 트렌드 선행시장) 뷰티 랭킹을 합법·무료 공식 API로.

> 보유 자산 연결: 위 신호를 `Kbeauty_Analysis`의 리뷰 RAG에 합치면 **"서구 수요(정량) + 실사용 페인(정성)"** 이 한 엔진에 모임 = GLOU 추천 + ReactionLens/SkinMatch 공용 백본. (→ [12_idea_scoring.md](12_idea_scoring.md) 듀얼트랙)
