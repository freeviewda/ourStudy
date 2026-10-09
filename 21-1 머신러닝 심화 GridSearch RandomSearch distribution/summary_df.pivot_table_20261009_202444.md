# summary_df.pivot_table - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 20:24:44

---

파이썬의 데이터 분석 라이브러리인 판다스(Pandas)에서 사용되는 `pivot_table` 함수에 대한 상세 해설입니다. 초보자의 눈높이에 맞춰 하나씩 친절하게 설명해 드릴게요!

---

### 1. 📌 함수 개요
`summary_df.pivot_table()`은 **엑셀의 '피벗 테이블' 기능과 정확히 똑같은 역할**을 하는 함수입니다. 
데이터프레임의 데이터를 우리가 보기 편하도록 **특정 기준(행과 열)에 따라 재배치하고, 데이터 요약(평균, 합계 등)을 수행**할 때 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석
제공해주신 코드에서 사용된 3개의 인자 각각이 어떤 역할을 하는지 살펴봅니다.

* **`values='Test Accuracy'`**
  * **역할**: 테이블의 **'칸(셀) 안을 채울 값'**을 지정합니다.
  * **의미**: 원래 데이터프레임에서 'Test Accuracy'(테스트 정확도)라는 열에 있는 숫자들을 가져와서 피벗 테이블의 빈칸에 채워 넣겠다는 뜻입니다.

* **`index='Model'`**
  * **역할**: 테이블의 **'행(Row, 가로 줄)'**로 배치할 기준을 지정합니다.
  * **의미**: 'Model'(모델 이름, 예: ResNet, BERT 등) 열에 있는 종류별로 행을 하나씩 만들겠다는 뜻입니다.

* **`columns='Method'`**
  * **역할**: 테이블의 **'열(Column, 세로 줄)'**로 배치할 기준을 지정합니다.
  * **의미**: 'Method'(학습 방법, 예: Baseline, Fine-tuning 등) 열에 있는 종류별로 열을 쫙 펼쳐서 배치하겠다는 뜻입니다.

---

### 3. 📤 반환값/할당 변수 (`pivot_acc`)
* **할당되는 변수**: `pivot_acc`
* **설명**: 위 함수의 실행 결과로 **새로운 판다스 데이터프레임(DataFrame)**이 만들어져 `pivot_acc`에 저장됩니다.
* 이 데이터프레임은 행에는 `Model`, 열에는 `Method`가 위치하고, 각 칸에는 해당 모델과 방법에 따른 `Test Accuracy` 값이 쏙쏙 들어가 있는 **격자 형태(Matrix)**의 깔끔한 표가 됩니다.

---

### 4. 🎁 요약 및 실행 예시
백문이 불여일견! 초보자분들이 직접 실행해 볼 수 있는 간단한 코드를 준비했습니다.

#### [실습 코드]
```python
import pandas as pd

# 1. 샘플 데이터(summary_df) 만들기
data = {
    'Model': ['Model_A', 'Model_A', 'Model_B', 'Model_B'],
    'Method': ['Scratch', 'Fine-tune', 'Scratch', 'Fine-tune'],
    'Test Accuracy': [0.85, 0.92, 0.78, 0.88]
}
summary_df = pd.DataFrame(data)

print("--- 원본 데이터 (summary_df) ---")
print(summary_df)
print("\n" + "="*40 + "\n")

# 2. 피벗 테이블 만들기 (질문하신 코드!)
pivot_acc = summary_df.pivot_table(values='Test Accuracy', index='Model', columns='Method')

print("--- 변환된 결과 (pivot_acc) ---")
print(pivot_acc)
```

#### [예상 결과]
```text
--- 원본 데이터 (summary_df) ---
     Model     Method  Test Accuracy
0  Model_A    Scratch           0.85
1  Model_A  Fine-tune           0.92
2  Model_B    Scratch           0.78
3  Model_B  Fine-tune           0.88

========================================

--- 변환된 결과 (pivot_acc) ---
Method   Fine-tune  Scratch
Model                      
Model_A       0.92     0.85
Model_B       0.88     0.78
```

#### 💡 **결과 해석**
길고 복잡하게 나열되어 있던 데이터(`summary_df`)가, `pivot_table`을 거치니 **모델별(행) & 학습방법별(열) 정확도**가 한눈에 비교되는 깔끔한 표(`pivot_acc`)로 변신한 것을 확인할 수 있습니다!