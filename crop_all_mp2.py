import os
from PIL import Image
import numpy as np

os.makedirs('processed_figures/auto_crops', exist_ok=True)

for idx in range(21, 51):
    fn = f"image{idx}.jpg"
    fp = os.path.join("extracted_images", fn)
    if os.path.exists(fp):
        im = Image.open(fp)
        arr = np.array(im.convert('RGB'))
        # find non-white bounding box
        is_white = (arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240)
        non_white_rows = np.where(~is_white.all(axis=1))[0]
        non_white_cols = np.where(~is_white.all(axis=0))[0]
        if len(non_white_rows) > 0 and len(non_white_cols) > 0:
            ymin, ymax = non_white_rows[0], non_white_rows[-1]
            xmin, xmax = non_white_cols[0], non_white_cols[-1]
            cropped = im.crop((xmin, ymin, xmax, ymax))
            cropped.save(f"processed_figures/auto_crops/crop_{idx}.png")
            print(f"Img {idx:2d}: cropped from {im.size} to {cropped.size} (bbox: {xmin},{ymin}..{xmax},{ymax})")
        else:
            print(f"Img {idx:2d}: BLANK")

