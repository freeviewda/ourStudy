# optuna.create_study - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 21:41:17

---

파이썬의 초보자 분들도 딥러닝과 머신러닝의 '하이퍼파라미터 튜닝(최적의 설정값 찾기)'을 쉽게 할 수 있도록 도와주는 **Optuna** 라이브러리의 핵심 함수 `optuna.create_study`에 대해 아주 쉽게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`optuna.create_study()`는 모델의 성능을 가장 좋게 만드는 최적의 조합(예: XGBoost의 learning_rate, max_depth 등)을 찾기 위해 **'실험실(Study)'을 새로 개설하는 함수**입니다. 이 실험실 안에서 여러 번의 테스트(Trial)를 거치며 가장 완벽한 설정값을 찾아내게 됩니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에서 사용된 3가지 인자가 각각 어떤 일을 하는지 살펴볼까요?

*   **`direction='maximize'`**
    *   **의미:** 우리가 찾는 목표값(예: 정확도, F1-score 등)을 **최대화**하겠다는 뜻입니다.
    *   **설명:** 만약 모델의 '에러율'이나 '손실(Loss)'을 줄이는 것이 목표였다면 `'minimize'`를 사용했겠지만, 여기서는 성능 지표를 높이는 것이 목적이므로 `maximize`로 설정되었습니다.

*   **`study_name=f'xgboost_run_{run+1}'`**
    *   **의미:** 이번 실험(Study)의 **이름을 지정**해 주는 인자입니다.
    *   **설명:** 파이썬의 f-string을 사용하여 실험 번호에 따라 `xgboost_run_1`, `xgboost_run_2` 같은 고유한 이름표를 붙여줍니다. 나중에 여러 실험 결과를 구분하거나 저장할 때 매우 유용합니다.

*   **`sampler=optuna.samplers.TPESampler(seed=run_seed)`**
    *   **의미:** 다음에 어떤 하이퍼파라미터 값을 테스트해 볼지 결정하는 **'두뇌(알고리즘)'를 선택하고, 그 두뇌의 무작위성을 고정(Seed)**하는 인자입니다.
    *   **설명:** 
        *   `TPESampler`: 현재까지의 실험 결과를 바탕으로 "이쯤의 숫자를 넣으면 성능이 좋겠네!" 하고 영리하게 다음 숫자를 추천해 주는 Optuna의 대표적인 인기 알고리즘입니다.
        *   `seed=run_seed`: 컴퓨터는 무작위 숫자를 만들 때 시작점(seed)이 필요합니다. 이 값을 고정해 주면, **코드를 언제 다시 실행해도 똑같은 실험 결과가 나와서 결과 재현(Debugging & Sharing)**이 가능해집니다.

---

### 3. 📤 반환값/할당 변수

*   **`study`**
    *   **무엇을 받나요?:** `optuna.create_study(...)`가 실행되면 방금 만든 빈 실험실 객체를 리턴하여 `study`라는 변수에 저장합니다.
    *   **이후에 무엇을 하나요?:** 이 `study` 변수를 이용해 앞으로 본격적인 최적화를 시작합니다. (예: `study.optimize(objective, n_trials=50)`)

---

### 4. 🎁 요약 및 실행 예시

복잡한 설정 없이 Optuna를 사용하여 간단하게 함수 최적화를 테스트해 볼 수 있는 초간단 예시 코드입니다.

```python
import optuna


# 1. 최적화할 대상 함수 정의 (간단한 예: (x-2)^2 값을 최소화... 대신 maximize니까 반대로)
def objective(trial):
    x = trial.suggest_float('x', -10, 10)
    # x가 2일 때 -(x-2)^2 은 0으로 최대가 됨
    return -((x - 2) ** 2)


# 2. study 객체 생성 (오늘 배운 핵심 내용!)
study = optuna.create_study(
    direction='maximize',
    study_name='simple_test_run',
    sampler=optuna.samplers.TPESampler(seed=42),
)

# 3. 실험 시작 (10번의 테스트 진행)
study.optimize(objective, n_trials=10)

# 4. 결과 출력
print('가장 좋은 결과(Value):', study.best_value)
print('가장 좋은 파라미터(Params):', study.best_params)
```

**💡 한 줄 요약:** 
`optuna.create_study(...)`는 **"성능을 최대화(`maximize`)하고, 재현 가능하도록 시드(`seed`)가 고정된 똑똑한 AI 탐색기(`TPESampler`)를 장착한 새로운 실험실(`study_name`)을 만들어줘!"** 라는 의미의 명령어입니다.