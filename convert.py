from PIL import Image

for i in [0, 246]:
    print(f"converting image: {i}")
    img = Image.open(f"out/{i}.jpg")
    img.convert("RGB").save(f"img/{i}.jpg")
