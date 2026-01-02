# 제품 개발 보고서 (TikTok Shop / US / Beauty & Personal Care)

## 1. 문서 메타 정보
- 문서 목적: TikTok Shop(미국) 화장품 카테고리에서 **숏폼 기반 구매 전환(CTR/CVR) 개선 및 CPA 안정화**를 위한 제품(또는 제품 세트) 시안을 정의한다.  
  (근거: Insight `0. 데이터 요약`에서 사용 가능 지표가 CTR/CVR/CPA로 명시, Insight `3. 개선 가능한 기회`)
- 데이터 범위(입력 기준): US / Beauty & Personal Care (601450), 기간 표기 last_7_days(정확한 시작/종료 미제공), 수집 시각 2025-01-02T06:00:00Z  
  (근거: Insight `0. 데이터 요약`)
- 데이터 품질 주의(최우선): 수집일(2025-01-02)과 related_videos 업로드 시각(2025-07-15~07-18) 충돌 가능 → 의사결정 전 검증 필요  
  (근거: Insight `G. 데이터 품질 체크`)

---

## 2. 핵심 근거 요약 (입력에서 관측된 사실만)
- 전환 효율 강신호(높은 CVR + 낮은 CPA):  
  - Shampoo & Conditioner: CVR 12.9%, CPA $1.23  
  - Moisturisers & Mists: CVR 12.59%, CPA $1.06  
  (근거: Insight `0. 데이터 요약`, `1-1`)
- 클릭 효율 강신호(높은 CTR):  
  - affordable makeup: CTR 6.23% (추가로 CVR 14.2%, CPA $0.98도 입력에 존재)  
  - Lipstick & Lip Gloss: CTR 4.08%  
  (근거: Insight `0. 데이터 요약`, `1-2`, `2-3`)
- 효율 약신호(비용↑/전환↓ 가능성, 단정 금지):  
  - Serums & Essences: CTR 1.81%, CVR 5.17%, CPA $5.76  
  - Perfume: impressions 262,000,000, CTR 1.35%, CPA $4.66  
  (근거: Insight `2-1`, `2-2`, `3-1`)
- 반복적으로 등장하는 콘텐츠/관심 프레임:  
  - 스킨케어: glass skin(+142.8%), skincare routine(+115.2%), 태그 #morningroutine #glassskin #skintok  
  - 성분/문제 해결: 태그 #niacinamide #acne, 상위 조회 2,450,000뷰  
  - 메이크업: 태그 #makeupdupes #drugstoremakeup #grwm, affordable 메시지 효율 강  
  (근거: Insight `1-3`, `1-4`, `1-5`, `4-1~4-3`)

---

## 3. 문제 정의 (Pain Points) 및 해결 목표
| 문제 ID | 문제(관측 신호) | 해결 목표(지표) | 근거 |
|---|---|---|---|
| P1 | Perfume: CTR 1.35%, CPA $4.66 → 유입(CTR) 병목 신호 | CTR 개선 또는 CPA 하락 | Insight `2-1`, `3-1` |
| P2 | Serums & Essences: CTR 1.81%, CVR 5.17%, CPA $5.76 → 유입+전환 동시 약 | CTR/CVR 개선 또는 CPA 하락 | Insight `2-2`, `3-1`, `3-2(실험3)` |
| P3 | Lipstick & Lip Gloss: CTR 4.08% 강하지만 CVR 6.16% → 전환 보강 필요 가능(원인 단정 불가) | CVR 개선 | Insight `2-3`, `3-2(실험4)` |
| P4 | 크리에이터 전환 지표(orders/GMV/ROAS 등) 미제공 → “전환 상위” 확정 불가 | 전환 지표 연결 가능한 데이터 요건 정의 | Insight `4`, `5(4주)` |
| P5 | 데이터 시점 충돌 가능 → 인사이트 해석 리스크 | 분석 기간/타임스탬프 정합성 확정 | Insight `G`, `5(1주)` |

