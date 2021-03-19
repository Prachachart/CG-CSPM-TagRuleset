# CG-CSPM-TagRuleset
# Author : Prachachart Stapornnanon
# Contact : prachas@checkpoint.com


#Import Library
import json


#Declare Variable
#Platform Selectiom 1.AWS 2.Azure 3.GCP
platform = 1

#Global Variable
tagKey = 'Name'
tagValue = 'public-1'

#Setting String to add to GSL depend on platform
if platform == 1:
    tagLogic = "( tags contain [ key='" + tagKey + "' ] and tags contain [ value='" + tagValue + "' ] )"
elif platform == 2:
    tagLogic = "( tags contain [ key='" + tagKey + "' ] and tags contain [ value='" + tagValue + "' ] )"
else:
    tagLogic = "( labels contain [ key='" + tagKey + "' ] and labels contain [ value='" + tagValue + "' ] )"

ruleCount = 0

#Test Print tagLogic
print(tagLogic)

#Path&File_Variable
jsonPath = r'D:\Python\CG-CSPM-TagRuleset\JSON'
OriginalFileName = 'AWS_CG_BestPractice.json'
OriginalFileNameList = OriginalFileName.split(".",1)

ExportFileName = OriginalFileNameList[0] + "_Tag_" + tagValue + "." + OriginalFileNameList[1]
print(ExportFileName)

print(jsonPath + '\\' + OriginalFileName)

#Get List of Dictionary -> 1 JSON Object = 1 Dict
with open(jsonPath + '\\' + OriginalFileName,encoding="utf8") as f:
  data = json.load(f)

#Test Print Whole List of Dict
#print(data)

#Test Print Each Dict
#print(data[0])
#print(data[1])

NewData = data

#Test Print Value in Dict
for i in data:
    #print("================================================================================================")
    #print(i["logic"])

    #split logic string by should
    logicList = i["logic"].split("should",1)

    # If has where in logic
    if 'where' in i["logic"]:
        #print("hasWhere!!!")
        newLogic =  logicList[0] + "and " + tagLogic + " should" + logicList[1]
        #print(newLogic)
    # If don't has where in logic
    else:
        #print("noWhere!!!")
        newLogic = logicList[0] + "where " + tagLogic + " should" + logicList[1]
        #print(newLogic)

    #add newLogic to new Data
    NewData[ruleCount]["logic"] = newLogic
    ruleCount += 1

#Test ruleCount
print("================================================================================================")
print("Rule Count = " + str(ruleCount))
print("==========================================Done==================================================")


with open(jsonPath + '\\' + ExportFileName, 'w', encoding='utf-8') as output:
    json.dump(NewData, output, ensure_ascii=False, indent=4)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# Test Commit