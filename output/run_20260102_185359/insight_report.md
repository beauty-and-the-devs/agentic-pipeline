# TikTok Shop 마케팅 인사이트 리포트 (미국 / 화장품)

## 0. 데이터 요약

- **데이터 범위 요약**:
  - 상품 수: 5개 상세 분석 (Manspot, CeraVe, The Ordinary, e.l.f., Goli Nutrition 등)
  - 크리에이터 수: 4명 (`@derminfluencer`, `@skincarebyanna`, `@makeupbymia`, `@brittney_reviews`)
  - 기간: 최근 7일 (2025년 1월 2일 기준 수집)
  - 지역: 미국(US)
  - 콘텐츠 수: 각 크리에이터당 1개 동영상 기준 (총 4개)

- **사용 가능한 주요 지표 목록**:
  - 조회수(`play_count`), 좋아요 수(`like_count`), 참여율(`avg_engagement_rate_percent`)
  - 클릭률(`ctr_percent`), 전환율(`cvr_percent`), CPA(비용/획득)
  - 상품 판매 수(`sold_count`), 리뷰 수(`review_count`), 평점(`score`)
  - 가격 정보(정가, 할인가, 할인율)
  - 인플루언서 카테고리, 콘텐츠 태그, 동영상 길이
  - 판매자 평가: 배송 정시율(`ship_on_time`), 응답률(`response_rate`), 긍정 피드백 비율
  - 트렌드 키워드: 인기도, 성장률, CTR/CVR

- **상위/하위 성과 요약**:
  - **상위 성과 상품**: CeraVe 클렌저 (판매 32.8만+), The Ordinary 세럼 (56.7만+), Goli 애쉬와간다 젤리 (123.5만+)
  - **상위 성과 콘텐츠**: `@derminfluencer` (조회 245만, ER 6.37%)
  - **하위 성과 콘텐츠**: `@brittney_reviews` (ER 0.56%, 조회 32.5만)

---

## 1. 잘 팔리는 이유

### ✅ 핵심 성공 요인 (상위 성과 상품/콘텐츠 공통점)

1. **합리적 가격 + 높은 할인율**
   - Manspot 면도기: 정가 $39.99 → 할인가 $21.19 (**47% 할인**)
   - Goli 애쉬와간다 젤리: $24.99 → $14.96 (**40% 할인**)
   - 저가 브랜드(The Ordinary, e.l.f.)는 정가 자체가 낮음 ($6.5~$14)
   - (근거: `tiktok_shop_products`의 `price.discount_percent`, `sale_price`)