---

## 4. Feedback 반영 항목 (입력된 FeedBack 기준)
> 아래 항목은 FeedBack의 지적사항을 **요구사항으로 전환**해 본 보고서에 반영한다.

| FeedBack 요구 | 반영 방식(이 문서 내 위치) | 근거 |
|---|---|---|
| “제품 형태(SKU/제형·텍스처/패키징/용량…) 최소 2개 이상 구체 스펙 필요” | 각 시안에 **‘제품 스펙(확정/변수/TBD)’ 표**를 추가하고, 최소 2개 이상의 스펙 필드를 명시(단, 입력 근거 없는 값은 ‘TBD/추가 정보 필요’로 표기) | FeedBack reason `기준1(구체성)` |
| “A/B(CTR·CVR·CPA) 외 누수·안정성·자극 등 검증 항목화 필요” | 섹션 6에 **‘퍼널 지표 + 제품 품질/안전 QA 체크리스트’** 추가 | FeedBack reason `기준1(구체성)` |
| “성과 병목(CTR/CVR/CPA) → 해결 인과/메커니즘 문장 부족” | 섹션 5의 문제-해결 매핑에 **‘왜 이 요소가 해당 병목을 완화하는지’**를 근거와 함께 1:1로 기재 | FeedBack reason `기준2(논리)` |
| “CTA가 추상적, 즉시 행동 지시 필요 + 강한 멈춤 포인트(감각 연출) 추가” | 각 시안에 **CTA 문구(명령형)**와 **Stop Point(시각/감각 연출 명사)**를 템플릿으로 포함(근거가 있는 프레임: 루틴/전후/스와치 등과 연결) | FeedBack reason `기준3(틱톡커블)` |

---

## 5. 제품 시안 및 특징 (2~3안)
> 주의: 가격/용량/리뷰/반품률/구체 SKU 데이터는 입력에 없으므로, 수치/확정 스펙은 “입력 근거 부족(추가 정보 필요)”로 표기한다.

### 시안 A) “Glass Skin Routine Duo” (Moisturisers & Mists 전환형)
- 핵심 컨셉: “결과(글라스 스킨) → 루틴(아침/밤)으로 구매 전환을 유도하는 2종 세트”  
  (근거: glass skin(+142.8%), skincare routine(+115.2%), #morningroutine #glassskin 태그 반복 — Insight `1-3`)
- 목표 병목/지표: 전환 효율 강 카테고리에서 **CVR 유지/개선, CPA 유지/하락**  
  (근거: Moisturisers & Mists CVR 12.59%, CPA $1.06 — Insight `1-1`, `0. 데이터 요약`)

**A-1) 제품 스펙(확정/변수/TBD)**
| 항목 | 값 | 상태 | 근거 |
|---|---|---|---|
| SKU 타입 | Moisturiser + Mist (2종) | 카테고리 기반 정의 | “Moisturisers & Mists” 카테고리 명시 — Insight `0`, `1-1` |
| 제형/텍스처 | 입력 근거 부족(추가 정보 필요): 크림/젤/로션(모이스처라이저), 워터/미스트(분사형) 중 확정 필요 | TBD(실험 변수) | 입력에 제형 정보 없음 — Insight 전반 |
| 패키징 | 입력 근거 부족(추가 정보 필요): 펌프/튜브(모이스처라이저), 스프레이/미스트 헤드(미스트) 확정 필요 | TBD(실험 변수) | 입력에 패키징 정보 없음 — Insight 전반 |
| 용량 옵션 | 입력 근거 부족(추가 정보 필요): 표준/미니 번들 여부 확정 필요 | TBD | 입력에 용량/오퍼 데이터 없음 — Insight `3-3` |

