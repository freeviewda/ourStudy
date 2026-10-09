# shap.waterfall_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 23:08:57

---

파이썬의 머신러닝 해석 라이브러리인 `SHAP`에서 사용되는 `shap.waterfall_plot` 함수에 대한 상세 해설입니다. 초보자분들도 쉽게 이해하실 수 있도록 단계별로 나누어 설명해 드릴게요!

---

### 1. 📌 함수 개요
`shap.waterfall_plot`은 **"AI(머신러닝) 모델이 왜 그런 예측을 했는지 그 이유를 폭포수(Waterfall) 모양의 그래프로 시각화해 주는 함수"**입니다. 
기본 예측값(시작점)에서부터 시작하여, 각 피처(특성)들이 예측값에 긍정적(+) 혹은 부정적(-)으로 기여한 양을 더하고 빼면서 최종 예측값에 도달하는 과정을 직관적으로 보여줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

이 코드는 크게 보면 `shap.waterfall_plot()`이라는 시각화 함수 안에, 그래프를 그리기 위한 데이터 묶음인 `shap.Explanation()` 객체를 통째로 만들어 전달하고 있습니다. 하나씩 뜯어볼까요?

#### ① `shap.Explanation(...)` (데이터 묶음)
그래프를 그리기 위한 모든 재료를 담아두는 상자입니다. 이 안에는 다음과 같은 재료들이 들어갑니다.

*   **`values=shap_values_plot[idx][:, 1]`**
    *   **역할:** 각 피처(특성)가 모델의 예측 결과에 얼마나 영향을 미쳤는지 나타내는 값(SHAP 값)입니다.
    *   **의미:** `idx`번째 데이터 한 개의 예측 결과에 대해, 이진 분류(0 또는 1) 중 **1번 클래스(주로 관심 있는 타겟)**에 영향을 준 SHAP 값들만 쏙 빼내어 사용하겠다는 뜻입니다.
*   **`base_values=base_value[1]`**
    *   **역할:** 모델이 피처들을 보기 전에 가지고 있던 기본 예측값(Baseline)입니다.
    *   **의미:** 모든 데이터들의 평균적인 예측값으로, 폭포수 그래프가 맨 처음 시작하는 기준점이 됩니다.
*   **`data=X_test_reset.iloc[idx].values`**
    *   **역할:** 실제 관측치(데이터)의 원본 값들입니다.
    *   **의미:** 테스트 데이터셋(`X_test_reset`)에서 `idx`번째 행에 해당하는 실제 값들(예: 나이=30, 연봉=5000 등)을 가져와 그래프의 피처 이름 옆에 같이 띄워줍니다.
*   **`feature_names=X.columns.tolist()`**
    *   **역할:** 피처(변수)들의 이름 목록입니다.
    *   **의미:** 데이터의 각 열(Column) 이름(예: 'age', 'income' 등)을 리스트 형태로 가져와 그래프의 Y축에 레이블로 표시합니다.

#### ② `show=True` (`shap.waterfall_plot`의 인자)
*   **역할:** 그래프를 화면에 바로 출력할지 여부입니다.
*   **의미:** `True`로 설정되어 있으므로, 코드가 실행되는 즉시 matplotlib을 통해 폭포수 그래프 화면이 팝업창이나 주피터 노트북에 나타납니다.

---

### 3. 📤 반환값/할당 변수

*   **반환값 없음 (`None`)**
*   이 함수는 별도의 데이터를 계산해서 돌려주는 함수가 아니라, **시각화 그림(그래프)을 그려서 화면에 보여주는 역할**만 합니다. 따라서 `=` 기호로 결과를 변수에 담아두는 과정(할당)이 필요 없습니다.

---

### 4. 🎁 요약 및 실행 예시

#### 💡 한눈에 보는 요약
> *"테스트 데이터 중 `idx`번째 사람의 데이터를 가지고, AI가 왜 그런 예측을 내렸는지를 1번 클래스 기준으로 폭포수 그래프를 그려서 화면에 보여줘!"*

#### 🧪 초보자를 위한 간단 실행 예시
실제 SHAP 라이브러리를 임포트하고 이 코드를 실행하는 최소한의 구조는 다음과 같습니다.

```python
import shap
import xgboost
from sklearn.model_selection import train_test_split

# 1. 예제 데이터 및 모델 준비
X, y = shap.datasets.adult()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = xgboost.XGBClassifier().fit(X_train, y_train)

# 2. SHAP 값 계산
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# (참고) 코드에서 사용된 변수 형태 맞추기
shap_values_plot = shap_values
base_value = explainer.expected_value
X_test_reset = X_test.reset_index(drop=True)
idx = 0  # 첫 번째 테스트 데이터

# 3. 폭포수 그래프 그리기 (질문하신 코드 적용)
shap.waterfall_plot(
    shap.Explanation(
        values=shap_values_plot[idx][:, 1],
        base_values=base_value[1],
        data=X_test_reset.iloc[idx].values,
        feature_names=X.columns.tolist()
    ),
    show=True
)
```

**예상 결과:** 
화면에 막대 그래프 형태의 시각화가 나타납니다. 
*   중간의 회색 기준선(`base_value`)에서 출발하여,
*   어떤 특징(예: 자산이 많아서)은 오른쪽(빨간색)으로 값을 밀어 올리고,
*   어떤 특징(예: 부채가 많아서)은 왼쪽(파란색)으로 값을 끌어내리는 과정을 거쳐,
*   최종적인 AI의 예측값에 도달하는 모습을 한눈에 확인할 수 있습니다!