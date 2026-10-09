# shap.summary_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:27:59

---

안녕하세요! 파이썬 머신러닝 해석에서 아주 유용하게 쓰이는 `shap.summary_plot` 함수에 대해 초보자의 눈높이에 맞춰 쉽고 명쾌하게 설명해 드리겠습니다.

---

### 1. 📌 함수 개요
`shap.summary_plot`은 **AI(머신러닝) 모델이 예측을 내릴 때, 어떤 데이터(특성)가 가장 큰 영향을 미쳤는지 한눈에 볼 수 있도록 시각화(요약 그림)해주는 함수**입니다. 
복잡한 블랙박스 모델의 결과를 직관적인 그래프로 보여주어, "이 모델은 어떤 기준으로 정답을 맞혔을까?"를 사람이 쉽게 이해할 수 있게 도와줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
코드에서 사용된 5가지 인자가 각각 어떤 역할을 하는지 뜯어볼까요?

* **`shap_values_xgb`**
  * **역할:** 모델이 계산해 낸 SHAP 값(기여도 점수)입니다.
  * **의미:** XGBoost 모델(`_xgb`)이 예측을 할 때 각 특성(Feature)이 결과에 얼마나 긍정적 혹은 부정적인 영향을 주었는지 수학적으로 계산된 결과물입니다.
* **`X_test`**
  * **역할:** 모델 성능을 평가하기 위해 남겨둔 테스트 데이터셋입니다.
  * **의미:** 실제 특성들의 값(예: 나이, 소득 등)을 담고 있으며, SHAP 값과 매칭되어 그래프를 그릴 때 기준 데이터로 사용됩니다.
* **`feature_names=feature_names`**
  * **역할:** 그래프에 표시될 특성(변수)들의 이름입니다.
  * **의미:** 컴퓨터가 이해하는 숫자 형태의 컬럼명 대신, 우리가 알아보기 쉬운 이름표(예: `['나이', '연봉', '근속년수']`)로 그래프 축을 꾸며줍니다.
* **`plot_type='bar'`**
  * **역할:** 시각화할 그래프의 모양(형태)을 지정합니다.
  * **의미:** `'bar'`는 막대그래프를 의미합니다. 각 특성이 모델에 얼마나 '절대적으로 중요한지'를 크기순으로 막대기로 정렬해 줍니다. (지정하지 않으면 점(Dot) 형태의 화려한 그래프가 나옵니다.)
* **`show=False`**
  * **역할:** 그래프를 즉시 화면에 띄울지 여부입니다.
  * **의미:** `False`로 설정하면 바로 화면에 출력되지 않고 파이썬 메모리(플롯 객체)에 저장됩니다. 보통 Jupyter Notebook 등에서 그래프 크기를 조절하거나 제목을 추가한 뒤 마지막에 `plt.show()`로 출력하기 위해 자주 씁니다.

---

### 3. 📤 반환값/할당 변수
* **반환값:** **없음 (`None`)**
* **설명:** 이 함수는 데이터를 계산해서 돌려주는 함수가 아니라, **그림을 그려서 화면(또는 메모리)에 띄워주는 역할**만 합니다. 따라서 별도의 변수에 값을 대입(`result = ...`)할 필요 없이, 함수만 단독으로 실행하면 됩니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 전체 흐름 속에서 이 코드를 어떻게 쓰는지 간단한 예시로 보여드릴게요!

```python
import shap
import xgboost as xgb
from sklearn.model_selection import train_test_split

# 1. 간단한 데이터 및 모델 준비 (예시)
X, y = shap.datasets.adult()  # 예제 데이터 로드
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = xgb.XGBClassifier().fit(X_train, y_train)

# 2. SHAP 값 계산
explainer = shap.Explainer(model)
shap_values_xgb = explainer(X_test)
feature_names = X_test.columns.tolist()

# ==========================================
# 3. 오늘의 핵심 코드 실행!
# ==========================================
import matplotlib.pyplot as plt

shap.summary_plot(
    shap_values_xgb,
    X_test,
    feature_names=feature_names,
    plot_type="bar",
    show=False,
)

# 제목을 추가하고 화면에 예쁘게 출력하기
plt.title("XGBoost Model Feature Importance", fontsize=14)
plt.show()
```

**💡 예상 결과:**
화면에 위에서부터 아래로 가장 중요한 특성(예: 나이, 자본 이익 등)이 **막대그래프** 형태로 쫙 펼쳐져 나타납니다. 어떤 변수가 우리 모델에게 가장 중요한 '핵심 정보'였는지 1초 만에 파악할 수 있습니다!