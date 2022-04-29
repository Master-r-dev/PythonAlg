import numpy as np 
import matplotlib.pyplot as plt
import math as math
from scipy import ndimage
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
# данные 18 варианта
a=4
b=13
alpha=2
c=0 # нижний предел для a
d=15 # верхний предел для b
karmany=200
# равномерное
x=np.array([(d-c)/karmany*x+c for x in range(karmany)])
y=np.array([0 for x in range(karmany)])
for i in range(10000):
    r=np.random.rand()*(b-a)+a
    y[find_nearest(x, r)]+=1
plt.plot(x,y,'ro-')
plt.grid(True)
plt.show()
#мат ожидание
mat=(b+a)/2
#дисперсия
dis=(b-a)*(b-a)/12
print("mat_uniform=",mat)
print("dis_uniform=",dis)
################################
#мат ожидание экспоненциально случ величины
mat=1/alpha
#дисперсия экспоненциально случ величины
dis=1/(alpha*alpha)
print("mat_exp=",mat)
print("dis_exp=",dis)
y=np.array([0 for x in range(karmany)])
for i in range(10000):
    r=-mat*math.log(1-np.random.rand()) # экспоненциально случ величины
    y[find_nearest(x, r)]+=1
plt.plot(x,y,'ro-')
plt.grid(True)
plt.show()
################################
c=-40
d=40
karmany=200
x=np.array([(d-c)/karmany*x+c for x in range(karmany)])
y=np.array([0 for x in range(karmany)])
m=10
sigma=6
N=10000
rrr=np.array([0 for x in range(N)])
for i in range(N):
    rr=0    
    for q in range(12):
        rr+=np.random.rand()
    r=m+sigma*(rr-6) # экспоненциально случ величины
    rrr[i]=r
    y[find_nearest(x, r)]+=1
plt.plot(x,y,'ro-')
plt.grid(True)
plt.show()
#мат ожидание экспоненциально случ величины
mat=ndimage.mean(rrr)
#дисперсия экспоненциально случ величины
dis=ndimage.variance(rrr)
print("mat_normal=",mat)
print("dis_normal=",dis)
