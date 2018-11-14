
#!/usr/bin/env python3
#INTL
# -*- coding: utf-8 -*-

import math #подключаем необходимые библиотеки
import numpy
import matplotlib.pyplot as mpp 


if __name__=='__main__': #этот код запускается сам по себе, а не импортирован как модуль куда-нибудь
    arguments = numpy.r_[0:200:0.1] #задаем параметры "прорисовки"(интервал аргумента и его шаг)
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #вычисляем значение функции
    )
    mpp.show() #выводим результат в виде графика

