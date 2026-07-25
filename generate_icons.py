import os

from PIL import Image

input_file = "assets/icon.png"
output_dir = "patches/images"

sizes = [16, 32, 48, 96, 128, 256, 512]
icons = {}

os.makedirs(output_dir, exist_ok=True)

img = Image.open(input_file)

for size in sizes:
    resized = img.resize((size, size), Image.LANCZOS)
    output_path = os.path.join(output_dir, f"icon{size}_sunset.png")
    resized.save(output_path, "PNG")
    icons[str(size)] = f"images/icon{size}_sunset.png"

print("Icons generated.")
print(icons)
