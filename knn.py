import numpy as np
from collections import Counter


def L2_norm(x, y):                                                   #функция считает Евклидово расстояние между двумя точками
    return np.linalg.norm(x-y, ord=2)


class Point:

    value_vector = None                                              #координаты точки
    ob_class = None                                                  #класс, к которому точка принадлежит

    def __init__(self, value, class_):
        self.value_vector = np.array(value)
        self.ob_class = class_

class Knn:

    tr_set = []                                                      #здесь будет храниться обучающая выборка
    k = None                                                         #колличество соседей

    def __init__(self, num_of_ngb):
        self.k = num_of_ngb

    def fit(self, x_val, y_val):                                    #принимает массив точек и массив классов, которым эти точки соответствуют
        num_of_points = len(y_val)

        for i in range(num_of_points):                              #заполняет массив tr_set
            self.tr_set.append(Point(x_val[i], y_val[i]))

    def predict(self, x_val):
        distance = sorted(self.tr_set, key=lambda item: L2_norm(x_val, item.value_vector))                      #сортирует точки в зависимости от расстояния до заданной
        distance = distance[:self.k]                                                                            #оставляет только первые k из них

        class_variety = [item.ob_class for item in distance]                                                    #массив из значений классов, которым принадлежат ближайшие k соседей

        return Counter(class_variety).most_common(1)[0][0]                                                      # возвращает класс, который встречался наибольшее число раз в массиве class_variety


points = np.array([[2, 2], [1, 1], [3, 1], [6, 5], [6, 4], [5, 3]])
point_class = np.array([0, 0, 0, 1, 1, 1])

my_knn = Knn(3)

my_knn.fit(points, point_class)
print(my_knn.predict([[2, 5]]))