**A-2) 주요 기능/특징(콘텐츠/오퍼 설계)**
- “루틴/결과” 숏폼 템플릿 2종(실험 단위로 정의):
  1) 결과(Glass skin) 선공개형  
  2) Morning routine 순서형  
  (근거: Insight `3-2 실험 2)`에서 포맷 A/B 제안)
- 메커니즘(왜 이게 병목을 개선하나):
  - 루틴/결과 프레임이 반복 상승 키워드로 관측됨 → 동일 프레임을 크리에이티브 표준으로 두면 **초반 주목(CTR) 및 메시지 이해를 개선할 가능성**이 있음(단정 금지)  
    (근거: glass skin, skincare routine 상승 — Insight `1-3`)

**A-3) 예상 사용자 플로우**
- 노출(숏폼): 결과 컷 → 루틴 3스텝 → “2종 세트로 끝”  
- 클릭(TikTok Shop): 2종 구성 확인  
- 구매: “루틴 그대로 따라하기” 메시지로 선택 부담 감소  
(근거: 루틴 프레이밍 반복 — Insight `1-3`)

**A-4) TikTok 커뮤니케이션 템플릿(훅/Stop Point/CTA)**
- Hook(0~2초): “글라스 스킨 결과 먼저 보여줄게요”  
  (근거: glass skin 프레임 — Insight `1-3`)
- Stop Point(멈춤 포인트, 감각/시각 연출):  
  - “광택(윤광) 클로즈업” / “미스트 분사 순간(입자/반사)” / “바른 직후 질감 변화(전/후 컷)”  
  (근거: 전/후 결과 + 루틴 구조 권장 — Insight `1-3`)
- CTA(명령형): “지금 TikTok Shop에서 **장바구니 담고** 루틴 그대로 따라해보세요.”  
  (근거: 구매 전환 목적(캠페인) 언급 — Insight `1-1`; FeedBack의 ‘구체 행동 지시’ 요구)

**A-5) 이미지 생성 프롬프트(1~2개)**
1) 제품 목업  
- Prompt: “TikTok Shop beauty product duo mockup, moisturizer + facial mist set, clean minimal bathroom countertop, soft morning light, dewy glass-skin vibe, realistic packaging without brand logos, vertical 9:16, 4k, high detail”  
- Negative: “watermark, readable text, brand logo, clutter, blurry, low-res”
2) 사용 장면  
- Prompt: “close-up skincare routine, applying moisturizer then mist, visible dewy glow, natural skin texture, soft diffused light, vertical 9:16, realistic, no text”  
- Negative: “over-retouched skin, uncanny face, watermark, heavy text overlays”

---

### 시안 B) “Ingredient x Problem Serum Pack” (Serums & Essences 효율 개선형)
- 핵심 컨셉: “성분 1개(niacinamide) + 문제 1개(acne)로 메시지를 단순화해 Serums 병목(CTR/CVR↓, CPA↑)을 개선”  
  (근거: #niacinamide #acne 상위 조회 2,450,000뷰 + Serums 지표 약신호 — Insight `1-4`, `2-2`, `3-3 기회1`)
- 목표 병목/지표: Serums의 **CTR 또는 CVR 개선, CPA 하락**  
  (근거: Insight `3-2 실험 3)` 성공 기준이 CTR/CVR 개선)

**B-1) 제품 스펙(확정/변수/TBD)**
| 항목 | 값 | 상태 | 근거 |
|---|---|---|---|
| SKU 타입 | Serum/Essence 1종(또는 2종 변형) | 카테고리 기반 정의 | “Serums & Essences” 카테고리 명시 — Insight `0`, `2-2` |
| 핵심 메시지 성분 | niacinamide(메시지 키워드로 사용) | 입력에 등장 | 태그 #niacinamide — Insight `1-4`, `4-2` |
| 타깃 문제 프레임 | acne(메시지 프레임으로 사용) | 입력에 등장 | 태그 #acne — Insight `1-4`, `4-2` |
| 제형/흡수감/자극 여부 | 입력 근거 부족(추가 정보 필요) | TBD | 입력에 제품 상세 스펙/리뷰 데이터 없음 — Insight `3-3` |
| 패키징/누수 방지 | 입력 근거 부족(추가 정보 필요) | TBD | 입력에 패키징 정보 없음 |

