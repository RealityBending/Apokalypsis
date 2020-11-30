import numpy as np
import PIL
import pyllusion as ill

# Test
# ill.pareidolia(
#     pattern="patterns/logo.png",
#     n=[20, 300, 4000],
#     sd=[4, 2, 1],
#     weight=[3, 2, 1],
#     alpha=80,
#     blur=0.2)


# Logo
logo = ill.pareidolia(
    pattern="patterns/logo.png",
    n=[20, 300, 4000],
    sd=[4, 2, 1],
    weight=[3, 2, 1],
    alpha=90,
    blur=0.2)
logo.save("logo.png")


# Demo
def make_demo(file="patterns/png/snake_7.png", name="snake", alpha=[60, 70, 80], blur=[1, 2, 4]):
    pattern = PIL.Image.open(file)
    imgs = []
    for a in alpha:
        for b in blur:
            stim = ill.pareidolia(pattern=pattern,
                                n=[20, 300, 4000],
                                sd=[4, 2, 1],
                                weight=[3, 2, 1],
                                alpha=a,
                                blur=b)


            PIL.ImageDraw.Draw(stim).text((0, 0),
                                        f"alpha = {a}%, blur = {b}%",
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
    new.save("demo_" + name + ".png")

# make_demo(file="patterns/png/snake_7.png", name="snake", alpha=[60, 70, 80], blur=[1, 2, 4])
# make_demo(file="patterns/faces/full_168_m_f_f_a.png", name="face", alpha=[20, 30, 40], blur=[1, 2, 3])
make_demo(file="patterns/png/skull_5.png", name="skull", alpha=[50, 65, 80], blur=[1, 2, 3])


# # Profile
# pattern = PIL.Image.open("patterns/final/snake_7.png")
# call = """
# ill.pareidolia(
#     pattern=pattern,
#     n=[20, 300, 4000],
#     sd=[4, 2, 1],
#     weight=[3, 2, 1],
#     alpha=80,
#     blur=0.5)
# """

# call2 = """
# ill.image_blobs(
#     n=[20, 300, 4000],
#     sd=[4, 2, 1],
#     weight=[3, 2, 1])
# """

# import cProfile
# import pstats

# cProfile.run(call2, "profile.stats")
# stats = pstats.Stats("profile.stats").strip_dirs()
# stats.sort_stats('tottime').print_stats()
