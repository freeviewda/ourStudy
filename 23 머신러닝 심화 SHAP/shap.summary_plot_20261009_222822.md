# shap.summary_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:28:22

---

안녕하세요! 파이썬의 머신러닝 해석 라이브러리인 **SHAP**에서 가장 많이 쓰이는 핵심 함수, `shap.summary_plot`에 대해 초보자 눈높이에 맞춰 아주 쉽게 정리해 드릴게요.

---

### 1. 📌 함수 개요
`shap.summary_plot`은 **인공지능(머신러닝) 모델이 어떤 기준으로 예측을 내렸는지 한눈에 보여주는 시각화 함수**입니다. 각 변수(특성)가 모델의 예측 결과에 얼마나, 그리고 어떤 방향(긍정적/부정적)으로 영향을 주었는지 '벌집 모양(beeswarm) 플롯'이나 '막대 그래프' 형태로 큼직하게 그려줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `shap.summary_plot(shap_values_lgbm, X_test, feature_names=feature_names, show=False)`에 사용된 4가지 인자의 역할은 다음과 같습니다.

*   **`shap_values_lgbm` (첫 번째 위치 인자)**
    *   **역할:** LightGBM 모델이 예측할 때 사용한 **SHAP 값(기여도)** 데이터입니다.
    *   **의미:** 각 데이터(행)마다 어떤 변수가 예측값에 얼만큼의 영향(플러스(+) 또는 마이너스(-))을 주었는지 계산된 수치들의 모음입니다.
*   **`X_test` (두 번째 위치 인자)**
    *   **역할:** 모델 성능을 평가하기 위해 남겨둔 **테스트 데이터셋**입니다.
    *   **의미:** 그래프를 그릴 때, 실제 변수들의 값(예: 나이가 30살인지, 소득이 얼마인지 등)이 높고 낮음을 색상으로 표현하기 위해 함께 전달합니다.
*   **`feature_names=feature_names`**
    *   **역할:** 그래프의 Y축에 표시될 **변수들의 이름(라벨)**을 지정합니다.
    *   **의미:** 컴퓨터가 이해하는 변수 번호(0, 1, 2...) 대신, 사람이 읽기 쉬운 실제 이름(예: '나이', '연봉', '구매 횟수')으로 변환하여 그래프를 보기 편하게 만들어 줍니다.
*   **`show=False`**
    *   **역할:** 그래프를 **즉시 화면에 띄우지 않고 대기**시키는 설정입니다.
    *   **의미:** 이 값을 `False`로 주면, 바로 화면에 출력되는 대신 파이썬 메모리(Matplotlib 객체)에 저장됩니다. 덕분에 나중에 그래프에 제목을 추가하거나, 이미지 파일로 저장(`plt.savefig()`)하는 등의 추가 작업을 할 수 있게 됩니다.

---

### 3. 📤 반환값/할당 변수
*   **반환값 없음 (`None`)**
    *   이 함수는 별도의 데이터를 계산해서 돌려주는(return) 함수가 아닙니다. 오직 **시각화 그림(Plot)을 생성**하는 역할만 수행합니다. 따라서 변수에 따로 결과값을 대입(`result = shap.summary_plot(...)`)할 필요가 없습니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 전체 흐름을 이해할 수 있도록 LightGBM과 SHAP을 함께 사용하는 간단한 전체 코드를 준비했습니다.

```python
import lightgbm as lgb
import shap
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1. 데이터 준비
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, random_state=42
)
feature_names = data.feature_names

# 2. 모델 학습 (LightGBM)
model = lgb.LGBMClassifier(random_state=42)
model.fit(X_train, y_train)

# 3. SHAP 값 계산
explainer = shap.TreeExplainer(model)
shap_values_lgbm = explainer.shap_values(X_test)

# 4. summary_plot 함수 호출 (질문하신 코드!)
shap.summary_plot(
    shap_values_lgbm, X_test, feature_names=feature_names, show=False
)

# 5. 화면에 예쁘게 출력하기
plt.title("My SHAP Summary Plot", fontsize=16)  # 제목 추가 가능 (show=False 덕분!)
plt.show()
```

💡 **예상 결과:** 
화면에 알록달록한 점들로 이루어진 그래프가 나타납니다. 
*   **Y축**에는 중요한 변수들이 위에서부터 순서대로 나열됩니다.
*   **X축**은 예측에 미친 영향력(오른쪽일수록 정답에 큰 양(+)의 영향, 왼쪽일수록 음(-)의 영향)을 보여줍니다.
*   **색상**은 변수의 실제 값(빨간색: 높음, 파란색: 낮음)을 의미하여, "이 변수가 높을수록 모델이 정답으로 예측하는구나!"를 직관적으로 알 수 있습니다.