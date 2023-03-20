import glob
from PIL import Image

# filepaths
fp_in = "./mm_figs/mm_*.png"
fp_out = "./probability_gif.gif"

img, *imgs = [Image.open(f"./mm_figs/mm_{i}.png") for i in range(1, 54)]
img.save(fp=fp_out, format='gif', append_images=imgs, save_all=True, duration=800, loop=0)
