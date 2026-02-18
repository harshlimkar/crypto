from PIL import Image

END_MARKER = '1111111111111110'


def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)


def embed_data(image, secret_data):
    """
    Embed secret data inside an image using LSB steganography
    """

    # ✅ Force image to RGB (fixes RGBA error)
    img = image.convert("RGB")
    pixels = img.load()

    binary_data = text_to_binary(secret_data) + END_MARKER
    data_index = 0
    data_length = len(binary_data)

    for y in range(img.height):
        for x in range(img.width):
            if data_index >= data_length:
                return img

            r, g, b = pixels[x, y]

            if data_index < data_length:
                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1

            if data_index < data_length:
                g = (g & ~1) | int(binary_data[data_index])
                data_index += 1

            if data_index < data_length:
                b = (b & ~1) | int(binary_data[data_index])
                data_index += 1

            pixels[x, y] = (r, g, b)

    return img


def extract_data(image):
    """
    Extract hidden data from an image using LSB steganography
    """

    # ✅ Force image to RGB (important!)
    img = image.convert("RGB")
    pixels = img.load()

    binary_data = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

            # ✅ Stop early if END_MARKER found
            if END_MARKER in binary_data:
                binary_data = binary_data.split(END_MARKER)[0]
                return binary_to_text(binary_data)

    return ""
