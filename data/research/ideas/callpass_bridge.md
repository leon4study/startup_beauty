# CallPass ("Call for me") — 본인인증·전화 벽을 넘는 브릿지

> 07/05 신촌 멘토링에서 나온 구체 서비스. 멘토가 말한 **"Must-have item(브릿지)"의 가장 유력한 후보.**
> 원출처: [docs/meetings/2026-07-05_신촌_멘토링.md](../../../docs/meetings/2026-07-05_신촌_멘토링.md) · 정리 2026-07-11

## 한 줄
**한국어 전화·예약·확인이 막히는 외국인을 위해, GLOU가 대신 문의하고 결과를 영어로 정리해주는 사람 기반 컨시어지.**

## 왜 이게 "브릿지"인가 (멘토 논리에 정확히 부합)
- 멘토: *"처음부터 뭘 새로 만드는 건 불가능. A와 B를 연결해서 도움을 주는 것부터."* → CallPass는 새 예약망을 만들지 않고, **외국인 ↔ 기존 한국 매장·기관**을 사람이 잇는다.
- 페인 1순위 직결: 실제 외국인 DM 증거 — *"Before you have an ARC and phone number, you cannot use any online services"*, *"ordering delivery without 신분증 or Korean number"* ([아이디어 DM 캡처] → [02_painpoints_community](../market/02_painpoints_community.md)).
- 기존 자산과 연결: [MindLens 조사설계](../../../docs/business/MindLens_조사설계.md)의 검증 컨셉 #6 **English Booking Concierge**의 구체화 = 지불의향을 바로 물어볼 수 있음. Notion MVP의 **Ask GLOU / K-Life Guide** 화면과도 이어짐.

## 서비스 흐름 (8단계)
1. 외국인이 GLOU에 들어온다
2. **"Call for me"** 버튼을 누른다
3. 요청 종류 선택 — Hospital / Beauty·Hair / Housing (확장: 배달·통신·행정)
4. 장소 링크 또는 사진 업로드
5. 궁금한 질문 선택
6. 결제
7. GLOU가 **한국어로 대신 문의**(전화 또는 DM)
8. **영어 요약 리포트**를 받는다

## 요금제 (초안)
| 플랜 | 가격 | 포함 |
|---|---|---|
| **Basic Check** | 4,900원 | 전화/DM 1회 문의 + 영어 요약 리포트 |
| **Booking Help** | 9,900원 | 문의 + 예약 가능시간 확인 + 예약 메시지 작성 + 준비물 안내 |
| **Priority Help** | 14,900원 | 빠른 처리 + 복잡한 질문 3개+ + 후속 질문 1회 |

## 왜 R1(9월)에 유리한가 — 트랙션 만들기 쉬움
- **앱 없이 시작 가능**: 인스타 DM + 구글폼 + 사람이 직접 전화 = 이번 주에 가동 가능(Trazy식 경량 컨시어지 모델, [07_overseas_payment_beauty](../market/07_overseas_payment_beauty.md) 참고).
- **트랙션이 곧 숫자**: "몇 건 대행했는지 · 첫 결제 얼마" 를 9월 발표에 그대로 올림. 심사 1순위 = 트랙션([program-summary](../../../docs/program/program-summary.md) §6).
- **콜드스타트 없음**: 공급(매장)을 미리 모을 필요 없이, 요청이 올 때마다 그 매장에 전화하면 됨.

## ⚠️ 리스크·열린 질문 (실현 가능성 체크)
- **의료 예약 대행 주의**: 병원·시술 예약을 "대행"하고 매장에서 수수료를 받으면 의료법상 **환자 유인·알선(수수료) 위법** 소지 — 강남언니 형사 선례([04_competitors_korea](../market/04_competitors_korea.md)·[경쟁사_벤치마킹](../../../docs/business/경쟁사_벤치마킹.md)). → 의료는 **이용자에게 받는 대행 수수료(컨시어지 요금)** 로만, 병원 리베이트 X.
- **대리 개인정보**: 예약 시 이용자 이름·연락처를 매장에 전달 → 동의·최소수집 필요.
- **본인인증 자체는 못 대신함**: 통신사 DB 기반 본인인증(휴대폰 명의)은 GLOU가 대체 불가. CallPass는 "인증이 필요 없는 경로(전화·DM)로 우회"하는 것이지, 인증을 발급/대행하는 게 아님. (→ 불가능 영역, [서비스_방향_결정](../../../docs/business/서비스_방향_결정_2026-07.md) 참조)
- **단가 vs 인건비**: 4,900원 문의를 사람이 처리하면 초기엔 적자 가능 → MVP는 수요·지불의향 검증이 목적, 흑자는 나중.

## 확장 경로
Basic Check(문의) → Booking Help(예약) → 반복 요청 데이터 축적 → **자주 나오는 요청을 템플릿·자동화** → K-Life Guide(정착 OS)로 확장. [small_wins](small_wins.md)의 "배달앱 대신 주문" 라인과 합류.
