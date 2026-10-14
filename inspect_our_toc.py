import docx

doc = docx.Document('Summer_Internship_Report_Divyanshu_Sharma_23BDS1155.docx')
print("=== OUR GENERATED TOC TABLE ===")
for t_idx, t in enumerate(doc.tables[:3]):
    txt = ' '.join(c.text for row in t.rows for c in row.cells)
    if 'CHAPTER' in txt.upper() or 'CONTENTS' in txt.upper() or 'TITLE' in txt.upper():
        print(f"Table {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)}):")
        for r_idx, row in enumerate(t.rows):
            cell_texts = [c.text.strip().replace('\n', ' ') for c in row.cells]
            print(f"  Row {r_idx:2d}: {cell_texts}")
        break

