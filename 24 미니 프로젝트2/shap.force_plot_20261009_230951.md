# shap.force_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 23:09:51

---

파이썬의 머신러닝 해석 라이브러리인 `SHAP`에서 사용되는 `shap.force_plot` 함수에 대한 상세 해설입니다. 초보자분들도 쉽게 이해하실 수 있도록 차근차근 설명해 드릴게요!

---

### 1. 📌 함수 개요
`shap.force_plot`은 **머신러닝 모델이 왜(Why) 그런 예측을 했는지 그 과정을 시각적으로 보여주는 함수**입니다. 
마치 줄다리기처럼, 어떤 특성(Feature)이 모델의 예측값을 '높이는 데(긍정적 영향)' 기여했는지, 반대로 '낮추는 데(부정적 영향)' 기여했는지를 1차원 그래프(Force Plot)로 한눈에 보여줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드에서 사용된 5가지 인자의 역할은 다음과 같습니다.

*   **`base_value[1]`**
    *   **역할:** 모델이 예측할 때 기준으로 삼는 '기본값(Base Value 또는 Expected Value)'입니다.
    *   **설명:** 전체 데이터셋에 대한 모델의 평균 예측값입니다. 여기서 `[1]`을 붙인 것은 이진 분류(Binary Classification) 문제에서 '1(양성/True)' 클래스에 해당하는 기준값을 선택하겠다는 뜻입니다.
*   **`shap_values_plot[idx][:, 1]`**
    *   **역할:** 특정 데이터(`idx`번째)의 각 특성들이 예측에 기여한 SHAP 값(기여도)들입니다.
    *   **설명:** 모델의 예측값에서 기본값(Base Value)을 제외하고, **각각의 특성(나이, 소득 등)이 예측 결과에 얼마나 밀고 당겼는지**를 나타냅니다. 역시 `[1]`을 통해 1번 클래스에 대한 기여도를 선택했습니다.
*   **`X_test_reset.iloc[idx]`**
    *   **역할:** 시각화하려는 **특정 데이터 하나의 실제 입력 값(특성 값들)**입니다.
    *   **설명:** `idx`번째 환자의 나이가 몇 살인지, 소득이 얼마인지 등 실제 데이터의 원본 값을 의미합니다. 마우스를 올렸을 때(인터랙티브 모드일 때) 실제 특성 값을 보여주는 용도로 쓰입니다.
*   **`feature_names=X.columns.tolist()`**
    *   **역할:** 그래프에 표시될 **특성(변수)들의 이름 목록**입니다.
    *   **설명:** 단순히 `[0, 1, 2...]` 같은 숫자 대신 `'연령'`, `'소득'`처럼 사람이 읽을 수 있는 원래 컬럼 이름(`X.columns`)을 리스트(`tolist()`) 형태로 변환하여 그래프에 텍스트로 띄워줍니다.
*   **`matplotlib=False`**
    *   **역할:** 그림을 그릴 때 **맷플롯립(Matplotlib) 엔진을 사용할지 여부**를 결정합니다.
    *   **설명:** `False`로 설정되어 있으므로, 맷플롯립 기반의 정적 이미지가 아니라 웹 브라우저나 주피터 노트북에서 마우스 상호작용이 가능한 **HTML 기반의 인터랙티브 플롯**을 생성하겠다는 의미입니다.

---

### 3. 📤 반환값 및 활용

*   **반환값:** 이 함수는 화면에 그림을 바로 띄워주거나, 주피터 노트북 환경에서 시각화 객체(HTML 형태)를 반환합니다. 
*   **할당 변수:** 제시해주신 코드 단독으로는 별도의 변수에 값을 대입(`변수 = shap.force_plot(...)`)하고 있지 않습니다. 이는 변수에 저장하기보다는 **그 즉시 주피터 노트북 화면에 시각화를 출력**하기 위해 실행하는 전형적인 형태입니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분이 주피터 노트북에서 이 코드를 실행할 때 필요한 전체적인 흐름을 아주 간단한 예시로 보여드릴게요.

```python
import shap
import xgboost
from sklearn.model_selection import train_test_split

# 1. 데이터 및 모델 준비 (예시)
X, y = shap.datasets.adult()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = xgboost.XGBClassifier().fit(X_train, y_train)

# 2. SHAP 값 계산
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# 인덱스 설정 (테스트 데이터 중 첫 번째 사람)
idx = 0 
X_test_reset = X_test.reset_index(drop=True)
base_value = explainer.expected_value
shap_values_plot = shap_values.values

# 3. ★ 질문하신 Force Plot 실행 코드
shap.force_plot(
    base_value[1],                          # 기준값 (평균 예측)
    shap_values_plot[idx][:, 1],            # 이 사람이 예측에 미친 기여도들
    X_test_reset.iloc[idx],                 # 이 사람의 실제 특성값들
    feature_names=X.columns.tolist(),       # 특성 이름들
    matplotlib=False                        # 인터랙티브 웹 화면으로 출력
)
```

**💡 예상 결과:**
주피터 노트북 화면에 빨간색(예측값을 높이는 요인)과 파란색(예측값을 낮추는 요인) 화살표들이 줄다리기하는 형태의 화려하고 직관적인 그래프가 짠 하고 나타납니다. 마우스를 갖다 대면 각 특성의 실제 값과 기여도를 상세히 확인할 수 있습니다!