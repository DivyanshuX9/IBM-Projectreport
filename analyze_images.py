import os
from PIL import Image
import numpy as np

# Let's inspect each image in extracted_images
for idx in range(1, 51):
    for ext in ['.jpg', '.png']:
        fn = f"image{idx}{ext}"
        fp = os.path.join("extracted_images", fn)
        if os.path.exists(fp):
            im = Image.open(fp)
            # check non-white bbox
            arr = np.array(im.convert('RGB'))
            is_white = (arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240)
            non_white_rows = np.where(~is_white.all(axis=1))[0]
            non_white_cols = np.where(~is_white.all(axis=0))[0]
            if len(non_white_rows) > 0 and len(non_white_cols) > 0:
                h_content = non_white_rows[-1] - non_white_rows[0]
                w_content = non_white_cols[-1] - non_white_cols[0]
                # check color variance (is it colorful or black/white text)
                r_std = np.std(arr[:, :, 0])
                g_std = np.std(arr[:, :, 1])
                b_std = np.std(arr[:, :, 2])
                print(f"image{idx:2d}{ext}: size={im.size}, content=({w_content}x{h_content}), color_std=({r_std:.1f},{g_std:.1f},{b_std:.1f})")
            else:
                print(f"image{idx:2d}{ext}: BLANK")

