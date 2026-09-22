#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_viewer.py for 07 머신러닝 기초_회귀_성능_지표
- 머신러닝 기초 회귀 성능 지표 ipynb 파일과 34개의 AI 해설 마크다운 노트를
  단계별 듀얼(좌: 코드+결과 / 우: 해설) 인터랙티브 웹 애플리케이션으로 번들링/생성하는 빌더 스크립트
- 한글 깨짐 방지용 koreanize-matplotlib 설치 셀(!pip install koreanize-matplotlib 및 Collecting...)은 사용자 요청에 따라 제외
"""

import os
import sys
import glob
import json
import re
import html

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTEBOOK_PATH = os.path.join(WORKSPACE_DIR, "07_머신러닝_기초_회귀_성능_지표.ipynb")
OUTPUT_HTML_PATH = os.path.join(WORKSPACE_DIR, "index07.html")

def md_to_html(md_text):
    """
    경량 마크다운 -> 깔끔한 HTML 변환기
    """
    lines = md_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    html_lines = []
    in_list = False
    in_code_block = False
    code_lang = ""
    code_buffer = []

    def close_list():
        nonlocal in_list
        if in_list:
            html_lines.append("</ul>")
            in_list = False

    def inline_format(text):
        text = html.escape(text)
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.+?)`', r'<code class="inline-code">\1</code>', text)
        return text

    for line in lines:
        stripped = line.strip()

        # Code block handler
        if stripped.startswith("```"):
            close_list()
            if in_code_block:
                in_code_block = False
                code_content = html.escape("\n".join(code_buffer))
                html_lines.append(f'<pre class="note-code-block"><code class="language-{code_lang}">{code_content}</code></pre>')
                code_buffer = []
            else:
                in_code_block = True
                code_lang = stripped[3:].strip()
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Horizontal rule
        if stripped in ["---", "***", "___"]:
            close_list()
            html_lines.append('<hr class="note-divider" />')
            continue

        # Headings
        if stripped.startswith("# "):
            close_list()
            h_text = inline_format(stripped[2:].strip())
            html_lines.append(f'<h1 class="note-h1">{h_text}</h1>')
            continue
        if stripped.startswith("## "):
            close_list()
            h_text = inline_format(stripped[3:].strip())
            html_lines.append(f'<h2 class="note-h2">{h_text}</h2>')
            continue
        if stripped.startswith("### "):
            close_list()
            h_text = inline_format(stripped[4:].strip())
            html_lines.append(f'<h3 class="note-h3">{h_text}</h3>')
            continue
        if stripped.startswith("#### "):
            close_list()
            h_text = inline_format(stripped[5:].strip())
            html_lines.append(f'<h4 class="note-h4">{h_text}</h4>')
            continue

        # Lists
        if stripped.startswith(("* ", "- ")):
            if not in_list:
                html_lines.append('<ul class="note-list">')
                in_list = True
            item_text = inline_format(stripped[2:].strip())
            html_lines.append(f'<li class="note-list-item">{item_text}</li>')
            continue

        # Empty line
        if not stripped:
            close_list()
            continue

        # Normal paragraph
        close_list()
        p_text = inline_format(stripped)
        html_lines.append(f'<p class="note-p">{p_text}</p>')

    close_list()
    return "\n".join(html_lines)


def load_markdown_files():
    """
    디렉토리 내의 모든 *.md 파일을 읽어 분석 및 인덱싱
    """
    md_files = glob.glob(os.path.join(WORKSPACE_DIR, "*.md"))
    notes = []

    # 직관적이고 상세한 탭 버튼 라벨 매핑
    label_overrides = {
        # 1단계
        "load_diabetes_해설_20260922_122256": "load_diabetes",
        "diabetes.data_해설_20260922_122310": "diabetes.data",
        "diabetes.target_해설_20260922_122319": "diabetes.target",
        "diabetes.feature_names_해설_20260922_122330": "diabetes.feature_names",
        "pd.DataFrame_해설_20260922_122346": "pd.DataFrame",
        "df.head_해설_20260922_122413": "df.head",
        "display_해설_20260922_122448": "display",

        # 2단계
        "train_test_split_해설_20260922_122512": "train_test_split",
        "X_train.shape_해설_20260922_122530": "X_train.shape (학습 문제)",
        "X_test.shape_해설_20260922_122539": "X_test.shape (시험 문제)",
        "y_train.shape_해설_20260922_122546": "y_train.shape (학습 정답)",
        "y_test.shape_해설_20260922_122557": "y_test.shape (시험 정답)",

        # 3단계
        "LinearRegression_해설_20260922_122614": "LinearRegression",
        "lr.fit_해설_20260922_122628": "lr.fit (X_train, y_train)",

        # 4단계
        "lr.predict_해설_20260922_122655": "lr.predict (X_test)",

        # 5단계
        "sklearn.metrics_해설_20260922_122717": "sklearn.metrics (평가지표 모듈)",
        "mean_absolute_error_해설_20260922_122735": "MAE (개요: 평균 절대 오차)",
        "mean_squared_error_해설_20260922_122743": "MSE (개요: 평균 제곱 오차)",
        "mean_absolute_error_해설_20260922_122834": "MAE 계산 (실제값 vs 예측값)",
        "mean_squared_error_해설_20260922_122850": "MSE 계산 (오차 제곱 페널티)",
        "np.sqrt_해설_20260922_122902": "np.sqrt (RMSE 제곱근 오차)",

        # 6단계
        "mean_absolute_percentage_error_해설_20260922_122802": "MAPE (개요: 백분율 오차)",
        "mean_squared_log_error_해설_20260922_122809": "RMSLE (개요: 로그 오차)",
        "mean_absolute_percentage_error_해설_20260922_122923": "MAPE 계산 (상대 비율 오차)",
        "any_해설_20260922_123004": "any (음수값 유무 검사)",
        "np.maximum_해설_20260922_123015": "np.maximum (음수 0 보정)",
        "mean_squared_log_error_해설_20260922_123040": "MSLE (보정값 safe 계산)",
        "mean_squared_log_error_해설_20260922_123058": "MSLE (일반값 계산)",
        "np.sqrt_해설_20260922_123109": "np.sqrt (보정 RMSLE 산출)",
        "np.sqrt_해설_20260922_123118": "np.sqrt (일반 RMSLE 산출)",

        # 7단계
        "r2_score_해설_20260922_122752": "R2 Score (개요: 결정 계수)",
        "r2_score_해설_20260922_123133": "R2 Score 계산 (모델 설명력)",
        "len_해설_20260922_123144": "len (학습 표본수 n)",
        "X_train.shape_해설_20260922_123155": "X_train.shape (독립변수수 p)"
    }

    for fpath in md_files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        m_func = re.search(r'대상 코드/함수\*\*:\s*`?([^`\n\r]+)`?', content)
        m_date = re.search(r'기록 일시\*\*:\s*([^\n\r]+)', content)

        func_name = m_func.group(1).strip() if m_func else fname.replace(".md", "")
        func_name = func_name.replace("`", "").strip()
        date_str = m_date.group(1).strip() if m_date else ""

        # 라벨 오버라이드 확인
        display_label = func_name
        for pattern, custom_label in label_overrides.items():
            if pattern in fname:
                display_label = custom_label
                break

        html_content = md_to_html(content)

        notes.append({
            "filename": fname,
            "func_name": func_name,
            "display_label": display_label,
            "date": date_str,
            "raw_md": content,
            "html": html_content
        })

    notes.sort(key=lambda x: (x["date"], x["filename"]))
    return notes


def clean_colab_table_html(html_str):
    """
    Colab 특정 버튼/스크립트 제거하고 순수 dataframe <table>만 남기기
    """
    m = re.search(r'(<table[\s\S]*?</table>)', html_str)
    if m:
        table_only = m.group(1)
        table_only = re.sub(r'class="dataframe"', 'class="dataframe modern-table"', table_only)
        return f'<div class="table-responsive-wrapper">{table_only}</div>'
    return html_str


def parse_notebook():
    """
    주피터 노트북을 단계(Step)별로 파싱
    - 사용자 요청에 따라 'koreanize-matplotlib 설치' 관련 마크다운 및 pip install 실행 셀은 완전히 제외
    """
    with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # 파이프라인 단계 정의 (Cell 0, 1은 koreanize-matplotlib 설치이므로 제외)
    steps_def = [
        {
            "id": "step0",
            "number": 0,
            "badge": "준비 단계",
            "title": "라이브러리 Import (Library Import)",
            "summary": "NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn 등 회귀 모델 분석 및 평가지표 산출 필수 패키지 로드",
            "cell_indices": [2, 3]
        },
        {
            "id": "step1",
            "number": 1,
            "badge": "1단계",
            "title": "데이터 로드 및 기본 구조 확인 (Data Loading & Inspection)",
            "summary": "Scikit-Learn 당뇨병(load_diabetes) 데이터셋 로드, 독립변수 특성(X) 및 종속변수 타깃(y) 분리, DataFrame 변환 및 샘플 확인(df.head)",
            "cell_indices": [4, 5, 6]
        },
        {
            "id": "step2",
            "number": 2,
            "badge": "2단계",
            "title": "학습용 및 테스트용 데이터 분할 (Train-Test Split)",
            "summary": "train_test_split을 사용하여 80:20 비율로 데이터를 분할하고, 모델 과적합 방지 및 일반화 평가를 위한 데이터셋 Shape 검증",
            "cell_indices": [7, 8]
        },
        {
            "id": "step3",
            "number": 3,
            "badge": "3단계",
            "title": "선형 회귀 모델 객체 생성 및 학습 (Linear Regression Modeling)",
            "summary": "LinearRegression 인스턴스를 생성하고 fit() 메서드로 학습 데이터를 이용해 최소제곱법(OLS) 기반 최적 회귀선 학습",
            "cell_indices": [9, 10]
        },
        {
            "id": "step4",
            "number": 4,
            "badge": "4단계",
            "title": "테스트 데이터 예측값 산출 (Model Prediction)",
            "summary": "학습된 모델의 predict() 메서드로 미지의 테스트 데이터(X_test)에 대한 예측 타깃값(y_pred) 산출",
            "cell_indices": [11, 12]
        },
        {
            "id": "step5",
            "number": 5,
            "badge": "5단계",
            "title": "오차 기반 대표 평가지표 (MAE, MSE, RMSE)",
            "summary": "실제값과 예측값의 차이를 측정하는 평균 절대 오차(MAE), 큰 오차에 페널티를 주는 평균 제곱 오차(MSE), 원 단위 복원 평균 제곱근 오차(RMSE) 계산",
            "cell_indices": [13, 14]
        },
        {
            "id": "step6",
            "number": 6,
            "badge": "6단계",
            "title": "상대 비율 및 로그 기반 지표 (MAPE, RMSLE)",
            "summary": "스케일 무관 비교를 위한 백분율 오차(MAPE)와 이상치/과소예측 왜곡을 방지하는 로그 오차(RMSLE) 계산 및 음수 예측값 보정 처리",
            "cell_indices": [15, 16]
        },
        {
            "id": "step7",
            "number": 7,
            "badge": "7단계",
            "title": "모델 설명력 및 적합도 평가 (R2 & Adjusted R2 Score)",
            "summary": "종속변수의 전체 분산 중 모델이 설명하는 비율인 결정계수(R2 Score)와 독립변수 추가에 따른 왜곡을 통계적으로 보정한 수정 결정계수 산출",
            "cell_indices": [17, 18]
        }
    ]

    all_cells = nb.get("cells", [])

    parsed_steps = []
    for sdef in steps_def:
        step_cells = []
        for idx in sdef["cell_indices"]:
            if idx < len(all_cells):
                c = all_cells[idx]
                ctype = c.get("cell_type")
                source = "".join(c.get("source", []))

                # 혹시 모를 koreanize-matplotlib 설치 셀 이중 필터링
                if "koreanize-matplotlib 설치" in source or "!pip install koreanize-matplotlib" in source:
                    continue

                parsed_outputs = []
                for out in c.get("outputs", []):
                    otype = out.get("output_type")
                    if otype == "stream":
                        text = "".join(out.get("text", []))
                        # Collecting koreanize-matplotlib 출력 필터링
                        if "Collecting koreanize-matplotlib" in text:
                            continue
                        parsed_outputs.append({
                            "type": "stream",
                            "content": html.escape(text)
                        })
                    elif otype in ["display_data", "execute_result"]:
                        data = out.get("data", {})
                        if "image/png" in data:
                            b64 = data["image/png"]
                            parsed_outputs.append({
                                "type": "image",
                                "content": b64
                            })
                        elif "text/html" in data:
                            raw_html = "".join(data["text/html"])
                            clean_tbl = clean_colab_table_html(raw_html)
                            parsed_outputs.append({
                                "type": "html",
                                "content": clean_tbl
                            })
                        elif "text/plain" in data:
                            text = "".join(data["text/plain"])
                            parsed_outputs.append({
                                "type": "text",
                                "content": html.escape(text)
                            })

                step_cells.append({
                    "cell_idx": idx,
                    "type": ctype,
                    "source": source,
                    "outputs": parsed_outputs
                })

        sdef["cells"] = step_cells
        parsed_steps.append(sdef)

    return parsed_steps


def map_notes_to_steps(steps, notes):
    """
    마크다운 노트를 해당 단계(Step)에 파일명/타임스탬프 패턴으로 완벽하게 매핑
    """
    step_file_patterns = {
        "step0": [],
        "step1": [
            "load_diabetes_해설_20260922_122256",
            "diabetes.data_해설_20260922_122310",
            "diabetes.target_해설_20260922_122319",
            "diabetes.feature_names_해설_20260922_122330",
            "pd.DataFrame_해설_20260922_122346",
            "df.head_해설_20260922_122413",
            "display_해설_20260922_122448"
        ],
        "step2": [
            "train_test_split_해설_20260922_122512",
            "X_train.shape_해설_20260922_122530",
            "X_test.shape_해설_20260922_122539",
            "y_train.shape_해설_20260922_122546",
            "y_test.shape_해설_20260922_122557"
        ],
        "step3": [
            "LinearRegression_해설_20260922_122614",
            "lr.fit_해설_20260922_122628"
        ],
        "step4": [
            "lr.predict_해설_20260922_122655"
        ],
        "step5": [
            "sklearn.metrics_해설_20260922_122717",
            "mean_absolute_error_해설_20260922_122735",
            "mean_squared_error_해설_20260922_122743",
            "mean_absolute_error_해설_20260922_122834",
            "mean_squared_error_해설_20260922_122850",
            "np.sqrt_해설_20260922_122902"
        ],
        "step6": [
            "mean_absolute_percentage_error_해설_20260922_122802",
            "mean_squared_log_error_해설_20260922_122809",
            "mean_absolute_percentage_error_해설_20260922_122923",
            "any_해설_20260922_123004",
            "np.maximum_해설_20260922_123015",
            "mean_squared_log_error_해설_20260922_123040",
            "mean_squared_log_error_해설_20260922_123058",
            "np.sqrt_해설_20260922_123109",
            "np.sqrt_해설_20260922_123118"
        ],
        "step7": [
            "r2_score_해설_20260922_122752",
            "r2_score_해설_20260922_123133",
            "len_해설_20260922_123144",
            "X_train.shape_해설_20260922_123155"
        ]
    }

    step_note_map = {s["id"]: [] for s in steps}

    for n in notes:
        fname = n["filename"]
        func = n["func_name"]

        mapped = False
        for step_id, patterns in step_file_patterns.items():
            for pat in patterns:
                if pat in fname:
                    step_note_map[step_id].append(n)
                    n["step_id"] = step_id
                    n["tab_id"] = f"{step_id}-{func.replace('.', '_')}-{fname[-13:-3]}"
                    mapped = True
                    break
            if mapped:
                break

    for s in steps:
        step_notes = step_note_map.get(s["id"], [])
        step_notes.sort(key=lambda x: (x["date"], x["filename"]))
        s["notes"] = step_notes

    return steps, notes


def highlight_code_keywords(code_str, step_notes, step_id):
    """
    코드 내에서 해설 대상 키워드를 찾아 클릭 가능한 배지/스팬으로 변환
    - 긴 키워드부터 우선 매칭하여 중복 방지
    """
    safe_code = html.escape(code_str)

    # 고유 함수 목록 추출 및 길이 역순 정렬
    unique_funcs = []
    for n in step_notes:
        f = n["func_name"]
        if f not in unique_funcs:
            unique_funcs.append(f)
    unique_funcs.sort(key=lambda x: len(x), reverse=True)

    for func in unique_funcs:
        pattern = re.escape(func)
        # 해당 함수에 매칭되는 가장 대표적인 노트 찾기 (최신 상세 해설 우선)
        matching_notes = [n for n in step_notes if n["func_name"] == func]
        target_note = matching_notes[-1] if matching_notes else None
        tab_id = target_note["tab_id"] if target_note else f"{step_id}-{func.replace('.', '_')}"

        replacement = (
            f'<span class="code-kw-interactive" '
            f'data-step="{step_id}" data-tab="{tab_id}" data-func="{func}" '
            f'title="💡 클릭하여 우측 \'{func}\' 상세 해설 보기">'
            f'{func}<span class="kw-sparkle">💡</span></span>'
        )
        safe_code = re.sub(r'(?<![a-zA-Z0-9_])' + pattern + r'(?![a-zA-Z0-9_])', replacement, safe_code)

    return safe_code


def generate_viewer_html(steps, notes):
    """
    모든 데이터와 UI/UX 요소를 결합하여 최종 index07.html 생성
    """
    steps_nav_html = []
    for s in steps:
        note_count = len(s["notes"])
        badge_count = f'<span class="nav-note-badge">{note_count}개 해설</span>' if note_count > 0 else ''
        steps_nav_html.append(
            f'<a href="#{s["id"]}" class="step-nav-item" data-step="{s["id"]}">'
            f'<span class="step-nav-num">{s["number"]}</span>'
            f'<span class="step-nav-label">{s["title"].split("(")[0].strip()}</span>'
            f'{badge_count}'
            f'</a>'
        )

    sections_html = []

    for s_idx, s in enumerate(steps):
        step_id = s["id"]
        step_title = s["title"]
        step_badge = s["badge"]
        step_summary = s["summary"]
        step_notes = s["notes"]

        # 좌측 컬럼: Jupyter Notebook 코드 및 실행 결과
        code_cells_html = []
        for c in s["cells"]:
            if c["type"] == "markdown":
                md_src = c["source"].strip()
                if not md_src.startswith("### " + step_badge):
                    clean_md = md_to_html(md_src)
                    code_cells_html.append(f'<div class="cell-markdown-box">{clean_md}</div>')
                continue

            if not c["source"].strip():
                continue

            highlighted_code = highlight_code_keywords(c["source"], step_notes, step_id)

            outputs_html = []
            for out in c["outputs"]:
                if out["type"] == "stream":
                    outputs_html.append(
                        f'<div class="output-item stream-output">'
                        f'<div class="output-type-tag">Console Output (콘솔 출력)</div>'
                        f'<pre>{out["content"]}</pre>'
                        f'</div>'
                    )
                elif out["type"] == "html":
                    outputs_html.append(
                        f'<div class="output-item html-table-output">'
                        f'<div class="output-type-tag">Interactive DataFrame / Diagram</div>'
                        f'{out["content"]}'
                        f'</div>'
                    )
                elif out["type"] == "image":
                    outputs_html.append(
                        f'<div class="output-item plot-image-output">'
                        f'<div class="output-type-tag">Visualization Plot</div>'
                        f'<div class="plot-img-container">'
                        f'<img src="data:image/png;base64,{out["content"]}" class="zoomable-plot" alt="Visualization plot" onclick="openLightbox(this.src)" />'
                        f'<div class="img-zoom-overlay" onclick="openLightbox(this.previousElementSibling.src)">🔍 클릭하여 고화질 확대</div>'
                        f'</div></div>'
                    )
                elif out["type"] == "text":
                    outputs_html.append(
                        f'<div class="output-item text-output">'
                        f'<div class="output-type-tag">Execution Result</div>'
                        f'<pre>{out["content"]}</pre>'
                        f'</div>'
                    )

            outputs_rendered = ""
            if outputs_html:
                outputs_rendered = (
                    f'<div class="cell-outputs-container">'
                    f'<div class="outputs-header">'
                    f'<span class="outputs-title">⚡ 실행 결과 ({len(outputs_html)})</span>'
                    f'<button class="toggle-output-btn" onclick="toggleOutput(this)">접기 ▲</button>'
                    f'</div>'
                    f'<div class="outputs-body">{"".join(outputs_html)}</div>'
                    f'</div>'
                )

            code_cells_html.append(
                f'<div class="code-cell-wrapper" id="cell-{c["cell_idx"]}">'
                f'<div class="cell-header">'
                f'<span class="cell-badge">In [{c["cell_idx"]}]</span>'
                f'<div class="cell-actions">'
                f'<button class="copy-code-btn" onclick="copyCode(this)" title="코드 복사">📋 복사</button>'
                f'</div>'
                f'</div>'
                f'<div class="code-editor-look">'
                f'<pre><code class="language-python">{highlighted_code}</code></pre>'
                f'</div>'
                f'{outputs_rendered}'
                f'</div>'
            )

        # 우측 컬럼: AI 함수별 상세 해설 노트 및 탭
        notes_column_html = []
        if step_notes:
            tab_buttons = []
            tab_panes = []

            for idx, n in enumerate(step_notes):
                is_active = (idx == 0)
                active_class = "active" if is_active else ""
                tab_id = n["tab_id"]

                tab_buttons.append(
                    f'<button class="func-tab-btn {active_class}" '
                    f'data-step="{step_id}" data-tab="{tab_id}" onclick="switchTab(\'{step_id}\', \'{tab_id}\')">'
                    f'<span class="tab-func-name">{n["display_label"]}</span>'
                    f'</button>'
                )

                tab_panes.append(
                    f'<div class="func-note-pane {active_class}" id="{tab_id}">'
                    f'<div class="note-meta-header">'
                    f'<div class="note-target-badge">🎯 해설 대상: <code>{n["func_name"]}</code></div>'
                    f'<div class="note-time-badge">⏱ {n["date"]}</div>'
                    f'</div>'
                    f'<div class="note-body-content">'
                    f'{n["html"]}'
                    f'</div>'
                    f'<div class="note-footer-actions">'
                    f'<button class="jump-to-code-btn" onclick="highlightMatchingKeyword(\'{step_id}\', \'{n["func_name"]}\', \'{tab_id}\')">'
                    f'👈 좌측 코드 위치 보기'
                    f'</button>'
                    f'</div>'
                    f'</div>'
                )

            notes_column_html.append(
                f'<div class="notes-panel-container">'
                f'<div class="notes-tabs-header">'
                f'<div class="tabs-label">📖 AI 학습 노트 ({len(step_notes)})</div>'
                f'<div class="tabs-scroll-wrapper">{"".join(tab_buttons)}</div>'
                f'</div>'
                f'<div class="notes-panes-wrapper">{"".join(tab_panes)}</div>'
                f'</div>'
            )
        else:
            notes_column_html.append(
                f'<div class="notes-panel-container">'
                f'<div class="notes-empty-guide">'
                f'<div class="guide-icon">📚</div>'
                f'<h3>회귀 평가 환경 및 라이브러리 안내</h3>'
                f'<p>이 단계에서는 선형 회귀 모델의 예측 성능을 다각도로 정량 평가하기 위한 필수 파이썬 패키지를 로드합니다.</p>'
                f'<div class="lib-cards-grid">'
                f'<div class="lib-card"><strong>koreanize-matplotlib</strong>: 차트 및 시각화 작성 시 한글 폰트 깨짐 현상을 원클릭으로 자동 방지해 주는 필수 유틸리티 패키지</div>'
                f'<div class="lib-card"><strong>sklearn.datasets.load_diabetes</strong>: 442명 당뇨병 환자의 건강 진단 지표와 질병 진행도를 담은 표준 회귀용 벤치마크 데이터셋</div>'
                f'<div class="lib-card"><strong>sklearn.linear_model.LinearRegression</strong>: 최소제곱법(OLS)을 활용해 독립변수와 종속변수 간의 최적 선형 관계식을 학습하는 회귀 모델</div>'
                f'<div class="lib-card"><strong>sklearn.model_selection.train_test_split</strong>: 일반화 성능 검증을 위해 데이터를 학습용(80%)과 테스트용(20%)으로 분할하는 도구</div>'
                f'<div class="lib-card"><strong>sklearn.metrics (회귀 평가지표 모듈)</strong>: MAE, MSE, RMSE, MAPE, RMSLE, R2 Score 등 예측 오차의 크기와 모델 설명력을 산출하는 핵심 패키지</div>'
                f'<div class="lib-card"><strong>numpy & pandas</strong>: 고성능 수치 배열 연산(오차 제곱근 계산, 음수 보정) 및 구조화된 테이블 데이터 핸들링 도구</div>'
                f'</div>'
                f'</div>'
                f'</div>'
            )

        sections_html.append(
            f'<section class="step-section" id="{step_id}">'
            f'<div class="step-section-header">'
            f'<div class="step-title-wrap">'
            f'<span class="step-number-badge">{step_badge}</span>'
            f'<h2 class="step-title-text">{step_title}</h2>'
            f'</div>'
            f'<p class="step-summary-desc">{step_summary}</p>'
            f'</div>'
            f'<div class="step-dual-grid">'
            f'<div class="grid-col-code">'
            f'<div class="col-sticky-label">💻 실행 코드 및 결과 (Jupyter Notebook)</div>'
            f'{"".join(code_cells_html)}'
            f'</div>'
            f'<div class="grid-col-notes">'
            f'<div class="col-sticky-label">📝 AI 함수별 상세 해설 노트 (Markdown)</div>'
            f'{"".join(notes_column_html)}'
            f'</div>'
            f'</div>'
            f'</section>'
        )

    total_notes_count = len(notes)

    full_html = f"""<!DOCTYPE html>
