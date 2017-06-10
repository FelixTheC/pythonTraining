#! /usr/env/python3
from statistics import mean
import getpass

class Grading():
    gradingDic = {}
    __admins = {'admin': 'python', 'nimda': 'some'}


    def __init__():
        Grading.readFileToDic()
        Grading.run()
        
    
    def login():
        name = input("Username: ")
        pwd = getpass.getpass("Password: ")
        try:
            if Grading.__admins[name] == pwd:
                return True
            else:
                return False
        except KeyError:
            return False
            
    def exit():
        with open('grading.txt', 'a+') as file:
            for item in Grading.gradingDic:
                file.write(item + '\n')
                for value in Grading.gradingDic[item]:
                    file.write(str(value) + ',')
                file.write('\n')    
        
        
    def readFileToDic():
        with open('grading.txt', 'r+') as file:
            data = file.read()
            temp = data.split()
            for item in range(0, len(temp)-1, 2):
                Grading.gradingDic[temp[item]] = [int(x) for x in temp[item+1].split(',') if x != '']


    def mainMenu():
        goOn = True
        print('\t Welcome to Grade Central \n')
        print(' [1] - Enter Grades')
        print(' [2] - Remove Student')
        print(' [3] - Student Average Grades')   
        print(' [4] - Exit')
        print('\n')
        choice = input('What would you like to do today? (Enter a number) ')
        if int(choice) == 1:
            Grading.enterGrades()
            print('Adding grades ...')
            print(Grading.gradingDic)
            print('\n')
        elif int(choice) == 2:
            Grading.removeStudent()
        elif int(choice) == 3:
            print('The average: ' + str(Grading.showStudentGrades()))
            print('\n')
        elif int(choice) == 4:
            print('Goodbye your changes will automatic be saved in grading.txt')
            Grading.exit()
            goOn = False
        return goOn
                

    def enterGrades():
        name = input('The name of the Student: ')
        grade = input('Grade for %s: ' % (name))
        try:
            if Grading.gradingDic[name]:
                Grading.gradingDic[name].append(grade)
        except:
            Grading.gradingDic[name] = [grade]


    def removeStudent():
        name = input('Which Student you want to remove?? ')
        check = input('Are you sure you want delete %s y/n: ' % (name))
        if check == 'y':
            del Grading.gradingDic[name]


    def showStudentGrades():
        name = input("Which Student's average you want to see?? ")
        average = -1
        try:
            grades = Grading.gradingDic[name]
            average = mean(grades)
        except:
            Grading.exit()
            Grading.readFileToDic()
            grades = Grading.gradingDic[name]
            average = mean(grades)            
        return average


    def run():
        access = Grading.login()
        if access:
            while True:
                if Grading.mainMenu() == False:
                    break
        else:
            print("Access denied")
            
        
if __name__ == '__main__':
    Grading.__init__()