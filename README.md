# Налоговый календарь

## Главное окно
<img src='./screenshot/Налоговый календарь.png'>

## Настройки
<img src='./screenshot/Налоговый календарь + настройки.png'>

## Для разработчиков
### Установка зависимостей
1. `python -m venv venv`
2. `.\venv\Scripts\activate` (windows)
3. `pip install -r requirements.txt`

### Запуск приложения
1. Константа `IS_DEV` в модулях [./main.py](./main.py) и [./autostart.py](./autostart.py) дожна быть равна `True`
2. Запуск приложения: `python main.py`

### Сборка
1. Константа `IS_DEV` в модулях [./main.py](./main.py) и [./autostart.py](./autostart.py) дожна быть равна `False`
2. Сборка программы `python setup build`
3. Сборка установщика `python setup bdist_msi`