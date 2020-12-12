# Оценка прибыли - [0,100000]
# Метки шкал - [Нулевая(0-12000), Незначительная(8000-37000), Ожидаемая(33000-72000), Значительная(68000-100000)]
# сократим 000 -> К
# Метки шкал - [Нулевая(0-12), Незначительная(8-37), Ожидаемая(33-72), Значительная(68-100)]
# Ф.принадлеж. = 1 - [Нулевая(0-9), Незначительная(10-34), Ожидаемая(35-69), Значительная(70-100)]
# Характеристики изменения - (рост, стабильность, снижение)
# Характеристики интенсивности изменения - (просто, сильный, значительный)

from matplotlib import pyplot as plt
import numpy as np
import random
TimeArray = [5,8,12,13,9,14,25,30,36,34,70,60,65,68,71]
predTimeArray = [71,70,82,83,94,88,93,97,100,99]
DictFP_1 = {"Zero" : [], "Minor" : [], "Expect" : [], "Major" : []}
for i in range(10): DictFP_1["Zero"].append(i)
for i in range(10,35): DictFP_1["Minor"].append(i)
for i in range(35,70): DictFP_1["Expect"].append(i)
for i in range(70,100): DictFP_1["Major"].append(i)
TendantionSymbolArray = ["decrease","stable", "groth"]
IntensiveSymbolArray = ["simple", "strong", "significant"]


def Tendetion(key,prevKey):
    if FuzzyMean(key)<FuzzyMean(prevKey): 
        a=[TendantionSymbolArray[0],IntensiveSymbolArray[FuzzyMean(prevKey)-FuzzyMean(key)-1]]
        return a
    if FuzzyMean(key)==FuzzyMean(prevKey): 
        a=[TendantionSymbolArray[1],""]
        return a
    if FuzzyMean(key)>FuzzyMean(prevKey): 
        a=[TendantionSymbolArray[2],IntensiveSymbolArray[FuzzyMean(key)-FuzzyMean(prevKey)-1]]
        return a

def FuzzyMean(key):
    count=0
    for k in DictFP_1:
        count+=1
        if key==k:break
    return count



FuzzyTimeArray=[]
TendantionArray=[]
IntensiveArray=[]
for i in range(len(TimeArray)):
    for key in DictFP_1:
        if TimeArray[i] in DictFP_1[key]: 
            FuzzyTimeArray.append(key)
            if i>=1: 
                TendantionArray.append(Tendetion(key,FuzzyTimeArray[i-1])[0])
                IntensiveArray.append(Tendetion(key,FuzzyTimeArray[i-1])[1])
            else:    
                TendantionArray.append(" ")
                IntensiveArray.append(" ")
            print(TimeArray[i],FuzzyTimeArray[i],TendantionArray[i],IntensiveArray[i])

# print(FuzzyTimeArray)
# print(TendantionArray)

plotX=[]
for i in range(len(FuzzyTimeArray)): plotX.append(i)
fig, axs = plt.subplots(2)
axs[0].plot(plotX,FuzzyTimeArray,c="blue")

barY=[0,0,0]
for i in TendantionArray:
    if i == TendantionSymbolArray[0] : barY[0]+=1
    if i == TendantionSymbolArray[1] : barY[1]+=1
    if i == TendantionSymbolArray[2] : barY[2]+=1
axs[1].bar(TendantionSymbolArray,barY)
# plt.show()



# Лаба 5 ПНВР
def predictTendention(arrTendanton, tendSymbol, countFA, maxCountFA, countPredict):
    # print("\n", arrTendanton)
    arrRuleBase = []
    for i in range(1,len(arrTendanton)): arrRuleBase.append(arrTendanton[i-1]+"-"+arrTendanton[i])
    # print("\n", arrRuleBase)
    dictRuleBase = {}
    for i in arrRuleBase: 
        if i not in dictRuleBase:
            dictRuleBase[i]=1
        else:
            dictRuleBase[i]+=1
    # print("\n", dictRuleBase)

    last = arrTendanton[len(arrTendanton)-1]
    # print(last)
    variation = {}
    summVariation=0
    for key in dictRuleBase:
        if last in key.split("-")[0]: 
            summVariation+=dictRuleBase[key]
            variation[key.split("-")[1]]=dictRuleBase[key]

    weight = []
    for i in variation: weight.append(variation[i]/summVariation)
    # print(variation, weight)
    predTend = np.random.choice(
        a=list(variation), 
        p=weight)
    # print(predTend)
    if predTend == tendSymbol[2]: 
        if countFA<maxCountFA: countFA+=1
        else: predTend=tendSymbol[1]
    if predTend == tendSymbol[0]:
        if countFA>0: countFA-=1
        else: predTend=tendSymbol[1]

    arrTendanton.append(predTend)
    if countPredict-1>0: predTend+=", " + predictTendention(arrTendanton, tendSymbol, countFA, maxCountFA, countPredict-1)
    return predTend


countFuzzyArr = 0
for key in DictFP_1:
    countFuzzyArr+=1
    if key == FuzzyTimeArray[len(FuzzyTimeArray)-2]: break
maxCountFuzzyArr = len(list(DictFP_1))
print( "\nПредсказываем отсюда - ", TimeArray[len(TimeArray)-2], FuzzyTimeArray[len(FuzzyTimeArray)-2], " Это по счётчику - ", countFuzzyArr)
arrTendanton = TendantionArray[1:(len(TendantionArray)-1)]


predTend = predictTendention(arrTendanton, TendantionSymbolArray, countFuzzyArr, maxCountFuzzyArr, 10)
print("Предсказанная тенденция - ", predTend, "\n")


def predArrGen(cFuzzyArr,arrFuzzySymbol):
    if cFuzzyArr==1: return arrFuzzySymbol[0]
    if cFuzzyArr==2: return arrFuzzySymbol[1]
    if cFuzzyArr==3: return arrFuzzySymbol[2]
    if cFuzzyArr==4: return arrFuzzySymbol[3]

arrFuzzyTimeSymbol=[]
for key in DictFP_1: arrFuzzyTimeSymbol.append(key)
# print(arrFuzzyTimeSymbol)

predFuzArr=[] #countFuzzyArr
for i in predTend.split(", "):
    if i == "stable": 
        predFuzArr.append(predArrGen(countFuzzyArr,arrFuzzyTimeSymbol))
    if i == "groth":
        if countFuzzyArr<maxCountFuzzyArr: countFuzzyArr+=1
        predFuzArr.append(predArrGen(countFuzzyArr,arrFuzzyTimeSymbol))
    if i == "decrease": 
        if countFuzzyArr>1: countFuzzyArr-=1
        predFuzArr.append(predArrGen(countFuzzyArr,arrFuzzyTimeSymbol))
# print(predFuzArr)

# predArrGen
predArrGet=[]
predArrErr=[]
countPredArrGen=0
for i in predFuzArr:
    if i == "Zero": predArrGet.append(random.randint(0,10))
    if i == "Minor": predArrGet.append(random.randint(10,35))
    if i == "Expect": predArrGet.append(random.randint(35,70))
    if i == "Major": predArrGet.append(random.randint(70,100))
    a=float(((predTimeArray[countPredArrGen]-predArrGet[countPredArrGen])/predTimeArray[countPredArrGen]))
    if a<0.0: a*=(-1)
    countPredArrGen+=1
    predArrErr.append(a)
for i in range(len(predTimeArray)):
    print("Ожидаемое - ", predTimeArray[i], "Предсказанное - ", predArrGet[i], "Ошибка - ", predArrErr[i])