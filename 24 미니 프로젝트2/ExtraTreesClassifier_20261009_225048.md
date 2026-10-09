# ExtraTreesClassifier - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 22:50:48

---

파이썬 머신러닝 라이브러리인 Scikit-Learn(사이킷런)에서 사용되는 `ExtraTreesClassifier`에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 쉽고 명쾌하게 정리해 드릴게요!

---

### 1. 📌 함수 개요
`ExtraTreesClassifier`는 여러 개의 **결정 트리(Decision Tree)**를 모아서 숲을 만드는 **앙상블(Ensemble) 머신러닝 모델**입니다. 
이름인 'Extra-Trees'는 **Extremely Randomized Trees(극도로 무작위화된 트리)**의 줄임말입니다. 데이터를 나눌 때 완전히 무작위로 분할을 시도하기 때문에, 일반적인 랜덤 포레스트(Random Forest)보다 **속도가 훨씬 빠르고 과적합(Overfitting)을 방지**하는 데 뛰어난 성능을 보입니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드(`ExtraTreesClassifier(random_state=RANDOM_STATE)`)에 사용된 인자와 기본적으로 자주 쓰이는 숨겨진 인자들을 살펴볼게요.

*   **`random_state=RANDOM_STATE`** *(현재 코드에 사용된 인자)*
    *   **역할:** 컴퓨터가 난수를 생성할 때 기준이 되는 '씨앗(Seed)' 값입니다.
    *   **의미:** 머신러닝 모델은 학습 과정에서 무작위성(데이터 섞기 등)을 사용합니다. 이 값을 지정해 주면 **코드를 언제 다시 실행해도 정확히 똑같은 결과**가 나오도록 보장해 줍니다. (결과의 재현성 확보)

> **💡 참고 (자주 함께 쓰이는 다른 인자들):**
> *   `n_estimators`: 만들 나무의 개수 (기본값은 보통 100개)
> *   `max_depth`: 트리의 최대 깊이 (과적합을 막기 위해 제한을 두기도 함)

---

### 3. 📤 반환값/할당 변수

코드에서 이 함수는 다음과 같이 사용되었습니다.
`'ExtraTrees': ExtraTreesClassifier(random_state=RANDOM_STATE)`

*   **반환값:** 설정된 옵션을 바탕으로 데이터를 학습할 준비가 완료된 **'ExtraTrees 분류기 모델 객체(Object)'**를 반환합니다.
*   **할당 변수 (`'ExtraTrees'`):** 딕셔너리(Dictionary) 구조의 키(Key) 값으로 할당되어 있습니다. 즉, 이 모델을 나중에 `models['ExtraTrees']` 같은 방식으로 쉽게 꺼내서 쓸 수 있도록 이름을 붙여둔 것입니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 붓꽃(Iris) 데이터를 가지고 이 모델을 직접 쓰고 학습시켜 볼 수 있는 가장 간단한 코드입니다. 복사해서 실행해 보세요!

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

# 1. 데이터 불러오기
iris = load_iris()
X, y = iris.data, iris.target

# 2. 학습용과 테스트용 데이터로 나누기
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. ExtraTrees 모델 생성하기 (질문하신 코드 적용!)
RANDOM_STATE = 42
model = ExtraTreesClassifier(random_state=RANDOM_STATE)

# 4. 모델 학습시키기 (공부시키기)
model.fit(X_train, y_train)

# 5. 예측 정확도 확인하기
accuracy = model.score(X_test, y_test)
print(f"모델 예측 정확도: {accuracy * 100:.2f}%")
```

**예상 결과:**
```text
모델 예측 정확도: 100.00% (또는 데이터에 따라 96~100%)
```
*이처럼 `ExtraTreesClassifier`는 코 한 줄로 강력한 성능을 내는 훌륭한 분류 모델입니다!*