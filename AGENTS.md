# OurStudy 프로젝트 에이전트 행동 지침 및 표준 규칙 (AGENTS.md)

이 문서는 `d:\ourStudy` 저장소에서 작업하는 모든 AI 어시스턴트(Antigravity 등)가 다음 대화 및 향후 모든 작업에서 반드시 영구적으로 기억하고 준수해야 하는 **불변의 표준 규칙(Ground Truth)**입니다.

---

## 1. 프로젝트 개요 및 트랙 분기
- 저장소는 머신러닝 **기초 과정(01~16)**과 **심화 과정(01, 02, 05, 05_1, 06_1, 07, 08, 08_1, 09, 16, 18, 21-1, 22-1, 23, 24 등)**의 듀얼 트랙으로 구성됩니다.
- 메인 허브 포털: [`index.html`](./index.html) (기초/심화 탭 전환, 실시간 다크/라이트 테마 동기화)
- **포털 화면 규칙**: "오픈 예정" 뱃지나 오픈 예정 카드는 화면에 일체 노출하지 않으며, 실제 사용 가능한 완성 모듈만 깔끔하게 노출합니다.

---

## 2. 머신러닝 심화 강좌(Advanced Track) 황금 표준 (Golden Standard)
모든 심화 강좌는 아래의 표준 규격을 100% 동일하게 따라야 합니다.

### 🎨 테마 및 시각 디자인
1. **기본 테마 (Light Mode Default)**:
   - 모든 페이지의 초기 로딩 기본값은 **라이트 모드 (Light Mode)**입니다.
   - `html` 태그는 `data-theme="light"`로 로드되며, 상단 테마 토글 스위치(`theme-toggle`)는 언체크(unchecked) 상태를 기본값으로 유지합니다.
   - 사용자가 스위치를 켰을 때만 다크 모드(`data-theme="dark"`)로 전환됩니다.
2. **안티그래비티 스타일 소프트 차콜 다크 코드/콘솔 에디터 룩**:
   - 코드 에디터 및 터미널 출력 영역은 눈부신 순백색이나 쨍한 검정을 피하고, 눈이 가장 편안한 **소프트 차콜 다크 톤**을 적용합니다.
   - **배경색**: `#1f1f1f` 또는 `#1e1e1e` (자극 없는 편안한 소프트 차콜)
   - **글자색**: `#cccccc` 또는 `#d4d4d4` (은은하고 따뜻한 웜 그레이/오프화이트)
   - **테두리**: `#3e4451`
   - **라이트 모드에서도 코드/콘솔 영역 톤 유지**: 라이트 모드 전환 시에도 코드 블록, 콘솔 출력 영역, 프리뷰는 위 편안한 딥 다크 에디터 룩(`background: #1f1f1f !important; color: #cccccc !important;`)을 그대로 유지하여 최상의 코드 가독성을 보장합니다.
3. **눈부심 방지 텍스트 톤 (Anti-Glare)**:
   - 눈을 찌르는 강한 순백색(`#ffffff`) 텍스트 및 배경을 배제하고, 차분하고 부드러운 톤(`#e0e0e0`, `#cccccc`, `#2d3748`)을 적용합니다.
4. **자연스러운 클린 코드 키워드 스타일**:
   - 코드 내부의 링크 걸린 함수명에는 눈 피로도를 유발하는 파란색/주황색 배경 박스나 강제 글자색을 일체 적용하지 않으며, 네이티브 코드 하이라이트(`background: transparent !important; color: inherit !important; border: none !important;`)를 100% 유지합니다.
   - 마우스 호버 시에만 부드러운 언더라인과 포인터 커서가 표시되고, 클릭 시 우측 AI 학습 노트로 즉시 연결됩니다.
   - 코드 가독성을 저해하는 전등 이모티콘(`💡`)은 일체 삽입하지 않습니다.
5. **하단 푸터 바 완전 제거 (Zero Bottom Footer)**:
   - 화면 맨 아래 공간을 낭비하고 시선을 분산시키는 하단 푸터 바(`viewer-footer`, `portal-footer`, `💡 OurStudy 머신러닝 심화 시리즈...`)는 일체 배치하지 않습니다 (`display: none !important;`).
   - 브라우저 뷰포트 맨 아래 끝(100vh)까지 50:50 좌우 분할 패널이 가득 차도록 설계합니다.
6. **상단 영웅 배너 및 이미지 줌 모달**:
   - 상단 영웅 배너: `.module-hero` (학습 목표, 실무 팁, 핵심 알고리즘 요약)
   - 이미지 줌 모달: 차트 클릭 시 고화질 풀스크린 팝업 `#zoom-modal` 탑재
   - 브레드크럼: `홈 > 심화 트랙 > 챕터` 내비게이션 바 탑재

---

### 🖥️ 50:50 완전 독립 분할 뷰 & 스텝 범위 한정 클릭 인터랙션 (Split-Screen & Step-Scoped Interaction)
1. **독립 스크롤 분할 레이아웃 (Split-Screen Architecture)**:
   - 브라우저 창 전체 높이(`100vh`)를 좌/우 50% : 50%로 고정 분할합니다.
   - **좌측 패널 (`.split-pane-left`)**: 1단계부터 마지막 단계까지의 모든 코드와 실행 결과가 하나의 독립 스크롤 영역(`height: 100%; overflow-y: auto`)에 배치되어, 마우스 휠을 아래로 내려도 우측은 1px도 움직이지 않고 고정됩니다.
   - **우측 패널 (`.split-pane-right`)**: 화면에 완전 고정되어 우측 패널 내부에서만 독립 스크롤(`height: 100%; overflow: hidden`)됩니다.
