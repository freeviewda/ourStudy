# shap.waterfall_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:33:57

---

파이썬의 머신러닝 해석 라이브러리인 **SHAP**에서 사용되는 `shap.waterfall_plot` 함수와 그 입력값들에 대해 초보자의 눈높이에 맞춰 아주 쉽게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`shap.waterfall_plot`은 **"AI(머신러닝) 모델이 왜 특정 데이터(환자, 집, 상품 등)에 대해 그런 예측을 내렸는지"**를 폭포(Waterfall) 모양의 그래프로 시각화해 주는 함수입니다. 
기본 점수(평균 예측값)에서 시작해서, 각 특징(Feature)들이 예측값에 **얼마나 더해지고 깎였는지**를 위아래로 쌓이는 막대 그래프 형태로 한눈에 보여줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에서는 크게 `shap.waterfall_plot()`이라는 큰 틀 안에, 그래프를 그릴 재료를 담은 `shap.Explanation()` 객체와 시각화 옵션인 `show=False`가 전달되고 있습니다. 하나씩 뜯어볼까요?

#### ① `shap.Explanation(...)` (그래프의 모든 재료를 담는 상자)
그래프를 그리기 위해 필요한 데이터를 하나로 묶어주는 SHAP 전용 데이터 클래스(상자)입니다. 이 상자에 담긴 4가지 재료는 다음과 같습니다.

*   **`values=shap_values_xgb[sample_idx]`**
    *   **의미:** 테스트 데이터 중 특정 샘플(`sample_idx`번째)의 **SHAP 값(기여도)**입니다.
    *   **설명:** 이 특징이 AI의 예측 결과에 **얼마나 긍정적 혹은 부정적인 영향**을 주었는지를 나타내는 숫자들의 모음입니다.
*   **`base_values=explainer_xgb.expected_value`**
    *   **의미:** AI 모델의 **기준점(기본 예측값)**입니다.
    *   **설명:** 모델이 가진 모든 데이터에 대한 평균적인 예측 결과입니다. 폭포 그래프가 시작되는 '출발선' 역할을 합니다.
*   **`data=X_test.iloc[sample_idx].values`**
    *   **의미:** 분석 중인 **실제 데이터의 원본 값**입니다.
    *   **설명:** 예를 들어, 그 집의 실제 방 개수가 3개인지, 연봉이 5천만 원인지 등 **실제 입력된 특성들의 값**입니다. 그래프에 마우스 오버를 하거나 이름을 표시할 때 "연봉 = 5,000만 원"처럼 실제 숫자를 함께 보여주기 위해 사용됩니다.
*   **`feature_names=feature_names`**
    *   **의미:** 특징들의 **이름 리스트**입니다.
    *   **설명:** `['나이', '연봉', '방 개수']`처럼 모델이 학습에 사용한 변수들의 사람이 읽을 수 있는 이름입니다. 이 이름이 없으면 그래프의 Y축이 `Feature 0`, `Feature 1` 같은 기계적인 이름으로 표시되어 알아보기 힘들기 때문에 이름을 꼭 넣어줍니다.

#### ② `show=False` (시각화 옵션)
*   **의미:** 그래프를 즉시 화면에 띄우지(Show) 말고, **메모리에만 저장**해 둔다는 뜻입니다.
*   **설명:** 이 설정을 해두면 주피터 노트북 등에서 그래프를 그린 뒤, 타이틀을 추가하거나 이미지로 저장(`plt.savefig()`)하는 등의 **추가적인 커스텀 작업**을 한 번에 처리할 수 있어서 실무에서 매우 유용하게 쓰입니다.

---

### 3. 📤 반환값/할당 변수

*   **반환값 없음 (None)**
*   **설명:** 이 함수는 별도의 데이터를 리턴(Return)하는 함수가 아니라, Matplotlib 기반의 **시각화 그림(Plot)을 화면이나 메모리에 그려주는 역할**만 합니다. 따라서 반환받아 변수에 담을 값은 따로 없고, 바로 그림을 출력하거나 조작하게 됩니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 이해할 수 있도록 아주 간단한 형태의 코드로 요약해 드릴게요.

```python
import shap
import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1. 간단한 데이터 및 모델 준비 (예시)
X, y = shap.datasets.california()  # 캘리포니아 집값 데이터
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = xgb.XGBRegressor().fit(X_train, y_train)

# 2. SHAP 값 계산기(Explainer) 생성
explainer_xgb = shap.Explainer(model, X_train)
shap_values_xgb = explainer_xgb(X_test)

# 3. 변수 정의
sample_idx = 0  # 첫 번째 테스트 환자(집)를 분석하겠다!
feature_names = X.columns.tolist()

# 4. 워터폴 플롯(Waterfall Plot) 그리기 (★ 오늘 배운 핵심 코드!)
shap.waterfall_plot(
    shap.Explanation(
        values=shap_values_xgb[sample_idx],
        base_values=explainer_xgb.expected_value,
        data=X_test.iloc[sample_idx].values,
        feature_names=feature_names,
    ),
    show=False,
)

# 그래프 제목 달기 및 화면 출력
plt.title("AI Prediction Explanation")
plt.show()
```

**🎯 예상 결과:**
화면에 알록달록한 폭포 모양의 그래프가 나타납니다. 
*   가장 아래쪽(또는 위쪽)에는 AI가 내린 **평균적인 예측값(Base value)**이 적혀 있습니다.
*   중간 막대들은 각 특징(예: 위치, 방 개수 등)이 집값을 **얼마나 올렸고(빨간색)** **얼마나 낮췄는지(파란색)**를 보여줍니다.
*   가장 꼭대기(또는 바닥)에는 이 집의 **최종 예측된 가격**이 표시됩니다.