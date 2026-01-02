# 제품 개발 보고서 (TikTok Shop / US / Beauty & Personal Care)

## 1. 문서 메타 정보
- 문서 목적: TikTok Shop(미국) 화장품 카테고리에서 **숏폼 기반 구매 전환을 높이는 제품(패키지/오퍼/메시지 포함) 시안**을 설계한다.  
  (근거: Insight `1. 잘 팔리는 이유`, `3. 개선 가능한 기회`, `5. 다음 액션 체크리스트`)
- 적용 범위: US / Beauty & Personal Care (601450), 기간 표기 last_7_days(정확한 시작/종료 미제공)  
  (근거: Insight `0. 데이터 요약`)
- 사용 지표(성공 기준 후보): CTR / CVR / CPA  
  (근거: Insight `0. 데이터 요약`)
- 데이터 품질 주의: 수집 시각(2025-01-02)과 related_videos 업로드 시각(2025-07-15~07-18) 충돌 가능 → 의사결정 전 검증 필요  
  (근거: Insight `G. 데이터 품질 체크`)

---

## 2. 문제 정의 (Pain Points)
> 아래 문제는 입력에 존재하는 **CTR/CVR/CPA/ER 관측치**만으로 정의하며, 원인 단정은 하지 않는다.

| 문제 ID | 문제(관측 신호) | 영향(퍼널 단계) | 근거 |
|---|---|---|---|
| P1 | Perfume: impressions 262,000,000 대비 CTR 1.35%, CPA $4.66 → 유입 병목 신호 | 노출→클릭(CTR) | Insight `2-1`, `3-1`의 Perfume 지표 |
| P2 | Serums & Essences: CTR 1.81%, CVR 5.17%, CPA $5.76 → 유입+전환 동시 약신호 | 클릭(CTR)+구매(CVR) | Insight `2-2`, `3-1`의 Serums 지표 |
| P3 | Lipstick & Lip Gloss: CTR 4.08% 강하지만 CVR 6.16%, CPA $2.28 → 전환 보강 필요 가능 | 클릭→구매(CVR) | Insight `2-3`, `3-1`의 Lipstick 지표 |
| P4 | 크리에이터 ‘전환 성과’ 직접 지표(orders/GMV/ROAS/CVR by creator) 미제공 → 전환 상위 크리에이터 확정 불가 | 크리에이터 선정/확장 | Insight `4. 화장품 종류별…` |
| P5 | 분석 기간(last_7_days) 정합성 충돌 가능(수집일 vs 업로드일) → 인사이트 해석 리스크 | 전 단계(해석/의사결정) | Insight `G. 데이터 품질 체크` |

---

## 3. 목표(Goal) 및 성공 지표
- Goal G1: “구매전환형 집행”에 유리한 카테고리/메시지를 활용해 **CVR을 유지 또는 개선**한다.  
  (근거: Shampoo & Conditioner CVR 12.9%/CPA $1.23, Moisturisers & Mists CVR 12.59%/CPA $1.06 관측 — Insight `1-1`, `0. 데이터 요약`)
- Goal G2: 유입 병목 카테고리(Perfume, Serums)에서 **CTR 개선 또는 CPA 하락**을 달성한다.  
  (근거: Perfume CTR 1.35%/CPA $4.66, Serums CTR 1.81%/CPA $5.76 — Insight `2-1`, `2-2`)
- Goal G3: “가성비(affordable)” 메시지의 강한 효율을 제품/오퍼/크리에이티브 설계의 기본값으로 반영한다.  
  (근거: affordable makeup CTR 6.23% / CVR 14.2% / CPA $0.98 — Insight `1-2`, `E. 트렌딩 키워드`)
- Success Metrics(입력 범위 내):
  - 1차: CTR 상대 개선(예: +8~10% 목표), CVR 유지 또는 개선, CPA 유지 또는 하락  
    (근거: Insight `3-2 빠른 실험(A/B 테스트)`에서 성공 기준 예시 제시)

---

