import matplotlib.pyplot as plt
import numpy as np


def cria_grafico(data):
 rpm_value = data
 rpm_time = []
 i = 0
 for i in range(len(rpm_value)):
   rpm_time.append(i)
 x = rpm_time  
 y = rpm_value
 fig, ax = plt.subplots()
 ax.plot(x, y)
 plt.show()