2. **클릭 시 노출 인터랙션 (Click-to-Reveal)**:
   - **초기 대기 상태 (`.notes-standby-view`)**: 페이지 로드 시에는 우측에 해설을 미리 펼치지 않고, 세련된 대기 안내 카드(📖 AI 인터랙티브 학습 노트 가이드)를 표시합니다.
   - **클릭 시 즉시 오픈 (`.notes-active-view`)**: 좌측 코드 속 키워드(`.interactive-kw`)를 클릭했을 때만 해당 함수의 상세 AI 해설 노트가 우측에 즉시 펼쳐집니다.
   - **해설 닫기 버튼 (`#desk-close-btn`)**: 우측 상단에 `[✕ 해설 닫기]` 버튼을 제공하여 언제든 대기 상태로 원터치 복귀할 수 있습니다.
3. **스텝 범위 한정 매칭 (Step-Scoped Click Matching)**:
   - 여러 스텝에 동일한 함수명(예: `fetch_openml`, `fit`, `predict` 등)이 반복 등장할 경우, 상단 스텝 1로 잘못 점프하는 일이 없도록 반드시 **클릭한 키워드가 속한 해당 스텝 컨테이너(`closest('.timeline-step')`)** 내부의 해설 탭으로만 정확하게 매칭되어 열리도록 구현합니다.
4. **상단 퀵 내비게이션 바 동기화**:
   - 상단 스텝 버튼 클릭 시 좌측 패널이 해당 스텝 위치로 스무스 스크롤되며, 좌측 스크롤 위치에 따라 상단 스텝 뱃지가 실시간 활성화됩니다.

---

### 📐 단계 분리 원칙 (Step 1 Separation Principle)
- **1단계 (필수 라이브러리 임포트 및 분석 환경 구축)**:
  - 오직 순수 라이브러리 임포트 셀(`In [2]`)만 단독 배치합니다.
  - 우측 해설 탭도 임포트 관련 노트만 단독 표시합니다.
  - **절대 데이터 로드나 EDA를 1단계에 합치지 않습니다.**
- **2단계 (데이터셋 로드 및 탐색적 데이터 분석 EDA / 전처리)**:
  - 실제 데이터 로드(`fetch_openml`, `load_wine` 등)와 타깃 인코딩, 형상 확인, EDA 셀들을 2단계부터 시작합니다.

---

### 🏷️ 우측 AI 학습 노트 탭 UI 규칙
- **헤더 타이틀**: `<div class="tabs-label">📖 AI 학습 노트 ({count})</div>`
- **다중행 래핑 레이아웃**: `.tabs-scroll-wrapper`는 반드시 `display: flex; flex-wrap: wrap; gap: 0.5rem;`을 사용하여 탭 버튼들이 아래로 정돈되어 한눈에 들어오게 합니다 (단일행 가로 스크롤 금지).
- **간결한 탭 텍스트**: 버튼 텍스트에 `[HH:MM:SS]` 타임스탬프를 넣지 않고, `import pandas as pd`, `import StandardScaler`, `import DBSCAN` 등 간결한 함수/라이브러리명만 표기합니다 (타임스탬프는 노트 본문 상단 메타 뱃지 `⏱️ YYYY-MM-DD HH:MM:SS`에 표기).
- **활성화 탭 스타일**:
  ```css
  .func-tab-btn.active {
    background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
    border-color: transparent;
    color: #ffffff !important;
    box-shadow: 0 4px 12px var(--accent-glow);
  }
  ```

---

### 📄 듀얼 출력 파일 네이밍 규격
- 심화 강좌는 반드시 두 개의 HTML 파일을 동일하게 생성/동기화합니다:
  - Ch 01: `index.html` + `index01.html`
  - Ch 02: `index.html` + `index02.html`
  - Ch 05: `index.html` + `index05.html`
  - Ch 05_1: `index.html` + `index05-1.html` + `index05_1.html`
  - Ch 06_1: `index.html` + `index06-1.html` + `index06_1.html`
  - Ch 07: `index.html` + `index07.html`
  - Ch 08: `index.html` + `index08.html`
  - Ch 08_1: `index.html` + `index08_1.html`
  - Ch 09: `index.html` + `index09.html`
  - Ch 16: `index.html` + `index16.html`
  - Ch 18: `index.html` + `index18.html`
  - Ch 21-1: `index.html` + `index21_1.html`
  - Ch 22-1: `index.html` + `index22_1.html`
  - Ch 23: `index.html` + `index23.html`
  - Ch 24: `index.html` + `index24.html`
  - 향후 후속 심화 모듈: `index.html` + `indexNN.html`

---

## 3. 타임스탬프 순서 엄격 준수 (Chronological 100%)
- 모든 AI 해설 노트는 마크다운 파일명 및 본문에 기록된 작업 일시(타임스탬프) 기준 **100% 오름차순 시간순 정렬**되어야 합니다.

---

## 4. Git 커밋 및 배포 원칙
- **`.ipynb` 및 `*.py` 파일은 절대 Git 커밋하지 않습니다** (오직 `.html`, `.md` 웹 에셋 및 포털만 반영).
- 작업 완료 후 GitHub 원격 저장소(`origin/main`)에 푸시하여 배포 상태를 유지합니다.
