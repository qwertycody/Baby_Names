import os

nameList = {"Elliot":0,
"Elijah":0,
"Mason":0}


for name1 in nameList:
  for name2 in nameList:
    if(name1 != name2):
      os.system('clear')
      print("Not Hudson - Choose which name you like better:")
      print("[1] " + name1)
      print("[2] " + name2)
      selection = input() 

      if(selection == "1"):
        currentValue = nameList[name1]
        currentValue = currentValue + 1
        nameList[name1] = currentValue

      if(selection == "2"):
        currentValue = nameList[name2]
        currentValue = currentValue + 1
        nameList[name2] = currentValue

for name in nameList:
  score = nameList[name]
  f = open("score.csv", "a")
  f.write(name + "," + str(score) + "\n")
  f.close()


