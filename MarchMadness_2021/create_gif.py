import glob
from PIL import Image

# filepaths
fp_in = "./mm_figs/mm_*.png"
fp_out = "./probability_gif.gif"

img, *imgs = [Image.open(f"./mm_figs/mm_{i}.png") for i in range(65)]
img.save(fp=fp_out, format='gif', append_images=imgs, save_all=True, duration=400, loop=0)