## 4. 타깃 사용자 및 사용 맥락
> 사용자 정의는 입력에 직접적인 데모그래픽이 없으므로, **콘텐츠/키워드로 관측된 관심 축**으로만 표현한다.

- T1. 스킨케어 루틴/결과 지향 사용자: `#morningroutine #glassskin #skintok`, 키워드 glass skin(+142.8%), skincare routine(+115.2%)  
  (근거: Insight `1-3`, `C-1`, `E-2`)
- T2. 성분/문제 해결 지향 사용자(트러블): `#niacinamide #acne #affordableskincare` 포함 상위 조회 영상(2,450,000뷰)  
  (근거: Insight `1-4`, `4-2`, `C-1`)
- T3. 가성비/듀프/드러그스토어 메이크업 사용자: 키워드 affordable makeup(CTR 6.23%, CVR 14.2%, CPA $0.98), 태그 `#makeupdupes #drugstoremakeup #grwm`  
  (근거: Insight `1-2`, `1-5`, `E-2`, `C-1`)

---

## 5. 제품 시안(안) 제시 (최소 2안)
> “제품”은 물리적 SKU 확정이 아니라, **TikTok Shop에서 바로 테스트 가능한 ‘제품 패키지/오퍼/메시지/콘텐츠 템플릿’ 설계**로 정의한다. (SKU/가격/리뷰 등은 입력 미제공)

### 시안 A) Glass Skin Routine Kit (Moisturisers & Mists 중심)
- 핵심 컨셉(한 줄): “결과(글라스 스킨)를 먼저 보여주고, 루틴으로 구매를 설득하는 스킨케어 키트”
- 해결하려는 문제(Problem → Solution):
  - P5(데이터 정합성 리스크)는 제품 설계로 직접 해결 불가 → 실행 전 ‘기간 검증’ 체크리스트 포함  
    (근거: Insight `G. 데이터 품질 체크`)
- 주요 기능/특징(오퍼/구성/메시지):
  1) “결과 컷 선공개” 숏폼 템플릿(2초 훅 포함)  
     (근거: glass skin 키워드 상승(+142.8%), 태그 `#glassskin`, Insight `1-3`)
  2) “아침/밤 루틴 단계형” 숏폼 템플릿(루틴 순서형)  
     (근거: skincare routine(+115.2%), 태그 `#morningroutine`, Insight `1-3`)
  3) 전환형 카테고리 우선 집행: Moisturisers & Mists(CVR 12.59%, CPA $1.06)  
     (근거: Insight `1-1`, `0. 데이터 요약`)
- 예상 사용자 플로우(구매 전환 흐름):
  1) 노출: 결과(글라스 스킨) 컷 + “루틴 공개” 훅 → 2) 클릭: 제품/키트 소개 → 3) 구매: “루틴 그대로 따라하면 된다” 메시지로 장벽 감소  
  (근거: 루틴/결과 프레이밍 반복 등장 — Insight `1-3`)
- 차별점(가능한 범위):
  - 동일 카테고리에서 “높은 CVR + 낮은 CPA” 관측 → 전환형 실험 우선순위가 높음  
    (근거: Moisturisers & Mists CVR 12.59%, CPA $1.06 — Insight `1-1`)
- 리스크/제약:
  - 정확한 분석 기간(last_7_days 시작/종료) 미제공 → 성과 비교 시점 정의 필요  
    (근거: Insight `0. 데이터 요약`)
  - SKU/가격/리뷰/반품률 미제공 → 오퍼(번들/프로모션) 확정 불가  
    (근거: Insight `3-3 추가로 필요한 입력`)
- 검증(실험) 제안:
  - “glass skin 결과 컷 선공개” vs “morningroutine 순서형” A/B, 성공 기준: CTR 상대 8%↑ + CVR 유지/개선  
    (근거: Insight `3-2 실험 2)`)

---

