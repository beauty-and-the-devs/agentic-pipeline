## A. 입력 데이터 개요

- 수집 범주 존재 여부  
  - 틱톡 메타: **있음** (TikTok Creative Center: top_products, trending_keywords)  
  - 인플루언서: **부분 있음** (related_videos 기반 파생 정보만 존재 / 팔로워·ER 추적 등 상세 API는 **미제공**)  
  - 시장(외부): **있음** (Creative Center 지표: 노출, CTR, CVR, CPA 등)  
  - PDF: **없음** (`user_uploaded_pdf: null`)

- 데이터 기간/범위  
  - 메타 수집 시각(원본): **2025-01-02T06:00:00Z**  
  - 메타 수집 시각(KST): **2025-01-02 15:00:00 (KST, Asia/Seoul)**  
  - 기간 표기: **last_7_days** (정확한 시작/종료 시각은 입력에 없어 **추정** 필요)

- 주요 식별자(연결 키)  
  - 배치: `batch_20250102_0600`  
  - 지역/카테고리: **US / Beauty & Personal Care (601450)**  
  - 상품: `product_id` (예: 1730383241618035288, 1730456789012345678 등)  
  - 판매자: `seller_id` (예: 7495794203056835079 등)  
  - 영상: `video_id` (예: 7529012345678901234 등)  
  - 크리에이터: `creator_id` / `author_id`

---

## B. 핵심 요약 (3~8줄)

- 최근 7일(표기 기준) **Beauty & Personal Care**에서 Creative Center 기준 **노출(impressions)**이 큰 상위 품목은 **Perfume(262,000,000)**, **Shampoo & Conditioner(111,000,000)**, **Serums & Essences(82,700,000)** 순입니다.  
- 전환 관점에서 **Shampoo & Conditioner(CVR 12.9%, CPA $1.23)**, **Moisturisers & Mists(CVR 12.59%, CPA $1.06)**가 **높은 CVR + 낮은 CPA** 조합으로 강한 신호입니다.  
- 키워드 중 **affordable makeup**은 **CTR 6.23% / CVR 14.2% / CPA $0.98**로 “클릭→구매” 효율이 가장 강하게 나타납니다.  
- related_videos 데이터 기준 상위 조회 영상은 **2,450,000뷰(niacinamide 관련)**, **1,250,000뷰(cleansing/glass skin 관련)**로, 스킨케어 루틴/글라스 스킨/가성비 스킨케어가 강한 관심 축으로 보입니다(단, 상세 기간 일치성은 아래 품질 체크 참고).  
- 크리에이터(파생 데이터) 중 **MakeupByMia(ER 7.53%)**, **SkinCareByAnna(ER 7.12%)**가 표본 내에서 참여율이 높습니다(표본은 각 1개 영상으로 제한적).

---

## C. 틱톡 콘텐츠 메타 분석

### 1) 상위 콘텐츠(있으면 Top N)
> 입력에서 “콘텐츠(영상) 성과”는 `related_videos.items`에만 존재하며, Creative Center의 top_products는 “상품 카테고리 집계 지표”입니다.

- Top 조회수(related_videos 기준)  
  1. **7529012345678901234** (제품: 1730567890123456789 / 크리에이터: DermInfluencer)  
     - 조회수: **2,450,000**, 좋아요: **156,000**  
     - 제목/태그: `#theordinary #niacinamide #affordableskincare #skintok #acne`  
  2. **7528901234567890123** (제품: 1730456789012345678 / 크리에이터: SkinCareByAnna)  
     - 조회수: **1,250,000**, 좋아요: **89,000**  
     - 제목/태그: `#skincare #cerave #cleanser #morningroutine #glassskin`  
  3. **7529123456789012345** (제품: 1730678901234567890 / 크리에이터: MakeupByMia)  
     - 조회수: **890,000**, 좋아요: **67,000**  
     - 제목/태그: `#elfcosmetics #haloglow #makeupdupes #drugstoremakeup #grwm`  
  4. **7527142083258305822** (제품: 1730383241618035288 / 크리에이터: Brittney)  
     - 조회수: **324,944**, 좋아요: **1,812**  
     - 제목/태그: `#clippers #manspot #balltrimmerformen #cleanshave #intimatetrimmer`

