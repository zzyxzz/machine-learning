import pylab as plt
import numpy as np
import random
tmp    = np.array([[random.randint(15,30), random.randint(10,30)] for row in range(400)])
sam    = np.array([[random.randint(0,20), random.randint(0,20)] for row in range(400)])

sample = np.concatenate((tmp,sam))

k = np.array([[random.randint(0,30),random.randint(0,30)],[random.randint(0,30),random.randint(0,30)]])
print k
k1list = []
k2list = []

def distance(sp,kp):
    x1 = sp[:,0]
    y1 = sp[:,1]
    x2 = kp[0]
    y2 = kp[1]
    dlist = []
    for i in range(len(x1)):
        euld  = (x1[i] - x2)**2 + (y1[i] - y2)**2
        dlist.append(euld)
    return dlist

for np in range(10):
    
    k1 = distance(sample,k[0])
    k2 = distance(sample,k[1])
    
    k1x,k2x,k1y,k2y = 0,0,0,0
    k1n,k2n = 0,0

    k1list[:] = []
    k2list[:] = []
    
    for i in range(len(k1)):
        if k1[i] < k2[i]:
            k1x += sample[i,0]
            k1y += sample[i,1]
            k1n += 1
            k1list.append(sample[i])
            
        else:
            k2x += sample[i,0]
            k2y += sample[i,1]
            k2n += 1
            k2list.append(sample[i])
            
            
    k[0] = [k1x/k1n,k1y/k1n]
    k[1] = [k2x/k2n,k2y/k2n]
    print k

    plt.figure()
    plt.scatter([k1list[i][0] for i in range(len(k1list))], [k1list[i][1] for i in range(len(k1list))], color = 'y')
    plt.scatter([k2list[i][0] for i in range(len(k2list))], [k2list[i][1] for i in range(len(k2list))], color = 'b')
    plt.scatter(k[0,0],k[0,1], color = 'yellow', s = 160)
    plt.scatter(k[1,0],k[1,1], color = 'blue', s = 160)
    plt.show()

