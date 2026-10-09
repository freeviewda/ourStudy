# shap.decision_plot - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:38:10

---

파이썬 머신러닝 해석 라이브러리인 `SHAP`에서 사용되는 `shap.decision_plot` 함수에 대해 초보자의 눈높이에 맞춰 친절하고 명쾌하게 설명해 드리겠습니다.

---

### 1. 📌 함수 개요
`shap.decision_plot`은 **머신러닝 모델이 내린 예측 결과에 각 특성(Feature)들이 어떻게 기여했는지를 꺾은선 그래프(Decision Plot)로 시각화해 주는 함수**입니다. 
기준값(기대값)에서 시작하여 각 특성 값을 거치며 최종 예측값으로 도달하는 과정을 한눈에 보여주어, 모델이 왜 그런 예측을 했는지 직관적으로 이해할 수 있게 도와줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

제공해주신 코드에 사용된 7가지 인자의 역할은 다음과 같습니다.

*   **`explainer_xgb.expected_value`**
    *   **역할:** 그래프의 시작점이 되는 기준값(Base Value 또는 Expected Value)입니다.
    *   **의미:** 모델이 학습한 데이터 전체의 평균적인 예측값으로, 모든 특성 기여도를 더하기 전의 기본 점수입니다.
*   **`shap_values_xgb[selected_samples]`**
    *   **역할:** 시각화할 샘플(데이터)들의 SHAP 값(기여도)입니다.
    *   **의미:** 우리가 선택한 특정 데이터(`selected_samples`)들이 모델의 예측에 각각 어떤 영향을 미쳤는지(증가시켰는지, 감소시켰는지)를 담고 있습니다.
*   **`X_test.iloc[selected_samples]`**
    *   **역할:** 실제 원본 데이터의 특성 값들입니다.
    *   **의미:** 그래프에 마우스를 올리거나(인터랙티브 기능) 할 때, 각 데이터가 실제로 어떤 값(예: 나이=30, 소득=5000 등)을 가지고 있었는지 함께 보여주기 위해 사용됩니다.
*   **`feature_names=feature_names`**
    *   **역할:** 특성(변수)들의 이름 지정입니다.
    *   **의미:** 그래프의 Y축에 "age", "income"처럼 알파벳 코드가 아니라 우리가 알아보기 쉬운 원래 특성 이름으로 표시되도록 합니다.
*   **`show=False`**
    *   **역할:** 그래프의 즉I적 출력 여부 설정입니다.
    *   **의미:** `False`로 설정하면 함수가 곧바로 화면에 그림을 띄우지 않습니다. 대신, 나중에 `plt.show()`를 호출하거나 그래프를 이미지 파일로 저장할 수 있도록 유연성을 줍니다.
*   **`legend_labels=['Positive (1-5)', 'Negative (6-10)']`**
    *   **역할:** 범례(Legend)에 표시될 이름 지정입니다.
    *   **의미:** 여러 개의 샘플을 비교할 때, 각 선이 무엇을 의미하는지 구분하기 쉽도록 사용자가 직접 이름을 붙여주는 것입니다. (예: 1~5점 그룹은 'Positive', 6~10점 그룹은 'Negative'로 표시)
*   **`legend_location='lower right'`**
    *   **역할:** 범례의 위치 설정입니다.
    *   **의미:** 그래프 안에서 범례가 데이터 선들과 겹쳐서 보기 불편하지 않도록 우측 하단(`lower right`) 빈 공간에 배치합니다.

---

### 3. 📤 반환값/할당 변수

*   **반환값 없음 (None)**
    *   이 함수는 별도의 데이터를 리턴(`return`)하지 않습니다. 
    *   대신 내부적으로 Matplotlib 기반의 시각화 객체를 생성하여 그림(Plot)을 그려주는 역할만 수행합니다. 따라서 반환값을 받을 변수(`result = ...`)를 앞에 지정할 필요가 없습니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름 속에서 이 코드를 어떻게 활용하는지 간단한 뼈대 코드로 살펴보겠습니다.

```python
import shap
import matplotlib.pyplot as plt
# (가정) 이미 모델(explainer_xgb), SHAP 값(shap_values_xgb), 테스트 데이터(X_test)가 준비되어 있음

selected_samples = [0, 1]  # 테스트 데이터 중 0번, 1번 환자(샘플)를 선택
feature_names = X_test.columns.tolist()

# 1. Decision Plot 그리기
shap.decision_plot(
    explainer_xgb.expected_value,
    shap_values_xgb[selected_samples],
    X_test.iloc[selected_samples],
    feature_names=feature_names,
    show=False,                               # 바로 출력하지 않고 설정을 유지
    legend_labels=['Patient A', 'Patient B'], # 샘플별 이름표
    legend_location='lower right'             # 범례 위치
)

# 2. 화면에 출력하기 (show=False를 썼기 때문에 plt.show()를 호출해 줌)
plt.title("XGBoost Model Decision Plot")
plt.show()
```

**💡 한 줄 요약:** 
이 코드는 **"XGBoost 모델이 특정 환자들(`selected_samples`)의 결과를 예측할 때, 어떤 요인들이 긍정적 혹은 부정적으로 작용했는지를 알기 쉽게 우측 하단에 범례를 포함한 하나의 꺾은선 그래프로 그려줘!"** 라는 뜻입니다.