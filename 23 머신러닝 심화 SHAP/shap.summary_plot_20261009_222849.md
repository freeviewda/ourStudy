# shap.summary_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:28:49

---

파이썬의 머신러닝 모델 해석 라이브러리인 `SHAP`에서 사용되는 `shap.summary_plot` 함수에 대해 초보자의 눈높이에 맞춰 쉽고 명쾌하게 설명해 드리겠습니다.

---

### 1. 📌 함수 개요
`shap.summary_plot`은 **"AI(머신러닝) 모델이 예측을 할 때, 어떤 데이터(특징)가 가장 큰 영향을 미쳤는지"**를 한눈에 볼 수 있도록 시각화(요약 그래프 생성)해 주는 함수입니다. 모델의 '결정 백과사전' 같은 역할을 합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드에서 사용된 5가지 인자가 각각 어떤 일을 하는지 살펴볼까요?

*   **`shap_values_lgbm`**
    *   **역할:** LightGBM 모델이 예측할 때 사용한 SHAP 값(기여도 점수)입니다.
    *   **의미:** 각 데이터가 예측 결과에 얼마나 긍정적 혹은 부정적인 영향을 주었는지 계산된 수치들의 모음입니다.
*   **`X_test`**
    *   **역할:** 모델이 예측에 사용한 **테스트 데이터(feature)**입니다.
    *   **의미:** 실제 사람이 살고 있는 집의 넓이, 방 개수 등 모델에 입력된 원본 데이터의 특징(Feature) 값들이 들어 있습니다.
*   **`feature_names=feature_names`**
    *   **역할:** 그래프에 표시될 **특징(변수)들의 이름표**를 지정합니다.
    *   **의미:** 코드 내 변수 `feature_names`에 저장된 이름(예: `['나이', '소득', '직업']`)을 가져와서 그래프의 Y축에 예쁘게 출력해 줍니다.
*   **`plot_type='bar'`**
    *   **역할:** 그래프의 **모양(시각화 형태)**을 결정합니다.
    *   **의미:** `'bar'`로 설정했기 때문에, 점(Dot) 형태가 아니라 알기 쉬운 **막대그래프** 형태로 전체 중요도를 보여줍니다. (막대가 길수록 모델에게 중요한 정보입니다.)
*   **`show=False`**
    *   **역할:** 그래프를 **즉시 화면에 출력할지 여부**를 결정합니다.
    *   **의미:** `False`로 설정하면 바로 화면에 띄우지 않고 대기 상태로 둡니다. 이 덕분에 이후에 `plt.savefig()`로 그림을 파일로 저장하거나, `plt.xlabel()` 등으로 그래프를 꾸민 뒤 마지막에 `plt.show()`로 깔끔하게 출력할 수 있습니다.

---

### 3. 📤 반환값/할당 변수
*   **반환값:** **없음 (`None`)**
*   **설명:** 이 함수는 별도의 데이터를 반환하는 것이 아니라, 파이썬의 시각화 도구(`matplotlib`)를 이용해 **그래프 그림(Plot)을 생성하고 화면(또는 메모리)에 띄우는 역할**만 합니다. 따라서 별도의 변수에 결과값을 담아둘 필요가 없습니다.

---

### 4. 🎁 요약 및 실행 예시

전체 코드가 어떻게 유기적으로 움직이는지 간단한 예시로 확인해 보겠습니다.

```python
import shap
import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1. 가짜 데이터 및 모델 준비
X, y = make_classification(n_samples=100, n_features=5, random_state=42)
feature_names = ['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = lgb.LGBMClassifier(random_state=42)
model.fit(X_train, y_train)

# 2. SHAP 값 계산
explainer = shap.TreeExplainer(model)
shap_values_lgbm = explainer.shap_values(X_test)

# ==========================================
# 3. 오늘의 핵심 코드 실행!
# ==========================================
shap.summary_plot(
    shap_values_lgbm, 
    X_test, 
    feature_names=feature_names, 
    plot_type='bar', 
    show=False
)

# 4. 그래프 꾸미기 및 출력
plt.title("My First SHAP Bar Plot")
plt.show()
```

**💡 예상 결과:**
화면에 위에서 아래로 내림차순 정렬된 막대그래프가 나타납니다. `feature_1`, `feature_2` 등 모델이 예측을 할 때 **어떤 특징을 가장 중요하게 여겼는지** 길이가 긴 막대 순서대로 한눈에 파악할 수 있습니다!