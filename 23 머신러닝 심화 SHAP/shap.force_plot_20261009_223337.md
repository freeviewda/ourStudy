# shap.force_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:33:37

---

파이썬의 머신러닝 해석 라이브러리인 **SHAP**에서 사용되는 `shap.force_plot` 함수에 대한 상세 해설입니다. 초보자분들도 이해하기 쉽도록 항목별로 나누어 설명해 드릴게요!

---

### 1. 📌 함수 개요
`shap.force_plot`은 **"특정 데이터 하나(단일 샘플)가 모델에 의해 왜 그런 예측값을 갖게 되었는지"**를 시각적으로 보여주는 강력한 도구입니다. 마치 줄다리기처럼, 어떤 특성(Feature)이 예측값을 '끌어올렸는지(양수)' 혹은 '끌어내렸는지(음수)'를 빨간색과 파란색 막대 그래프로 한눈에 보여줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에 사용된 5가지 인자의 역할과 의미는 다음과 같습니다:

*   **`explainer_xgb.expected_value`**
    *   **역할:** 모델의 **기준값(Base Value 또는 Expected Value)**입니다.
    *   **의미:** 모델이 학습한 전체 데이터셋에 대한 평균적인 예측값입니다. 즉, 어떤 특성 정보도 고려하지 않았을 때 모델이 기본적으로 뱉어내는 출발선 점수라고 생각하면 됩니다.
*   **`shap_values_xgb[sample_idx]`**
    *   **역할:** 특정 샘플의 **SHAP 값(기여도)**입니다.
    *   **의미:** `sample_idx`번째 데이터의 각 특성들이 모델의 예측값에 얼마나 긍정적(+) 혹은 부정적(-) 영향을 주었는지를 담은 수치들의 모음입니다.
*   **`X_test.iloc[sample_idx]`**
    *   **역할:** 실제 **특성(Feature)들의 원본 값**입니다.
    *   **의미:** 테스트 데이터셋(`X_test`) 중에서 `sample_idx`번째에 해당하는 실제 데이터(예: 나이가 30세, 연봉이 5천만 원 등)입니다. 이 값들은 그래프 위에 마우스를 올리거나 텍스트로 함께 표시되어, "어떤 실제 값 때문에 이런 기여도가 생겼는지"를 알 수 있게 해줍니다.
*   **`matplotlib=True`**
    *   **역할:** 출력 형식을 지정하는 인자입니다.
    *   **의미:** `True`로 설정하면 웹 기반의 인터랙티브(동적) HTML 형식 대신, 파이썬의 표준 시각화 라이브러리인 **Matplotlib 그림(Static Plot)** 형태로 그래프를 그려줍니다. 주피터 노트북이나 일반 스크립트에서 이미지로 저장하거나 바로 띄워볼 때 유용합니다.
*   **`show=False`**
    *   **역할:** 그래프 출력 제어 인자입니다.
    *   **의미:** `True`로 두면 함수가 실행되는 즉시 화면에 그래프가 그려지고 코드가 멈출 수 있습니다. `False`로 설정하면 **"지금 당장 화면에 띄우지 말고 메모리에만 그려놔"**라는 뜻이 되어, 이후에 `plt.show()`를 호출하거나 그래프를 이미지 파일로 저장(`plt.savefig()`)하는 등의 추가 작업을 자유롭게 할 수 있습니다.

---

### 3. 📤 반환값/할당 변수

*   **별도의 변수 할당이 없는 이유:**
    *   제시해주신 코드에는 함수 앞에 `=` 기호(변수 할당)가 없습니다. 즉, 어떤 데이터를 반환받아 변수에 저장하는 것이 아니라, **함수 자체의 부수 효과(Side Effect)로 Matplotlib 그림 객체를 생성하여 메모리에 올리는 역할**만 수행합니다.
    *   이후 보통 바로 밑 줄에서 `plt.tight_layout()`, `plt.savefig('파일명.png')`, 혹은 `plt.show()`와 함께 사용됩니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 파악할 수 있도록, 위 코드가 포함된 간단한 실행 예시 코드를 보여드립니다.

```python
import shap
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 1. 간단한 데이터 및 XGBoost 모델 준비 (예시)
X, y = shap.datasets.adult()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = xgb.XGBClassifier().fit(X_train, y_train)

# 2. SHAP Explainer 생성 및 값 계산
explainer_xgb = shap.Explainer(model, X_train)
shap_values_xgb = explainer_xgb(X_test)

# 3. 분석할 샘플 지정 (예: 테스트 데이터의 첫 번째 사람)
sample_idx = 0

# 4. Force Plot 그리기 (질문하신 코드!)
shap.force_plot(
    explainer_xgb.expected_value,
    shap_values_xgb[sample_idx],
    X_test.iloc[sample_idx],
    matplotlib=True,
    show=False,
)

# 5. 화면에 출력하기
plt.title("XGBoost Model Force Plot")
plt.show()
```

**💡 예상 결과:**
화면에 가로로 긴 막대 그래프가 나타납니다. 
*   기준값(Base Value)에서 시작하여, 
*   어떤 특성(예: 자산이 많음, 교육 수준이 높음 등)은 **빨간색**으로 밀어 올려 최종 예측값을 만들고,
*   어떤 특성(예: 직업군 등)은 **파란색**으로 끌어내려 최종 예측값을 완성했는지 한눈에 확인할 수 있습니다!