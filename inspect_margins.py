import os
from PIL import Image
import numpy as np

images = [
    'image6.jpg', 'image10.jpg', 'image15.png', 'image18.png', 
    'image19.png', 'image20.png', 'image25.jpg', 'image28.jpg', 
    'image29.jpg', 'image37.jpg', 'image42.jpg', 'image46.jpg', 
    'image50.jpg'
]

for name in images:
    fp = os.path.join('processed_figures', name)
    im = Image.open(fp)
    print(f"=== {name} === (Size: {im.size})")
    arr = np.array(im.convert('RGB'))
    # Let's inspect rows from top, bottom, left, right to see how many rows are near pure white (>240)
    top_white = 0
    while top_white < im.size[1] and np.mean(arr[top_white, :, :]) > 240:
        top_white += 1
    bot_white = 0
    while bot_white < im.size[1] and np.mean(arr[im.size[1]-1-bot_white, :, :]) > 240:
        bot_white += 1
    left_white = 0
    while left_white < im.size[0] and np.mean(arr[:, left_white, :]) > 240:
        left_white += 1
    right_white = 0
    while right_white < im.size[0] and np.mean(arr[:, im.size[0]-1-right_white, :]) > 240:
        right_white += 1
    print(f"Whitespace margins: top={top_white}, bot={bot_white}, left={left_white}, right={right_white}")

