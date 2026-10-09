# plt.title - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 19:58:11

---

파이썬 데이터 분석 및 시각화에서 가장 많이 쓰이는 `matplotlib` 라이브러리의 `plt.title` 함수에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 쉽고 명쾌하게 정리해 드릴게요!

---

### 1. 📌 함수 개요
`plt.title()`은 **그려진 그래프의 상단 중앙에 제목(Title)을 달아주는 함수**입니다. 그래프가 무엇을 표현하는지 시각적으로 한눈에 알아볼 수 있도록 이름을 붙여줄 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `plt.title("Feature Importances (CatBoost)")`에서 사용된 인자를 분석해 보겠습니다.

*   **`"Feature Importances (CatBoost)"` (문자열, Positional Argument)**
    *   **역할:** 그래프에 표시될 텍스트 내용입니다.
    *   **설정된 값의 의미:** 
        *   `Feature Importances`: 머신러닝 모델에서 어떤 특성(Feature)이 예측에 가장 중요한 영향을 미쳤는지를 나타내는 **'특성 중요도'**를 의미합니다.
        *   `(CatBoost)`: 이 중요도를 계산한 머신러닝 알고리즘이 **'CatBoost'**라는 것을 명시해 줍니다.
    *   *(참고)* 이 외에도 글자 크기를 키우는 `fontsize=14`, 글자 색상을 바꾸는 `color='blue'`, 위치를 바꾸는 `loc='left'` 등 다양한 추가 인자를 사용할 수 있습니다.

---

### 3. 📤 반환값/할당 변수
*   **반환값:** `plt.title()` 함수는 내부적으로 생성된 텍스트 객체(`matplotlib.text.Text`)를 반환합니다.
*   **할당 여부:** 위 코드처럼 별도의 변수(`title = plt.title(...)`)에 저장하지 않고 단독으로 호출해도 그래프에 제목이 정상적으로 출력됩니다. (필요에 따라 반환된 객체를 이용해 나중에 제목의 속성을 수정할 수도 있습니다.)

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 주피터 노트북이나 파이썬 파일에서 복사해서 바로 실행해 볼 수 있는 가장 간단한 예시 코드입니다.

**[실행 코드]**
```python
import matplotlib.pyplot as plt

# 1. 간단한 막대그래프 데이터 준비
features = ['Age', 'Salary', 'Gender']
importance = [0.45, 0.35, 0.20]

# 2. 막대그래프 그리기
plt.bar(features, importance)

# 3. 그래프 제목 달기 (오늘 배운 함수!)
plt.title("Feature Importances (CatBoost)")

# 4. 화면에 그래프 출력하기
plt.show()
```

**[예상 결과]**
*   가로축에는 'Age, Salary, Gender', 세로축에는 중요도 숫자가 표시된 막대그래프가 나타납니다.
*   **그래프 맨 위 중앙**에 깔끔하게 **`Feature Importances (CatBoost)`**라는 제목이 적혀 있는 것을 확인할 수 있습니다!