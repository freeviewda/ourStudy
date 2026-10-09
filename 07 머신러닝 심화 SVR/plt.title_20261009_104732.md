# plt.title - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 10:47:32

---

파이썬 데이터 시각화의 대표적인 라이브러리인 **Matplotlib**에서 사용하는 `plt.title()` 함수에 대해 초보자의 눈높이에 맞춰 쉽고 명쾌하게 해설해 드릴게요!

---

### 1. 📌 함수 개요
`plt.title()`은 **현재 그려지고 있는 그래프의 상단 중앙에 제목(Title)을 달아주는 함수**입니다. 그래프가 무엇을 표현하는지 한눈에 알아볼 수 있도록 이름을 붙여줄 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제공해주신 코드 `plt.title("RFECV (Linear SVR): Performance vs Number of Features")`에서 전달된 인자의 의미는 다음과 같습니다.

*   **문자열(String) 인자**: `"RFECV (Linear SVR): Performance vs Number of Features"`
    *   **역할**: 그래프의 제목으로 표시될 텍스트를 전달합니다.
    *   **설정값의 의미**: 
        *   `RFECV (Linear SVR)`: **선형 서포트 벡터 회귀(Linear SVR)** 모델과 **재귀적 특성 제거 교차 검증(RFECV)** 기법을 사용해 머신러닝 모델을 학습시켰음을 나타냅니다.
        *   `Performance vs Number of Features`: **특성(변수)의 개수**에 따른 **모델의 성능(Performance)** 변화를 그래프로 시각화했다는 의미입니다.

*(참고: 이외에도 글자 크기를 키우는 `fontsize`, 글자 색상을 바꾸는 `color`, 위치를 조정하는 `loc` 등 다양한 추가 인자를 넣을 수 있습니다.)*

---

### 3. 📤 반환값/할당 변수
*   **반환값**: `plt.title()` 함수는 제목에 해당하는 텍스트 객체(`matplotlib.text.Text`)를 반환합니다.
*   **할당 변수**: 제공해주신 코드에서는 반환값을 별도의 변수(`=`를 사용해)에 저장하지 않고, **함수만 단독으로 호출**했습니다. 이 경우, 제목이 그래프에 곧바로 출력되며 반환값은 화면에 표시되지 않고 조용히 사라집니다. (파이썬에서는 변수에 담지 않아도 화면에 그려지는 데 아무런 문제가 없습니다.)

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 직접 Jupyter Notebook이나 파이썬 파일에서 복사해서 실행해 볼 수 있는 가장 간단한 예시 코드입니다.

**[실행 코드]**
```python
import matplotlib.pyplot as plt

# 1. 간단한 더미 데이터 준비 (X축: 특성 개수, Y축: 성능)
features = [1, 2, 3, 4, 5]
performance = [0.50, 0.75, 0.88, 0.92, 0.90]

# 2. 선 그래프 그리기
plt.plot(features, performance, marker='o')

# 3. 그래프에 제목 달기 (오늘 배운 함수!)
plt.title("RFECV (Linear SVR): Performance vs Number of Features")

# 4. X축, Y축 이름(라벨) 붙이기
plt.xlabel("Number of Features")
plt.ylabel("Performance (Score)")

# 5. 화면에 그래프 출력하기
plt.show()
```

**[예상 결과]**
*   창이 뜨면서 1부터 5까지의 특성 개수에 따른 성능 변화를 나타내는 꺾은선 그래프가 그려집니다.
*   **그래프 맨 위 중앙**에 우리가 설정한 제목인 **"RFECV (Linear SVR): Performance vs Number of Features"**가 깔끔하게 출력되는 것을 확인할 수 있습니다!