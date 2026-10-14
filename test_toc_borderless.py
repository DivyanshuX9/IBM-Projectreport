import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml

# Test building clean borderless TOC, LOT, LOF
doc = docx.Document()

# Set standard 1-inch margins
for sec in doc.sections:
    sec.top_margin = Inches(1.0)
    sec.bottom_margin = Inches(1.0)
    sec.left_margin = Inches(1.25)
    sec.right_margin = Inches(1.0)

def add_borderless_table(headers, rows, col_widths, font_size=10.5, row_spacing=3.5):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Remove all borders from tblPr
    tblPr = table._element.tblPr
    tblBorders = parse_xml(r'''
        <w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>
            <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>
        </w:tblBorders>
    ''')
    tblPr.append(tblBorders)

    # Header row
    hdr_row = table.rows[0]
    for i, h_text in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.width = col_widths[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if i == len(headers) - 1 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(h_text)
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(font_size + 0.5)

    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
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
            
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(font_size)
            
            # Bold for main chapters
            if c_idx == 0 and val in ['1', '2', '3', '4']:
                run.bold = True
            elif c_idx == 1:
                if any(val.strip().startswith(x) for x in ['1', '2', '3', '4', 'Introduction', 'Theoretical Foundations', 'Technical Implementation', 'Conclusion and Future Scope', 'References', 'Appendix I']):
                    if not val.strip().startswith('3.'):
                        run.bold = True

p_h = doc.add_paragraph()
p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_h.paragraph_format.space_before = Pt(12)
p_h.paragraph_format.space_after = Pt(16)
r = p_h.add_run("CONTENTS")
r.bold = True
r.font.name = "Times New Roman"
r.font.size = Pt(14)

toc_headers = ["Chapter", "Title", "Page"]
toc_rows = [
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
    ["", "", ""], # empty spacer row
    ["1", "Introduction", "01"],
    ["2", "Theoretical Foundations and Course Work", "04"],
    ["3", "Technical Implementation and Mini Projects", "09"],
    ["", "      3.1 Practical Coursework Exercises and Assignment 1", "09"],
    ["", "      3.2 Mini Project 1: Data Science with Generative AI", "09"],
    ["", "      3.3 Mini Project 2: Software Development Using Generative AI", "17"],
    ["4", "Conclusion and Future Scope", "26"],
    ["", "", ""], # empty spacer row
    ["", "References", "28"],
    ["", "Appendix I: Certificates, Links, and Source Code", "29"]
]

add_borderless_table(toc_headers, toc_rows, [Inches(1.0), Inches(4.5), Inches(0.8)], font_size=10, row_spacing=3)

doc.save("test_borderless_toc.docx")
print("Saved test_borderless_toc.docx")

