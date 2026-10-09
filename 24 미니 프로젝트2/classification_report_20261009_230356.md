# classification_report - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 23:03:56

---

안녕하세요! 머신러닝 모델의 성능을 평가할 때 가장 많이 쓰이는 필수 함수 중 하나인 `classification_report`에 대해 초보자의 눈높이에 맞춰 쉽고 명쾌하게 설명해 드리겠습니다.

---

### 1. 📌 함수 개요
`classification_report`는 머신러닝 분류(Classification) 모델이 예측한 결과가 실제 정답과 얼마나 잘 맞았는지를 한눈에 파악할 수 있도록 **성능 지표들을 요약해서 텍스트 형태로 보여주는 함수**입니다. 
(주로 사이킷런 `sklearn.metrics` 모듈에서 가져와서 사용합니다.)

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드 `classification_report(y_test, y_pred, target_names=['Normal', 'Heart Disease'])`에 사용된 3개의 인자를 하나씩 뜯어보겠습니다.

*   **첫 번째 인자: `y_test` (실제 정답)**
    *   **역할:** 테스트 데이터셋의 **실제 진짜 정답 레이블**입니다. 모델이 맞혀야 하는 목표치입니다.
*   **두 번째 인자: `y_pred` (모델의 예측값)**
    *   **역할:** 모델이 학습을 마치고 테스트 데이터를 보고 **"이것일 거야!"라고 예측한 결과**입니다.
*   **세 번째 인자: `target_names=['Normal', 'Heart Disease']` (출력 이름 지정)**
    *   **역할:** 컴퓨터가 이해하는 숫자 레이블(예: 0, 1) 대신, 사람이 읽기 쉬운 **클래스 이름(문자열)을 보고서에 출력**해 줍니다.
    *   **의미:** 
        *   0번(또는 첫 번째 클래스)은 `'Normal'` (정상)
        *   1번(또는 두 번째 클래스)은 `'Heart Disease'` (심장병)
        *   이렇게 이름표를 달아주어 리포트를 훨씬 직관적으로 읽을 수 있게 도와줍니다.

---

### 3. 📤 반환값 및 출력 형태

이 함수는 튜플이나 리스트를 반환하는 것이 아니라, **하나의 잘 정렬된 텍스트(String)를 반환**합니다. 이 텍스트를 `print()` 함수 안에 넣었기 때문에 콘솔에 예쁜 표 형태로 출력됩니다.

출력되는 리포트에는 다음 네 가지 핵심 지표가 클래스별로 표시됩니다:
1.  **Precision (정밀도):** 모델이 '심장병'이라고 예측한 것들 중 **실제로 심장병이었던 비율**
2.  **Recall (재현율):** 실제 '심장병'인 환자들 중 **모델이 심장병이라고 정확히 찾아낸 비율**
3.  **F1-score (F1 점수):** 정밀도와 재현율의 조화 평균 (모델의 성능이 균형 잡혀 있는지 확인)
4.  **Support (개수):** 각 클래스에 속하는 실제 데이터의 개수

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 직접 코랩(Colab)이나 파이썬 환경에서 복사해서 바로 실행해 볼 수 있는 간단한 예시 코드입니다.

```python
from sklearn.metrics import classification_report

# 1. 실제 정답 (0: Normal, 1: Heart Disease)
y_test = [0, 1, 1, 0, 1, 0]

# 2. 모델이 예측한 값
y_pred = [0, 1, 0, 0, 1, 0]

# 3. classification_report 호출 및 출력
report = classification_report(y_test, y_pred, target_names=['Normal', 'Heart Disease'])

print(report)
```

**[예상 실행 결과]**
```text
                  Precision    Recall  f1-score   support

          Normal       0.75      1.00      0.86         3
Heart Disease          1.00      0.67      0.80         3

       accuracy                           0.83         6
      macro avg       0.88      0.83      0.83         6
   weighted avg       0.88      0.83      0.83         6
```

> **💡 한 줄 요약:** `classification_report`는 **"내 모델이 정상(Normal)과 심장병(Heart Disease)을 각각 얼마나 잘 맞혔는지"**를 점수 매겨서 친절한 성적표로 뽑아주는 고마운 함수입니다!