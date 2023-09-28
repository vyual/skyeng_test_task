# Используем официальный образ Python 3.11
FROM python:3.11

# Устанавливаем переменную окружения для отключения вывода сообщений pip
ENV PYTHONUNBUFFERED 1

# Создаем директорию для приложения и устанавливаем ее в качестве рабочей
RUN mkdir /app
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения
COPY . /app/

# Этот порт будет использоваться для доступа к вашему Django приложению
EXPOSE 8000

# Запускаем Django приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
