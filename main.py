from PIL import Image
import os

DIR = "in"
MAX = 1600
SAVE_DIR = "out"
Image.MAX_IMAGE_PIXELS = None

for filename in os.listdir(DIR):
  if filename.endswith(('.png', '.jpg', '.jpeg')):
    filepath = os.path.join(DIR, filename)

    pre, ext = os.path.splitext(filename)
    output_path = os.path.join(SAVE_DIR, pre + '.jpg')

    with Image.open(filepath) as img:
      img.load()
      img = img.convert('RGB')
      print("filepath:", filepath)

      resize_ratio = (MAX / img.size[0] + MAX / img.size[1]) / 2
      print("resize_ratio:", resize_ratio)

      new_size = (int(img.size[0] * resize_ratio), int(img.size[1] * resize_ratio))
      print("new_size:", new_size)

      img = img.resize(new_size)

      img.save(output_path, quality=80)

