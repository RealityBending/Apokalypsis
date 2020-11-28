import numpy as np
import PIL
import pyllusion as ill


def hide_pattern(path, n=[10, 1000], sd=[20, 2], alpha=80, blur=30, negative=False):

    # Load pattern
    if isinstance(path, PIL.Image.Image):
        img = path.copy()
    else:
        img = PIL.Image.open(path)
    width, height = img.size


    # Make it negative if need be
    if negative is True:
        r,g,b,a = img.split()
        temp = PIL.Image.merge('RGB', (r,g,b))
        temp = PIL.ImageOps.invert(temp)
        r2,g2,b2 = temp.split()
        img = PIL.Image.merge('RGBA', (r2,g2,b2,a))

    # Blur the image
    img = img.filter(PIL.ImageFilter.GaussianBlur(blur / 100 * width))

    # Generate noise
    sd = np.array(sd) / 100 * width
    noise = ill.image_blobs(img.size, n=n, sd=sd).convert("RGB")
    noise.putalpha(PIL.Image.new('L', noise.size, 255))

    # Blend with noise
    stim = PIL.Image.blend(img, noise, alpha=alpha / 100)

    # Normalize
    arr = np.array(stim)
    arr[:, :, 0:3] = ill.rescale(arr[:, :, 0:3], to=[0, 255])
    arr[:, :, 3] = 255
    stim = PIL.Image.fromarray(arr)
    # stim = PIL.ImageOps.autocontrast(stim.convert("RGB"))

    stim.convert("RGB")

    return stim




# hide_pattern(path="patterns/png/woman_4.png",
#              n=[10, 1000],
#              sd=[20, 2],
#              alpha=25,
#              blur=0.1,
#              negative=False)





# Demo
pattern = PIL.Image.open("patterns/png/woman_4.png")
imgs = []
for alpha in [50, 70, 90]:
    for blur in [1, 2, 4]:
        stim = hide_pattern(path=pattern,
                            n=[10, 1000],
                            sd=[20, 2],
                            alpha=alpha,
                            blur=blur)


        PIL.ImageDraw.Draw(stim).text((0, 0),
                                      f"alpha = {alpha}%, blur = {blur}%",
                                      (255, 0, 0),
                                      font = PIL.ImageFont.truetype("arial.ttf", 60))

        imgs.append(stim)




nrows, ncols = int(np.sqrt(len(imgs))), int(np.sqrt(len(imgs)))
new = PIL.Image.new('RGBA', (imgs[0].width * nrows, imgs[0].height * ncols))
i = 0
for row in range(nrows):
    for col in range(ncols):
        new.paste(imgs[i], (imgs[i].width * row, imgs[i].height * col))
        i += 1

new.putalpha(PIL.Image.new('L', noise.size, 255))
new.save("demo.png")
