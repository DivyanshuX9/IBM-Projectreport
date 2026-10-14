with open('compile_perfect_report.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check where def add_frontmatter_table is at top
top_func_end = 0
for i, line in enumerate(lines[:100]):
    if line.startswith('def add_frontmatter_table'):
        # find where it ends
        for j in range(i+1, 100):
            if lines[j].startswith('import ') or lines[j].startswith('from ') or lines[j].startswith('def ') or lines[j].startswith('#'):
                top_func_end = j
                break
        break

if top_func_end > 0:
    lines = lines[top_func_end:]

# Now define add_frontmatter_table inside generate_perfect_report
func_body = '''    def add_frontmatter_table(headers, rows, col_widths, font_size=10, row_spacing=3.0, is_toc=False):
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

# Find def add_table_data inside generate_perfect_report
insert_pos = 0
for i, line in enumerate(lines):
    if 'def add_table_data' in line:
        # find end of add_table_data (next def at indent 4)
        for j in range(i+1, len(lines)):
            if lines[j].startswith('    def ') or lines[j].startswith('    # ---'):
                insert_pos = j
                break
        break

lines = lines[:insert_pos] + [func_body + '\n'] + lines[insert_pos:]

with open('compile_perfect_report.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Placed add_frontmatter_table inside generate_perfect_report()!")

