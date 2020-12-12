# На языке Python разработайте скрипт, позволяющий выполнить операцию пересечения заданных пользователем 
# нечетких множеств с треугольными функциями принадлежности. Входными данными будут параметры функций 
# принадлежности и четкие объекты для каждого из множеств. Выходными – пересечение данных нечетких множеств. 

# In:   
# Незначительная 0.9 0.6 0.3 0 0
# Ожидаемая 0.3 0.6 0.9 0.6 0.3
# Значительная 0 0 0.3 0.6 0.9

# Out в виде plot

import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

print("Пишите функции принадлежности (пример - Незначительная 0.9 0.6 0.3 0 0), после напишите END")
funcP={}
while True:
    inString = input()
    if inString == "END": break
    if inString == "t1": inString = "Незначительная 0.9 0.6 0.3 0 0"
    if inString == "t2": inString = "Ожидаемая 0.3 0.6 0.9 0.6 0.3"
    if inString == "t3": inString = "Значительная 0 0 0.3 0.6 0.9"

    splitInString=inString.split(" ")
    arr=[]
    for i in splitInString[1:]:
         arr.append(float(i))
    funcP[splitInString[0]] = arr

minArr=[]
for i in range(len(funcP[splitInString[0]])): minArr.append(1.0)
for a in funcP: 
    for i in range(len(funcP[a])): 
        if funcP[a][i]<minArr[i]: minArr[i]=float(funcP[a][i])
funcP["ПЕРЕСЕЧЕНИЕ"] = minArr

x=linspace(0,100,len(funcP[splitInString[0]]), dtype=int) #задаем множество х
for a in funcP: 
    print(a,x,funcP[a])
    plt.plot(x, funcP[a], label=a)

for i in range(len(funcP["ПЕРЕСЕЧЕНИЕ"])) :
    if funcP["ПЕРЕСЕЧЕНИЕ"][i]!=0 and i>0 and i<len(funcP["ПЕРЕСЕЧЕНИЕ"]):
        print("\nПересечение принадлежит промежутку от {} до {}".format(x[i-1],x[i+1]))
    if funcP["ПЕРЕСЕЧЕНИЕ"][i]!=0 and i==0:
        print("\nПересечение принадлежит промежутку от 0 до {}".format(x[i+1]))
    if funcP["ПЕРЕСЕЧЕНИЕ"][i]!=0 and i==len(funcP["ПЕРЕСЕЧЕНИЕ"]):
        print("\nПересечение принадлежит промежутку от {} до 1".format(x[i-1]))

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
plt.show()