from PIL import Image
import os

def compress_image(input_path, output_path, target_size_kb=10):
    target_size = target_size_kb * 1024

    img = Image.open(input_path)

    quality = 85
    img.save(output_path, format='JPEG', quality=quality)

    while os.path.getsize(output_path) > target_size:
        quality -= 5
        img.save(output_path, format='JPEG', quality=quality)

        if quality < 10:
            break

    if os.path.getsize(output_path) > target_size:
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.LANCZOS)

        img.save(output_path, format='JPEG', quality=quality)

        while os.path.getsize(output_path) > target_size:
            quality -= 5
            img.save(output_path, format='JPEG', quality=quality)

            if quality < 10:
                break


compress_image('111.jpg', 'output.jpg')
