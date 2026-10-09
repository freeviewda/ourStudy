# optuna.create_study - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 21:56:52

---

파이썬 머신러닝/딥러닝에서 최적의 하이퍼파라미터를 찾을 때(Hyperparameter Optimization) 가장 많이 쓰이는 라이브러리가 바로 **Optuna**입니다. 

질문해주신 코드를 초보자의 눈높이에 맞춰 하나씩 친절하고 명쾌하게 해설해 드리겠습니다.

---

### 1. 📌 함수 개요
`optuna.create_study()`는 **AI 모델이 가장 좋은 성능을 내도록 최적의 설정값(하이퍼파라미터)을 찾아주는 '연구(Study) 공간'을 생성하는 함수**입니다. 이 함수를 실행하면 앞으로 진행될 실험들을 기록하고 관리할 수 있는 가상의 연구실(Study 객체)이 만들어집니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에 사용된 3가지 인자가 각각 어떤 역할을 하는지 살펴볼까요?

*   **`direction='maximize'`**
    *   **역할:** 최적화의 방향을 결정합니다.
    *   **의미:** CatBoost 모델의 평가 지표(예: 정확도, F1-score 등)를 **'최대화(maximize)'**하는 방향으로 하이퍼파라미터를 찾겠다는 뜻입니다. (만약 오차를 줄이는 게 목표라면 `'minimize'`를 사용합니다.)

*   **`study_name=f'catboost_run_{run+1}'`**
    *   **역할:** 이번 연구(실험)의 이름을 붙여줍니다.
    *   **의미:** 파이썬의 f-string을 사용하여 실험 번호에 따라 이름을 다르게 지정합니다. (예: 첫 번째 실행이면 `'catboost_run_1'`, 두 번째면 `'catboost_run_2'`). 나중에 로그를 확인하거나 여러 실험을 구분할 때 매우 유용합니다.

*   **`sampler=optuna.samplers.TPESampler(seed=run_seed)`**
    *   **역할:** 다음 실험에서 어떤 하이퍼파라미터 값을 시도해 볼지 결정하는 '전략가(샘플러)'를 지정합니다.
    *   **의미:** 
        *   `TPESampler`: 베이지안 최적화 기반의 고성능 샘플러로, 이전 실험 결과를 바탕으로 "이쯤 숫자로 하면 더 좋아질 것 같은데?" 하고 똑똑하게 다음 값을 추천해 줍니다.
        *   `seed=run_seed`: 랜덤 시드(씨앗값)를 고정하여, **코드를 다시 실행해도 똑같은 랜덤 값이 나오도록 재현성(Reproducibility)**을 확보합니다.

---

### 3. 📤 반환값/할당 변수

*   **`study` (할당 변수)**
    *   **의미:** `optuna.create_study(...)`가 만들어낸 **연구소(Study 객체)**가 이 변수에 담깁니다.
    *   **활용:** 앞으로 우리는 이 `study` 변수를 이용해 모델을 학습시키고(`study.optimize(...)`), 가장 좋은 결과가 무엇이었는지(`study.best_value`), 그때의 파라미터는 무엇이었는지(`study.best_params`) 확인할 수 있습니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 Optuna를 아주 간단하게 테스트해 볼 수 있는 미니 코드를 준비했습니다.

**[간단한 실행 예시 코드]**
```python
import optuna

# 1. 목적 함수 정의 (우리가 최적화하고 싶은 가상의 함수: y = -(x-2)^2 + 10)
def objective(trial):
    # -10부터 10 사이에서 x 값을 임의로 골라라
    x = trial.suggest_float('x', -10, 10)
    
    # x가 2일 때 가장 큰 값(10)이 나오는 수식
    score = -((x - 2) ** 2) + 10
    return score

# 2. 🌟 연구(Study) 생성 (질문하신 핵심 코드!)
study = optuna.create_study(
    direction='maximize',
    study_name='simple_math_run_1',
    sampler=optuna.samplers.TPESampler(seed=42)
)

# 3. 최적화 시작 (이 함수를 10번 시도해라)
study.optimize(objective, n_trials=10)

# 4. 결과 출력
print("가장 찾은 최적의 x값:", study.best_params['x'])
print("그때의 최대 점수:", study.best_value)
```

**[예상 결과]**
> `TPESampler`가 똑똑하게 숫자를 바꿔가며 시도한 끝에, 최적의 `x`값인 `2`에 아주 가까운 숫자를 찾아내고 최대 점수인 `10`에 수렴하는 결과를 보여줍니다.