### 시안 B) Ingredient + Problem Solver Serum Pack (Serums & Essences 개선형)
- 핵심 컨셉(한 줄): “성분 1개 + 문제 1개(여드름)로 메시지를 단순화해 Serums의 효율 병목을 개선하는 패키지”
- 해결하려는 문제(Problem → Solution):
  - P2(Serums: CTR↓, CVR↓, CPA↑) → ‘성분/문제 해결형’ 메시지로 재정렬 + 결과 컷 강화  
    (근거: Serums CTR 1.81%, CVR 5.17%, CPA $5.76 — Insight `2-2`; 성분/문제 해결 관심 축 — Insight `1-4`, `4-2`)
- 주요 기능/특징(오퍼/구성/메시지):
  1) 메시지 규칙: “문제 1개(여드름) → 성분 1개(niacinamide) → 전/후”  
     (근거: 상위 조회 영상 태그 `#niacinamide #acne` 및 성분/문제 해결형 강신호 — Insight `1-4`, `4-2`)
  2) “가성비(affordable)” 결합 오퍼(번들/프로모션) 아이디어는 가능하나, 실제 가격/혜택 데이터 미제공 → ‘추가 정보 필요’로 표기  
     (근거: 가성비 메시지 효율 강함 — affordable makeup CPA $0.98, Insight `1-2`; 단, 오퍼 데이터 미제공 — Insight `3-3`)
- 예상 사용자 플로우:
  1) 노출: “여드름 고민?” 훅 + 성분(니아신아마이드) 명시 → 2) 클릭: 전/후/사용법 → 3) 구매: “가성비/루틴”로 결정 보조(단, 오퍼 확정은 추가 정보 필요)  
  (근거: Insight `1-4`, `3-2 실험 3)`)
- 차별점:
  - Serums 자체 효율은 약하지만, 관심 축(성분/트러블)은 강하게 관측됨 → “관심은 있는데 전환이 막힌 상태”로 해석 가능(단정 아님)  
    (근거: 2,450,000뷰 성분/트러블 태그 vs Serums 효율 지표 — Insight `3-3 기회 1)`)
- 리스크/제약:
  - 리뷰/불만/반품률 미제공 → “불만 해결”을 데이터로 확정 불가  
    (근거: Insight `3-3`의 누락 필드 명시)
- 검증(실험) 제안:
  - “성분(niacinamide)+문제(acne)” vs “제품 효능 일반” A/B, 성공 기준: CTR 또는 CVR 상대 10%↑  
    (근거: Insight `3-2 실험 3)`)

---

### 시안 C) Affordable Dupe Makeup Set (Makeup: 듀프/드러그스토어/GRWM)
- 핵심 컨셉(한 줄): “가성비(affordable) + 듀프 비교 + GRWM 포맷으로 클릭·구매를 동시에 끌어올리는 메이크업 세트”
- 해결하려는 문제(Problem → Solution):
  - P3(Lipstick CTR 강하지만 CVR 약) 포함 메이크업 전환 보강 → 스와치/조명/피부톤 가이드 컷을 세트 기본 요소로 설계  
    (근거: Lipstick CTR 4.08% vs CVR 6.16% — Insight `2-3`; 전환 보강 제안(컬러 가이드) — Insight `3-2 실험 4)`)
- 주요 기능/특징:
  1) 훅 기본값: “affordable makeup” 문구/자막 고정(첫 2초)  
     (근거: affordable makeup CTR 6.23%, CVR 14.2%, CPA $0.98 — Insight `1-2`)
  2) 포맷: “고가 vs 듀프 비교 → 바르는 장면 → 결과 컷 → 가격/구매 CTA” 템플릿  
     (근거: 태그 `#makeupdupes #drugstoremakeup #grwm` 반복 강신호 — Insight `1-5`)
  3) 전환 보강 컷: “피부톤별 컬러 가이드/스와치/조명 고정” (실험 요소)  
     (근거: Lipstick 전환 보강 실험 제안 — Insight `3-2 실험 4)`)
