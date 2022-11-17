import numpy as np
import scipy
x = np.array([172,177,158,170,178,175,164,160,169,165])
y = np.array([173,175,162,174,175,168,155,170,160])

mother = np.mean(x)
print(f'Среднее значение по выборке матери = {mother}')
daughter = np.mean(y)
print(f'Среднее значение по выборке дочери = {daughter}')
S = np.std(y,ddof = 1)
print(f'Стандартное несмещенное отклонение по выборке = {S}
L = len(y)
print(f'Количество значений по выборке дочери = {L}')
delta = 168 -168,8
a = delta/S
b = a/np.sqrt(9)
#t = 168-168,8/7,35/np.sqrt(9)
print(f'Критерий Стъюдента = {b}')
K = L - 1
print(f'Значение степени свободы = {K}')
Res = scipy.stats.ttest_rel(x,y)
print(f'Зависимые выборки, двухвыборочный тест.Значение p-value = {Res}')