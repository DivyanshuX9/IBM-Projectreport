with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add add_frontmatter_table definition before TOC
frontmatter_def = '''
def add_frontmatter_table(headers, rows, col_widths, font_size=10, row_spacing=3.0, is_toc=False):
    tbl = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    # Remove all borders completely (clean template style)
    tblPr = tbl._element.tblPr
    tblBorders = parse_xml(r\'\'\'
        <w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>
        </w:tblBorders>
    \'\'\')
    tblPr.append(tblBorders)

    # Header Row
    hdr_row = tbl.rows[0]
    for i, h in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.width = col_widths[i]
        p = cell.paragraphs[0]
        if i == len(headers) - 1:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(h)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(font_size + 0.5)

    # Body Rows
    for r_idx, row_data in enumerate(rows):
        row = tbl.rows[r_idx + 1]
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            p = cell.paragraphs[0]
            if c_idx == len(row_data) - 1:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(row_spacing)
            p.paragraph_format.line_spacing = 1.15
            
            run = p.add_run(str(val))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)
            
            if is_toc:
                if c_idx == 0 and str(val) in ['1', '2', '3', '4']:
                    run.bold = True
                elif c_idx == 1:
                    clean_title = str(val).strip()
                    if any(clean_title.startswith(x) for x in ['1', '2', '3', '4', 'Introduction', 'Theoretical Foundations', 'Technical Implementation', 'Conclusion', 'References', 'Appendix']):
                        if not clean_title.startswith('3.'):
                            run.bold = True
'''

# Find insertion point
target_pos = code.find('# 6. TABLE OF CONTENTS')
code = code[:target_pos] + frontmatter_def + "\n    " + code[target_pos:]

# Replace TOC table call
old_toc_call = 'add_table_data(toc_headers, toc_rows, col_widths=[Inches(0.9), Inches(4.6), Inches(0.8)], font_size=9.5, pad_v=24)'
new_toc_call = 'add_frontmatter_table(toc_headers, toc_rows, col_widths=[Inches(1.0), Inches(4.5), Inches(0.8)], font_size=10, row_spacing=3.0, is_toc=True)'
code = code.replace(old_toc_call, new_toc_call)

# Replace LOT table call
old_lot_call = 'add_table_data(lot_headers, lot_rows, col_widths=[Inches(1.2), Inches(4.3), Inches(0.8)], font_size=10, pad_v=40)'
new_lot_call = 'add_frontmatter_table(lot_headers, lot_rows, col_widths=[Inches(1.1), Inches(4.5), Inches(0.8)], font_size=10, row_spacing=4.0)'
code = code.replace(old_lot_call, new_lot_call)

# Replace LOF table call
old_lof_call = 'add_table_data(lof_headers, lof_rows, col_widths=[Inches(1.0), Inches(4.5), Inches(0.8)], font_size=10, pad_v=24)'
new_lof_call = 'add_frontmatter_table(lof_headers, lof_rows, col_widths=[Inches(1.0), Inches(4.6), Inches(0.8)], font_size=10, row_spacing=3.0)'
code = code.replace(old_lof_call, new_lof_call)

# Replace Abbr table call
old_abbr_call = 'add_table_data(abbr_headers, abbr_rows, col_widths=[Inches(0.9), Inches(2.2), Inches(0.9), Inches(2.3)], font_size=9.5, pad_v=22)'
new_abbr_call = 'add_frontmatter_table(abbr_headers, abbr_rows, col_widths=[Inches(1.0), Inches(2.2), Inches(1.0), Inches(2.2)], font_size=9.5, row_spacing=3.0)'
code = code.replace(old_abbr_call, new_abbr_call)

# Update Title case in TOC rows to match template perfectly
old_toc_rows = '''    toc_rows = [
        ["", "Title Page", "i"],
        ["", "Declaration", "ii"],
        ["", "Certificate", "iii"],
        ["", "Industry Internship Certificate (IBM Career Education)", "iv"],
        ["", "Course Completion Certificate (AdroIT Prolearn)", "v"],
        ["", "Acknowledgement", "vi"],
        ["", "Table of Contents", "vii"],
        ["", "List of Tables", "viii"],
        ["", "List of Figures", "ix"],
        ["", "List of Abbreviations", "x"],
        ["", "Abstract", "xi"],
        ["1", "INTRODUCTION", "01"],
        ["2", "THEORETICAL FOUNDATIONS AND COURSE WORK", "04"],
        ["3", "TECHNICAL IMPLEMENTATION AND MINI PROJECTS", "09"],
        ["", "      3.1 Practical Coursework Exercises and Assignment 1", "09"],
        ["", "      3.2 Mini Project 1: Data Science with Generative AI", "09"],
        ["", "      3.3 Mini Project 2: Software Development Using Generative AI", "17"],
        ["4", "CONCLUSION AND FUTURE SCOPE", "26"],
        ["", "REFERENCES", "28"],
        ["", "APPENDIX I", "29"]
    ]'''

new_toc_rows = '''    toc_rows = [
        ["", "Title Page", "i"],
        ["", "Declaration", "ii"],
        ["", "Certificate", "iii"],
        ["", "Industry Internship Certificate (IBM Career Education)", "iv"],
        ["", "Course Completion Certificate (AdroIT Prolearn)", "v"],
        ["", "Acknowledgement", "vi"],
        ["", "Table of Contents", "vii"],
        ["", "List of Tables", "viii"],
        ["", "List of Figures", "ix"],
        ["", "List of Abbreviations", "x"],
        ["", "Abstract", "xi"],
        ["", "", ""],
        ["1", "Introduction", "01"],
        ["2", "Theoretical Foundations and Course Work", "04"],
        ["3", "Technical Implementation and Mini Projects", "09"],
        ["", "    3.1 Practical Coursework Exercises and Assignment 1", "09"],
        ["", "    3.2 Mini Project 1: Data Science with Generative AI", "09"],
        ["", "    3.3 Mini Project 2: Software Development Using Generative AI", "17"],
        ["4", "Conclusion and Future Scope", "26"],
        ["", "", ""],
        ["", "References", "28"],
        ["", "Appendix I: Certificates, Links, and Source Code", "29"]
    ]'''
code = code.replace(old_toc_rows, new_toc_rows)

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Applied add_frontmatter_table to compile_perfect_report.py!")