<html lang="ko" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>머신러닝 기초: 회귀 모델 성능 평가 지표 (Regression Metrics) 인터랙티브 듀얼 뷰어</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Pretendard:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" id="prism-theme" />

  <style>
    :root[data-theme="dark"] {{
      --bg-base: #0b0f19;
      --bg-surface: #111827;
      --bg-card: #1f2937;
      --bg-card-hover: #283548;
      --bg-code: #0d1117;
      --border-subtle: #2d3748;
      --border-accent: #3b82f6;
      
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-dim: #6b7280;
      
      --accent-primary: #38bdf8;
      --accent-primary-hover: #0ea5e9;
      --accent-secondary: #818cf8;
      --accent-success: #34d399;
      --accent-warning: #fbbf24;
      --accent-glow: rgba(56, 189, 248, 0.25);
      
      --pill-bg: rgba(56, 189, 248, 0.15);
      --pill-border: rgba(56, 189, 248, 0.4);
      --pill-text: #7dd3fc;
      --pill-hover-bg: rgba(56, 189, 248, 0.3);
      
      --table-th-bg: #1e293b;
      --table-td-stripe: #151e2e;
      --table-border: #334155;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.4);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -1px rgba(0, 0, 0, 0.3);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -2px rgba(0, 0, 0, 0.4);
      --shadow-glow: 0 0 20px rgba(56, 189, 248, 0.4);
    }}

    :root[data-theme="light"] {{
      --bg-base: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #f1f5f9;
      --bg-card-hover: #e2e8f0;
      --bg-code: #1e293b;
      --border-subtle: #e2e8f0;
      --border-accent: #2563eb;
      
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      
      --accent-primary: #0284c7;
      --accent-primary-hover: #0369a1;
      --accent-secondary: #6366f1;
      --accent-success: #059669;
      --accent-warning: #d97706;
      --accent-glow: rgba(2, 132, 199, 0.2);
      
      --pill-bg: #e0f2fe;
      --pill-border: #7dd3fc;
      --pill-text: #0369a1;
      --pill-hover-bg: #bae6fd;
      
      --table-th-bg: #f1f5f9;
      --table-td-stripe: #f8fafc;
      --table-border: #e2e8f0;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
      --shadow-glow: 0 0 20px rgba(2, 132, 199, 0.25);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      font-size: 15px;
    }}

    body {{
      font-family: 'Pretendard', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.6;
      transition: background-color 0.25s ease, color 0.25s ease;
      min-height: 100vh;
    }}

    .app-header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(17, 24, 39, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      transition: background-color 0.25s ease;
    }}
    :root[data-theme="light"] .app-header {{
      background: rgba(255, 255, 255, 0.88);
    }}

    .header-main-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 1720px;
      margin: 0 auto;
      padding: 0.85rem 1.5rem;
      gap: 1.5rem;
    }}

    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .brand-icon {{
      font-size: 1.7rem;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 42px;
      height: 42px;
      border-radius: 10px;
      background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
      box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
    }}

    .brand-titles h1 {{
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }}

    .brand-titles p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .stats-pill {{
      display: inline-block;
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      background: var(--pill-bg);
      border: 1px solid var(--pill-border);
      color: var(--pill-text);
      font-weight: 600;
      font-size: 0.75rem;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .search-box-wrap {{
      position: relative;
      display: flex;
      align-items: center;
    }}

    .search-input {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.45rem 0.85rem 0.45rem 2rem;
      color: var(--text-main);
      font-size: 0.85rem;
      outline: none;
      width: 230px;
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: var(--accent-primary);
      box-shadow: 0 0 0 3px var(--accent-glow);
      width: 290px;
    }}
    .search-icon {{
      position: absolute;
      left: 0.65rem;
      color: var(--text-dim);
      font-size: 0.85rem;
      pointer-events: none;
    }}

    .theme-toggle-btn, .expand-all-btn, .home-hub-btn {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .theme-toggle-btn:hover, .expand-all-btn:hover, .home-hub-btn:hover {{
      background: var(--bg-card);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .steps-nav-bar {{
      display: flex;
      align-items: center;
      overflow-x: auto;
      max-width: 1720px;
      margin: 0 auto;
      padding: 0.35rem 1.5rem 0.65rem 1.5rem;
      gap: 0.6rem;
      scrollbar-width: thin;
    }}
    .steps-nav-bar::-webkit-scrollbar {{
      height: 4px;
    }}
    .steps-nav-bar::-webkit-scrollbar-thumb {{
      background: var(--border-subtle);
      border-radius: 4px;
    }}

    .step-nav-item {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.35rem 0.75rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 500;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .step-nav-item:hover {{
      color: var(--accent-primary);
      border-color: var(--accent-primary);
      background: var(--bg-card);
      transform: translateY(-1px);
    }}
    .step-nav-item.active {{
      background: var(--accent-primary);
      color: #ffffff;
      border-color: var(--accent-primary);
      box-shadow: 0 2px 8px var(--accent-glow);
    }}
    .step-nav-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.2);
      font-size: 0.7rem;
      font-weight: 700;
    }}
    .nav-note-badge {{
      font-size: 0.7rem;
      padding: 0.1rem 0.4rem;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.2);
    }}

    .app-main {{
      max-width: 1720px;
      margin: 1.5rem auto 4rem auto;
      padding: 0 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
    }}

    .step-section {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      box-shadow: var(--shadow-md);
      overflow: hidden;
      transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }}
    .step-section:hover {{
      border-color: rgba(56, 189, 248, 0.35);
      box-shadow: var(--shadow-lg);
    }}

    .step-section-header {{
      padding: 1.25rem 1.75rem;
      background: linear-gradient(180deg, var(--bg-card) 0%, var(--bg-surface) 100%);
      border-bottom: 1px solid var(--border-subtle);
    }}

    .step-title-wrap {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.35rem;
    }}

    .step-number-badge {{
      display: inline-block;
      padding: 0.25rem 0.75rem;
      background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      border-radius: 6px;
      letter-spacing: 0.03em;
    }}

    .step-title-text {{
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.01em;
    }}

    .step-summary-desc {{
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.5;
    }}

    .step-dual-grid {{
      display: grid;
      grid-template-columns: 50% 50%;
      min-height: 480px;
    }}
    @media (max-width: 1180px) {{
      .step-dual-grid {{
        grid-template-columns: 100%;
      }}
    }}

    .grid-col-code {{
      border-right: 1px solid var(--border-subtle);
      padding: 1.5rem;
      background: var(--bg-base);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      overflow-x: hidden;
    }}
    @media (max-width: 1180px) {{
      .grid-col-code {{
        border-right: none;
        border-bottom: 2px dashed var(--border-subtle);
      }}
    }}

    .grid-col-notes {{
      padding: 1.5rem;
      background: var(--bg-surface);
      display: flex;
      flex-direction: column;
    }}

    .col-sticky-label {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      padding-bottom: 0.65rem;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .code-cell-wrapper {{
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      background: var(--bg-code);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }}

    .cell-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.5rem 0.85rem;
      background: rgba(255, 255, 255, 0.04);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .cell-badge {{
      font-family: 'Fira Code', monospace;
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--accent-primary);
    }}

    .copy-code-btn {{
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-muted);
      border-radius: 4px;
      padding: 0.2rem 0.5rem;
      font-size: 0.75rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .copy-code-btn:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-main);
      border-color: var(--accent-primary);
    }}

    .code-editor-look {{
      position: relative;
    }}

    .code-editor-look pre {{
      margin: 0 !important;
      padding: 1rem !important;
      background: transparent !important;
      font-family: 'Fira Code', monospace !important;
      font-size: 0.88rem !important;
      line-height: 1.6 !important;
      overflow-x: auto;
    }}

    .code-kw-interactive {{
      display: inline-flex;
      align-items: center;
      gap: 3px;
      padding: 1px 6px;
      margin: 0 2px;
      background: var(--pill-bg);
      border: 1px solid var(--pill-border);
      border-radius: 4px;
      color: var(--pill-text) !important;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }}
    .code-kw-interactive:hover {{
      background: var(--pill-hover-bg);
      border-color: var(--accent-primary);
      color: #ffffff !important;
      transform: translateY(-1px) scale(1.03);
      box-shadow: 0 0 12px var(--accent-glow);
    }}
    .code-kw-interactive.active-target {{
      background: var(--accent-primary);
      color: #ffffff !important;
      box-shadow: 0 0 16px var(--accent-primary);
      animation: pulse-glow 1.5s infinite;
    }}

    .kw-sparkle {{
      font-size: 0.72rem;
      filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.6));
    }}

    @keyframes pulse-glow {{
      0%, 100% {{ box-shadow: 0 0 8px var(--accent-primary); }}
      50% {{ box-shadow: 0 0 20px var(--accent-primary); }}
    }}

    .cell-outputs-container {{
      border-top: 1px solid var(--border-subtle);
      background: var(--bg-surface);
    }}

    .outputs-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.45rem 0.85rem;
      background: var(--bg-card);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-subtle);
    }}

    .toggle-output-btn {{
      background: transparent;
      border: none;
      color: var(--accent-primary);
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
    }}

    .outputs-body {{
      padding: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .output-type-tag {{
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-dim);
      margin-bottom: 0.4rem;
    }}

    .stream-output pre, .text-output pre {{
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 6px;
      padding: 0.75rem 1rem;
      font-family: 'Fira Code', monospace;
      font-size: 0.84rem;
      color: #38bdf8;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-all;
    }}

    .table-responsive-wrapper {{
      max-width: 100%;
      overflow-x: auto;
      border: 1px solid var(--table-border);
      border-radius: 8px;
      background: var(--bg-surface);
      box-shadow: var(--shadow-sm);
    }}

    table.modern-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      text-align: right;
    }}
    table.modern-table th, table.modern-table td {{
      padding: 0.5rem 0.75rem;
      border: 1px solid var(--table-border);
      white-space: nowrap;
    }}
    table.modern-table thead th {{
      background: var(--table-th-bg);
      color: var(--text-main);
      font-weight: 600;
      position: sticky;
      top: 0;
    }}
    table.modern-table tbody tr:nth-child(even) {{
      background: var(--table-td-stripe);
    }}
    table.modern-table tbody tr:hover {{
      background: rgba(56, 189, 248, 0.12);
    }}
    table.modern-table th:first-child, table.modern-table td:first-child {{
      text-align: center;
      font-weight: 600;
      background: var(--table-th-bg);
    }}

    .plot-img-container {{
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      background: #ffffff;
      padding: 0.5rem;
      cursor: pointer;
      display: inline-block;
      max-width: 100%;
    }}
    .zoomable-plot {{
      max-width: 100%;
      height: auto;
      display: block;
      transition: transform 0.2s ease;
    }}
    .plot-img-container:hover .zoomable-plot {{
      transform: scale(1.015);
    }}
    .img-zoom-overlay {{
      position: absolute;
      bottom: 0.75rem;
      right: 0.75rem;
      background: rgba(0, 0, 0, 0.75);
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.3rem 0.65rem;
      border-radius: 20px;
      backdrop-filter: blur(4px);
      pointer-events: none;
    }}

    .cell-markdown-box {{
      padding: 0.75rem 1rem;
      background: var(--bg-card);
      border-left: 4px solid var(--accent-primary);
      border-radius: 6px;
      font-size: 0.95rem;
      font-weight: 500;
    }}

    .notes-panel-container {{
      display: flex;
      flex-direction: column;
      height: 100%;
    }}

    .notes-tabs-header {{
      margin-bottom: 1.25rem;
    }}

    .tabs-label {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-primary);
      margin-bottom: 0.65rem;
    }}

    .tabs-scroll-wrapper {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .func-tab-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.45rem 0.85rem;
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }}
    .func-tab-btn:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--text-main);
    }}
    .func-tab-btn.active {{
      background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
      color: #ffffff;
      border-color: transparent;
      box-shadow: 0 4px 12px var(--accent-glow);
    }}

    .notes-panes-wrapper {{
      flex: 1;
      position: relative;
    }}

    .func-note-pane {{
      display: none;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
      animation: fadeIn 0.25s ease-out;
    }}
    .func-note-pane.active {{
      display: block;
    }}
    .func-note-pane.highlight-pulse {{
      animation: pulse-border 1.5s ease-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes pulse-border {{
      0% {{ box-shadow: 0 0 0 4px var(--accent-primary); border-color: var(--accent-primary); }}
      100% {{ box-shadow: var(--shadow-sm); border-color: var(--border-subtle); }}
    }}

    .note-meta-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.5rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 1.25rem;
    }}

    .note-target-badge {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
    }}
    .note-target-badge code {{
      font-family: 'Fira Code', monospace;
      color: var(--accent-primary);
      background: var(--bg-base);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
    }}

    .note-time-badge {{
      font-size: 0.78rem;
      color: var(--text-dim);
      background: var(--bg-base);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }}

    .note-body-content {{
      font-size: 0.92rem;
      line-height: 1.7;
      color: var(--text-main);
    }}

    .note-h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 1rem 0 0.75rem 0;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .note-h2 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 1.2rem 0 0.65rem 0;
    }}
    .note-h3 {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--accent-primary);
      margin: 1.4rem 0 0.6rem 0;
      padding-bottom: 0.3rem;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .note-h4 {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-main);
      margin: 0.8rem 0 0.4rem 0;
    }}

    .note-p {{
      margin-bottom: 0.85rem;
    }}

    .note-list {{
      margin: 0.5rem 0 1rem 1.4rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}
    .note-list-item {{
      list-style-type: disc;
    }}

    .inline-code {{
      font-family: 'Fira Code', monospace;
      font-size: 0.85em;
      background: var(--bg-base);
      color: var(--accent-primary);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
    }}

    .note-code-block {{
      background: var(--bg-code);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.85rem 1rem;
      margin: 0.85rem 0;
      font-family: 'Fira Code', monospace;
      font-size: 0.84rem;
      overflow-x: auto;
    }}

    .note-divider {{
      border: none;
      height: 1px;
      background: var(--border-subtle);
      margin: 1.25rem 0;
    }}

    .note-footer-actions {{
      margin-top: 1.5rem;
      padding-top: 1rem;
      border-top: 1px dashed var(--border-subtle);
      display: flex;
      justify-content: flex-end;
    }}

    .jump-to-code-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      color: var(--accent-primary);
      padding: 0.35rem 0.75rem;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .jump-to-code-btn:hover {{
      background: var(--accent-primary);
      color: #ffffff;
      border-color: var(--accent-primary);
    }}

    .notes-empty-guide {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 2rem;
      text-align: center;
    }}
    .guide-icon {{
      font-size: 3rem;
      margin-bottom: 0.75rem;
    }}
    .notes-empty-guide h3 {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
    }}
    .notes-empty-guide p {{
      color: var(--text-muted);
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
    }}
    .lib-cards-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      text-align: left;
    }}
    .lib-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .lib-card strong {{
      color: var(--accent-primary);
      font-family: 'Fira Code', monospace;
    }}

    .lightbox-modal {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}
    .lightbox-modal.active {{
      display: flex;
    }}
    .lightbox-content {{
      max-width: 90vw;
      max-height: 85vh;
      object-fit: contain;
      border-radius: 10px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
      background: #ffffff;
      padding: 1rem;
    }}
    .lightbox-close-btn {{
      position: absolute;
      top: 1.5rem;
      right: 2rem;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #ffffff;
      font-size: 1.5rem;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}
    .lightbox-close-btn:hover {{
      background: rgba(255, 255, 255, 0.3);
      transform: scale(1.1);
    }}

    .toast-msg {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--text-main);
      color: var(--bg-base);
      padding: 0.65rem 1.25rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      box-shadow: var(--shadow-lg);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.25s ease;
      z-index: 2000;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toast-msg.show {{
      transform: translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>

  <header class="app-header">
    <div class="header-main-bar">
      <div class="brand-wrap">
        <div class="brand-icon">📊</div>
        <div class="brand-titles">
          <h1>머신러닝 기초: 회귀 모델 성능 평가 지표 (Regression Metrics)</h1>
          <p>
            <span>인터랙티브 듀얼 학습 뷰어</span>
            <span class="stats-pill">8개 파이프라인 단계 (준비+7단계)</span>
            <span class="stats-pill">{total_notes_count}개 AI 상세 해설 노트 연결</span>
            <span class="stats-pill">MAE · MSE · RMSE · MAPE · RMSLE · R² · Adj-R²</span>
          </p>
        </div>
      </div>

      <div class="header-actions">
        <a href="../index.html" class="home-hub-btn" title="메인 학습 포털로 이동">🏠 메인 포털</a>
        <div class="search-box-wrap">
          <span class="search-icon">🔍</span>
          <input type="text" id="global-search" class="search-input" placeholder="함수 검색 (ex: r2_score, rmse...)" oninput="filterFunctions(this.value)" />
        </div>
        <button class="expand-all-btn" onclick="toggleAllOutputs()">결과 전체 펼치기</button>
        <button class="theme-toggle-btn" id="theme-btn" onclick="toggleTheme()">☀️ 테마 전환</button>
      </div>
    </div>

    <nav class="steps-nav-bar" id="steps-nav">
      {"".join(steps_nav_html)}
    </nav>
  </header>

  <main class="app-main">
    {"".join(sections_html)}
  </main>

  <div class="lightbox-modal" id="lightbox" onclick="closeLightbox()">
    <button class="lightbox-close-btn">&times;</button>
    <img src="" class="lightbox-content" id="lightbox-img" onclick="event.stopPropagation()" alt="Enlarged Plot" />
  </div>

  <div class="toast-msg" id="toast">✅ 알림 메시지</div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>

  <script>
    function toggleTheme() {{
      const html = document.documentElement;
      const current = html.getAttribute('data-theme') || 'dark';
      const next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('study_theme_07', next);
      
      const btn = document.getElementById('theme-btn');
      btn.textContent = next === 'dark' ? '☀️ 라이트 모드' : '🌙 다크 모드';
      showToast(next === 'dark' ? '🌙 다크 테마 적용됨' : '☀️ 라이트 테마 적용됨');
    }}

    (function initTheme() {{
      const saved = localStorage.getItem('study_theme_07') || localStorage.getItem('study_theme');
      if (saved) {{
        document.documentElement.setAttribute('data-theme', saved);
        const btn = document.getElementById('theme-btn');
        if (btn) btn.textContent = saved === 'dark' ? '☀️ 라이트 모드' : '🌙 다크 모드';
      }}
    }})();

    function switchTab(stepId, tabId) {{
      const stepElem = document.getElementById(stepId);
      if (!stepElem) return;

      const tabBtns = stepElem.querySelectorAll('.func-tab-btn');
      tabBtns.forEach(btn => {{
        if (btn.getAttribute('data-tab') === tabId) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      const panes = stepElem.querySelectorAll('.func-note-pane');
      panes.forEach(pane => {{
        if (pane.id === tabId) {{
          pane.classList.add('active');
          pane.classList.remove('highlight-pulse');
          void pane.offsetWidth;
          pane.classList.add('highlight-pulse');
        }} else {{
          pane.classList.remove('active');
        }}
      }});
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const kwSpans = document.querySelectorAll('.code-kw-interactive');
      kwSpans.forEach(span => {{
        span.addEventListener('click', (e) => {{
          const stepId = span.getAttribute('data-step');
          const tabId = span.getAttribute('data-tab');
          const funcName = span.getAttribute('data-func');

          kwSpans.forEach(s => s.classList.remove('active-target'));
          span.classList.add('active-target');

          switchTab(stepId, tabId);

          if (window.innerWidth <= 1180) {{
            const notePane = document.getElementById(tabId);
            if (notePane) {{
              notePane.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
          }}

          showToast("💡 '" + funcName + "' AI 학습 노트로 이동");
        }});
      }});
    }});

    function highlightMatchingKeyword(stepId, funcName, tabId) {{
      const stepElem = document.getElementById(stepId);
      if (!stepElem) return;

      const kwSpans = stepElem.querySelectorAll('.code-kw-interactive');
      let found = false;

      // 1순위: tabId 일치하는 스팬
      if (tabId) {{
        kwSpans.forEach(span => {{
          if (span.getAttribute('data-tab') === tabId) {{
            span.classList.add('active-target');
            span.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            found = true;
          }} else {{
            span.classList.remove('active-target');
          }}
        }});
      }}

      // 2순위: funcName 일치하는 첫 번째 스팬
      if (!found) {{
        for (let span of kwSpans) {{
          if (span.getAttribute('data-func') === funcName) {{
            span.classList.add('active-target');
            span.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            found = true;
            break;
          }}
        }}
      }}

      if (found) {{
        showToast("🔍 좌측 코드에서 '" + funcName + "' 위치 강조");
      }}
    }}

    function copyCode(btn) {{
      const cellWrapper = btn.closest('.code-cell-wrapper');
      const codeBlock = cellWrapper.querySelector('pre code');
      if (codeBlock) {{
        const text = codeBlock.innerText;
        navigator.clipboard.writeText(text).then(() => {{
          const original = btn.textContent;
          btn.textContent = '✅ 복사됨!';
          btn.style.borderColor = 'var(--accent-success)';
          btn.style.color = 'var(--accent-success)';
          setTimeout(() => {{
            btn.textContent = original;
            btn.style.borderColor = '';
            btn.style.color = '';
          }}, 2000);
          showToast('📋 코드가 클립보드에 복사되었습니다.');
        }});
      }}
    }}

    function toggleOutput(btn) {{
      const container = btn.closest('.cell-outputs-container');
      const body = container.querySelector('.outputs-body');
      if (body.style.display === 'none') {{
        body.style.display = 'flex';
        btn.textContent = '접기 ▲';
      }} else {{
        body.style.display = 'none';
        btn.textContent = '펼치기 ▼';
      }}
    }}

    let allExpanded = true;
    function toggleAllOutputs() {{
      const allBodies = document.querySelectorAll('.outputs-body');
      const allBtns = document.querySelectorAll('.toggle-output-btn');
      allExpanded = !allExpanded;

      allBodies.forEach(b => b.style.display = allExpanded ? 'flex' : 'none');
      allBtns.forEach(btn => btn.textContent = allExpanded ? '접기 ▲' : '펼치기 ▼');
      
      const toggleAllBtn = document.querySelector('.expand-all-btn');
      toggleAllBtn.textContent = allExpanded ? '결과 전체 접기' : '결과 전체 펼치기';
      showToast(allExpanded ? '⚡ 모든 실행 결과가 펼쳐졌습니다.' : '⚡ 모든 실행 결과가 접혔습니다.');
    }}

    function openLightbox(src) {{
      const lb = document.getElementById('lightbox');
      const img = document.getElementById('lightbox-img');
      img.src = src;
      lb.classList.add('active');
    }}
    function closeLightbox() {{
      const lb = document.getElementById('lightbox');
      lb.classList.remove('active');
    }}
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeLightbox();
    }});

    function filterFunctions(query) {{
      const q = query.trim().toLowerCase();
      const tabBtns = document.querySelectorAll('.func-tab-btn');
      const sections = document.querySelectorAll('.step-section');

      if (!q) {{
        tabBtns.forEach(b => b.style.display = '');
        sections.forEach(s => s.style.opacity = '1');
        return;
      }}

      tabBtns.forEach(b => {{
        const text = b.textContent.toLowerCase();
        if (text.includes(q)) {{
          b.style.display = '';
          b.style.border = '2px solid var(--accent-primary)';
        }} else {{
          b.style.display = 'none';
          b.style.border = '';
        }}
      }});
    }}

    window.addEventListener('scroll', () => {{
      const sections = document.querySelectorAll('.step-section');
      const navLinks = document.querySelectorAll('.step-nav-item');
      let currentId = '';

      sections.forEach(s => {{
        const rect = s.getBoundingClientRect();
        if (rect.top <= 200 && rect.bottom >= 200) {{
          currentId = s.id;
        }}
      }});

      if (currentId) {{
        navLinks.forEach(link => {{
          if (link.getAttribute('data-step') === currentId) {{
            link.classList.add('active');
          }} else {{
            link.classList.remove('active');
          }}
        }});
      }}
    }});

    let toastTimeout = null;
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        t.classList.remove('show');
      }}, 2500);
    }}
  </script>
</body>
</html>
"""

    with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"성공적으로 index07.html 파일이 생성되었습니다: {OUTPUT_HTML_PATH}")
    print(f"   - 총 단계: {len(steps)}개")
    print(f"   - 총 해설 노트: {len(notes)}개")


def main():
    print("머신러닝 회귀 성능 지표 인터랙티브 듀얼 뷰어 빌더 시작...")
    notes = load_markdown_files()
    print(f"마크다운 해설 파일 {len(notes)}개 로드 완료")

    steps = parse_notebook()
    print(f"주피터 노트북 단계 {len(steps)}개 파싱 완료")

    steps, filtered_notes = map_notes_to_steps(steps, notes)
    for s in steps:
        print(f"   - [{s['id']}] {s['title'][:35]} -> {len(s['notes'])}개 해설 노트 매핑됨")

    generate_viewer_html(steps, filtered_notes)
    print("빌드 완료!")


if __name__ == "__main__":
    main()
