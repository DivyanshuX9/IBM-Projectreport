import os
import subprocess
import win32com.client
import pypdfium2 as pdfium

with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update add_frontmatter_table
old_frontmatter_fn = text[text.find('    def add_frontmatter_table'):text.find('    def add_table_caption')]

new_frontmatter_fn = '''    def add_frontmatter_table(headers, rows, col_widths, font_size=9.5, is_toc=False):
        tbl = doc.add_table(rows=len(rows) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        set_table_borders(tbl, color="000000", sz="4", val="single")

        # Header Row
        hdr_row = tbl.rows[0]
        for i, h in enumerate(headers):
            cell = hdr_row.cells[i]
            cell.width = col_widths[i]
            cell.text = h
            set_cell_margins(cell, top=40, bottom=40, left=70, right=70)
            set_cell_shading(cell, "EBF1F5")
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            for r in p.runs:
                r.bold = True
                r.font.name = 'Times New Roman'
                r.font.size = Pt(font_size + 0.5)

        # Body Rows
        for r_idx, row_data in enumerate(rows):
            row = tbl.rows[r_idx + 1]
            for c_idx, val in enumerate(row_data):
                cell = row.cells[c_idx]
                cell.width = col_widths[c_idx]
                cell.text = str(val)
                set_cell_margins(cell, top=22, bottom=22, left=70, right=70)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.15
                
                # Alignment
                if is_toc:
                    if c_idx == 0:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    elif c_idx == 1:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    else:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    if c_idx == 0 or len(str(val)) < 15:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    else:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT

                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(font_size)
                    if is_toc:
                        if row_data[0] in ['1', '2', '3', '4']:
                            r.bold = True
                        elif row_data[1] in ["References", "Appendix I: Certificates, Links, and Source Code"]:
                            r.bold = True

        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_after = Pt(1)
        return tbl
'''

text = text.replace(old_frontmatter_fn, new_frontmatter_fn)

# 2. Add Score Card after Certificate - AdroIT Prolearn
old_cert2 = text[text.find('    cert_adroit_path = r"c:\\Users\\symdr\\Downloads\\adddr\\processed_figures\\cert_adroit.png"'):text.find('    # -------------------------------------------------------------\n    # 5. ACKNOWLEDGEMENT')]

new_cert2_and_scorecard = '''    cert_adroit_path = r"c:\\Users\\symdr\\Downloads\\adddr\\processed_figures\\cert_adroit.png"
    if os.path.exists(cert_adroit_path):
        add_fig(cert_adroit_path, "Official Course Completion Certificate from AdroIT Prolearn", height=Inches(5.0))

    doc.add_page_break()

    # -------------------------------------------------------------
    # 5. STUDENT PERFORMANCE SCORE CARD (Page vi)
    # -------------------------------------------------------------
    add_h1("STUDENT PERFORMANCE SCORE CARD", space_before=6, space_after=4)
    add_p("Official examination score card and assessment breakdown for Divyanshu Sharma (Register No: 23BDS1155) for the IBM - Advanced Generative AI training program, issued by the IBM Career Education Program team. The candidate secured an aggregate score of 90/100 (90%) across coursework assignments, progressive quizzes, and the final certification examination.", space_before=2, space_after=8, line_spacing=1.2)

    scorecard_path = r"c:\\Users\\symdr\\Downloads\\adddr\\scorecard.png"
    if os.path.exists(scorecard_path):
        add_fig(scorecard_path, "Official Performance Score Card issued by IBM CE Team", width=Inches(5.6))

    doc.add_page_break()
'''

text = text.replace(old_cert2, new_cert2_and_scorecard)

# 3. Update TOC rows to include Score Card and shifted Roman page numbers
old_toc = text[text.find('    # Table of Contents matching the template\'s exact structure'):text.find('    doc.add_page_break()\n\n    # -------------------------------------------------------------\n    # 7. LIST OF TABLES')]

new_toc = '''    # Table of Contents with bordered outline and shaded header
    toc_headers = ["Chapter", "Title", "Page"]
    toc_rows = [
        ["", "Title Page", "i"],
        ["", "Declaration", "ii"],
        ["", "Certificate", "iii"],
        ["", "Industry Internship Certificate (IBM Career Education)", "iv"],
        ["", "Course Completion Certificate (AdroIT Prolearn)", "v"],
        ["", "Student Performance Score Card (IBM Career Education)", "vi"],
        ["", "Acknowledgement", "vii"],
        ["", "Table of Contents", "viii"],
        ["", "List of Tables", "ix"],
        ["", "List of Figures", "x"],
        ["", "List of Abbreviations", "xi"],
        ["", "Abstract", "xii"],
        ["1", "Introduction", "01"],
        ["2", "Theoretical Foundations and Course Work", "04"],
        ["3", "Technical Implementation and Mini Projects", "09"],
        ["", "    3.1 Practical Coursework Exercises and Assignment 1", "09"],
        ["", "    3.2 Mini Project 1: Data Science with Generative AI", "09"],
        ["", "    3.3 Mini Project 2: Software Development Using Generative AI", "17"],
        ["4", "Conclusion and Future Scope", "25"],
        ["", "References", "27"],
        ["", "Appendix I: Certificates, Links, and Source Code", "28"]
    ]
    add_frontmatter_table(toc_headers, toc_rows, col_widths=[Inches(1.0), Inches(4.6), Inches(0.9)], font_size=9.2, is_toc=True)
'''

