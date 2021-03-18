# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Import Library
import json
import os

#Global Variable
tagKey = 'Name'
tagValue = 'public-1'
tagLogic = "( tags contain [ key='" + tagKey + "' ] and tags contain [ value='" + tagValue + "' ] )"
ruleCount = 0

#Test Print tagLogic
print(tagLogic)

#FileVariable
jsonPath = r'D:\Python\CG-CSPM-TagRuleset\JSON'
OriginalFileName = 'ExampleRule.json'
ExportFileName = 'ExportRule.json'


#Get List of Dictionary -> 1 JSON Object = 1 Dict
with open(jsonPath + '\\' + OriginalFileName) as f:
  data = json.load(f)

#Test Print Whole List of Dict
print(data)

#Test Print Each Dict
print(data[0])
print(data[1])

#Test Print Value in Dict
for i in data:
    print("================================================================================================")
    print(i["logic"])

    #split logic string by should
    logicList = i["logic"].split("should",1)
    print(logicList[0])
    print(logicList[1])
    ruleCount += 1

    # If has where in logic
    if 'where' in i["logic"]:
        print("hasWhere!!!")
        newLogic =  logicList[0] + "and " + tagLogic + " should" + logicList[1]
        print(newLogic)
    # If don't has where in logic
    else:
        print("noWhere!!!")
        newLogic = logicList[0] + "where " + tagLogic + " should" + logicList[1]
        print(newLogic)

#Test ruleCount
print("================================================================================================")
print("Rule Count = " + str(ruleCount))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Test Commit