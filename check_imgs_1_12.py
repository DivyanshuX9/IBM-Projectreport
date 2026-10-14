import os
import pypdfium2 as pdfium
import docx

doc = docx.Document('Assigment2 - Divyanshu Sharma.docx')
for i in range(1, 13):
    fn = f"image{i}.jpg"
    fp = os.path.join("extracted_images", fn)
    if os.path.exists(fp):
        # check size
        print(f"{fn} exists, size {os.path.getsize(fp)} bytes")

# What text is around image 1 to 6 in docx?
print("\n--- Docx text near image 1 to 10 ---")
for i, p in enumerate(doc.paragraphs[:50]):
    for r in p.runs:
        if 'graphic' in r._element.xml:
            print(f"Graphic at P{i}: text above='{doc.paragraphs[i-1].text[:70]}'")