text = text.replace(old_toc, new_toc)

# 4. Update LOT column widths and font size
old_lot = text[text.find('    lot_headers = ["Table No.", "Table Caption", "Page"]'):text.find('    doc.add_page_break()\n\n    # -------------------------------------------------------------\n    # 8. LIST OF FIGURES')]

new_lot = '''    lot_headers = ["Table No.", "Table Caption", "Page"]
    lot_rows = [
        ["Table 3.1", "Heart Disease Normalized SQLite Database Schema (3NF Structure)", "10"],
        ["Table 3.2", "Summary of Clinical Hypotheses, Statistical Findings, and Decisions", "13"],
        ["Table 3.3", "Performance Evaluation and Comparison of Machine Learning Models", "14"],
        ["Table 3.4", "Hyperparameter Tuning and Overfitting Mitigation Comparison", "17"],
        ["Table 3.5", "College Library Management System Requirements Specification Table", "17"],
        ["Table 3.6", "Non-Functional Requirements (NFRs) for Library Application", "18"],
        ["Table 3.7", "Automated Test Suite Execution Summary across Four Testing Modules", "21"],
        ["Table 3.8", "Server Performance Telemetry and Critical Threshold Predictions", "23"]
    ]
    add_frontmatter_table(lot_headers, lot_rows, col_widths=[Inches(1.2), Inches(4.4), Inches(0.9)], font_size=9.5)
'''

text = text.replace(old_lot, new_lot)

# 5. Update LOF column widths and font size
old_lof = text[text.find('    lof_headers = ["Fig No.", "Figure Caption", "Page"]'):text.find('    doc.add_page_break()\n\n    # -------------------------------------------------------------\n    # 9. LIST OF ABBREVIATIONS')]

new_lof = '''    lof_headers = ["Fig No.", "Figure Caption", "Page"]
    lof_rows = [
        ["Fig 3.1", "Entity Relationship Diagram for Normalized Heart Disease Database Schema", "11"],
        ["Fig 3.2", "Univariate and Bivariate Clinical Distributions Dashboard", "12"],
        ["Fig 3.3", "Bivariate Clinical Feature Scatter Distributions and Associations", "13"],
        ["Fig 3.4", "Random Forest Feature Importance Assessment across 13 Clinical Attributes", "15"],
        ["Fig 3.5", "SHAP Beeswarm Summary Plot for Global Feature Impact on Predictions", "16"],
        ["Fig 3.6", "SHAP Force Plot for Local Single Patient Decision Explanation", "16"],
        ["Fig 3.7", "Visily UI Wireframes for College Library Management System Screens", "19"],
        ["Fig 3.8", "Multi-Tier System Architecture Diagram Generated with Eraser.io", "19"],
        ["Fig 3.9", "Eraser.io Entity Relationship Diagram for Library Relational Database", "20"],
        ["Fig 3.10", "Interactive HTML Frontend Interface Rendered inside Google Colab", "21"],
        ["Fig 3.11", "Automated Test Suite Execution Output Showing 100% Pass Rate", "22"],
        ["Fig 3.12", "API Latency Telemetry Simulation with Real-time Surge and AI Mitigation", "23"],
        ["Fig 3.13", "Predictive Maintenance Telemetry Forecast and Resource Saturation Curves", "24"]
    ]
    add_frontmatter_table(lof_headers, lof_rows, col_widths=[Inches(1.1), Inches(4.5), Inches(0.9)], font_size=9.2)
'''

text = text.replace(old_lof, new_lof)

# 6. Update List of Abbreviations
old_abbr = text[text.find('    add_frontmatter_table(abbr_headers, abbr_rows, col_widths=[Inches(1.0), Inches(2.2), Inches(1.0), Inches(2.2)], font_size=9.5, row_spacing=3.0)'):text.find('    doc.add_page_break()\n\n    # -------------------------------------------------------------\n    # 10. ABSTRACT')]

new_abbr = '    add_frontmatter_table(abbr_headers, abbr_rows, col_widths=[Inches(1.1), Inches(2.15), Inches(1.1), Inches(2.15)], font_size=9.0)'

text = text.replace(old_abbr, new_abbr)

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated compile_perfect_report.py successfully!')

