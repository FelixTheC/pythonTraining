#! /usr/env/python3

class Grading():
    gradingDic = {}
    
    def __init__(self):
        gradingDic = self.readFileToDic
    
    
    def readFileToDic():
        gradingDic = {}
        with open('grading.txt', 'r+') as file:
            data = file.read()
            temp = data.split()
            for item in range(0, len(temp)-1, 2):
                gradingDic[temp[item]] = [int(x) for x in temp[item+1].split(',') if x != '']
        return gradingDic
    
    
    def exit(gradingDic):
        print('Goodbye your changes will automatic be saved in grading.txt')
        with open('grading.txt', 'a+') as file:
            for item in gradingDic:
                file.write(item + '\n')
                for value in gradingDic[item]:
                    file.write(str(value) + ',')
                file.write('\n')
            
    def mainMenu():
        print('\t Welcome to Grade Central \n\n')
        print('[1] - Enter Grades')
        print('[2] - Remove Student')
        print('[3] - Student Average Grades')
        print('[4] - Exit')
        print('\n')
        while True:
            choice = input('What would you like to do today? (Enter a number) ')
            try:
                int(choice)
                break
            except:
                print('Please type in a number')
    
    
    def enterGrades(gradingDic):
        name = input('The name of the Student: ')
        grade = input('Grade for %s' % (name))
        if gradingDic[name]:
            gradingDic[name].append(grade)
        else:
            gradingDic[name] = [grade]
        return self.gradingDic
    
    
    def removeStudent(gradingDic):
        deleted = False
        name = input('Which Student you want to remove?? ')
        check = input('Are you sure you want delete %s y/n: ' % (name))
        if check == 'y':
            del gradingDic[name]
        return deleted
    
    def showStudentGrades(gradingDic):
        name = input('Which Student you want to see?? ')
        grades = gradingDic[name]
        print(grades)