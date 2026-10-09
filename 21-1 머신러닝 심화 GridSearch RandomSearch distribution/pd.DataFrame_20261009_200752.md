# pd.DataFrame - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:07:52

---

파이썬 데이터 분석에서 가장 많이 쓰이는 필수 함수 중 하나인 `pd.DataFrame`에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 쉽고 명쾌하게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`pd.DataFrame`은 파이썬의 대표적인 데이터 분석 라이브러리인 **Pandas**에서 제공하는 함수로, **엑셀의 '표(Table)'와 같은 형태의 2차원 데이터 구조(DataFrame)를 생성**하는 역할을 합니다. 리스트, 딕셔너리, 2차원 배열 등의 데이터를 받아 행(Row)과 열(Column)이 있는 깔끔한 표로 만들어 줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시해주신 코드 `pd.DataFrame(baseline_results)`에서 전달된 인자는 하나입니다.

* **`baseline_results`**
  * **역할:** 데이터프레임의 재료가 되는 원본 데이터입니다.
  * **설정된 값의 의미:** 코드의 이름(`baseline_results`)으로 유추해 볼 때, 머신러닝 모델의 초기 성능(Baseline)을 테스트한 결과물들이 담겨 있을 가능성이 높습니다. 이 데이터는 주로 **딕셔너리(Dictionary)**, **리스트의 리스트(List of Lists)**, 또는 **넘파이 배열(NumPy Array)** 형태일 것입니다.
  * *예시:* 만약 `baseline_results`가 `[{'model': '사과', 'score': 0.85}, {'model': '바나나', 'score': 0.90}]` 같은 딕셔너리 리스트였다면, 자동으로 키(Key)는 열 이름이 되고 값(Value)은 데이터가 됩니다.

---

### 3. 📤 반환값/할당 변수
* **할당 변수:** `baseline_df`
* **반환값 설명:** 
  * `pd.DataFrame()` 함수가 실행되면 엑셀 시트처럼 행과 열을 가진 **Pandas DataFrame 객체**가 만들어집니다.
  * 이 결과물이 `baseline_df`라는 변수에 쏙 담기게 됩니다. 
  * 이제 초보자분들은 `baseline_df.head()`를 써서 앞부분을 미리 보거나, `baseline_df['score'].mean()`처럼 평균을 구하는 등 강력한 데이터 분석 기능을 사용할 수 있게 됩니다.

---

### 4. 🎁 요약 및 실행 예시
백문이 불여일견! 직접 파이썬 환경에서 실행해 볼 수 있는 간단한 예시 코드입니다.

**[실행 코드]**
```python
import pandas as pd

# 1. 재료 데이터 준비 (모델 이름과 정확도를 담은 딕셔너리 리스트)
baseline_results = [
    {'model': 'Logistic Regression', 'accuracy': 0.82},
    {'model': 'Random Forest', 'accuracy': 0.89},
    {'model': 'Support Vector Machine', 'accuracy': 0.85}
]

# 2. pd.DataFrame() 함수를 사용해 표 형태로 변환
baseline_df = pd.DataFrame(baseline_results)

# 3. 결과 확인
print(baseline_df)
```

**[예상 결과]**
```text
                    model  accuracy
0     Logistic Regression      0.82
1           Random Forest      0.89
2  Support Vector Machine      0.85
```

> **💡 초보자를 위한 팁:** 
> 파이썬으로 데이터를 다룰 때, 파편화되어 있던 데이터(리스트, 딕셔너리 등)를 `pd.DataFrame()`에 넣는 순간 **정렬, 필터링, 통계 계산, 시각화**가 가능한 강력한 무기가 생긴다고 생각하시면 됩니다!