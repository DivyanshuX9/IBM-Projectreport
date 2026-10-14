import os
import pypdfium2 as pdfium
from PIL import Image

# Let's inspect images 1 to 12 by saving a thumbnail or printing what text is near them
# In mini-project 1.ipynb - Colab.pdf, let's see which pages correspond to what
pdf = pdfium.PdfDocument('mini-project 1.ipynb - Colab.pdf')
for i in range(len(pdf)):
    text = pdf[i].get_textpage().get_text_range()
    first_lines = [l.strip() for l in text.split('\n') if l.strip()][:2]
    print(f"Colab PDF Page {i+1}: {first_lines}")

