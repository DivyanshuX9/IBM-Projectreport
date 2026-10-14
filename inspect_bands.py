import os
from PIL import Image
import numpy as np

# Let's inspect where dark pixels / non-white pixels are in image6.jpg and image10.jpg
im6 = Image.open(os.path.join('processed_figures', 'image6.jpg'))
arr6 = np.array(im6.convert('L'))
print("image6.jpg mean per vertical band (10 bands):")
h = im6.size[1]
band = h // 10
for b in range(10):
    val = np.mean(arr6[b*band:(b+1)*band, :])
    print(f"Band {b} (y={b*band}..{(b+1)*band}): mean brightness {val:.1f}")

im10 = Image.open(os.path.join('processed_figures', 'image10.jpg'))
arr10 = np.array(im10.convert('L'))
print("\nimage10.jpg mean per vertical band (10 bands):")
h10 = im10.size[1]
band10 = h10 // 10
for b in range(10):
    val = np.mean(arr10[b*band10:(b+1)*band10, :])
    print(f"Band {b} (y={b*band10}..{(b+1)*band10}): mean brightness {val:.1f}")

