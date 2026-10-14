import os
from PIL import Image

for idx in range(31, 45):
    fp = f"processed_figures/auto_crops/crop_{idx}.png"
    if os.path.exists(fp):
        im = Image.open(fp)
        print(f"Crop {idx}: size={im.size}")