### 2) 참여 지표(가능하면)
- 입력에 “참여율(ER)”이 일부 계산되어 제공됨(`influencer_meta.creators.content_metrics.avg_engagement_rate_percent`)  
  - Brittney: **0.56%** (표본 1개)  
  - SkinCareByAnna: **7.12%** (표본 1개)  
  - DermInfluencer: **6.37%** (표본 1개)  
  - MakeupByMia: **7.53%** (표본 1개)

> 주의: 표본이 각 크리에이터당 **영상 1개**로 매우 작아 “채널 평균”으로 일반화는 **확인 필요**입니다.

### 3) 콘텐츠 특징(입력에 있을 때만)
- 해시태그/훅/CTA 관찰(제목 기반, **추정/정성 요약**)  
  - 스킨케어: `#glassskin`, `#morningroutine`, `#skintok`, `#acne` → 루틴/피부결과(글라스 스킨)/문제 해결형(여드름) 프레이밍  
  - 메이크업: `#makeupdupes`, `#drugstoremakeup`, `#grwm` → 가성비/대체품/메이크업 루틴(준비 영상)  
  - 그루밍(남성): `#cleanshave`, `#intimatetrimmer` → 기능/사용성 중심(단, 뷰 대비 참여 낮음)

---

## D. 인플루언서(크리에이터) 메타 분석

### 1) 핵심 크리에이터 요약(가능한 필드만)
- **MakeupByMia** (`creator_id: 7034567890123456789`, 제휴: Commission paid)  
  - 표본 성과: 조회 **890,000**, 좋아요 **67,000**, ER **7.53%**  
  - 카테고리: Makeup / Drugstore Beauty / GRWM
- **SkinCareByAnna** (`creator_id: 7012345678901234567`, 제휴: Commission paid)  
  - 표본 성과: 조회 **1,250,000**, 좋아요 **89,000**, ER **7.12%**  
  - 카테고리: Skincare / Beauty Routine / Glass Skin
- **DermInfluencer** (`creator_id: 7023456789012345678`, 제휴: Organic)  
  - 표본 성과: 조회 **2,450,000**, 좋아요 **156,000**, ER **6.37%**  
  - 카테고리: Skincare / Acne / Affordable Beauty
- **Brittney** (`creator_id: 6680168318781539334`, 제휴: Commission paid)  
  - 표본 성과: 조회 **324,944**, 좋아요 **1,812**, ER **0.56%**  
  - 카테고리: Beauty / Personal Care / Men’s Grooming

> 미제공/확인 필요: 팔로워 수, 채널 평균 조회수, 최근 성장 추이, 국가/언어(일부는 추정 가능하나 입력 근거 부족), 어필리에이션 “점수”.

### 2) 성과가 좋은 유형 vs 낮은 유형(근거 포함)
- 성과가 좋은 유형(표본 기준)  
  - **루틴/결과 중심 스킨케어**: `#glassskin`, `#morningroutine` 포함 영상(1.25M뷰, ER 7.12%)  
  - **가성비/듀프/드러그스토어 메이크업**: `#makeupdupes`, `#drugstoremakeup` 포함(890K뷰, ER 7.53%)  
  - **문제 해결형(여드름/성분 키워드)**: `#niacinamide #acne`(2.45M뷰, ER 6.37%)
- 성과가 낮은 유형(표본 기준, **확인 필요**)  
  - 남성 그루밍 제품 태그 중심 영상(324,944뷰 대비 ER 0.56%)  
  - 단, 제품/크리에이터/콘텐츠 품질 등 변수 분리가 불가하므로 일반화는 **추정**에 그침

