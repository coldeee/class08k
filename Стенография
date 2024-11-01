from PIL import Image

def embed_data(image_path, data, output_image_path):
    """
    Встраивает зашифрованные данные в изображение с использованием LSB-стеганографии.

    :param image_path: Путь к исходному изображению.
    :param data: Данные для встраивания (зашифрованный текст).
    :param output_image_path: Путь для сохранения нового изображения.
    """
    # Преобразуем данные в двоичный формат
    binary_data = ''.join(format(ord(i), '08b') for i in data)
    binary_data += '1111111111111110'  # Концевой маркер

    # Открываем изображение
    img = Image.open(image_path)
    img = img.convert("RGB")  # Убедимся, что изображение в формате RGB
    data_len = len(binary_data)

    if data_len > img.size[0] * img.size[1] * 3:
        raise ValueError("Данные слишком большие для изображения.")

    data_index = 0
    pixels = list(img.getdata())

    for i in range(len(pixels)):
        if data_index < data_len:
            pixel = list(pixels[i])
            for j in range(3):  # Проходим по каждому каналу RGB
                if data_index < data_len:
                    pixel[j] = (pixel[j] & ~1) | int(binary_data[data_index])
                    data_index += 1
            pixels[i] = tuple(pixel)

        if data_index >= data_len:
            break

    # Сохраняем измененное изображение
    img.putdata(pixels)
    img.save(output_image_path)
    print(f"Данные успешно встроены в изображение и сохранены как {output_image_path}")

if __name__ == "__main__":
    # Пример использования функции
    image_path = input("Введите путь к исходному изображению: ")
    encrypted_data = input("Введите зашифрованные данные для встраивания: ")
    output_image_path = input("Введите путь для сохранения нового изображения: ")

    try:
        embed_data(image_path, encrypted_data, output_image_path)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
