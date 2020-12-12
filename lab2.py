# На языке Python разработайте скрипт, кластеризующий загруженные данные о стоимости n автомобилей на 
# определенные им кластеры, обозначенные заданными в программе лингвистическими метками. Максимальное 
# количество меток задать самостоятельно

# Static parametrs
m=1.6
r=3.33
count=0

import matplotlib.pyplot as plt


plCluster = []
xAxys=[]
yAxys=[]
# Input
n = input()
FuncP={}
if n!="t": # "t" mean "test"
    n=int(n)
    for i in range(n):
        cost=input() 
        FuncP[cost]=list(map(int,input().split( )))
else:
    n=5
    cost=10
    FuncP[1*cost]=[0.2,0.3,0.5]
    FuncP[2*cost]=[0.3,0.2,0.5]
    FuncP[3*cost]=[0.1,0.7,0.2]
    FuncP[4*cost]=[0.8,0.1,0.1]
    FuncP[5*cost]=[0.4,0.3,0.3]

    
for keyF in FuncP: plCluster.append(keyF)

# Work
def Clusterization(oldJ,count,FuncP):
    ncluster = len(FuncP[cost])
    cluster={}
    u={}
    ux={}
    for i in range(ncluster):
        u[i]=[]
        ux[i]=[]
        for nameFuncP in FuncP:
            u[i].append(FuncP[nameFuncP][i]**m)
            ux[i].append(nameFuncP*FuncP[nameFuncP][i]**m)

    for i in u: u[i]=sum(u[i])
    for i in ux: ux[i]=sum(ux[i])

    for i in range(ncluster):
        cluster[i]=ux[i]/u[i]

    l={}
    for i in range(ncluster):
        l[i]=[]
        for nameFuncP in FuncP:
            l[i].append(abs(nameFuncP-cluster[i]))

    lr={}
    for i in range(ncluster):
        lr[i]=[]
        lr_kosta=[]
        for a in range(len(l[0])):
            summl=0
            for j in range(ncluster):
                summl+=(l[j][a]/l[i][a])**r        
            lr_kosta.append(1/summl)
        lr[i]=(lr_kosta)
    # print(lr)

    J=0
    for keyLr in lr:
        for i in range(len(lr[keyLr])): 
            J+=l[keyLr][i]*lr[keyLr][i]**m
    
    newFuncP={}
    for key in lr:
        for i in range(len(lr[key])):
            newFuncP[i*cost]=[]
            for key2 in lr:
                newFuncP[i*cost].append(lr[key2][i])
    
    if J!=oldJ :
        Clusterization(J,count+1,newFuncP)
    else:
        print("Кол-во итераций: ", count)
        # for key in lr:
        #     print(key, " : ", lr[key],"\n")
        # print(cluster)
    ans=[]
    ans.append(cluster)
    ans.append(lr)
    return ans

ans = Clusterization(-1,0,FuncP)

clust=ans[0]
lrAns=ans[1]
print(clust)
for key in lrAns:
    print(key, " : ", lrAns[key],"\n")

for kClust in clust:
    plCluster.append(clust[kClust])

for keyF in FuncP: xAxys.append(keyF)

for x in xAxys: 
    plt.scatter(x,1, c='blue')
for x in clust: 
    plt.scatter(clust[x],1, c='red')

plt.show()