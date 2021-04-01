# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import csv


class LoanApprovalSystem():
    professionList = []
    AgeList=[]
    ageDict={}
    def readfile(self):
        with open('H:\\bank-data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    line_count += 1
                    self.professionList.append(row[1])
                    self.AgeList.append(row[0])
            print(f'Processed {line_count} lines.')


    def getuniqueprofset(self):
        myset=set(self.professionList)
        self.professionList=list(myset)
        myset = set(self.AgeList)
        self.AgeList = list(myset)
        return self.professionList

    def  checkprofession(self):
        profession = input("Enter a Profession: ")
        while profession!="END":
            iseligible = False
            for value in self.professionList:
                if profession.lower() == value.lower():
                    iseligible = True
                    break

            if iseligible:
                print("Client is eligible in Profession list")
            else:
                print("Client is not eligible in Profession list")

            profession = input("Enter a Profession: ")




    def computeMinMaxAge(self):
        min_age=min(self.AgeList)
        print("minimun age in the list :", min_age)
        self.ageDict["minAge"]=min_age
        max_age = max(self.AgeList)
        print("minimun age in the list :", max_age)
        self.ageDict["maxAge"] = max_age




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    professionList=[]
    loanapprovalSystem = LoanApprovalSystem()
    loanapprovalSystem.readfile()
    professionList=loanapprovalSystem.getuniqueprofset()
    for value in professionList:
        print(value)
    loanapprovalSystem.checkprofession()
    loanapprovalSystem.computeMinMaxAge()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
