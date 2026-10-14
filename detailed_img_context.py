import docx

doc = docx.Document('Assigment2 - Divyanshu Sharma.docx')
img_num = 0
for i, p in enumerate(doc.paragraphs):
    has_img = any('graphic' in r._element.xml for r in p.runs)
    if has_img:
        img_num += 1
        # find the most recent phase/part/step heading
        phase = ""
        context = []
        for j in range(max(0, i-10), i):
            t = doc.paragraphs[j].text.strip()
            if t:
                context.append(t)
        print(f"=== Image {img_num:2d} (at P{i}) ===")
        for c in context[-3:]:
            print(f"   {c[:90]}")