**B-2) 주요 기능/특징(콘텐츠/오퍼 설계)**
- 템플릿: “문제 1개 → 성분 1개 → 전/후(또는 과정) → 구매”  
  (근거: Insight `1-4`의 메시지 단순화 제안, `3-2 실험 3)`)
- 메커니즘(왜 이게 병목을 개선하나):
  - 성분/문제 해결형 콘텐츠가 조회·참여 신호로 관측됨 → 동일 프레임을 Serums 메시지로 가져오면 **유입(CTR) 개선 가능성**이 있음(단정 금지)  
    (근거: 2,450,000뷰 + ER 6.37% 표본 — Insight `1-4`, `4-2`)
  - Serums는 현재 CTR/CVR이 낮고 CPA가 높게 관측됨 → 메시지 재배치가 “유입+전환” 병목을 동시에 점검하는 실험으로 적합  
    (근거: Serums CTR 1.81%, CVR 5.17%, CPA $5.76 — Insight `2-2`)

**B-3) 예상 사용자 플로우**
- 노출: “트러블 고민?” 훅 → 성분(niacinamide) 명시 → 전/후(또는 과정)  
- 클릭: 제품 페이지에서 사용법/핵심 포인트 확인(단, 상세 데이터는 추가 필요)  
- 구매: “한 가지 문제에 집중” 메시지로 선택 부담 감소  
(근거: “성분 1개 + 문제 1개” 단순화 제안 — Insight `1-4`)

**B-4) TikTok 템플릿(훅/Stop Point/CTA)**
- Hook: “여드름(트러블) 때문에 루틴이 복잡해졌다면, **성분 1개로만** 시작”  
  (근거: 성분/문제 해결 프레임 — Insight `1-4`)
- Stop Point: “세럼 한 방울 점도(클로즈업)”, “흡수 전/후 표면 변화(전/후 컷)”  
  (근거: 전/후 결과 프레이밍 권장 — Insight `1-3`의 ‘결과’ 구조를 Serums로 확장(전/후 자체는 일반화가 아니라 ‘결과 컷’ 포맷 차용임))
- CTA: “지금 TikTok Shop에서 **바로 확인하고 장바구니 담기**”  
  (근거: FeedBack의 구체 CTA 요구)

**B-5) 이미지 생성 프롬프트(1~2개)**
1) 성분/문제 해결 컨셉 목업  
- Prompt: “clinical skincare serum product mockup, ingredient-focused concept (niacinamide), clean lab aesthetic, glass dropper, macro liquid texture, neutral background, vertical 9:16, 4k, no brand logos, no text”  
- Negative: “watermark, readable text, brand logo, messy background”
2) 전/후 컨셉(텍스트 없는 구도)  
- Prompt: “split-frame skincare before-after concept, acne-problem framing without text, realistic skin texture, soft clinical lighting, vertical 9:16, 4k”  
- Negative: “unrealistic transformation, heavy retouching, watermark, text overlays”

---

