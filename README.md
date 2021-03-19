# CG-CSPM-TagRuleset
Python code to edit JSON Ruleset File to add specific Tag to each rule in ruleset


Project Start 17/03/2021

Version : 0.1  -  Release 19/03/2021

Author : Prachachart Stapornnanon

Contact : prachas@checkpoint.com

Prerequisite
-
- Python (I use at version 3.8.6)

Procedure
-
- Revise variable in code in "Declare Variable" Section
- Parameter that you need to set list below
    
    - Platform  #Platform Selection 1.AWS 2.Azure 3.GCP
    - tagKey -> Tag Key Name
    - tagValue -> Tag Value
    - jsonPath -> Directory that JSON file located
    - OriginalFileName -> JSON File name

Output
-
- You will get revise JSON file in same directory that host original JSON file
- You can copy this JSON to Ruleset in Cloudguard CSPM

Roadmap
-
- Support Replace TAG Parameter
- Support input Parameter (Maybe via CLI or GUI)
- Browse JSON File from Directory 
- GSL Logic Bug Fixed

Remark
-
As this code is develop by myself with hope that can help anyone to use Cloudguard CSPM easier.

By the way this project is work as best effort basis - so please bear with any bug occurred and please recheck and verify result by yourselves.

Hope this help.