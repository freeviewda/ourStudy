# plt.title - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 10:32:05

---

파이썬 데이터 분석 및 시각화에서 가장 많이 쓰이는 라이브러리인 **Matplotlib**의 `plt.title` 함수에 대한 상세 해설입니다. 초보자분들도 쉽게 이해하실 수 있도록 차근차근 설명해 드릴게요!

---

### 1. 📌 함수 개요
`plt.title()` 함수는 **현재 그려지고 있는 그래프의 상단 중앙에 제목(Title)을 달아주는 함수**입니다. 그래프가 무엇을 표현하는지 한눈에 알아볼 수 있도록 이름을 붙여줄 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `plt.title("RFECV (Linear SVC): Accuracy vs Number of Features")`에서 전달된 인자를 분석해 보겠습니다.

*   **전달된 인자:** `"RFECV (Linear SVC): Accuracy vs Number of Features"` (문자열 형태)
*   **역할:** 그래프 상단에 표시될 **텍스트 내용**을 지정합니다.
*   **설정된 값의 의미:** 
    *   **RFECV:** '재귀적 특징 제거(Recursive Feature Elimination with Cross-Validation)'라는 머신러닝 기법을 의미합니다.
    *   **(Linear SVC):** 모델로 '선형 서포트 벡터 머신(Linear Support Vector Classifier)'을 사용했음을 뜻합니다.
    *   **Accuracy vs Number of Features:** 이 그래프가 **'특징(변수)의 개수'**에 따른 **'정확도(Accuracy)'**의 변화를 비교하고 있음을 명확하게 설명해 줍니다.

*(참고: 이외에도 글자 크기를 키우는 `fontsize`, 글자 색상을 바꾸는 `color`, 위치를 조정하는 `loc` 등 다양한 추가 인자를 넣을 수 있습니다.)*

---

### 3. 📤 반환값/할당 변수
*   **반환값:** `plt.title()` 함수는 텍스트 객체(`matplotlib.text.Text`)를 반환합니다.
*   **할당 변수:** 위 코드에서는 별도의 변수에 저장(`title_obj = plt.title(...)`)하지 않고, 곧바로 화면에 출력되도록 단독으로 사용되었습니다. 보통 제목은 시각적인 용도로만 쓰이기 때문에 변수에 담아두고 나중에 조작할 일이 많지 않아 이처럼 단독으로 자주 호출합니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들도 직접 복사해서 실행해 볼 수 있는 가장 간단한 전체 코드 예시입니다.

**[실행 코드]**
```python
import matplotlib.pyplot as plt

# 1. 간단한 더미 데이터 준비 (특징 개수와 정확도)
feature_counts = [1, 2, 3, 4, 5]
accuracies = [0.60, 0.75, 0.85, 0.83, 0.80]

# 2. 선 그래프 그리기
plt.plot(feature_counts, accuracies, marker='o')

# 3. 그래프에 제목 달기 (오늘 배운 핵심 함수!)
plt.title("RFECV (Linear SVC): Accuracy vs Number of Features")

# 4. 축 이름 설정
plt.xlabel("Number of Features")
plt.ylabel("Accuracy")

# 5. 화면에 그래프 띄우기
plt.show()
```

**[예상 결과]**
*   창이 하나 뜨면서 꺾은선 그래프가 나타납니다.
*   **그래프 맨 위 중앙**에 딱 하니 `"RFECV (Linear SVC): Accuracy vs Number of Features"`라는 깔끔한 제목이 출력되어, 이 그래프가 어떤 분석 결과를 담고 있는지 누구나 쉽게 이해할 수 있게 됩니다.