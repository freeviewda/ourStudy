# sns.heatmap - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:31:39

---

파이썬 데이터 분석에서 널리 쓰이는 `seaborn` 라이브러리의 `sns.heatmap` 함수에 대한 상세 해설입니다. 초보자분들도 쉽게 이해하실 수 있도록 차근차근 설명해 드릴게요!

---

### 1. 📌 함수 개요
`sns.heatmap`은 **숫자 데이터의 크기에 따라 색상을 달리하여 2차원 표(Matrix) 형태로 시각화해 주는 함수**입니다. 데이터의 패턴이나 상관관계, 성능 비교 등을 한눈에 파악할 수 있도록 마치 '열화상 카메라'처럼 색상으로 표현해 줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에 사용된 6가지 인자의 역할과 설정된 값의 의미는 다음과 같습니다.

*   **`heatmap_data[['Baseline', 'GridSearch', 'RandomSearch']]`**
    *   **역할:** 시각화할 원본 데이터(DataFrame)에서 특정 열(Column)들만 골라내어 전달합니다.
    *   **의미:** 여기서는 모델 성능을 비교하는 세 가지 방법(`Baseline`, `GridSearch`, `RandomSearch`)에 해당하는 데이터만 뽑아서 히트맵을 그리겠다는 뜻입니다.
*   **`annot=True`**
    *   **역할:** 셀(Cell) 안에 실제 데이터 값을 글자로 표시할지 여부를 결정합니다.
    *   **의미:** `True`로 설정했기 때문에, 색상만 채워지는 것이 아니라 각 칸마다 정확한 숫자 값이 함께 표시되어 가독성이 좋아집니다.
*   **`fmt='.4f'`**
    *   **역할:** `annot=True`에 의해 표시되는 숫자 데이터의 형식을 지정합니다.
    *   **의미:** `'.4f'`는 소수점 아래 **넷째 자리**까지 반올림하여 실수(float) 형태로 보여달라는 뜻입니다. (예: `0.852312` ➡️ `0.8523`)
*   **`cmap='YlOrRd'`**
    *   **역할:** 히트맵의 색상 팔레트(Colormap)를 지정합니다.
    *   **의미:** `'YlOrRd'`는 **Yellow(노랑) - Orange(주황) - Red(빨강)**의 조합입니다. **값이 클수록(성능이 좋을수록) 더 진한 빨간색**으로 표현되어 직관적으로 우수한 모델을 찾을 수 있습니다.
*   **`ax=ax1`**
    *   **역할:** 그려질 그래프가 위치할 캔버스(Axes 객체)를 지정합니다.
    *   **의미:** 전체 화면을 여러 개로 쪼개어 쓸 때, 미리 만들어둔 `ax1` 이라는 특정 위치(subplot)에 이 히트맵을 그려넣으라는 뜻입니다.
*   **`cbar_kws={'label': 'Test Accuracy'}`**
    *   **역할:** 색상의 진한 정도를 나타내는 막대기(Colorbar)에 추가적인 설정을 전달합니다.
    *   **의미:** 컬러바 옆에 **'Test Accuracy'(테스트 정확도)** 라는 라벨(이름표)을 붙여서, 이 색상이 무엇을 의미하는지 명확히 알려줍니다.

---

### 3. 📤 반환값/할당 변수

해당 코드는 별도의 변수에 결과를 대입(`ax2 = ...` 등)하지 않고 함수만 단독으로 호출했습니다. 

*   **반환값:** 이 함수는 시각화가 완료된 **Axes 객체(그래프 그림판)**를 반환합니다.
*   **동작 방식:** 반환된 객체는 지정해 둔 `ax1` 공간에 곧바로 그림을 그려 넣는 데 사용되고 소멸합니다. 즉, 추가로 반환값을 받아 활용할 필요가 없을 때 이렇게 단독으로 사용합니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 직접 실행해 볼 수 있는 가장 간단한 형태의 예시 코드입니다.

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. 가상의 성능 데이터 만들기 (DataFrame)
data = {
    "Baseline": [0.7523, 0.6512],
    "GridSearch": [0.8921, 0.8815],
    "RandomSearch": [0.8850, 0.8790],
}
heatmap_data = pd.DataFrame(data, index=["Model_A", "Model_B"])

# 2. 도화지(Figure)와 축(Axes) 만들기
fig, ax1 = plt.subplots(figsize=(6, 4))

# 3. sns.heatmap 실행 (해설한 코드 적용)
sns.heatmap(
    heatmap_data[["Baseline", "GridSearch", "RandomSearch"]],
    annot=True,
    fmt=".4f",
    cmap="YlOrRd",
    ax=ax1,
    cbar_kws={"label": "Test Accuracy"},
)

# 4. 그래프 출력
plt.title("Model Performance Comparison")
plt.show()
```

**💡 예상 결과:**
*   가로축에는 `Baseline`, `GridSearch`, `RandomSearch`가, 세로축에는 `Model_A`, `Model_B`가 배치된 2x3 크기의 표가 나타납니다.
*   각 칸마다 소수점 넷째 자리까지의 정확도 숫자가 적혀 있습니다.
*   숫자가 높을수록(성능이 좋을수록) 붉은색을 띠며, 우측의 컬러바에 "Test Accuracy"라는 설명이 예쁘게 붙어 출력됩니다.