from PIL import Image

END_MARKER = '1111111111111110'

def text_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def embed_data(image, secret_data):
    img = image.copy()
    binary_data = text_to_binary(secret_data) + END_MARKER
    data_index = 0
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            if data_index < len(binary_data):
                r = (r & ~1) | int(binary_data[data_index]); data_index += 1
            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index]); data_index += 1
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index]); data_index += 1

            pixels[x, y] = (r, g, b)

            if data_index >= len(binary_data):
                return img
    return img

def extract_data(image):
    binary_data = ""
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    binary_data = binary_data.split(END_MARKER)[0]
    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    return ''.join(chr(int(byte, 2)) for byte in bytes_data if len(byte) == 8)
