# random_search.fit - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:20:34

---

파이썬 머신러닝에서 자주 쓰이는 `random_search.fit(X_train, y_train)` 코드에 대해 초보자의 눈높이에 맞춰 친절하고 명쾌하게 해설해 드리겠습니다!

---

### 1. 📌 함수 개요
`random_search.fit()`은 **머신러닝 모델이 가장 좋은 성능을 낼 수 있는 최적의 하이퍼파라미터(설정값)를 무작위로 탐색하여 찾아내는 핵심 함수**입니다. 
우리가 지정해 준 여러 후보 값들 중에서 무작위로(Random) 조합을 골라가며 학습(Fit)을 반복하고, 가장 성적이 좋았던 조합을 찾아내어 모델에 적용해 줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드에는 총 2개의 입력 인자가 전달되었습니다. 각각 어떤 역할을 하는지 살펴볼까요?

*   **`X_train` (학습용 독립변수 / Feature)**
    *   **역할:** 모델에게 보여줄 '문제집'에 해당합니다. (예: 집의 평수, 방의 개수, 위치 등이 담긴 표 데이터)
    *   **의미:** AI가 정답을 맞히기 위해 분석해야 할 특징(Feature) 데이터들입니다. 보통 2차원 형태(행과 열)의 데이터로 이루어져 있습니다.
*   **`y_train` (학습용 종속변수 / Target)**
    *   **역할:** 모델이 맞춰야 할 '정답지'에 해당합니다. (예: 실제 집의 가격)
    *   **의미:** `X_train`이라는 문제를 풀었을 때 나와야 하는 실제 결과값(Label/Target)입니다. 보통 1차원 형태(리스트 또는 시리즈)로 이루어져 있습니다.

> **💡 요약하자면:** `fit(X_train, y_train)`은 **"자, 이 문제집(`X_train`)과 정답지(`y_train`)를 줄 테니, 네가 가진 설정값들을 무작위로 조합해가면서 가장 정답을 잘 맞히는 최적의 방법을 찾아내!"**라고 명령하는 것입니다.

---

### 3. 📤 반환값/할당 변수
질문하신 코드 라인 자체(`random_search.fit(X_train, y_train)`)에서는 별도의 변수로 값을 받아오지 않고(언패킹 없이) 함수만 실행하고 있습니다. 

하지만 이 함수가 실행되고 나면, `random_search` 객체 내부의 상태가 업데이트되며 다음과 같은 유용한 속성(Attribute)들을 사용할 수 있게 됩니다.
*   **`random_search.best_params_`**: 탐색한 조합 중 **가장 성능이 좋았던 하이퍼파라미터(설정값) 조합**을 알려줍니다.
*   **`random_search.best_estimator_`**: 최적의 설정값으로 **이미 학습이 완료된 완벽한 상태의 머신러닝 모델**을 반환합니다. (바로 예측에 사용할 수 있습니다!)

---

### 4. 🎁 요약 및 실행 예시
초보자분들이 전체 흐름을 쉽게 이해할 수 있도록, `RandomizedSearchCV`를 만들고 `fit`을 실행하는 전체 과정을 간단한 코드로 보여드릴게요.

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# 1. 데이터 불러오기 및 나누기 (문제와 정답 준비)
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, random_state=42
)

# 2. 기본 모델과 탐색할 하이퍼파라미터 범위 설정
model = RandomForestClassifier(random_state=42)
param_dist = {
    "n_estimators": [10, 50, 100, 200],
    "max_depth": [None, 5, 10, 20],
}

# 3. 무작위 탐색 객체(random_search) 생성
random_search = RandomizedSearchCV(
    estimator=model, param_distributions=param_dist, n_iter=5, random_state=42
)

# ==========================================
# 4. 🔥 오늘의 주인공 함수 실행!
random_search.fit(X_train, y_train)
# ==========================================

# 5. 결과 확인하기
print("🏆 가장 좋은 설정값:", random_search.best_params_)
print(
    "🎯 최적의 모델 점수:", random_search.best_score_
)  # 교차 검증 평균 정확도
```

**[예상 실행 결과]**
```text
🏆 가장 좋은 설정값: {'n_estimators': 10, 'max_depth': 5}
🎯 최적의 모델 점수: 0.955...
```
*설명: `fit` 함수가 내부적으로 여러 조합을 테스트한 뒤, `n_estimators=10, max_depth=5`일 때 가장 성적(약 95.5%)이 좋았다고 찾아내어 저장한 것입니다!*