2. **진정성 있는 콘텐츠 + 비영리(organic) 리뷰**
   - `@derminfluencer`의 비영리 동영상이 **조회 245만**, **좋아요 15.6만**, **ER 6.37%** 기록
   - 진정성 있는 리뷰 형식(예: #affordableskincare, #acne)이 신뢰 유도
   - (근거: `related_videos`의 `ad_label: null`, `video_info.title` 해시태그)

3. **트렌드 키워드 전략적 활용**
   - `#glassskin`, `#affordablemakeup`, `#vitamincserum` 등 급상승 키워드 사용
   - `affordable makeup` 키워드: **CTR 6.23%, CVR 14.2%** → 최고 전환 효율
   - (근거: `market_trends.trending_keywords`의 `cvr_percent`, `ctr_percent`)

4. **짧고 직관적인 동영상 포맷**
   - 상위 콘텐츠 동영상 길이: **28초~58초**
   - 메시지 집중: 제품 사용 루틴(GRWM, morning routine)과 연계
   - (근거: `related_videos.video_info.duration_ms`)

5. **기존 대중 브랜드 신뢰성 + 높은 리뷰 수**
   - CeraVe: 리뷰 4.5만+, 평점 4.8
   - The Ordinary: 리뷰 7.8만+, 평점 4.6
   - (근거: `tiktok_shop_products.rating`)

---

## 2. 안 팔리는 이유

### ❌ 낮은 성과 상품/콘텐츠의 공통 패턴

1. **타겟 시장이 좁거나 니즈 불일치**
   - `@brittney_reviews`는 남성 정리기구(Manspot 면도기) 중심
   - 남성용 제품은 미국 TikTok 뷰티 카테고리에서 상대적으로 관심 낮음
   - (근거: `influencer_meta.categories`, `related_videos.title` 해시태그)

2. **참여 유도 약한 콘텐츠 형식**
   - `@brittney_reviews`의 제목: `#clippers #manspot #balltrimmerformen` → 단순 해시태그 나열
   - 감정 유발, 스토리텔링, CTA 부족
   - (근거: `related_videos.video_info.title`)

3. **낮은 참여율(ER) → 퍼널 상단에서 병목**
   - `@brittney_reviews`: ER 0.56% (타 크리에이터 대비 10배 이상 낮음)
   - 조회수 32.5만 대비 좋아요 1,812 → **CTR 및 CVR 하락 가능성**
   - (근거: `influencer_meta.content_metrics.avg_engagement_rate_percent`)

4. **단일 동영상 기반 → 통계적 신뢰도 낮음**
   - 모든 크리에이터가 `total_videos_in_dataset: 1` → 일시적 이상치 가능성
   - (근거: `influencer_meta.content_metrics.total_videos_in_dataset`)

---

## 3. 개선 가능한 기회

| 개선 항목 | 요약 | 근거 | 기대 효과 | 우선순위 |
|---------|------|------|-----------|--------|
| 콘텐츠 형식 개선 | 해시태그 중심 → 스토리 기반 리뷰로 전환 | `@brittney_reviews` 제목이 단순 태그 나열 | ER↑, CTR↑ | High |
| 번들 구성 도입 | 면도기 + 클렌저/애프터케어 제품 번들 | Manspot 리뷰에서 "good shipping", "light weight" 언급 | CVR↑, AOV↑ | Med |
| 사용 가이드 강화 | 동영상 내 사용법/주의사항 추가 | `ship_on_time` 97%지만 사용법 부족 가능성 | 반품률↓, 평점↑ | Med |
| 트렌드 키워드 통합 | `#affordable`, `#glassskin` 등 태그 추가 | `affordable makeup` 키워드 CVR 14.2% | CTR↑, ROAS↑ | High |

### 빠른 실험(A/B 테스트) 제안

| 실험 | 변수 | 성공 기준 | 대상 |
|------|------|-----------|------|
| A/B 콘텐츠 형식 | (A) 스토리 리뷰 vs (B) 제품 나열 | ER 3% 이상, CTR 2배 | `@brittney_reviews` |
| 번들 테스트 | 면도기 + 클렌저 vs 단일 제품 | CVR 8% 이상 | Manspot 상품 |
| 해시태그 실험 | `#affordable` 포함 vs 미포함 | CTR 4% 이상 | 모든 신규 콘텐츠 |

---

### [제품 기회 분석 로직 기반] 잘 팔리지만 불만이 있는 제품 기회

#### [대상 카테고리/상품명]  
**Manspot 전기 면도기**

#### [Positive Driver]:  
- **"Good shipping"**: 3회 언급 (50%)  
- **"Does not nick"**: 2회 언급 (33%)  
- **"Holds charge"**: 2회 언급 (33%)  
- **"Light weight"**: 1회 언급 (17%)  
(근거: `product_details.reviews.sample_reviews.text`)

#### [Negative Driver]:  
- **"Used in the shower"**: 1회 언급 → 방수 기능 강조되나, 실제 사용 리스크 존재 가능성  
- **리뷰 수 적음**: 595건 (CeraVe 대비 1.3%) → 사회적 증거 부족  
- **배송 신뢰도 낮음**: `ship_on_time` 50% (Goli Nutrition 대비 절반)  
(근거: `sellers.store_scores.ship_on_time`, `review_count`)

#### [문제점]:  
- 제품 성능은 긍정적이나, **배송 신뢰도 낮음**(50%) + **리뷰 수 부족** → 구매 결정 장벽 존재

#### [기회]:  
1. **배송 개선 + "빠른 배송 보장" 태그 도입**  
2. **리뷰 유도 캠페인**(예: 구매 후 리뷰 작성 시 할인 쿠폰)  
3. **방수 기능 강조 + 사용 가이드 동영상 제작**

#### [기대 효과]:  
- 리뷰 수↑ → 사회적 증거 강화 → **CVR↑**  
- 배송 신뢰도↑ → **반품률↓, ROAS↑**  
- 사용 가이드 → **CS 문의↓, 평점↑**

---

## 4. 화장품 종류별 전환 성과 상위 크리에이터

### 스킨케어 (Skincare)

- **@derminfluencer**  
  - 성과: 조회 245만, ER 6.37%, 비영리 콘텐츠  
  - 강점: 진정성 있는 리뷰, #affordableskincare, #acne 키워드 활용  
  - 협업 제안: The Ordinary, CeraVe 등 저가 스킨케어 제품 리뷰 → **CVR 9%+ 기대**

- **@skincarebyanna**  
  - 성과: 조회 125만, ER 7.12%  
  - 강점: #glassskin, #morningroutine 등 일상 연계 콘텐츠  
  - 협업 제안: 유리피부 루틴 구성 제품 번들 추천 → **GMV↑**

### 메이크업 (Makeup)

- **@makeupbymia**  
  - 성과: 조회 89만, ER 7.53%  
  - 강점: #drugstoremakeup, #grwm, #makeupdupes 등 합리적 메이크업 강조  
  - 협업 제안: e.l.f. Halo Glow 필터 + 드럭스토어 제품 조합 → **CVR 14%+ 기대**

### 남성 정리기구 (Men's Grooming)

- **@brittney_reviews**  
  - 성과: 조회 32.5만, ER 0.56% → **낮음**  
  - 문제점: 콘텐츠 형식 단순, 해시태그 중심  
  - 개선 제안: "남성용 데일리 루틴" 스토리텔링 도입 + #menskincare 연계

---

## 5. 다음 액션 체크리스트

| 기간 | 실행 항목 | 담당 | 지표 |
|------|----------|------|------|
| 1주 | `@derminfluencer`와 The Ordinary 세럼 협업 콘텐츠 제작 | 마케팅팀 | ER > 6%, GMV $50K+ |
| 1주 | Manspot 리뷰 유도 캠페인 설계 (구매 후 리뷰 쿠폰) | 운영팀 | 리뷰 수 1,000+ |
| 2주 | `@brittney_reviews` 콘텐츠 A/B 테스트 (스토리 vs 나열) | 콘텐츠팀 | ER 3% 이상 |
| 2주 | `#affordable` 키워드 포함 콘텐츠 확대 | 마케팅팀 | CTR 4% 이상 |
| 4주 | Manspot + 클렌저 번들 구성 테스트 | 제품팀 | CVR 8% 이상, AOV $30+ |

> ✅ **추가 수집 제안**:  
> - 인플루언서 **팔로워 수**, **댓글/공유/저장 수** → 참여 지표 정확도 향상  
> - **다수 동영상 기반 평균 ER** → 통계적 신뢰도 확보  
> - **업로드 일시 정확한 KST 변환** → 타이밍 분석 가능  
> - **반품률, CS 이슈 로그** → Negative Driver 심층 분석 가능

> ⚠️ **데이터 상 확인 불가 항목**:  
> - 정확한 반품률, 감정 점수, 리뷰 원문 감정 분석, 크리에이터 성별/연령 타겟  
> → 향후 PDF 또는 추가 API 수집 필요