- 예상 사용자 플로우:
  1) 노출: “이 가격에 이 퀄리티?”(가성비) → 2) 클릭: 비교/스와치 상세 → 3) 구매: 컬러 가이드로 선택 장벽 감소  
  (근거: affordable 메시지 효율 + 전환 병목 가능성 지적 — Insight `1-2`, `2-3`)
- 리스크/제약:
  - 실제 상품 옵션/재고/가격/번들 구성 데이터 미제공 → 세트 SKU 확정 불가(추가 정보 필요)  
    (근거: Insight `3-3 추가로 필요한 입력`)
- 검증(실험) 제안:
  - “affordable makeup 훅” vs “drugstore dupes 훅” A/B, 성공 기준: CTR 상대 10%↑ 또는 CPA 유지/하락  
    (근거: Insight `3-2 실험 1)`)

---

## 6. 문제 → 해결 → 기능 매핑(필수)
| 문제 ID | 관측된 문제 신호 | 해결 전략(제품 설계) | 구현 기능/요소 | 근거 |
|---|---|---|---|---|
| P1 | Perfume CTR 1.35%, CPA $4.66 (유입 병목) | 첫 2초 훅을 “향 설명” 대신 “반응/상황극/리액션 UGC”로 전환(가설, 단정 금지) | 리액션 중심 숏폼 템플릿 / 시향 반응 컷 구성 | Insight `2-1`, `3-1`의 Perfume 실행 항목 |
| P2 | Serums CTR 1.81%, CVR 5.17%, CPA $5.76 (유입+전환 약) | 성분 1개+문제 1개로 메시지 단순화 + 전/후 결과 컷 강화 | “niacinamide + acne” 템플릿 / 전후 컷 / 사용 루틴 3단계 | Insight `1-4`, `3-2 실험 3)`, `3-3 기회 1)` |
| P3 | Lipstick CTR 4.08% 대비 CVR 6.16% (전환 보강 필요 가능) | 선택 장벽(컬러) 완화 요소를 숏폼 내 포함 | 피부톤별 컬러 가이드 컷 / 스와치 조명 고정 | Insight `2-3`, `3-2 실험 4)` |
| P4 | 크리에이터 전환 지표 미제공 | ER/조회 기반 ‘집행 후보’로 시작 후 전환 지표 연결 스키마 보강 | creator_id/video_id ↔ orders/GMV/ROAS 연결 요구사항 | Insight `4`, `5. 다음 액션(4주)` |
| P5 | 수집일 vs 업로드일 충돌 가능 | 집행 전 데이터 정합성 검증을 1순위로 워크플로우에 포함 | last_7_days 정확한 시작/종료, 타임스탬프 원천 로직 점검 체크리스트 | Insight `2-5`, `5. 다음 액션(1주)` |

---

## 7. 검증(실험) 설계 (1~2주)
> 성공 기준은 입력에 존재하는 지표(CTR/CVR/CPA)로만 둔다.

1) 메이크업 훅 실험  
- 비교: “affordable makeup” vs “drugstore dupes”  
- 성공 기준: CTR 상대 10%↑ 또는 CPA 유지/하락  
- 적용 시안: C  
(근거: Insight `3-2 실험 1)`)

2) 스킨케어 포맷 실험  
- 비교: “glass skin 결과 컷 선공개” vs “morningroutine 순서형”  
- 성공 기준: CTR 상대 8%↑ + CVR 유지/개선  
- 적용 시안: A  
(근거: Insight `3-2 실험 2)`)

3) Serums 메시지 실험  
- 비교: “성분+문제 해결형(niacinamide+acne)” vs “제품 효능 일반”  
- 성공 기준: CTR 또는 CVR 상대 10%↑  
- 적용 시안: B  
(근거: Insight `3-2 실험 3)`)

4) Lip 전환 보강 실험  
- 비교: “컬러 가이드(피부톤별) 포함” vs “미포함”  
- 성공 기준: CVR 상대 10%↑  
- 적용 시안: C(특히 Lip 하위 템플릿)  
(근거: Insight `3-2 실험 4)`)

---

