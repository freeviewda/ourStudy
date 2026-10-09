# summary_data.append - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 23:12:10

---

파이썬 코드에서 사용된 **`summary_data.append(...)`** 구문은 머신러닝 모델들의 성능(정확도)을 한눈에 비교하기 위해 데이터를 표(리스트) 형태로 차곡차곡 쌓아두는 과정입니다. 

초보자의 눈높이에 맞춰 하나씩 쉽고 명쾌하게 해설해 드릴게요!

---

### 1. 📌 함수 개요
* **`summary_data`**라는 이름의 빈 리스트(List)에 새로운 요약 정보(딕셔너리 형태)를 **하나의 행(Row)으로 추가**하는 함수입니다.
* 여러 모델(예: Logistic Regression, Random Forest 등)의 성능 결과를 반복문 안에서 차례대로 모을 때 주로 사용됩니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
이 함수의 인자로는 파이썬의 **딕셔너리(Dictionary)** 자료형이 통째로 전달되었습니다. 딕셔너리는 `Key: Value`(이름: 값) 쌍으로 이루어져 있으며, 데이터프레임의 **'열(Column) 이름'과 '그에 들어갈 실제 값'**이 됩니다.

전달된 5가지 데이터를 하나씩 뜯어볼까요?

* **`'Model': name`**
  * **역할:** 현재 평가하고 있는 머신러닝 모델의 이름입니다.
  * **의미:** `name` 변수에 들어 있는 문자열(예: `"RandomForest"`, `"SVM"`)이 모델 이름으로 기록됩니다.

* **`'Base': round(base_acc, 4)`**
  * **역할:** 기본 설정(Default) 상태인 모델의 정확도입니다.
  * **의미:** `base_acc` 소수점 아래 5번째 자리에서 반올림(`round(..., 4)`)하여 소수점 **넷째 자리까지** 깔끔하게 기록합니다.

* **`'GridSearch': round(grid_acc, 4)`**
  * **역할:** GridSearch(일일이 다 해보는 방식)로 최적화한 모델의 정확도입니다.
  * **의미:** `grid_acc` 값을 소수점 넷째 자리까지 반올림하여 기록합니다.

* **`'Optuna': round(optuna_acc, 4)`**
  * **역할:** Optuna(AI를 이용한 최신 하이퍼파라미터튜닝 방식)로 최적화한 모델의 정확도입니다.
  * **의미:** `optuna_acc` 값을 소수점 넷째 자리까지 반올림하여 기록합니다.

* **`'Best': round(max(base_acc, grid_acc, optuna_acc), 4)`**
  * **역할:** 세 가지 방식(`base`, `grid`, `optuna`) 중 **가장 높은(최대값) 정확도**를 찾아냅니다.
  * **의미:** `max()` 함수로 최고 성적을 뽑아낸 뒤, 역시 소수점 넷째 자리까지 반올림하여 '어떤 방식이든 최고 성능이 얼마였나'를 기록합니다.

---

### 3. 📤 반환값/할당 변수
* **반환값:** 파이썬의 리스트 `.append()` 메서드는 **`None`을 반환**합니다. 즉, 새로운 변수에 값을 리턴하는 것이 아니라, **원본 `summary_data` 리스트를 직접 수정(업데이트)**합니다.
* **결과적으로 `summary_data`는 어떻게 될까요?**
  코드가 실행되고 나면, `summary_data` 리스트 안에는 다음과 같은 데이터가 차곡차곡 쌓이게 됩니다.
  ```python
  [
      {'Model': 'KNN', 'Base': 0.8501, 'GridSearch': 0.8702, 'Optuna': 0.8805, 'Best': 0.8805},
      {'Model': 'Tree', 'Base': 0.8200, 'GridSearch': 0.8500, 'Optuna': 0.8650, 'Best': 0.8650}
      # ... 모델 개수만큼 행이 추가됨
  ]
  ```
  *(나중에 이 리스트를 `pd.DataFrame(summary_data)`에 넣으면 예쁜 성적표 표(Table)가 완성됩니다!)*

---

### 4. 🎁 요약 및 실행 예시
초보자분이 이 코드가 왜 쓰이는지 직접 실행해 보며 감을 잡을 수 있는 간단한 예시 코드입니다.

**[따라 하기 실습 코드]**
```python
# 1. 빈 리스트 준비
summary_data = []

# 2. 임의의 모델 성적 데이터
name = "RandomForest"
base_acc = 0.812345
grid_acc = 0.856789
optuna_acc = 0.891234

# 3. append 함수 사용
summary_data.append({
    'Model': name, 
    'Base': round(base_acc, 4), 
    'GridSearch': round(grid_acc, 4), 
    'Optuna': round(optuna_acc, 4), 
    'Best': round(max(base_acc, grid_acc, optuna_acc), 4)
})

# 4. 결과 확인
print(summary_data)
```

**[예상 출력 결과]**
```text
[{'Model': 'RandomForest', 'Base': 0.8123, 'GridSearch': 0.8568, 'Optuna': 0.8912, 'Best': 0.8912}]
```

💡 **핵심 요약:** `summary_data.append(...)`는 **"우리 모델의 실험 성적표 한 줄을 요약해서 리스트에 차곡차곡 모아두는 작업"**이라고 이해하시면 가장 정확합니다!