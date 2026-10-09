# ax.set_xticklabels - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 23:13:22

---

파이썬의 데이터 시각화 라이브러리인 **Matplotlib**에서 그래프를 그릴 때 자주 사용하는 `ax.set_xticklabels` 함수에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 하나씩 친절하게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`ax.set_xticklabels()`는 **그래프의 X축 눈금(Ticks)에 표시되는 텍스트(이름)를 사용자가 원하는 텍스트로 지정(변경)**하는 함수입니다. 주로 막대그래프나 선그래프에서 데이터 카테고리의 이름을 보기 좋게 바꾸거나 회전시킬 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `ax.set_xticklabels(summary_df['Model'], rotation=45, ha='right')`에 사용된 3가지 인자의 역할은 다음과 같습니다.

*   **`summary_df['Model']` (첫 번째 위치 인자)**
    *   **역할:** X축 눈금에 실제로 출력할 텍스트들의 모음입니다.
    *   **의미:** Pandas 데이터프레임(`summary_df`)의 'Model' 열(Column)에 들어있는 모델 이름들(예: 'LinearRegression', 'RandomForest' 등)을 가져와서 X축 아래에 하나씩 이름표로 붙여줍니다.
*   **`rotation=45`**
    *   **역할:** 글자의 회전 각도를 설정합니다.
    *   **의미:** 글자를 시계 반대 방향으로 **45도 기울여서** 출력합니다. 모델 이름이 길면 서로 겹치기 때문에, 이렇게 비스듬히 눕혀주면 훨씬 읽기 편해집니다.
*   **`ha='right'`**
    *   **역할:** 수평 정렬(Horizontal Alignment) 방식을 설정합니다.
    *   **의미:** 글자를 45도 회전시켰을 때, 글자의 **오른쪽 끝(right)**을 기준으로 X축 눈금 위치에 딱 맞게 정렬합니다. 이렇게 하면 글자가 눈금 선에 예쁘게 걸쳐지어 시각적으로 깔끔해집니다. *(보통 `rotation`을 사용할 때 짝꿍처럼 함께 쓰입니다.)*

---

### 3. 📤 반환값/할당 변수
*   **반환값:** 이 함수는 지정된 텍스트 객체들의 리스트(Text objects list)를 반환합니다.
*   **할당 여부:** 제시된 코드에서는 반환값을 별도의 변수에 저장하지 않고(`= 기호 없음`), 함수를 실행하는 자체로 끝냈습니다. Matplotlib에서는 이렇게 시각화 요소를 설정만 하고 반환값을 받지 않는 경우가 매우 흔합니다.

---

### 4. 🎁 요약 및 실행 예시
백문이 불여일견! 아래의 간단한 코드를 복사해서 직접 실행해 보세요. 글자가 겹쳐서 보기 불편할 때 `set_xticklabels`가 얼마나 유용한지 바로 체감할 수 있습니다.

**[실습 코드]**
```python
import matplotlib.pyplot as plt
import pandas as pd

# 1. 테스트용 데이터프레임 만들기
data = {
    'Model': [
        'Logistic Regression',
        'Random Forest Classifier',
        'Support Vector Machine',
        'Gradient Boosting',
    ],
    'Accuracy': [0.85, 0.92, 0.88, 0.94],
}
summary_df = pd.DataFrame(data)

# 2. 그래프 그리기 기본 설정
fig, ax = plt.subplots(figsize=(8, 5))

# 막대그래프 생성 (X축은 숫자로 자동 지정됨)
ax.bar(summary_df['Model'], summary_df['Accuracy'])

# 3. ★오늘 배운 핵심 함수 적용!★
# X축 눈금 이름을 'Model' 열의 값으로 바꾸고, 45도 회전하여 오른쪽 정렬
ax.set_xticklabels(summary_df['Model'], rotation=45, ha='right')

# 그래프 제목 및 여백 조정
ax.set_title('Model Accuracy Comparison')
plt.tight_layout()  # 글자가 잘리지 않도록 여백 자동 조절

# 4. 그래프 출력
plt.show()
```

**[예상 결과]**
막대그래프 아래의 X축 이름들이 가로로 길게 늘어져 서로 겹치는 대신, **오른쪽으로 45도 예쁘게 기울어진 상태**로 출력되어 누구나 한눈에 어떤 모델인지 알아볼 수 있게 됩니다!