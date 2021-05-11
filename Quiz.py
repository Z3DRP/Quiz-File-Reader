#Quiz Class for TriviaQuiz by Zach Palmer

import os

class Quiz:
    def __init__(self,path):
        self.setFile(path)
        self._Error = ""
        #keeps seperate lists for questions vs answers
        self._Questions = []
        self._Answers = []
        self._Qcount = 0
        self._Qnumber = 0 #next question to be given
        self._over = False
        #open and read file represented by 'path'
        try:
            file = open(path,"r") #open file in "r" read only mode
            EOF = False #end of file
            while EOF == False:
                ques = file.readline() #read full line up to newline
                if ques != "":
                    #question was read  - assume answer is presnt
                    self._Questions.append(ques)
                    self._Answers.append(file.readline()) # if missing, returns "" so wont crash
                    self._Qcount += 1
                else:
                    EOF = True
            file.close()
        except OSError as e:
            self._Error = f"Quiz file error: {e}"
        if self._Error == "" and self._Qcount > 0:
            self._over = False
            self._Qnumber = 1
        else:
            self._over = True
            self._Qnumber = 0

    def setFile(self,path):
        self._Path = path
    def getFile(self):
        return self._Path

    def getErrorMsg(self):
        return self._Error

    def getQcount(self):
        return self._Qcount

    def getQnumber(self):
        return self._Qnumber

    def getQuestion(self, ques = None):
        #overloaded: ques either has a value if sent
        #or will be given the value "None" if not sent
        
        #question method doesnt worry about end of quiz issue
        if ques == None:
            #give them next question in line - if quiz is not over
            if self._over == True:
                response = f"No more questions: # {self._Qcount} was last one"
                #return is the response plus boolean
                #that indicates whether or not an answer comes next
                return (response,False)
            else:
                response = self._Questions[self._Qnumber-1]
                return (response,True)
        else:
            #seem to be asking for specific question #(in ques variable)
            try:
                qn = int(ques) #is requested value actually an integer?
            except ValueError:
                response = "Question requested was not an iteger"
                return (response,False)
            if qn < 1:
                return("Questions start at 1, please",False)
            elif qn > self._Qcount:
                response = f"Requested question out of bounds : There {self._Qcount} questions"
                return(response, False)
            else:
                response = self._Questions[qn-1]
                self._Qnumber = qn
                self._over = False
                return (response,True)
            
    def getAnswer(self):
        #end of quiz logic goes here
        #anser method only returns string (not tuple)
        if self._over == True:
            return "Quiz already over: no answer to return."
        a = self._Answers[self._Qnumber -1] #answer to current question
        if self._Qnumber + 1 <= self._Qcount:
            self._Qnumber += 1
        else:
            self._over = True
        return a

    def isOver(self):
        return self._over

    
            
        
            
    
