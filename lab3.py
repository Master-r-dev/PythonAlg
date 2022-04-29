import numpy as np
import matplotlib.pyplot as plt
s=2 # стандартное отклонение наблюдаемых значений
k=0.25 #теор значение параметра k (y=kx+b)
b=3 #теор значение параметра b (y=kx+b)
N=500 # число экспериментов
t=np.array([k*i+b for i in range(N)])
y=np.random.normal(0,s,N) + t
x=np.array(range(N))

mx=x.sum()/N
my=y.sum()/N
a2=np.dot(x.T, x)/N
a11=np.dot(x.T, y)/N

k_gauss=(a11-mx*my)/(a2-mx**2)
b_gauss=my-k_gauss*mx
t_gauss=np.array([k_gauss*i+b_gauss for i in range(N)])

plt.plot(t)
plt.plot(t_gauss,c='yellow')
plt.scatter(x,y,s=2,c='blue')
plt.grid(True)
plt.show()