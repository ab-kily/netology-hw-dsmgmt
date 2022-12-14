Анализ вина по физико-химическим данным
=======================================

Ежегодное потребление вина в мире постоянно увеличивается. Но знаем ли мы, какого качества вино мы пьем? В попытке ответить на этот вопрос мы разработали нейронную сеть на основе датасета из конкурса Kaggle. Содержимое датасета содержит данные по красному и белому вариантам португальского вина «Vinho Verde». 

Данный репозиторий сделан на основе методологии CRISP-DM.

Сама модель находится здесь: [Модель](model/)
Отчет об исследовании: [Отчeт](docs/report.pdf)

### Быстрый старт

Используется `poetry` для управления зависимости виртуальными средами. Для прохождения всего пути исследования используйте:
```
pip install poetry
poetry install
poetry run jupyter notebook docs/model.ipynb
```

Если вы хотите просто воспользоваться моделью:
```python
from tensorflow import keras
model = keras.models.load_model('./model')
```


### Описание признаков и целевой переменной

Входные переменные (на основе физико-химических тестов):
- фиксированная кислотность
- летучая кислотность
- лимонная кислота
- остаточный сахар
- хлориды
- свободный диоксид серы
- общий диоксид серы
- плотность
- pH
- сульфаты
- алкоголь

Выходная переменная (на основе сенсорных данных):
- качество (оценка от 0 до 10)

### Методы решения

Задачу определения качества вина можно свести как к задаче классификации, так и к задаче регрессии (в случае, если представить качество вина в виде числа от 0 до 10). В данной работе мы решили эту задачу методом регрессии.

### Feature Engeneering

В данной работы мы не использовали методы Feature Engeneering.

### Модели и их настройка

В работе использовалась одна модель - многослойный перцептрон со слоями Dropout и BatchNormalization. [Модель](models/perceptron.ipynb)

### План выбора финальной модели

Модель выбиралась по принципу наименьшего значения Mean Absolute Error (MAE). По результатам обучения нейронной сети, которое продолжалось на протяжении 100 эпох, удалось достичь показателя MAE в 0.563, что является неплохим результатом. Если говорить простым языком, модель ошибается в среднем на 0.5 балла при оценке качества вина. 

