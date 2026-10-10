# OurStudy 프로젝트 에이전트 행동 지침 및 표준 규칙 (AGENTS.md)

이 문서는 `d:\ourStudy` 저장소에서 작업하는 모든 AI 어시스턴트(Antigravity 등)가 다음 대화 및 향후 모든 작업에서 반드시 영구적으로 기억하고 준수해야 하는 **불변의 표준 규칙(Ground Truth)**입니다.

---

## 1. 프로젝트 개요 및 트랙 분기
- 저장소는 머신러닝 **기초 과정(01~16)**과 **심화 과정(01, 02, 05, ...)**의 듀얼 트랙으로 구성됩니다.
- 메인 허브 포털: [`index.html`](./index.html) (기초/심화 탭 전환, 실시간 다크/라이트 테마 동기화)

---

## 2. 머신러닝 심화 강좌(Advanced Track) 황금 표준 (Golden Standard)
모든 심화 강좌는 [`01 머신러닝 심화 Mean Shift Clustering`](./01%20머신러닝%20심화%20Mean%20Shift%20Clustering)의 규격을 100% 동일하게 따라야 합니다.

### 🎨 테마 및 시각 디자인
- **테마 팔레트**: 일렉트릭 앰버 & 네온 오렌지 (`--accent-primary: #f97316` / 다크: `#fb923c`, `--accent-secondary: #fbbf24`, `--accent-glow: rgba(249, 115, 22, 0.35)`). 기초 트랙의 스카이블루(`#38bdf8`) 및 기존 바이올렛과 명확히 구분되는 세련된 주황색 계열을 적용합니다.
- **상단 영웅 배너**: `.module-hero` (학습 목표, 실무 팁, 핵심 알고리즘 요약).
- **이미지 줌 모달**: 차트 클릭 시 고화질 풀스크린 팝업 `#zoom-modal` 필수 탑재.
- **인터랙티브 키워드**: 코드 가독성을 저해하는 전등 이모티콘(`💡`)은 일체 삽입하지 않으며, 함수명에 깔끔한 점선 언더라인(`border-bottom: 1.5px dashed var(--accent-primary)`) 및 클릭 시 우측 해설 탭으로 점프합니다.
- **브레드크럼**: `홈 > 심화 트랙 > 챕터` 내비게이션 바.

### 📐 단계 분리 원칙 (Step 1 Separation Principle)
- **1단계 (필수 라이브러리 임포트 및 분석 환경 구축)**:
  - 오직 순수 라이브러리 임포트 셀(`In [2]`)만 단독 배치합니다.
  - 우측 해설 탭도 임포트 관련 노트만 단독 표시합니다.
  - **절대 데이터 로드나 EDA를 1단계에 합치지 않습니다.**
- **2단계 (데이터셋 로드 및 탐색적 데이터 분석 EDA / 전처리)**:
  - 실제 데이터 로드(`fetch_openml`, `load_wine` 등)와 타깃 인코딩, 형상 확인, EDA 셀들을 2단계부터 시작합니다.

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

### 💻 코드 에디터 배경색 규칙 (#2d2d2d)
- **VS Code Tomorrow Night 다크 에디터 룩**:
  ```css
  .code-editor-look {
    background: #2d2d2d;
    border: 1px solid #3e4451;
    border-radius: 8px;
    padding: 1.1rem 1.35rem;
    font-family: 'Fira Code', monospace;
    font-size: 0.88rem;
    line-height: 1.6;
    overflow-x: auto;
    margin-bottom: 0.85rem;
  }
  .code-editor-look pre, .code-editor-look code {
    background: transparent !important;
  }
  :root[data-theme="light"] .code-editor-look {
    background: #2d2d2d;
    border-color: #3e4451;
    color: #f8fafc;
  }
  .note-code-block {
    background: #2d2d2d;
    border: 1px solid #3e4451;
    border-radius: 8px;
  }
  ```
  - 라이트 모드 전환 시에도 터미널/코드 영역은 완벽한 시인성을 위해 `#2d2d2d` 딥 다크 에디터 룩을 유지합니다.

### 🖥️ 50:50 완전 독립 분할 뷰 & 클릭 노출 규격 (Split-Screen & Click-to-Reveal)
- **독립 스크롤 분할 레이아웃 (Split-Screen Architecture)**:
  - 브라우저 창 전체 높이(`100vh`)를 좌/우 50% : 50%로 고정 분할합니다.
  - **좌측 패널 (`.split-pane-left`)**: 1단계부터 마지막 단계까지의 모든 코드와 실행 결과가 하나의 독립 스크롤 영역(`height: 100%; overflow-y: auto`)에 배치되어, 마우스 휠을 아래로 내려도 우측은 1px도 움직이지 않고 고정됩니다.
  - **우측 패널 (`.split-pane-right`)**: 화면에 완전 고정되어 우측 패널 내부에서만 독립 스크롤(`height: 100%; overflow: hidden`)됩니다.
- **클릭 시 노출 인터랙션 (Click-to-Reveal)**:
  - **초기 대기 상태 (`.notes-standby-view`)**: 처음 페이지를 열었을 때는 우측에 해설이 펼쳐지지 않고, 세련된 대기 안내 카드(📖 AI 인터랙티브 학습 노트 가이드)가 표시됩니다.
  - **클릭 시 즉시 오픈 (`.notes-active-view`)**: 좌측 코드 속의 주황 점선 언더라인 키워드(`.interactive-kw`)를 클릭했을 때만 해당 함수의 상세 AI 해설 노트가 우측에 즉시 펼쳐집니다.
  - **해설 닫기 버튼 (`#desk-close-btn`)**: 우측 상단에 `[✕ 해설 닫기]` 버튼을 제공하여 언제든 대기 상태로 원터치 복귀할 수 있습니다.
  - **상단 퀵 내비게이션 바 동기화**: 상단 스텝 버튼 클릭 시 좌측 패널이 해당 스텝 위치로 스무스 스크롤되며, 좌측 스크롤 위치에 따라 상단 스텝 뱃지가 실시간 활성화됩니다.

### 📄 듀얼 출력 파일 네이밍 규격
- 심화 강좌는 반드시 두 개의 HTML 파일을 동일하게 생성/동기화합니다:
  - Ch 01: `index.html` + `index01.html`
  - Ch 02: `index.html` + `index02.html`
  - Ch 05: `index.html` + `index05.html`
  - 향후 후속 심화 모듈: `index.html` + `indexNN.html`

---

## 3. 타임스탬프 순서 엄격 준수 (Chronological 100%)
- 모든 AI 해설 노트는 마크다운 파일명 및 본문에 기록된 작업 일시(타임스탬프) 기준 **100% 오름차순 시간순 정렬**되어야 합니다.

---

## 4. Git 커밋 및 배포 원칙
- **`.ipynb` 및 `*.py` 파일은 절대 Git 커밋하지 않습니다** (오직 `.html`, `.md` 웹 에셋 및 포털만 반영).
- 작업 완료 후 GitHub 원격 저장소(`origin/main`)에 푸시하여 배포 상태를 유지합니다.