## 8. 제품 예시 이미지 생성 프롬프트(텍스트) (시안별 1~3개)
> 실제 이미지는 첨부하지 않으며, 아래 텍스트를 이미지 생성 도구에 그대로 입력하는 것을 전제로 한다.

### 8-A) 시안 A (Glass Skin Routine Kit)
1) 제품 목업(키트) 프롬프트  
- Prompt: “minimal skincare kit product mockup for TikTok Shop, dewy ‘glass skin’ concept, 3-piece set arranged on a clean bathroom countertop, soft morning light, high-key photography, subtle water droplets, no visible brand logo, realistic materials, shallow depth of field, 4k, vertical composition”  
- Negative Prompt: “blurry, low resolution, heavy text, watermark, brand logo, cluttered background, extra hands, distorted bottles”

2) 사용 장면(루틴) 프롬프트  
- Prompt: “young adult applying moisturizer and facial mist in a morning skincare routine, close-up on glowing skin texture, warm natural light, minimal aesthetic, TikTok-style vertical frame, realistic skin, gentle smile, no makeup heavy look, 4k”  
- Negative Prompt: “over-retouched skin, uncanny face, harsh shadows, excessive props, text overlays, watermark”

---

### 8-B) 시안 B (Ingredient + Problem Solver Serum Pack)
1) 전/후 결과 컷 프롬프트  
- Prompt: “split-screen before-and-after skincare result concept, acne-prone skin improving to clearer skin, ingredient-focused serum theme, clean clinical lighting, neutral background, realistic skin pores, vertical TikTok composition, no text, 4k”  
- Negative Prompt: “medical claims text, exaggerated unrealistic transformation, plastic skin, watermark, brand logos”

2) 성분 강조(니아신아마이드) 프롬프트  
- Prompt: “macro shot of transparent serum dropper with a single highlighted ingredient concept (niacinamide), clean lab aesthetic, glass reflections, soft diffused light, minimal background, realistic liquid viscosity, 4k, vertical”  
- Negative Prompt: “chemical hazard symbols, brand labels, busy background, text, watermark”

---

### 8-C) 시안 C (Affordable Dupe Makeup Set)
1) 듀프 비교 목업 프롬프트  
- Prompt: “makeup dupe comparison flat lay, two similar lip gloss shades side-by-side with price-tag style stickers (no readable text), drugstore affordable vibe, clean pastel background, soft studio lighting, vertical TikTok composition, 4k”  
- Negative Prompt: “readable brand names, heavy text, watermark, messy layout, low-res, distorted product shapes”

2) 스와치/피부톤 가이드 컷 프롬프트  
- Prompt: “lip gloss swatches on multiple skin tones, consistent lighting, close-up arms with swatches, clean background, realistic texture and shine, educational yet aesthetic, vertical frame, 4k, no text”  
- Negative Prompt: “uneven lighting, over-saturation, unrealistic colors, watermark, text overlays, extra fingers”

---

## 9. 리스크/의존성 및 추가 입력 요구
- 데이터 정합성(최우선): 수집일(2025-01-02) vs 업로드일(2025-07-15~07-18) 충돌 가능 → ‘동일 last_7_days’인지 검증 필요  
  (근거: Insight `G. 데이터 품질 체크`, `5. 다음 액션(1주)`)
- 전환 지표 부재: 크리에이터별 orders/GMV/ROAS/CVR 미제공 → “전환 성과 상위 크리에이터” 확정 불가  
  (근거: Insight `4`, `5. 다음 액션(4주)`)
- 리뷰/불만/반품률 부재: 판매는 높지만 불만 존재 여부 확정 불가 → Negative Driver는 “데이터 상 확인 불가”로 유지  
  (근거: Insight `3-3`)
- 추가로 필요(입력 요청):
  - orders/GMV/ROAS/CVR(크리에이터·영상·상품 단위), return_rate, 불만 키워드 Top N, 평점 추이  
    (근거: Insight `3-3 추가로 필요한 입력`, `5. 다음 액션(4주)`)

---
