# ax.barh - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 21:53:46

---

파이썬의 데이터 시각화 라이브러리인 Matplotlib에서 사용되는 `ax.barh` 함수에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 쉽고 명쾌하게 정리해 드릴게요!

---

### 1. 📌 함수 개요
`ax.barh()`는 가로 막대 그래프(Horizontal Bar Chart)를 그려주는 함수입니다. 데이터의 항목 이름과 수치 값을 전달하여, 수평 방향으로 길쭉한 막대 그래프를 생성할 때 사용합니다. (세로 막대 그래프를 그리는 `ax.bar()`의 가로 버전이라고 생각하시면 됩니다!)

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `ax.barh(params, values, color='forestgreen')`에서 사용된 세 가지 인자의 역할은 다음과 같습니다.

*   **`params` (첫 번째 위치 인자)**
    *   **역할:** 막대 그래프의 **Y축(세로축)**에 표시될 카테고리(항목) 이름들의 목록입니다.
    *   **의미:** 예를 들어 `['A', 'B', 'C']` 같은 리스트가 들어가며, 위에서 아래 순서로 각 막대의 이름이 됩니다.
*   **`values` (두 번째 위치 인자)**
    *   **역할:** 각 막대의 **길이(수치 값)**를 결정하는 데이터 목록입니다.
    *   **의미:** `params`와 1:1로 매칭되는 숫자 데이터(`[10, 25, 15]` 등)가 들어가며, 숫자가 클수록 막대가 오른쪽으로 길어집니다.
*   **`color='forestgreen'` (키워드 인자)**
    *   **역할:** 막대의 내부 색상을 지정합니다.
    *   **의미:** `'forestgreen'`은 싱그러운 짙은 숲속의 초록색(Forest Green)을 의미합니다. 이 값을 바꾸어 그래프의 분위기를 다채롭게 꾸밀 수 있습니다.

---

### 3. 📤 반환값/할당 변수
질문하신 코드 스니펫(`ax.barh(params, values, color='forestgreen')`) 단독으로는 반환값을 별도의 변수에 저장(할당)하고 있지 않습니다. 

*   **반환값:** 이 함수는 그려진 막대들의 정보가 담긴 **`BarContainer` 객체**를 반환합니다.
*   **활용법:** 만약 막대의 투명도를 조절하거나 추가 설정을 하고 싶다면 다음과 같이 변수에 담아 사용할 수도 있습니다.
    ```python
    bars = ax.barh(params, values, color='forestgreen')
    ```
    하지만 단순 시각화 목적이라면 변수에 담지 않고 그냥 함수만 호출해도 그래프가 화면에 잘 그려집니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 Jupyter Notebook이나 파이썬 파일에서 직접 복사해서 실행해 볼 수 있는 가장 간단한 전체 코드 예시입니다.

```python
import matplotlib.pyplot as plt

# 1. 도화지(fig)와 축(ax) 만들기
fig, ax = plt.subplots()

# 2. 데이터 준비
params = ['Python', 'Java', 'C++', 'HTML']
values = [85, 60, 45, 70]

# 3. 가로 막대 그래프 그리기 (오늘의 핵심 함수!)
ax.barh(params, values, color='forestgreen')

# 4. 그래프 제목과 축 이름 달기
ax.set_title('Programming Language Popularity')
ax.set_xlabel('Score')
ax.set_ylabel('Languages')

# 5. 화면에 보여주기
plt.show()
```

**🎯 예상 결과:**
Y축에는 'Python', 'Java', 'C++', 'HTML'이 아래부터 위로 예쁘게 적히고, X축의 수치에 맞춰 오른쪽으로 뻗어나가는 **초록색(forestgreen) 가로 막대 그래프**가 짠 하고 나타납니다!