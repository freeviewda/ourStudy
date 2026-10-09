# pima.target.map - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 21:35:16

---

`pima.target.map({'tested_negative': 0, 'tested_positive': 1}).astype(int)` 코드에서 사용된 **Pandas의 `map()` 함수와 전체 문맥**을 초보자의 눈높이에 맞춰 친절하게 설명해 드릴게요.

---

### 1. 📌 함수 개요
* `map()`은 판다스(Pandas) 시리즈(데이터프레임의 한 열)에 있는 데이터를 **내가 정한 규칙에 따라 새로운 값으로 1:1 변환(매핑)**해 주는 함수입니다.
* 머신러닝 모델은 문자열을 이해하지 못하기 때문에, **문자 형태의 정답 레이블을 컴퓨터가 계산할 수 있는 숫자(0과 1)로 변환**할 때 주로 사용합니다.

---

### 2. 🔍 입력 인자(매개변수) 분석

코드에서 `map()` 함수 내부에는 **파이썬 딕셔너리(`{key: value}`)**가 인자로 전달되었습니다.

* **`{'tested_negative': 0, 'tested_positive': 1}` (변환 사전)**
  * **역할:** 어떤 기존 값을 어떤 새 값으로 바꿀지 정의한 '변환 규칙 표'입니다.
  * **`'tested_negative': 0`**: 기존 데이터에 `'tested_negative'`(음성/정상)라는 글자가 있으면 숫자 **`0`**으로 바꿉니다.
  * **`'tested_positive': 1`**: 기존 데이터에 `'tested_positive'`(양성/당뇨 발병)라는 글자가 있으면 숫자 **`1`**로 바꿉니다.
  * *(참고)* 만약 사전에 적혀있지 않은 다른 글자가 데이터에 들어있다면, 그 자리는 `NaN`(결측치/빈값)으로 변환됩니다.

*(부가 설명)*
* **뒤에 붙은 `.astype(int)`**: `map()`으로 바꾼 결과를 **정수형(Integer)** 데이터 타입으로 확실하게 굳혀주는 역할을 합니다.

---

### 3. 📤 반환값 및 할당 변수

* **반환값 (`pima.target.map(...)`의 결과)**
  * 기존의 문자열(`'tested_negative'`, `'tested_positive'`)이 전부 숫자(`0`, `1`)로 치환된 **새로운 판다스 시리즈(Series)**가 반환됩니다.
* **할당 변수 `y`**
  * 머신러닝에서 예측의 목표가 되는 **정답 데이터(타깃/라벨, Target/Label)**를 담는 변수입니다.
  * 이제 `y`에는 모델 학습에 바로 사용할 수 있는 숫자 `[0, 1, 0, 0, 1, ...]` 형태의 정답 데이터가 깔끔하게 저장됩니다.

---

### 4. 🎁 요약 및 실행 예시

직접 복사해서 주피터 노트북이나 파이썬 쉘에 실행해 볼 수 있는 미니 코드입니다.

#### [실행 코드]
```python
import pandas as pd

# 1. 예시 데이터 만들기 (기존 pima.target과 유사한 형태)
target_data = pd.Series(
    ["tested_negative", "tested_positive", "tested_negative", "tested_positive"]
)

print("--- [변환 전] ---")
print(target_data)

# 2. 질문하신 코드 실행 (문자 -> 숫자 매핑 후 정수형 변환)
y = target_data.map({"tested_negative": 0, "tested_positive": 1}).astype(int)

print("\n--- [변환 후 (변수 y)] ---")
print(y)
```

#### [출력 결과]
```text
--- [변환 전] ---
0    tested_negative
1    tested_positive
2    tested_negative
3    tested_positive
dtype: object

--- [변환 후 (변수 y)] ---
0    0
1    1
2    0
3    1
dtype: int64
```

> **한 줄 요약:** 
> 문자열로 된 검사 결과(`tested_negative`, `tested_positive`)를 머신러닝 모델이 학습할 수 있도록 **0과 1의 정수 데이터로 변환하여 `y`에 담는 과정**입니다.