### 3) 협업 우선순위 제안(근거 없으면 추정 표기)
- 우선 협업 후보(근거: 표본 ER + 조회수, 제휴 가능성)  
  1) **MakeupByMia**: ER 7.53%, Commission paid → 성과/제휴 신호 모두 존재  
  2) **SkinCareByAnna**: ER 7.12%, Commission paid → 스킨케어 루틴 축에서 강함  
  3) **DermInfluencer**: Organic이나 조회수/ER 강함 → 성과 검증 후 제휴 전환은 **추정**
- 보류/추가 검증  
  - Brittney: ER 0.56% → 추가 영상 표본 및 팔로워/도달 데이터 확인 필요

---

## E. 시장 전반 상황(외부 데이터) 요약

### 1) 상위 상품 카테고리(Top Products, Creative Center)
- **Perfume**  
  - 게시물 수: 24,600 / 노출: **262,000,000**  
  - CTR **1.35%**, CVR **8.21%**, CPA **$4.66**
- **Lipstick & Lip Gloss**  
  - 노출: 62,600,000 / CTR **4.08%**, CVR **6.16%**, CPA **$2.28**
- **Shampoo & Conditioner**  
  - 노출: 111,000,000 / CTR **2.14%**, CVR **12.9%**, CPA **$1.23**
- **Serums & Essences**  
  - 노출: 82,700,000 / CTR **1.81%**, CVR **5.17%**, CPA **$5.76**
- **Moisturisers & Mists**  
  - 노출: 71,500,000 / CTR **2.43%**, CVR **12.59%**, CPA **$1.06**

**해석(근거 기반):**
- “전환 효율” 관점의 강신호:  
  - **Moisturisers & Mists (CPA $1.06, CVR 12.59%)**  
  - **Shampoo & Conditioner (CPA $1.23, CVR 12.9%)**
- “유입(클릭)” 관점의 강신호:  
  - **Lipstick & Lip Gloss (CTR 4.08%)**
- “노출은 크나 비용/효율은 약한 편” 가능성(단정 금지):  
  - Perfume(노출 262M 대비 CPA $4.66)  
  - Serums & Essences(CPA $5.76)

### 2) 트렌딩 키워드(Trending Keywords)
- 상승률(change%) 상위  
  - **glass skin**: 인기 67,000 / 변화 **+142.8%**, CTR 4.12%, CVR 9.2%, CPA $1.89  
  - **affordable makeup**: 인기 42,000 / 변화 **+125.6%**, CTR **6.23%**, CVR **14.2%**, CPA **$0.98**  
  - **skincare routine**: 인기 89,000 / 변화 **+115.2%**, CTR 3.45%, CVR 7.8%, CPA $2.15
- 효율(CTR/CVR/CPA) 최강 신호  
  - **affordable makeup**: CTR 6.23% / CVR 14.2% / CPA $0.98 (가성비 메시지의 구매 효율 신호)

### 3) 위험/기회 요인(가능한 항목만)
- 기회 요인(근거: 키워드+성과)  
  - “가성비(affordable)” + “듀프/드러그스토어” + “루틴/글라스 스킨” 축이 동시 강화
- 위험 요인/확인 필요  
  - 플랫폼 정책/규제/이슈: **미제공**  
  - 경쟁 강도/가격대 분포: **미제공** (단, Creative Center의 게시물 수(post_count)는 경쟁 강도에 대한 간접지표일 수 있으나 단정은 금지)

---

## F. 사용자 PDF 데이터 통합 요약

- PDF 핵심 주장/수치/표 요약: **없음(미제공)**  
- 틱톡/인플루언서/시장 데이터와 일치/충돌: **판단 불가(미제공)**  
- PDF 기반 추가 가설: **없음(미제공)**

---

## G. 데이터 품질 체크

### 1) 누락된 필드/범주
- PDF 범주: **누락**  
- 인플루언서 상세 메타(팔로워, 평균 조회, 성장 추이, 국가/언어 등): **누락**  
- 콘텐츠 메타(영상의 댓글/공유/저장, 링크 클릭, 전환 등): **대부분 누락** (영상은 조회·좋아요 중심)

