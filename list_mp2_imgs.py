import os
from PIL import Image

# Let's save a summary or inspect each image from 20 to 50
for idx in range(21, 51):
    fn = f"image{idx}.jpg"
    fp = os.path.join("extracted_images", fn)
    if os.path.exists(fp):
        im = Image.open(fp)
        print(f"Index {idx}: size={im.size}")

