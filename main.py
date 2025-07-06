# Импорт необходимых библиотек
import shutil  # Для расширенных файловых операций
from pathlib import Path  # Нужна для получения пути


class FileManager:  # Вводим класс FileManager

    # Вводим метод __init__, который
    def __init__(self, path):
        # Преобразуем путь и сохраняем как Path
        self.path = Path(path)

    # Вводим метод create, который создаёт файл или директорию с проверкой на их существование
    def create(self, is_file: bool = True, content=""):

        # Проверка существования пути
        if self.path.exists():
            # Генерируем соответствующее сообщение об ошибке
            print(f"{'Файл' if is_file else 'Директория'} уже существует: {self.path}")

        # Создание файла
        if is_file:
            # Создаем родительские директории при необходимости
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # Открываем файл для записи
            with open(self.path, 'w', encoding='utf-8') as f:
                # Записываем содержимое, если оно передано
                if content:
                    f.write(content)
        # Создание директории
        else:
            # Создаем директорию (с родительскими при необходимости)
            self.path.mkdir(parents=True)

    # Вводим метод read, который выводит содержимое файла в консоль
    def read(self):

        # Проверка что это директория
        if self.path.is_dir():
            print(f"Невозможно прочитать директорию как файл: {self.path}")
        # Проверка существования файла
        if not self.path.exists():
            print(f"Файл не найден: {self.path}")
        # Чтение файла
        with open(self.path, 'r') as f:
            return f.read()

    # Вводим метод delete, который удаляет файл или директорию, запрашивая подтверждение
    def delete(self):
        # Проверка существования пути
        if not self.path.exists():
            print(f"Путь не найден: {self.path}")
        # Запрос подтверждения у пользователя
        confirmation = input(f"Вы уверены, что хотите удалить {self.path}? [y/N]: ")
        # Проверка ответа (только 'y' или 'Y' подтверждает удаление)
        if confirmation.lower() != 'y':
            print("Удаление отменено")
            return False

        # Удаление файла
        if self.path.is_file():
            self.path.unlink()
        # Удаление директории
        else:
            shutil.rmtree(self.path)  # Рекурсивное удаление директории
        return True

    def list(self):  # Вводим метод list, который вывоит список файлов в директории
        # Проверка что это директория
        if not self.path.is_dir():
            print(f"Путь не является директорией: {self.path}")
        # Возвращаем список имен содержимого директории
        return [item.name for item in self.path.iterdir()]

    def __str__(self):
        """Вводим магический метод __str__,
    который описывает текстовое представление объекта данного класса"""
        # Если путь не существует
        if not self.path.exists():
            print(f"Путь не существует: {self.path}")
        # Если файл - возвращаем информацию с размером
        if self.path.is_file():
            print(f"Файл: {self.path} (размер: {self.path.stat().st_size} байт)")

        # Для директории - возвращаем информацию о количестве элементов
        print(f"Директория: {self.path} (содержит {len(list(self.path.iterdir()))} элементов)")
