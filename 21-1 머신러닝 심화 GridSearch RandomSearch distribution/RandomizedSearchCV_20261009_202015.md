# RandomizedSearchCV - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:20:15

---

파이썬 머신러닝 라이브러리인 Scikit-Learn에서 제공하는 **`RandomizedSearchCV`** 함수에 대해 초보자의 눈높이에 맞춰 친절하고 명쾌하게 해설해 드리겠습니다.

---

### 1. 📌 함수 개요
`RandomizedSearchCV`는 머신러닝 모델의 성능을 가장 높여주는 **최적의 하이퍼파라미터(설정값)를 효율적으로 찾아주는 탐색 도구**입니다. 
모든 경우의 수를 다 찾아보는 `GridSearchCV`와 달리, 지정된 횟수만큼 **무작위로(Random) 조합을 선택해 테스트**하므로, 탐색 시간이 훨씬 빠르다는 강력한 장점이 있습니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드에서 사용된 7가지 인자의 역할과 설정된 값의 의미는 다음과 같습니다.

*   **`model`**
    *   **역할:** 최적화(튜닝)를 진행할 대상 머신러닝 모델입니다. (예: 랜덤 포레스트, 서포트 벡터 머신 등)
*   **`param_distributions[name]`**
    *   **역할:** 탐색할 하이퍼파라미터들의 후보군(딕셔너리 형태)입니다. 모델 `name`에 맞는 다양한 설정값 범위를 전달하여 이 중에서 최적의 조합을 고르게 됩니다.
*   **`n_iter=50`**
    *   **역할:** 무작위로 시도해볼 **조합의 개수**입니다. 
    *   **설정값 의미:** 총 50번의 서로 다른 파라미터 조합을 무작위로 골라 성능을 테스트해봅니다.
*   **`cv=5`**
    *   **역할:** 교차 검증(Cross-Validation)을 할 때 데이터를 쪼개는 횟수(Fold)입니다.
    *   **설정값 의미:** 데이터를 5개 조각으로 나누어 1개 조각은 검증용, 나머지 4개 조각은 훈련용으로 사용하는 과정을 5번 반복하여 모델의 평균 성능을 객관적으로 평가합니다.
*   **`scoring='accuracy'`**
    *   **역할:** 모델의 성능을 평가하는 기준(지표)입니다.
    *   **설정값 의미:** 분류(Classification) 문제에서 가장 직관적인 지표인 **정확도(Accuracy)**를 기준으로 가장 성능이 좋은 조합을 찾습니다.
*   **`n_jobs=-1`**
    *   **역할:** 컴퓨터의 CPU 코어를 몇 개나 사용할 것인지 지정합니다.
    *   **설정값 의미:** `-1`은 **"내 컴퓨터의 모든 CPU 코어를 총동원해라"**라는 뜻으로, 학습 속도를 획기적으로 빠르게 만들어 줍니다.
*   **`random_state=42`**
    *   **역할:** 난수(무작위 숫자)를 생성할 때의 기준점(씨앗값)입니다.
    *   **설정값 의미:** 코드를 다시 실행해도 똑같은 조합들을 무작위로 뽑도록 **결과를 재현 가능하게 고정**해 줍니다. (숫자 42는 관습적으로 자주 쓰이는 행운의 숫자입니다.)
*   **`verbose=0`**
    *   **역할:** 학습 과정에서 화면에 로그(출력문)를 얼마나 자세히 띄울 것인지 결정합니다.
    *   **설정값 의미:** `0`으로 설정되어 있어, 탐색 과정에서 복잡한 텍스트 출력을 숨기고 조용히 실행됩니다.

---

### 3. 📤 반환값 및 할당 변수 분석

코드의 결과로 만들어진 `random_search` 객체는 파이썬에서 마치 **"훈련이 완료된 똑똑한 도구 상자"**처럼 작동합니다. 

*   **`random_search` 변수:**
    *   50번의 무작위 탐색을 통해 **가장 성능이 좋았던 모델의 설정값**과 **그때의 학습된 모델**을 통째로 품고 있는 객체입니다.
    *   이 변수를 통해 나중에 `.best_params_`(최적의 파라미터 확인), `.best_score_`(최고 점수 확인), 혹은 `.predict()`(새로운 데이터 예측) 등의 기능을 사용할 수 있습니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 이해할 수 있도록 아주 간단한 예시 코드를 준비했습니다.

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# 1. 데이터 불러오기
data = load_iris()
X, y = data.data, data.target

# 2. 모델 준비
model = RandomForestClassifier(random_state=42)

# 3. 탐색할 파라미터 범위 설정 (여기서는 간단히 트리 개수만 후보로 둠)
param_distributions = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [None, 5, 10, 20]
}

# 4. RandomizedSearchCV 객체 생성 (질문하신 바로 그 코드!)
random_search = RandomizedSearchCV(
    model,
    param_distributions=param_distributions, # 딕셔너리 전체 전달
    n_iter=5,                                # 편의상 5번만 무작위 탐색
    cv=3,                                    # 3겹 교차 검증
    scoring='accuracy',
    n_jobs=-1,
    random_state=42,
    verbose=1                                # 과정을 보기 위해 1로 설정
)

# 5. 최적의 조합 찾기 (학습 시작!)
random_search.fit(X, y)

# 6. 결과 확인하기
print("가장 좋은 설정값:", random_search.best_params_)
print("가장 높은 정확도:", random_search.best_score_)
```

**💡 실행 결과 (예시):**
```text
가장 좋은 설정값: {'n_estimators': 10, 'max_depth': 5}
가장 높은 정확도: 0.9666...
```
이처럼 `RandomizedSearchCV`를 사용하면 일일이 수동으로 모델을 수정해 볼 필요 없이, 컴퓨터가 알아서 가장 완벽한 조합을 척척 찾아준답니다!