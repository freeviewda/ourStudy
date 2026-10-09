# grid_search.fit - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:08:56

---

파이썬 머신러닝에서 가장 중요하고 흥미로운 과정 중 하나인 `grid_search.fit(X_train, y_train)`에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 하나씩 친절하게 풀어드릴게요!

---

### 1. 📌 함수 개요
`grid_search.fit()`은 우리가 미리 정해둔 여러 하이퍼파라미터(설정값)들의 조합 중에서 **머신러닝 모델의 성능을 가장 극대화해 주는 최고의 조합을 찾아내는(학습하는) 함수**입니다. 이 과정에서 교차 검증(Cross-Validation)을 사용하여 모델이 특정 데이터에만 과대적합(Overfitting)되지 않도록 공정하게 평가합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에 전달된 `X_train`과 `y_train`은 모델을 가르치기 위한 훈련용 데이터입니다. 각각의 역할은 다음과 같습니다.

*   **`X_train` (특징 데이터, Features)**
    *   **역할:** 모델이 학습할 때 정답을 맞히기 위해 보는 '문제집(단서)'입니다. (예: 집의 크기, 방의 개수, 위치 등)
    *   **형태:** 보통 2차원 표(DataFrame 또는 NumPy Array) 형태입니다. (행: 데이터 개수, 열: 특징 개수)

*   **`y_train` (타겟 데이터, Target / Label)**
    *   **역할:** 모델이 맞혀야 하는 '정답지'입니다. (예: 실제 집 가격)
    *   **형태:** 보통 1차원 리스트나 시리즈(Series) 형태입니다.

> 💡 **동작 원리 (Grid Search의 마법):**
> `.fit()`이 실행되는 순간, `grid_search` 객체 안에 미리 설정해 둔 파라미터 조합(예: 결정 트리의 깊이를 3으로 할까, 5로 할까?)을 하나씩 `X_train`과 `y_train`에 적용해 보며 **가장 점수가 높은 완벽한 조합**을 찾아냅니다.

---

### 3. 📤 반환값 및 후속 작업

`grid_search.fit(X_train, y_train)` 코드가 실행되고 나면, **`grid_search` 객체 자체에 학습 결과가 저장**됩니다. (별도의 변수로 값을 반환받지 않고, 객체 내부의 상태가 업데이트됩니다.)

학습이 끝난 후 우리가 주로 꺼내 쓰는 주요 속성(Attribute)들은 다음과 같습니다.

*   **`grid_search.best_params_`**
    *   수많은 조합 중에서 가장 뛰어난 성능을 보여준 **최적의 파라미터 조합**을 딕셔너리 형태로 반환합니다. (예: `{'max_depth': 5, 'n_estimators': 100}`)
*   **`grid_search.best_score_`**
    *   그 최적의 조합일 때 나온 **최고의 교차 검증 점수(정확도 등)**를 반환합니다.
*   **`grid_search.best_estimator_`**
    *   가장 성능이 좋았던 설정으로 **완전히 학습이 끝난 최종 머신러닝 모델 자체**를 반환합니다. 이 모델을 이용해 바로 예측(`predict`)을 할 수 있습니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 전체 흐름을 이해할 수 있도록, 사이킷런(Scikit-Learn)을 이용한 간단한 전체 실행 코드를 준비했습니다. 복사해서 주피터 노트북 등에 바로 실행해 보세요!

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# 1. 데이터 불러오기 및 나누기
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, random_state=42
)

# 2. 기본 모델 생성
rf_model = RandomForestClassifier(random_state=42)

# 3. 테스트해볼 파라미터 조합 정의 (Grid)
param_grid = {
    'n_estimators': [10, 50, 100],  # 나무의 개수
    'max_depth': [2, 4, 6],  # 나무의 최대 깊이
}

# 4. 그리드 서치 객체 생성 (3겹 교차 검증 사용)
grid_search = GridSearchCV(
    estimator=rf_model, param_grid=param_grid, cv=3, scoring='accuracy'
)

# ==========================================
# 5. 핵심: 학습 및 최적의 조합 탐색 실행!
grid_search.fit(X_train, y_train)
# ==========================================

# 6. 결과 확인
print('📌 가장 좋은 설정값:', grid_search.best_params_)
print('📌 그때의 최고 점수:', grid_search.best_score_)

# 7. 최적의 모델로 새로운 데이터(X_test) 예측하기
best_model = grid_search.best_estimator_
predictions = best_model.predict(X_test)
print('📌 테스트 데이터 예측 결과:', predictions[:5])
```

**예상 결과:**
```text
📌 가장 좋은 설정값: {'max_depth': 2, 'n_estimators': 10}
📌 그때의 최고 점수: 0.955...
📌 테스트 데이터 예측 결과: [1 0 2 1 1]
```

이제 `grid_search.fit(X_train, y_train)`이 무엇을 하는 친구인지 명확하게 감이 오셨죠? 궁금한 점이 있다면 언제든 다시 질문해 주세요!