### 2) 충돌/중복/이상치 의심 항목
- **시간 충돌(중요)**  
  - 메타 수집 시각은 **2025-01-02**인데, related_videos의 `upload_timestamp`는 **2025-07-15 ~ 2025-07-18 (KST 기준)**로 변환됩니다.  
  - product_details의 sample_review `timestamp: 2025-06-15` 또한 메타 수집 시각 이후입니다.  
  → 동일 배치/기간 데이터인지 **충돌** 가능성이 있어 “샘플/혼합 데이터” 여부 **확인 필요**.
- URL 품질 이슈  
  - 일부 `image_url`, `shop_logo_url`, `cover_image_url`에 `https://example.com/...` 형태가 포함되어 **실데이터가 아닐 가능성(확인 필요)**.
- 검색 쿼리 불일치 가능성  
  - `search_query: "skincare"`인데 상품 목록에 **구미(영양제), 바디 헤어 면도기** 등 스킨케어와 직접 무관한 품목이 포함 → 검색/필터 로직 또는 카테고리 매핑 **확인 필요**.
- 중복/병합 포인트(정상)  
  - 동일 `product_id`가 **products / product_details / related_videos / sellers**에 분산 존재  
  - 병합 기준(권장): `product_id` 우선, 보조로 `seller_id`, `video_id` 연결

### 3) 추가 수집이 필요한 데이터(구체적으로)
- (인플루언서) creator_id별: 팔로워 수, 최근 30일 평균 조회/ER, 성장률, 국가/언어, 브랜드 협업 이력  
- (콘텐츠) 영상별: 댓글수/공유수/저장수, 클릭/전환 이벤트(가능 시), 게시일(원본 타임존 포함), 광고 여부 일관 표기  
- (상품) 가격 이력(할인 전후 기간), 카테고리 정합성(스킨케어 검색 결과 필터), 재고/품절 빈도  
- (시장) 경쟁 강도 지표(상위 경쟁 상품/브랜드, 가격대 분포), 리뷰/불만 요약(주요 클레임)

---

## H. 최종 정리

### 1) 실행에 바로 쓰는 결론 3~5개(근거 기반)
1. **가성비 메시지(affordable makeup)**는 CTR 6.23%, CVR 14.2%, CPA $0.98로 효율이 가장 강함 → “가성비/듀프/드러그스토어” 포지셔닝을 우선 실험하는 것이 합리적입니다.  
2. 스킨케어에서는 **글라스 스킨(glass skin)** 키워드가 +142.8% 상승, CVR 9.2% → “결과(피부 표현) + 루틴”형 숏폼/라이브 소재가 유효할 가능성이 큽니다.  
3. 상품 카테고리 집계 기준으로는 **Moisturisers & Mists / Shampoo & Conditioner**가 높은 CVR(12%대)과 낮은 CPA($1.x) → “구매전환형 캠페인” 우선 카테고리 후보입니다.  
4. 표본 영상 기준으로 참여율은 **MakeupByMia(7.53%)**, **SkinCareByAnna(7.12%)**가 높음 → 초기 협업 테스트 후보로 우선 검토 가능합니다(단, 표본 1개로 **확인 필요**).  
5. 데이터 내 시간대 충돌(수집일 vs 업로드일)이 있어, 의사결정 전 **데이터 시점 정합성 검증**이 선행되어야 합니다.

### 2) 다음 단계(추가 분석/추가 수집/실험 아이디어) 3개
1. **데이터 시점 정합성 검증**: related_videos/product_details의 타임스탬프가 배치 기간(last_7_days)과 맞는지 원천 수집 로직(파이프라인) 확인.  
2. **키워드→콘텐츠→상품 연결 실험**:  
   - (가설) `affordable makeup`, `glass skin`, `lip gloss` 키워드 기반 숏폼 3종을 제작해 CTR/CVR 비교(가능하면 동일 예산/기간).  
3. **크리에이터 협업 후보 확장 수집**: 현재는 각 1개 영상 표본이므로, 동일 키워드/카테고리에서 상위 크리에이터 20~50명을 추가 수집해 “팔로워 대비 성과(ER, CVR)”로 재랭킹.
