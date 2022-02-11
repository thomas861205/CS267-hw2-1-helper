import numpy as np
import re
from sklearn.linear_model import LinearRegression


# x = np.array([10, 100, 1000, 10000, 100000]).reshape(-1, 1)
# y = np.array([0.0130276, 0.149636, 1.66018, 18.7878, 224.509])
x = []
y = []

with open('benchmark.txt', 'r') as file:
    lines = file.readlines()

for idx, line in enumerate(lines):
    n_pattern = re.compile('for (.*) particles')
    t_pattern = re.compile('Time = (.*) seconds')
    n = n_pattern.findall(line)[0]
    t = t_pattern.findall(line)[0]
    # print(n, t)
    x.append(int(n))
    y.append(float(t))

x = np.array(x).reshape(-1, 1)
y = np.array(y)

logx = np.log(x)
logy = np.log(y)

my_model = LinearRegression().fit(logx, logy)
print('r-square: ', my_model.score(logx, logy))
print('serial slowdown: ', my_model.coef_[0])