import os
from PIL import Image

im6 = Image.open('extracted_images/image6.jpg')
# crop top and bottom
im6_top = im6.crop((40, 30, 1200, 600))
im6_bot = im6.crop((40, 600, 1200, 1720))
im6_top.save('processed_figures/test_im6_top.png')
im6_bot.save('processed_figures/test_im6_bot.png')

im10 = Image.open('extracted_images/image10.jpg')
# In image10, y=34..810 is the actual content!
im10_crop = im10.crop((40, 30, 1200, 815))
im10_crop.save('processed_figures/test_im10_crop.png')

print("Saved test crops for im6 and im10")

