import numpy as np
import PIL
import pyllusion as ill

# Demo
pattern = PIL.Image.open("patterns/final/snake_7.png")
imgs = []
for alpha in [60, 70, 80]:
    for blur in [1, 2, 4]:
        stim = ill.pareidolia(pattern=pattern,
                              n=[20, 300, 4000],
                              sd=[4, 2, 1],
                              weight=[3, 2, 1],
                              alpha=alpha,
                              blur=blur)


        PIL.ImageDraw.Draw(stim).text((0, 0),
                                      f"alpha = {alpha}%, blur = {blur}%",
                                      (255, 0, 0),
                                      font = PIL.ImageFont.truetype("arial.ttf", 60))

        imgs.append(stim)




nrows, ncols = int(np.sqrt(len(imgs))), int(np.sqrt(len(imgs)))
new = PIL.Image.new('RGB', (imgs[0].width * nrows, imgs[0].height * ncols))
i = 0
for row in range(nrows):
    for col in range(ncols):
        new.paste(imgs[i], (imgs[i].width * row, imgs[i].height * col))
        i += 1
new
new.save("demo_snake.png")


# Profile
pattern = PIL.Image.open("patterns/final/snake_7.png")
call = """
ill.pareidolia(
    pattern=pattern,
    n=[20, 300, 4000],
    sd=[4, 2, 1],
    weight=[3, 2, 1],
    alpha=80,
    blur=0.5)
"""

call2 = """
ill.image_blobs(
    n=[20, 300, 4000],
    sd=[4, 2, 1],
    weight=[3, 2, 1])
"""

import cProfile
import pstats

cProfile.run(call2, "profile.stats")
stats = pstats.Stats("profile.stats").strip_dirs()
stats.sort_stats('tottime').print_stats()
