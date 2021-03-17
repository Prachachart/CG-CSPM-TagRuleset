# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Import Library
import json
import os

#Global Variable
tagKey = 'service'
tagValue = 'production'

#FileVariable
jsonPath = r'D:\Python\CG-CSPM-TagRuleset\JSON'
OriginalFileName = 'ExampleRule.json'
ExportFileName = 'ExportRule.json'

with open(jsonPath + '\\' + OriginalFileName) as f:
  data = json.load(f)

print(data)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Test Commit