import matplotlib.pyplot as plt
import euc
import cos


# Функция для создания графика по выходым данным КНН
def scatter_plot(complete_data, match_data, obj_classifying, title=None,):
    # Создаём объект графика
    _, scatter_plot = plt.subplots()
    
    # Создаём два списка чтобы хранить координаты X и Y полных данных
    x_complete_data = []
    y_complete_data = []
    # Заполняем эти списки
    for age, review in complete_data:
        x_complete_data.append(age)
        y_complete_data.append(review)
    # Отрисовываем график со всеми данными
    scatter_plot.scatter(x_complete_data, y_complete_data, color = '#0066cc')

    # Создаём два списка чтобы хранить координаты X и Y данных выбранных алгоритмом
    x_match_data = []
    y_match_data = []
    # Заполняем эти списки
    for age, review in match_data:
        x_match_data.append(age)
        y_match_data.append(review)
    # Перерисовываем часть графика, чтобы изменить цвета
    # Теперь обычные точки – синие, а точки выбранные алгоритмом – красные
    scatter_plot.scatter(x_match_data, y_match_data, color = '#ff0806')
    
    # Ещё раз перерисовываем график
    # Обычные точки – синие, точки выбранные алгоритмом – красные, точка классификации – зелёная
    scatter_plot.scatter(obj_classifying[0], obj_classifying[1], color = '#00984c')

    # Подписываем график
    scatter_plot.set_title(title)
    # Подписываем ось X как возраст
    scatter_plot.set_xlabel('Возраст')
    # Подписываем ось Y как оценку
    scatter_plot.set_ylabel('Оценка')
    # Показываем график на экране
    plt.show()


# Получаем данные от КНН на Евклидовой метрике
euc_match = euc.KNN(euc.user_for_classifying, euc.age_review, 5)
# Создаём список точек выбранных алгоритмом
euc_match_by_age_review = []
# Перегоняем данные из вида [(дистанция, айдишник)] пользователя
# В вид [(возраст, оценка)] пользователя
for _, index in euc_match:
    age = euc.age_review[index][0]
    review = euc.age_review[index][1]
    euc_match_by_age_review.append((age, review))

# Получаем данные от КНН на Метрике косинусов
cos_match = cos.KNN(cos.user_for_classifying, cos.age_review, 5)
# Создаём список точек выбранных алгоритмом
cos_match_by_age_review = []
# Перегоняем данные из вида [(дистанция, айдишник)] пользователя
# В вид [(возраст, оценка)] пользователя
for _, index in cos_match:
    age = cos.age_review[index][0]
    review = cos.age_review[index][1]
    cos_match_by_age_review.append((age, review))

# Рисуем график по данным КНН на Евклидовой метрике
scatter_plot(euc.age_review.values(), euc_match_by_age_review, euc.user_for_classifying, 'Евклидова метрика')
# Рисуем график по данным КНН на Метрике косинусов
scatter_plot(cos.age_review.values(), cos_match_by_age_review, cos.user_for_classifying, 'Метрика косинусов')