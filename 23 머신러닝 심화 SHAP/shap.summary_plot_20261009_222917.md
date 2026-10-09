# shap.summary_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:29:17

---

파이썬 머신러닝 해석 라이브러리인 `shap`에서 가장 많이 쓰이는 핵심 함수 중 하나인 `shap.summary_plot`에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 하나씩 쉽게 풀어드릴게요!

---

### 1. 📌 함수 개요
`shap.summary_plot`은 **머신러닝 모델이 예측을 내릴 때, 각 데이터 특성(Feature)들이 얼마나 큰 영향을 미쳤는지 한눈에 보여주는 요약 그래프**를 그려주는 함수입니다. 모델의 '전체적인 중요도'와 '특성값이 높고 낮음에 따라 예측값에 미치는 영향(양(+)의 영향인지 음(-)의 영향인지)'을 동시에 파악할 수 있습니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `shap.summary_plot(shap_values_cat, X_test, feature_names=feature_names, show=False)`에 사용된 4가지 인자의 역할은 다음과 같습니다.

*   **`shap_values_cat` (첫 번째 위치 인자)**
    *   **역할:** 모델이 예측할 때 사용한 **SHAP 값(기여도)** 데이터입니다.
    *   **의미:** 각 데이터 샘플마다 어떤 특성이 모델의 예측 결과에 얼마만큼의 플러스(+) 혹은 마이너스(-) 영향을 주었는지 계산된 수치들의 모음입니다.
*   **`X_test` (두 번째 위치 인자)**
    *   **역할:** 모델을 평가하거나 테스트할 때 사용한 **원본 테스트 데이터(특성 값들)**입니다.
    *   **의미:** 그래프를 그릴 때, 실제 특성 값의 크기(예: 나이가 많고 적음, 소득이 높고 낮음 등)를 색상(빨강/파랑)으로 표현하기 위해 함께 전달합니다.
*   **`feature_names=feature_names`**
    *   **역할:** 그래프의 Y축에 표시될 **특성(변수)들의 이름**을 지정합니다.
    *   **의미:** 보통 `X_test`의 컬럼 이름 리스트(`X_test.columns`)를 전달하여, 컴퓨터가 이해하는 숫자 인덱스 대신 사람이 읽기 쉬운 변수명(예: '연령', '소득' 등)으로 그래프를 표시하게 만듭니다.
*   **`show=False`**
    *   **역할:** 그래프를 **즉시 화면에 출력(가시화)할지 여부**를 결정합니다.
    *   **의미:** `False`로 설정하면 그래프를 바로 띄우지 않고 메모리에 저장해 둡니다. 이를 통해 나중에 `matplotlib.pyplot.show()`를 호출하거나, 그래프를 이미지 파일로 저장(`plt.savefig()`)하는 등의 추가적인 커스텀(제목 추가, 사이즈 조절 등)을 할 수 있습니다.

---

### 3. 📤 반환값/할당 변수
*   **반환값 없음 (`None`)**
    *   이 함수는 별도의 데이터를 초록색 변수나 결과값으로 반환하지 않습니다.
    *   대신 화면(또는 메모리)에 **시각화 그래프 객체(Plot)**를 생성하는 역할을 수행하므로, 코드를 작성할 때 앞에 `변수 = ` 형태의 할당 코드를 붙이지 않고 함수만 단독으로 호출합니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 전체 흐름을 이해할 수 있도록, SHAP 라이브러리를 임포트하고 위 함수를 활용하는 전체적인 미니 예시 코드를 준비했습니다.

**[간단 실행 예시 코드]**
```python
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 1. 데이터 로드 및 분할
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, random_state=42
)
feature_names = iris.feature_names

# 2. 머신러닝 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 3. SHAP 값 계산
explainer = shap.TreeExplainer(model)
shap_values_cat = explainer.shap_values(X_test)

# 4. summary_plot 함수 호출 (질문하신 바로 그 코드!)
shap.summary_plot(shap_values_cat[0], X_test, feature_names=feature_names, show=False)

# 5. 그래프 꾸미기 및 출력
plt.title("My First SHAP Summary Plot")
plt.show()
```

**💡 예상 결과:**
*   화면에 알록달록한 가로 막대 형태의 점들이 찍힌 그래프가 나타납니다.
*   위쪽에 있는 특성일수록 모델 예측에 가장 중요한 역할을 한 변수이며, 점들의 색상(빨강/파랑)을 통해 해당 값이 클수록 예측값에 어떤 영향을 주는지 직관적으로 알 수 있게 됩니다.