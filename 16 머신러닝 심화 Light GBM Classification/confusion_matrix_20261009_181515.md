# confusion_matrix - AI 파이썬 학습 노트

- 생성 일시: 2026-10-09 18:15:15

---

`confusion_matrix(y_test, y_pred)`는 실제 클래스와 예측 클래스를 교차 분석한 2x2 혼동 행렬(TN, FP, FN, TP)을 계산하는 함수예요.

정상 환자를 정상으로 맞춘 수(TN)와 당뇨 환자를 정확히 찾아낸 수(TP), 그리고 오진단(FP, FN) 건수를 수치로 파악합니다.
