# explainer_lgbm.shap_values - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:26:47

---

파이썬 머신러닝 해석(XAI)에서 가장 널리 쓰이는 **SHAP(SHapley Additive exPlanations)** 라이브러리의 핵심 함수 중 하나입니다. 초보자의 눈높이에 맞춰 아주 쉽고 명쾌하게 해설해 드릴게요!

---

### 1. 📌 함수 개요
> `explainer_lgbm.shap_values(X_test)`는 **"AI 모델(여기서는 LightGBM)이 왜 그런 예측을 했는지 그 이유를 각 피처(특성)별 기여도로 쪼개어(분해하여) 설명해 주는 마법 같은 함수"**입니다.

우리가 만든 머신러닝 모델이 "이 집은 5억 원입니다!"라고 예측했을 때, 이 함수는 *"위치가 좋아서 +2억, 평수가 넓어서 +3억, 연식이 오래돼서 -1억..."* 과 같이 각 요인(피처)이 가격에 얼마만큼 영향을 줬는지 수학적으로 계산해 줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드에서는 괄호 안에 `X_test` 단 한 개의 인자가 전달되었습니다.

*   **`X_test` (테스트 데이터셋)**
    *   **역할:** 모델이 학습할 때 사용하지 않고, 성능을 평가하기 위해 아껴둔 **새로운 데이터(표 형태의 데이터프레임 또는 넘파이 배열)**입니다.
    *   **의미:** "이 데이터들을 모델에 넣었을 때, 모델이 각 샘플마다 어떤 과정을 거쳐 예측을 내렸는지 분석해 줘!"라고 SHAP Explainer에게 요청하는 대상입니다.

---

### 3. 📤 반환값/할당 변수

*   **할당 변수:** `shap_values_lgbm`
*   **반환되는 데이터의 정체:** 
    *   `X_test` 데이터의 모양(행과 열의 크기)과 **완전히 똑같은 형태의 숫자 배열(Array)**이 반환됩니다.
    *   다만, 원래 데이터에는 '나이', '연봉', '집값' 같은 실제 숫자 값이 들어있었다면, **반환된 `shap_values_lgbm`에는 그 값이 예측에 얼마나 기여했는지를 나타내는 SHAP 값(기여도 점수)**이 들어있습니다.
    *   *예시:* 양수(+)면 예측값을 높이는데 기여한 것, 음수(-)면 예측값을 낮추는데 기여한 것을 뜻합니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 이해할 수 있도록, LightGBM 모델 학습부터 SHAP 값을 구하고 시각화하는까지의 간단한 전체 코드를 준비했습니다.

```python
import lightgbm as lgb
import shap
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# 1. 가상 데이터 생성 및 모델 학습 (준비 단계)
X, y = make_regression(n_samples=100, n_features=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = lgb.LGBMRegressor(random_state=42)
model.fit(X_train, y_train)

# 2. SHAP Explainer 객체 만들기
# LightGBM 모델 전용 해석기를 생성합니다.
explainer_lgbm = shap.TreeExplainer(model)

# 3. 🔥 오늘의 핵심 함수 호출!
# X_test의 각 데이터가 예측에 미친 영향력(SHAP 값)을 계산합니다.
shap_values_lgbm = explainer_lgbm.shap_values(X_test)

# 4. 결과 확인 (시각화)
# 첫 번째 테스트 데이터가 왜 그런 예측값을 가졌는지 시각적으로 보여줍니다.
shap.initjs()  # 주피터 노트북 환경용
shap.force_plot(
    explainer_lgbm.expected_value, shap_values_lgbm[0], X_test[0]
)
```

> **💡 한 줄 요약:** `explainer_lgbm.shap_values(X_test)`는 테스트 데이터를 입력받아 **"AI가 내린 예측의 원인(각 피처의 기여도)을 속속들이 파헤쳐 숫자로 돌려주는 기능"**입니다!