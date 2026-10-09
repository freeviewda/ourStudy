# plt.title - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 23:04:58

---

파이썬 머신러닝 및 데이터 시각화에서 가장 많이 쓰이는 `plt.title` 함수에 대한 상세 해설입니다. 초보자분들도 쉽게 이해하실 수 있도록 항목별로 친절하게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`plt.title()`은 파이썬의 시각화 라이브러리인 **Matplotlib(`matplotlib.pyplot`)**에서 현재 그려지고 있는 그래프의 **상단 제목(Title)을 설정**하는 함수입니다. 그래프가 무엇을 나타내는지 한눈에 알아볼 수 있도록 이름을 붙여줄 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `plt.title(f'Feature Importance ({best_model_name})')`에서 괄호 안의 값은 파이썬의 **f-string(포맷 문자열)**을 사용해 만들어진 하나의 문자열입니다.

*   **`f'Feature Importance ({best_model_name})'`**
    *   **역할:** 그래프의 제목으로 표시될 텍스트를 지정합니다.
    *   **설정된 값의 의미:** 
        *   `Feature Importance`: 영어 그대로 **'특성 중요도'**라는 뜻으로, 머신러닝 모델이 예측을 할 때 어떤 데이터(특성)를 가장 중요하게 보았는지를 나타내는 그래프임을 뜻합니다.
        *   `({best_model_name})`: 파이썬 변수(`best_model_name`)에 들어있는 **최고 성능 모델의 이름**을 문자열 안에 쏙 집어넣어 동적으로 제목을 완성합니다. 
        *   *예시:* 만약 `best_model_name` 변수에 `'Random Forest'`가 들어있다면, 최종 그래프 제목은 **`Feature Importance (Random Forest)`**로 예쁘게 출력됩니다.

---

### 3. 📤 반환값/할당 변수
*   **반환값 없음 (None)**
*   `plt.title()` 함수는 별도의 데이터를 반환(return)하여 변수에 저장하는 함수가 아닙니다. 
*   대신, 내부적으로 현재 활성화된 그래프 객체(Axes)의 제목 속성값을 직접 변경한 뒤 작업을 조용히 끝마칩니다. 따라서 `=` 기호를 써서 변수에 결과를 담을 필요가 없습니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 직접 주피터 노트북이나 파이썬 환경에서 복사해서 실행해 볼 수 있는 가장 간단한 전체 코드 예시입니다.

```python
import matplotlib.pyplot as plt

# 1. 최고 성능을 낸 모델의 이름이라고 가정해 봅시다.
best_model_name = 'Random Forest'

# 2. 간단한 막대그래프 그리기 (예시 데이터)
features = ['Age', 'Salary', 'Gender']
importance = [0.5억, 0.3억, 0.2억] # 임의의 중요도 수치
plt.bar(features, [0.5, 0.3, 0.2])

# 3. 오늘의 주인공 함수 사용!
plt.title(f'Feature Importance ({best_model_name})')

# 4. 화면에 그래프 띄우기
plt.show()
```

**🎯 예상 결과:**
그래프가 화면에 나타나며, **그래프 맨 위 중앙**에 다음과 같은 제목이 굵게 표시됩니다.
> **Feature Importance (Random Forest)**