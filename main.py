# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Import Library
import json
import os

#Global Variable
tagKey = 'service'
tagValue = 'production'
ruleCount = 0

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
    print(i["logic"])
    ruleCount += 1

#Test ruleCount
print(ruleCount)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Test Commit