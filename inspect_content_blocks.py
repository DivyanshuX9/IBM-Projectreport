import os
from PIL import Image
import numpy as np

# Let's inspect image6.jpg, image10.jpg, and other images in detail
# Save cropped chunks or inspect non-white bounding boxes of sub-regions
im6 = Image.open('extracted_images/image6.jpg')
arr6 = np.array(im6.convert('L'))
row_means6 = np.mean(arr6, axis=1)

print("Rows in image6 with mean brightness < 250:")
non_white_rows = np.where(row_means6 < 250)[0]
# find contiguous blocks of non-white rows
blocks = []
start = None
for r in non_white_rows:
    if start is None:
        start = r
    elif r > prev + 20: # gap of more than 20 white lines
        blocks.append((start, prev))
        start = r
    prev = r
if start is not None:
    blocks.append((start, prev))

print("image6.jpg blocks of content:")
for s, e in blocks:
    print(f"  y={s}..{e} (height={e-s+1}), mean_brightness={np.mean(row_means6[s:e+1]):.1f}")

im10 = Image.open('extracted_images/image10.jpg')
arr10 = np.array(im10.convert('L'))
row_means10 = np.mean(arr10, axis=1)
non_white_rows10 = np.where(row_means10 < 250)[0]
blocks10 = []
start = None
for r in non_white_rows10:
    if start is None:
        start = r
    elif r > prev + 20:
        blocks10.append((start, prev))
        start = r
    prev = r
if start is not None:
    blocks10.append((start, prev))

print("\nimage10.jpg blocks of content:")
for s, e in blocks10:
    print(f"  y={s}..{e} (height={e-s+1}), mean_brightness={np.mean(row_means10[s:e+1]):.1f}")