### 시안 C) “Affordable Dupe Makeup (Lip Focus) Set” (클릭 강 → 전환 보강)
- 핵심 컨셉: “가성비(affordable) + 듀프 비교 + GRWM 포맷에 ‘컬러 가이드/스와치’ 컷을 포함해 CVR 병목을 보강”  
  (근거: affordable makeup CTR 6.23% & CVR 14.2% & CPA $0.98, Lipstick CTR 4.08% vs CVR 6.16%, #makeupdupes #drugstoremakeup #grwm — Insight `1-2`, `1-5`, `2-3`, `3-2 실험4)`)

**C-1) 제품 스펙(확정/변수/TBD)**
| 항목 | 값 | 상태 | 근거 |
|---|---|---|---|
| SKU 타입 | Lipstick/Lip Gloss 중심 1~N종 세트 | 카테고리 기반 정의(수량은 TBD) | “Lipstick & Lip Gloss” 카테고리 명시 — Insight `0`, `2-3` |
| 핵심 메시지 | affordable makeup(훅 키워드) | 입력에 존재 | Insight `1-2`, `E. 트렌딩 키워드` |
| 옵션/컬러 가이드 | 피부톤별 스와치/조명 고정 컷 포함(콘텐츠 요소) | 실험 요소로 정의 | Insight `3-2 실험4)` |
| 제형/발색/지속력 | 입력 근거 부족(추가 정보 필요) | TBD | 입력에 제품 리뷰/스펙 없음 — Insight `3-3` |
| 번들 구성(2+1 등) | 입력 근거 부족(추가 정보 필요) | TBD | “번들(2+1) 실험”은 제안으로만 존재, 실제 오퍼 데이터 미제공 — Insight `3-1` |

**C-2) 주요 기능/특징(콘텐츠/오퍼 설계)**
- 포맷(템플릿): “고가 vs 듀프 비교 → 바르는 장면 → 결과 컷 → 컬러 가이드 → CTA”  
  (근거: Insight `1-5`의 템플릿 제안)
- 메커니즘(왜 CVR 보강에 도움이 되나):
  - Lipstick은 CTR은 강하지만 CVR이 상대적으로 낮게 관측됨 → “컬러 선택/발색 신뢰” 같은 구매 설득 요소가 병목일 수 있다고 입력에서 ‘가능성’으로 언급됨(단정 불가) → 따라서 스와치/조명/피부톤 가이드를 실험 변수로 넣는 것이 합리적  
    (근거: Insight `2-3`의 “가능” 언급 + `3-2 실험4)`)

**C-3) 예상 사용자 플로우**
- 노출: “이 가격에 이 컬러?”(affordable) 훅 → 비교/스와치  
- 클릭: 컬러 옵션 확인  
- 구매: 가이드로 선택 장벽 완화  
(근거: affordable 메시지 효율 강 + Lip 전환 병목 가능성 — Insight `1-2`, `2-3`)

**C-4) TikTok 템플릿(훅/Stop Point/CTA)**
- Hook: “affordable makeup로 **바로 듀프 비교**해볼게요”  
  (근거: affordable makeup 강신호 — Insight `1-2`)
- Stop Point: “스와치 한 번에 3톤 비교(조명 고정)”, “글로스 질감 늘어남/광택 클로즈업”  
  (근거: 스와치/가이드 실험 — Insight `3-2 실험4)`)
- CTA: “지금 TikTok Shop에서 **원하는 톤 바로 고르고 구매하기**”  
  (근거: FeedBack의 구체 행동 지시 요구)

**C-5) 이미지 생성 프롬프트(1~2개)**
1) 듀프 비교 플랫레이  
- Prompt: “affordable makeup dupe comparison flat lay, lip gloss shades side-by-side, clean pastel background, studio lighting, texture shine visible, vertical 9:16, 4k, no brand logos, no readable text”  
- Negative: “watermark, readable labels, clutter, blur”
2) 피부톤별 스와치 가이드  
- Prompt: “lip gloss swatches on multiple skin tones, consistent neutral lighting, close-up arms, realistic texture and shine, educational composition, vertical 9:16, 4k, no text”  
- Negative: “uneven lighting, over-saturation, watermark, text overlays”

---

## 6. 검증 계획 (퍼널 지표 + 제품 품질/안전 QA)
> 주의: 아래 QA 항목은 “문제 발생 사실”이 아니라 **검증 체크리스트**이며, 입력에 없는 수치/결과는 기입하지 않는다.  
(근거: FeedBack reason `누수·안정성·자극 등 검증 항목화`)

