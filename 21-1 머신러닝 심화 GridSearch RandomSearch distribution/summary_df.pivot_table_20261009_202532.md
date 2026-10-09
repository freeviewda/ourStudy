# summary_df.pivot_table - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:25:32

---

파이썬 데이터 분석에서 널리 쓰이는 `pandas` 라이브러리의 핵심 기능 중 하나인 `pivot_table` 함수에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 하나씩 친절하게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`summary_df.pivot_table()`은 **엑셀의 '피벗 테이블' 기능과 똑같은 역할**을 하는 함수입니다. 
데이터프레임(`summary_df`)에 있는 방대한 데이터 중에서 내가 보고 싶은 기준(행과 열)만 쏙쏙 뽑아, 한눈에 보기 쉽게 요약된 표(Matrix 형태)로 만들어 줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

제시해주신 코드에서 사용된 3가지 인자의 역할은 다음과 같습니다.

*   **`values='Test F1-Score'`**
    *   **역할:** 표의 **알맹이(값)**로 채워질 데이터를 지정합니다.
    *   **의미:** 여러 모델과 방법론에 따른 "테스트 F1-점수(Test F1-Score)" 숫자들을 표의 빈칸에 채워 넣겠다는 뜻입니다.
*   **`index='Model'`**
    *   **역할:** 표의 **행(Row, 가로줄 기준)** 제목으로 사용할 열을 지정합니다.
    *   **의미:** 표의 세로 줄마다 어떤 모델(예: Logistic Regression, Random Forest 등)인지 이름이 적히게 됩니다.
*   **`columns='Method'`**
    *   **역할:** 표의 **열(Column, 세로줄 기준)** 제목으로 사용할 열을 지정합니다.
    *   **의미:** 표의 가로 줄(상단)마다 어떤 전처리나 학습 방법(예: Baseline, Augmentation 등)인지 이름이 적히게 됩니다.

---

### 3. 📤 반환값/할당 변수 (`pivot_f1`)

*   **`pivot_f1`**
    *   **역할:** 위 함수가 실행된 결과로 만들어진 **새로운 요약표(DataFrame)**가 이 변수에 저장됩니다.
    *   **데이터 형태:** 행에는 `Model`, 열에는 `Method`, 값에는 `Test F1-Score`가 들어간 격자(Grid) 형태의 표가 됩니다. 이를 통해 어떤 모델이 어떤 방법(Method)을 썼을 때 가장 성능이 좋은지 교차하여 비교할 수 있습니다.

---

### 4. 🎁 요약 및 실행 예시

초보자분들이 이해하기 쉽도록 가상의 데이터를 가지고 직접 실행해 볼 수 있는 코드를 준비했습니다.

#### [실습 코드]
```python
import pandas as pd

# 1. 샘플 데이터(summary_df) 만들기
data = {
    'Model': ['Model_A', 'Model_A', 'Model_B', 'Model_B'],
    'Method': ['GridSearch', 'RandomSearch', 'GridSearch', 'RandomSearch'],
    'Test F1-Score': [0.85, 0.82, 0.90, 0.88]
}
summary_df = pd.DataFrame(data)

print("--- 원본 데이터 (summary_df) ---")
print(summary_df)
print("\n")

# 2. pivot_table 적용하기
pivot_f1 = summary_df.pivot_table(values='Test F1-Score', index='Model', columns='Method')

print("--- 피벗된 결과 (pivot_f1) ---")
print(pivot_f1)
```

#### [예상 결과]
```text
--- 원본 데이터 (summary_df) ---
     Model        Method  Test F1-Score
0  Model_A    GridSearch           0.85
1  Model_A  RandomSearch           0.82
2  Model_B    GridSearch           0.90
3  Model_B  RandomSearch           0.88


--- 피벗된 결과 (pivot_f1) ---
Method   GridSearch  RandomSearch
Model                            
Model_A        0.85          0.82
Model_B        0.90          0.88
```

💡 **한 줄 요약:** 길쭉하고 복잡했던 원본 데이터(`summary_df`)가 `pivot_table`을 거치면서, **모델별 & 방법별 F1-점수**를 바둑판처럼 한눈에 비교할 수 있는 예쁜 표(`pivot_f1`)로 변신했습니다!