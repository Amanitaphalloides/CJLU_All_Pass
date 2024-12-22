from PIL import Image

CHARS = " 　的一是了不在有我他她它们这那你们是个好一个人们和为上来去对说而也就要"

def image_to_ascii(input_image_path, output_text_path, width=100):

    img = Image.open(input_image_path)
    img = img.convert("L")

    # 计算图像的高度
    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width * 0.5)

    img = img.resize((width, height))

    pixels = img.getdata()

    ascii_str = ""
    num_chars = len(CHARS)

    for pixel in pixels:

        char_index = min(pixel * num_chars // 256, num_chars - 1)
        ascii_str += CHARS[char_index]

    ascii_str_len = len(ascii_str)
    ascii_image = "\n".join(ascii_str[i:i + width] for i in range(0, ascii_str_len, width))

    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(ascii_image)

image_to_ascii('111.jpg', 'output.txt')
