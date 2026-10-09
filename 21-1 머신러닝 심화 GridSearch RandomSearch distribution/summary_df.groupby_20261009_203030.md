# summary_df.groupby - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:30:30

---

안녕하세요! 파이썬 데이터 분석에서 가장 많이 쓰이는 마법 같은 기능 중 하나인 `groupby`에 대해 아주 쉽고 친절하게 설명해 드릴게요. 

제시해주신 코드는 데이터 분석 라이브러리인 **Pandas**를 사용할 때 데이터 요약(Aggregating)을 위해 쓰는 전형적인 패턴입니다. 하나씩 뜯어볼까요?

---

### 1. 📌 함수 개요
`summary_df.groupby('Method')`는 **엑셀의 '피벗 테이블'이나 '그룹별 집계' 기능과 정확히 똑같은 역할**을 하는 함수입니다. 커다란 데이터프레임(`summary_df`)에서 특정 열(`'Method'`)을 기준으로 데이터를 끼리끼리 묶은 뒤, 각 그룹별로 통계치(평균, 합계 등)를 구할 수 있도록 준비해 주는 역할을 합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
작성해주신 코드 조각에서 `groupby` 안에 들어간 인자를 살펴보겠습니다.

*   **인자:** `'Method'` (문자열 형태)
*   **역할:** 데이터를 어떤 기준으로 쪼개고 묶을지 정해주는 **'기준 열(Column) 이름'**입니다.
*   **설정된 값의 의미:** 
    *   예를 들어, `summary_df` 안에 기계학습 모델의 이름들이 들어있는 `'Method'`라는 열(Column)이 있다면, 이 열에 적힌 값(예: 'LinearRegression', 'RandomForest', 'SVM' 등)이 **같은 것끼리 하나의 그룹으로 묶으라**는 뜻입니다.

---

### 3. 📤 반환값/할당 변수
코드 뒷부분의 `.agg({...})`까지 포함해서 전체 코드가 실행될 때 반환되는 결과와 변수를 설명해 드릴게요.

*   **전체 코드 문맥:** 
    ```python
    method_performance = summary_df.groupby('Method').agg(...)
    ```
*   **반환값 (`method_performance`에 저장되는 것):**
    *   기준이 되었던 `'Method'`가 **새로운 행 인덱스(Index)**가 되고, 뒤이어 `.agg()`에서 계산된 요약 통계 결과들이 **열(Column)**로 이루어진 **새로운 데이터프레임(DataFrame)**이 반환되어 `method_performance` 변수에 쏙 담깁니다.

---

### 4. 🎁 요약 및 실행 예시
초보자분들도 직접 눈으로 보고 이해할 수 있도록 아주 간단한 예시 코드를 준비했습니다. 복사해서 파이썬 환경(주피터 노트북 등)에서 바로 실행해 보세요!

**[실습 코드]**
```python
import pandas as pd

# 1. 예시 데이터 만들기 (모델 이름과 그 모델들의 성능 점수)
data = {
    'Method': ['Linear', 'Linear', 'Tree', 'Tree', 'SVM'],
    'Accuracy': [0.85, 0.83, 0.90, 0.92, 0.88],
    'Time': [1.2, 1.1, 3.5, 3.7, 2.0]
}
summary_df = pd.DataFrame(data)

print("--- 원본 데이터 ---")
print(summary_df)
print("\n")

# 2. 질문하신 groupby 코드 사용하기 (Method 별 Accuracy의 평균 구하기)
method_performance = summary_df.groupby('Method').agg({'Accuracy': 'mean'})

print("--- groupby 실행 결과 (method_performance) ---")
print(method_performance)
```

**[예상 결과]**
```text
--- 원본 데이터 ---
   Method  Accuracy  Time
0  Linear      0.85   1.2
1  Linear      0.83   1.1
2    Tree      0.90   3.5
3    Tree      0.92   3.7
4     SVM      0.88   2.0


--- groupby 실행 결과 (method_performance) ---
          Accuracy
Method            
Linear      0.840  <-- (0.85 + 0.83) / 2
SVM         0.880  <-- 데이터 1개이므로 그대론
Tree        0.910  <-- (0.90 + 0.92) / 2
```

**💡 한 줄 요약:** 
`summary_df.groupby('Method')`는 데이터를 **'Method'별로 묶어주는 준비 작업**이며, 뒤에 `.agg()`를 붙여서 평균, 합계 등 원하는 통계를 내면 멋진 요약표를 얻을 수 있습니다!