### 6-1) 퍼널 지표 검증 (입력 지표 기반)
- 공통 성공 기준(실험별):
  - CTR 상대 개선(예: +8~10% 목표), CVR 유지/개선, CPA 유지/하락 중 최소 1개 충족  
  (근거: Insight `3-2 빠른 실험`의 성공 기준 예시)
- 실험 매핑:
  - 시안 A: 결과 선공개 vs 루틴 순서형 (CTR/CVR)  
    (근거: Insight `3-2 실험2)`)
  - 시안 B: 성분+문제 해결형 vs 일반 효능 (CTR 또는 CVR)  
    (근거: Insight `3-2 실험3)`)
  - 시안 C: 컬러 가이드 포함 vs 미포함 (CVR)  
    (근거: Insight `3-2 실험4)`)

### 6-2) 제품 품질/안전 QA 체크리스트(실행 전/후 점검 항목)
- 누수/패키징(특히 미스트/향수/드로퍼 가능 제품):
  - 운송/흔들림/낙하 시 누수 여부 점검(항목만 정의, 결과는 TBD)  
  - 캡/헤드 밀폐성 점검(항목만 정의)  
  (근거: FeedBack의 ‘누수’ 요구)
- 안정성/분리(특히 모이스처라이저/세럼 가능 제품):
  - 보관 조건 변화(상온/고온/저온)에서 분리/침전/점도 변화 관찰(항목만 정의)  
  (근거: FeedBack의 ‘안정성’ 요구)
- 자극/민감 반응(특히 성분/트러블 프레임 사용 시):
  - 민감 피부 사용 시 주의 문구/가이드 필요 여부(입력 근거 부족 → 내부 제품 데이터 필요)  
  - 패치 테스트 안내 문구 적용 여부(항목만 정의)  
  (근거: FeedBack의 ‘자극’ 요구, 단 입력에 실제 자극 데이터 없음 → TBD)
- 사용성(옵션 선택/컬러 선택):
  - 컬러 가이드의 이해도(사용자 테스트/댓글 반응 등으로 확인)  
  (근거: Insight `3-2 실험4)`가 ‘컬러 가이드’ 자체를 변수로 제안)

---

## 7. 리스크/의존성 및 추가 정보 필요
- 데이터 정합성(최우선): last_7_days의 정확한 시작/종료 시각 미제공 + 업로드일/수집일 충돌 가능 → 실험 결과 해석 전 기간 확정 필요  
  (근거: Insight `0`, `G`, `5(1주)`)
- 전환 지표 부재: 크리에이터별 orders/GMV/ROAS/CVR 미제공 → “전환 상위 크리에이터” 확정 불가(현재는 ER/조회 기반 후보만 가능)  
  (근거: Insight `4`, `5(4주)`)
- 제품 상세 스펙 부재: 제형/용량/가격/리뷰/반품률 미제공 → 본 문서의 스펙 표에서 TBD로 남은 항목은 내부 데이터 필요  
  (근거: Insight `3-3 추가로 필요한 입력`)

---

## 8. 실행 로드맵 (1주/2주/4주)
### 1주: 데이터 신뢰 확보 + 실험 세팅
- last_7_days 시작/종료 확정 및 타임스탬프 충돌 원인 점검  
  (근거: Insight `5(1주)`)
- 실험 2~3개 캠페인 세팅(시안 A/B/C 중 우선)  
  (근거: Insight `5(1주)`, `3-2`)

### 2주: 숏폼 제작/집행 + 학습
- 템플릿 기반 숏폼 6~12개 제작(루틴/성분/듀프 포맷) 후 CTR/CVR/CPA 비교  
  (근거: Insight `5(2주)`)

### 4주: 전환 지표 연결/고도화
- creator_id/video_id ↔ orders/GMV/ROAS/CVR 연결 스키마 보강  
  (근거: Insight `5(4주)`)
