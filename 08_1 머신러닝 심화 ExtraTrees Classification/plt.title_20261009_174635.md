# plt.title - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 17:46:35

---

파이썬의 데이터 시각화 라이브러리인 **Matplotlib**에서 사용되는 `plt.title` 함수에 대한 상세 해설입니다. 초보자분들도 쉽게 이해하실 수 있도록 항목별로 친절하게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`plt.title()` 함수는 **현재 그려지고 있는 그래프의 상단 중앙에 제목(Title)을 달아주는 함수**입니다. 그래프가 무엇을 나타내는지 보는 사람이 직관적으로 알 수 있도록 설명 문구를 추가할 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `plt.title("Feature Importances (Random Forest Classifier)")`에서 전달된 인자는 다음과 같습니다.

*   **`"Feature Importances (Random Forest Classifier)"` (문자열, Positional Argument)**
    *   **역할:** 그래프의 제목으로 표시될 텍스트를 전달합니다.
    *   **설정된 값의 의미:** 
        *   `Feature Importances`: 직역하면 '특성 중요도'라는 뜻으로, 머신러닝 모델이 예측을 할 때 어떤 데이터(특성)를 가장 중요하게 여겼는지를 보여주는 그래프임을 나타냅니다.
        *   `(Random Forest Classifier)`: 이 중요도를 계산해낸 머신러닝 알고리즘의 이름이 '랜덤 포레스트 분류기'라는 것을 명시하고 있습니다.

*(참고: 이 외에도 글자 크기를 키우는 `fontsize`, 글자 색상을 바꾸는 `color`, 위치를 조정하는 `loc` 등 다양한 추가 인자를 넣을 수 있지만, 위 코드에서는 가장 기본이 되는 제목 텍스트만 전달되었습니다.)*

---

### 3. 📤 반환값/할당 변수
*   **반환값:** `plt.title()` 함수는 제목에 해당하는 텍스트 객체(`matplotlib.text.Text`)를 반환합니다.
*   **할당 변수:** 위 코드에서는 별도의 변수에 저장(`title_obj = plt.title(...)`)하지 않고 **함수만 단독으로 호출**했습니다. 
    *   이처럼 파이썬에서는 반환값을 꼭 변수에 담지 않고 그냥 실행만 해도, Matplotlib 내부에서 현재 그림(Figure)에 자동으로 제목을 척! 하고 붙여줍니다.

---

### 4. 🎁 요약 및 실행 예시
백문이 불여일견! 아래의 간단한 코드를 복사해서 직접 실행해 보세요. 랜덤 포레스트 모델의 특성 중요도를 시각화하고 제목이 어떻게 붙는지 눈으로 확인할 수 있습니다.

**[실행 코드]**
```python
import matplotlib.pyplot as plt

# 1. 예시 데이터 (특성 이름과 중요도 점수)
features = ['Age', 'Salary', 'Credit Score', 'Gender']
importance = [0.45, 0.30, 0.15, 0.10]

# 2. 막대 그래프 그리기
plt.bar(features, importance, color='skyblue')

# 3. 🌟 오늘의 주인공 함수 사용! (그래프 제목 달기)
plt.title("Feature Importances (Random Forest Classifier)")

# 4. 축 이름 달기
plt.xlabel("Features")
plt.ylabel("Importance")

# 5. 화면에 그래프 띄우기
plt.show()
```

**[예상 결과]**
*   창이 뜨면서 4개의 막대 그래프가 나타납니다.
*   **그래프 맨 위 중앙**에 깔끔한 글씨로 **"Feature Importances (Random Forest Classifier)"** 라는 제목이 굵게 표시되어, 이 그래프가 어떤 모델의 결과인지 누구나 한눈에 알아볼 수 있게 됩니다.