# optuna.create_study - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 21:50:06

---

안녕하세요! 파이썬의 대표적인 하이퍼파라미터 최적화(AutoML) 라이브러리인 **Optuna**의 핵심 함수에 대해 아주 쉽고 친절하게 설명해 드릴게요. 

머신러닝 모델의 성능을 가장 좋게 만드는 마법의 조합을 찾을 때 이 함수가 출발점이 됩니다. 하나씩 살펴볼까요?

---

### 1. 📌 함수 개요
`optuna.create_study()`는 모델 성능을 최적화하기 위한 **'연구(Study) 공간'을 생성하는 함수**입니다. 이 함수는 앞으로 어떤 방향으로(최대화 혹은 최소화), 어떤 이름으로, 어떤 알고리즘(샘플러)을 써서 최적화를 진행할지 전반적인 규칙을 설정하는 역할을 합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에 사용된 3가지 인자가 각각 어떤 의미를 가지는지 살펴봅시다.

* **`direction='maximize'`**
  * **역할:** 최적화의 목표 방향을 설정합니다.
  * **설정값 의미:** `'maximize'`는 모델의 평가 지표(예: 정확도, F1-score 등)를 **'최대화'** 하는 방향으로 학습을 진행하겠다는 뜻입니다. (반대로 오차를 줄이는 게 목표라면 `'minimize'`를 사용합니다.)

* **`study_name=f'lgbm_run_{run+1}'`**
  * **역할:** 이번 최적화 작업(Study)의 이름을 지어줍니다.
  * **설정값 의미:** 문자열 포매팅(`f-string`)을 사용하여 반복문 안에서 `lgbm_run_1`, `lgbm_run_2`와 같이 고유한 이름을 자동으로 생성합니다. 나중에 여러 실험 결과를 로그나 데이터베이스로 관리할 때 구분하기 쉽게 만들어 줍니다.

* **`sampler=optuna.samplers.TPESampler(seed=run_seed)`**
  * **역할:** 다음에 시도할 하이퍼파라미터를 어떤 방식으로 추천(샘플링)받을지 알고리즘을 지정합니다.
  * **설정값 의미:** `TPESampler`는 Optuna에서 가장 성능이 좋다고 널리 알려진 베이지안 최적화 기반의 알고리즘입니다. 여기에 `seed=run_seed`를 주어, 코드를 다시 실행해도 **랜덤 결과가 똑같이 나오도록(재현 가능하도록)** 고정했습니다.

---

### 3. 📤 반환값/할당 변수

* **`study` (Study 객체)**
  * **데이터 의미:** `create_study()` 함수는 설정된 규칙을 담고 있는 **'Study 객체'**를 반환하여 `study` 변수에 저장합니다.
  * **활용:** 이 `study` 객체는 앞으로 `study.optimize(objective, n_trials=100)` 같은 코드를 통해 실제로 최적화 탐색을 수행하고, 가장 좋은 결과(`study.best_value`)나 그때의 파라미터(`study.best_params`)를 꺼내보는 데 사용됩니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 이해할 수 있도록 아주 간단한 예시 코드를 준비했습니다.

#### 📝 간단한 실습 코드
```python
import optuna

# 1. 목적 함수 정의 (우리가 최대화하고 싶은 간단한 수학 함수 예시: -(x-2)^2 + 10)
def objective(trial):
    x = trial.suggest_float('x', -10, 10)
    score = -((x - 2) ** 2) + 10  # x가 2일 때 최대값 10이 나옴
    return score

# 2. Study 생성 (오늘 배운 함수!)
study = optuna.create_study(
    direction='maximize',
    study_name='simple_optimization',
    sampler=optuna.samplers.TPESampler(seed=42)
)

# 3. 최적화 실행 (10번 시도)
study.optimize(objective, n_trials=10)

# 4. 결과 확인
print(f"가장 좋은 점수: {study.best_value}")
print(조합된 최적의 파라미터: {study.best_params})
```

#### 💡 실행 결과 (예시)
```text
[I 2023-10-25 ...] A study created with name 'simple_optimization' using sampler TPESampler
[I 2023-10-25 ...] Trial 0 finished with value: ...
...
가장 좋은 점수: 9.999...
최적의 파라미터: {'x': 1.998...}
```
> **요약하자면:** `optuna.create_study(...)`는 최적화 실험을 위한 **'경기장'을 짓는 과정**이며, 인자들을 통해 경기 규칙(최대화), 경기장 이름, 경기 방식(TPE 알고리즘)을 셋팅하는 것입니다!