# shap.summary_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:27:36

---

파이썬 머신러닝 해석 도구인 `SHAP` 라이브러리의 핵심 함수인 `shap.summary_plot`에 대해 초보자의 눈높이에 맞춰 쉽고 명쾌하게 설명해 드리겠습니다.

---

### 1. 📌 함수 개요
`shap.summary_plot`은 **머신러닝 모델이 예측을 내릴 때, 각 데이터(특성, Feature)가 얼마나 중요한지, 그리고 예측에 어떤 방향으로 영향을 미쳤는지(양(+)의 영향인지 음(-)의 영향인지) 한눈에 보여주는 요약 그래프**를 그려주는 함수입니다. (일명 'SHAP 요약 플롯' 또는 '비즈니스 관점의 중요도 랭킹 맵')

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드 `shap.summary_plot(shap_values_xgb, X_test, feature_names=feature_names, show=False)`에 들어간 각 인자의 의미는 다음과 같습니다.

*   **`shap_values_xgb` (첫 번째 위치 인자)**
    *   **역할:** 모델이 예측할 때 계산된 **SHAP 값(기여도 값)**들의 모음입니다.
    *   **의미:** XGBoost 모델(`_xgb`)이 각 데이터 샘플의 예측 결과에 대해 "어떤 변수가 얼마만큼 기여했는지" 수학적으로 계산해 둔 결과물입니다.
*   **`X_test` (두 번째 위치 인자)**
    *   **역할:** 모델 성능을 평가하기 위해 남겨둔 **테스트 데이터셋(특성 값들)**입니다.
    *   **의미:** 그래프를 그릴 때, 실제 입력된 특성 값의 크기(예: 나이가 실제로 많은지 적은지)를 색상으로 표현하기 위해 사용됩니다.
*   **`feature_names=feature_names`**
    *   **역할:** 그래프의 Y축에 표시될 **특성(변수)들의 이름**을 지정합니다.
    *   **의미:** 컴퓨터가 알아보기 힘든 컬럼 번호(0, 1, 2...) 대신 `['나이', '소득', '직업']` 같은 사람이 읽기 편한 실제 변수 이름으로 바꿔서 보여줍니다.
*   **`show=False`**
    *   **역할:** 그래프를 **즉시 화면에 출력할지 여부**를 결정합니다.
    *   **의미:** `False`로 설정하면 화면에 바로 띄우지 않고 대기시킵니다. 이 설정을 통해 나중에 `plt.title()`로 제목을 넣거나, `plt.savefig()`로 이미지를 파일로 저장하는 등 **추가적인 커스텀 작업**을 한 뒤에 마지막에 출력(`plt.show()`)할 수 있어 실무에서 매우 유용하게 쓰입니다.

---

### 3. 📤 반환값/할당 변수

*   **반환값 없음 (`None`)**
    *   이 함수는 파이썬 변수에 어떤 데이터를 돌려주는(Return) 함수가 **아닙니다.**
    *   대신 화면(Matplotlib 캔버스)에 그림(Plot)을 그리고 끝내는 역할을 하므로, `result = shap.summary_plot(...)`처럼 변수에 담아 사용할 필요가 없습니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 이해할 수 있도록, 데이터 생성부터 그래프 출력까지 이어지는 **최소한의 실행 코드 예시**를 준비했습니다.

```python
import matplotlib.pyplot as plt
import shap
from sklearn.datasets import make_regression
from xgboost import XGBRegressor

# 1. 간단한 가짜 데이터와 XGBoost 모델 준비
X, y = make_regression(n_samples=100, n_features=3, random_state=42)
feature_names = ["Feature_A", "Feature_B", "Feature_C"]

model = XGBRegressor()
model.fit(X, y)

# 2. SHAP 값 계산 (모델이 어떻게 예측했는지 분석)
explainer = shap.Explainer(model)
shap_values_xgb = explainer(X)

# 3. 질문하신 핵심 코드 실행!
shap.summary_plot(shap_values_xgb, X, feature_names=feature_names, show=False)

# 4. 추가 커스텀 및 화면 출력
plt.title("My First SHAP Summary Plot", fontsize=14)
plt.show()  # 화면에 그래프 띄우기
```

**💡 이 코드를 실행하면 나오는 예상 결과:**
*   세로축에는 `Feature_A`, `Feature_B`, `Feature_C`가 중요도 순서대로 위에서부터 정렬됩니다.
*   가로축에는 SHAP 값이 나타나며, 우측으로 갈수록 예측값을 높이는 데 기여한 것, 좌측으로 갈수록 낮추는 데 기여한 것을 뜻합니다.
*   점들의 색상(빨강/파랑)을 통해 실제 특성 값의 크기가 높았는지 낮았는지를 직관적으로 파악할 수 있습니다.