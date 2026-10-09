# summary_df.pivot_table - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:31:25

---

파이썬 데이터 분석 라이브러리인 **Pandas**에서 가장 유용하고 자주 쓰이는 함수 중 하나인 `pivot_table`에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 쉽고 명쾌하게 정리해 드릴게요!

---

### 1. 📌 함수 개요
`summary_df.pivot_table(...)`은 **엑셀의 '피벗 테이블' 기능과 똑같은 역할**을 하는 함수입니다. 커다란 표(데이터프레임)에서 우리가 원하는 데이터만 쏙쏙 골라, **행과 열을 기준으로 보기 쉽게 요약·재배치**해 줍니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제시된 코드에서 사용된 3가지 인자의 역할은 다음과 같습니다.

*   **`values='Test Accuracy'`**
    *   **역할:** 표의 **알맹이(채워질 값)**로 사용할 데이터를 지정합니다.
    *   **의미:** 요약된 표 안쪽 칸들에 'Test Accuracy(테스트 정확도)' 숫자들을 채워 넣겠다는 뜻입니다.
*   **`index='Model'`**
    *   **역할:** 표의 **행(가로줄 기준)**으로 사용할 열(Column)을 지정합니다.
    *   **의미:** 표의 맨 왼쪽에 모델 이름들(예: ResNet, BERT 등)이 세로로 쭈르륵 나열되도록 만듭니다.
*   **`columns='Method'`**
    *   **역할:** 표의 **열(세로줄 기준)**으로 사용할 열(Column)을 지정합니다.
    *   **의미:** 표의 맨 위쪽에 분석 방법들(예: Baseline, Fine-tuning 등)이 가로로 쭈르륵 나열되도록 만듭니다.

---

### 3. 📤 반환값/할당 변수 (`heatmap_data`)
*   **반환되는 데이터:** 인자들을 바탕으로 재구조화된 **새로운 Pandas 데이터프레임(표)**이 만들어집니다.
*   **`heatmap_data` 변수의 의미:** 
    *   행에는 `Model`, 열에는 `Method`, 값에는 `Test Accuracy`가 들어간 **2차원 형태의 요약 표**가 저장됩니다.
    *   변수 이름(`heatmap_data`)에서 유추할 수 있듯, 이 결과물은 나중에 시각화 라이브러리(Seaborn 등)를 사용해 **히트맵(Heatmap, 색상으로 수치의 높낮이를 표현하는 그림)을 그리기 딱 좋은 형태**로 변환된 것입니다.

---

### 4. 🎁 요약 및 실행 예시
백문이 불여일견! 초보자도 직접 실행해 볼 수 있는 간단한 코드를 준비했습니다.

#### 🛠️ 실습 코드
```python
import pandas as pd

# 1. 엉성한 원본 데이터프레임 만들기
data = {
    'Model': ['Model_A', 'Model_A', 'Model_B', 'Model_B'],
    'Method': ['Method_1', 'Method_2', 'Method_1', 'Method_2'],
    'Test Accuracy': [0.85, 0.90, 0.78, 0.88]
}
summary_df = pd.DataFrame(data)

print("--- 원본 summary_df ---")
print(summary_df)
print("\n" + "="*30 + "\n")

# 2. pivot_table 적용하기 (질문하신 코드!)
heatmap_data = summary_df.pivot_table(values='Test Accuracy', index='Model', columns='Method')

print("--- 변환된 heatmap_data ---")
print(heatmap_data)
```

#### 📊 예상 결과
```text
--- 원본 summary_df ---
     Model    Method  Test Accuracy
0  Model_A  Method_1           0.85
1  Model_A  Method_2           0.90
2  Model_B  Method_1           0.78
3  Model_B  Method_2           0.88

==============================

--- 변환된 heatmap_data ---
Method   Method_1  Method_2
Model                      
Model_A      0.85      0.90
Model_B      0.78      0.88
```

> **💡 한 줄 요약:** 길쭉하고 보기 힘들었던 데이터(`summary_df`)를, 모델별·방법별로 정확도를 한눈에 비교할 수 있는 깔끔한 격자 모양의 표(`heatmap_data`)로 변환해 주는 마법 같은 함수입니다!