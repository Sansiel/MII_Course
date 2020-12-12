# Сцепление с дорогой – ({Среднее, трапеция, 50 50 70 85}, {Высокое, трапеция, 75, 100, 100, 100})
# Скорость – ({Низкая, трапеция, 0 30 60 70}, {Среднее, треугольник, 60 90 115}, {Высокая, трапеция, 110, 150, 200, 200})
# Угол поворота в заносе без потери управления – ({Малый, трапеция, 0 0 30 45}, {Средний, треугольник, 40 70 90}, {Высокий, трапеция, 80, 110, 180, 180})

arrGrip = {"Medium":[0,50,70,80],"High":[81,90,90,100]}
arrSpeed = {"Low":[0,30,60,66], "Medium":[67,90,90,112],"High":[113,150,180,200]}
arrAngle = {"Low":[0,10,30,43], "Medium":[44,70,70,86],"High":[87,110,150,180]}

ruleVase=[
    ["Medium","Low","Medium"],
    ["Medium","Medium","High"],
    ["Medium","High","High"],
    ["High","Low","Low"],
    ["High","Medium","Medium"],
    ["High","High","Medium"],
    ]

testObject = [70, 200] #Grip = 70, Speed = 200
testFuzzyObject=[]
count=-1
for key in arrGrip:
    if testObject[0] in range(arrGrip[key][0],arrGrip[key][3]+1):
        if testObject[0] in range(arrGrip[key][2]+1,arrGrip[key][3]+1): testFuzzyObject.append(key+","+str((testObject[0]-arrGrip[key][2])/(arrGrip[key][3]-arrGrip[key][2])))
        if testObject[0] in range(arrGrip[key][1],arrGrip[key][2]+1): testFuzzyObject.append(key+",1.0")
        if testObject[0] in range(arrGrip[key][0],arrGrip[key][1]): testFuzzyObject.append(key+","+str((testObject[0]-arrGrip[key][0])/(arrGrip[key][1]-arrGrip[key][0])))
for key in arrSpeed:
    # if testObject[1] in range(arrSpeed[key][0],arrSpeed[key][3]+1): testFuzzyObject.append(key)
    if testObject[1] in range(arrSpeed[key][0],arrSpeed[key][3]+1):
        if testObject[1] in range(arrSpeed[key][2]+1,arrSpeed[key][3]+1): testFuzzyObject.append(key+","+str((testObject[1]-arrSpeed[key][2])/(arrSpeed[key][3]-arrSpeed[key][2])))
        if testObject[1] in range(arrSpeed[key][1],arrSpeed[key][2]+1): testFuzzyObject.append(key+",1.0")
        if testObject[1] in range(arrSpeed[key][0],arrSpeed[key][1]): testFuzzyObject.append(key+","+str((testObject[1]-arrSpeed[key][0])/(arrSpeed[key][1]-arrSpeed[key][0])))
# print(testFuzzyObject)

testRuleVase=[]
for line in ruleVase:
    a=[]

    if testFuzzyObject[0].split(",")[0] == line[0]: a.append(float(testFuzzyObject[0].split(",")[1]))
    else: a.append(0.0)
    if testFuzzyObject[1].split(",")[0] == line[1]: a.append(float(testFuzzyObject[1].split(",")[1]))
    else: a.append(0.0)
    if a[0]==1 and a[1]==1:
        a.append(1.0)
        a.append(1.0)
    else:
        a.append(min(a[0],a[1]))
        a.append(min(1-a[0],a[1]))

    testRuleVase.append(a)

countLine=0
controlNum=0
controlLine=-1
for line in testRuleVase: 
    # print(line)
    countLine+=1   
    count=0
    for i in line:
        if i==0.0:
            # print(line)
            # print("\n")
            break
        count+=1
    # print(count)
    if count==4:
        # print("ok")
        if controlNum<max(line[2],line[3]): 
            controlNum=max(line[2],line[3])
            controlLine=countLine

controlLine-=1 
if controlLine==-1 and controlLine==-2: print("No variants")
else:
    print("Результат агрегации - ", controlNum)
    print("Нечёткое значение угла поворота - ", ruleVase[controlLine][2])

    #[87,110,150,180]
    if controlNum<1: ans = "около "+str((arrAngle[ruleVase[controlLine][2]][1]-arrAngle[ruleVase[controlLine][2]][0])*controlNum+arrAngle[ruleVase[controlLine][2]][0]) + " или около "+str((arrAngle[ruleVase[controlLine][2]][3]-arrAngle[ruleVase[controlLine][2]][2])*controlNum+arrAngle[ruleVase[controlLine][2]][2])
    else: 
        if ruleVase[controlLine][2] == "High": ans = "в промежутке ["+str(arrAngle[ruleVase[controlLine][2]][1]) + ", " + str(arrAngle[ruleVase[controlLine][2]][3]) + "]."
        if ruleVase[controlLine][2] == "Medium": ans = "в промежутке ["+str(arrAngle[ruleVase[controlLine][2]][1]) + ", " + str(arrAngle[ruleVase[controlLine][2]][2]) + "]." #Впрочем, если это предельное значение, то до предела доходит и промежуток
        if ruleVase[controlLine][2] == "Low": ans = "в промежутке ["+str(arrAngle[ruleVase[controlLine][2]][0]) + ", " + str(arrAngle[ruleVase[controlLine][2]][2]) + "]."
    

    print("Значение угла поворота - ", ans)