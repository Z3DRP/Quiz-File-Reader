#command line control file for TriviaQuiz

import os #from chapter 14 of school text
from Quiz import Quiz

def main():
    fileName = getFile() #method to navigate and select file from file system
    while fileName != "":
        q = Quiz(fileName)
        if q.getErrorMsg() != "":
            print(f"Quiz File Error: {q.getErrorMsg()}")
        else:
            doQuiz(q)
        fileName = getFile()


def doQuiz(q):
    print(f"Quiz opened: it has {q.getQcount()} questions")
    qinProgress = True
    while qinProgress:
        qn = str(input(f"Press <enter> for question  {q.getQnumber()} or enter specific question number ('Q' for quit :) ")).upper()
        if len(qn) > 0 and qn[0] == "Q":
            qinProgress = False
            needAnwser = False
        elif qn == "":
            qtuple = q.getQuestion()
            print(qtuple[0])        #reponse from qustion (question or error msg)
            needAnwser = qtuple[1] #boolean indicating anwser needed Y/N
        else:
            #python version of 'overloaded methods': same method different # paramenters
            qtuple = q.getQuestion(qn)
            print(qtuple[0])
            needAnwser = qtuple[1]

        if qinProgress == True and needAnwser == True:
            input("Press <enter> for the anwser: ")
            print(q.getAnswer())
            if q.isOver() and qn == "":
                print("That was the last anwser!")
                qinProgress = False


def getFile():
    choice = ""
    while choice != "Q" and choice != "S":
        #loop runs until user says quit or select
        cwd = os.getcwd() #get current working directory (as strings)
        print(f"Current Directory: {cwd}")
        choice = str(input("Action: show all <F>iles, <T>ext files, <D>irectories, <C>hange directories, <S>elect file or <Q>uit: ")).upper()
        if choice == "C":
            dirName = str(input("<..> for parent or new dirctory name: "))
            if dirName != "":
                try:
                    os.chdir(dirName)  #does process .. as 'move up one level'
                except Exception as e:
                    print(f"CD:Error: {e}")
            else:
                print("No directory entered.")
        elif choice == "F" or choice == "T" or choice == "D":
             for entry in os.listdir(cwd): #foreach style
                 #entry does not have full path info..
                fullpath = os.path.join(cwd,entry) #recreates fullpath for directory entry
                if choice == "D" and os.path.isdir(fullpath):
                     print(f"D: {entry}")
                elif choice == "F" and os.path.isfile(fullpath):
                    print(f"F: {entry}")
                elif choice == "T" and os.path.isfile(fullpath) and entry.endswith(".txt"):
                    print(f"T: {entry}")
        elif choice == "S":
            fileName = str(input("Enter file name (with extension): "))
            #verify that input is  a file...
            fullpath = os.path.join(cwd,fileName)
            if not os.path.isfile(fullpath):
                print("Entered name is not a file.")
                choice = ""
                
    #after while loop is over via 'Q' or 'S'
    if choice == "Q":
        return ""
    return fullpath #only returned if 's' option yielded a file entry




if __name__ == "__main__":
    main()

    
