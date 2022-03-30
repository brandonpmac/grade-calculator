import os
import string
import dill.settings
dill.settings['recurse'] = True

def main():
    # filePath = 'gradesData.pickle'
    
    # data = Data(filePath)
    # name = "data"
    # semester = '2221'
    # course = 'mae306'
    # section = 'Labs'
    # data.semesters[semester] = Semester(semester)
    # data.semesters['2218'] = Semester('2218')
    # data.semesters['2218'].name = 'Sophmore_Spring'
    # data.semesters[semester].courses[course] = (Course(course))

    # dill.dump_session('gradesDataDump.pkl')
    # data.write()
    pass
    
    

class Data:
    name = ''
    semesters = dict()
    filePath = ''
    def __init__(self,filePath):
        self.filePath = filePath
        
        def readData(filePath):
            if os.path.exists(filePath):
                with open(filePath,'rb') as f:      # Reads the pickle
                    return dill.load(f)
            else:
                return dict()


        self.semesters = readData(filePath)         # Saves the data to the semesters 

    def write(self):
        with open(self.filePath,'wb') as f:
            dill.dump(self.semesters,f)             # Dumps the pickle

    def ls(self,userInput):
        pass

    def getSemesters(self) -> list:                 # Returns list of all semesters
        return list(self.semesters.keys())

    def getCourses(self) -> dict:
        semList = self.getSemesters()
        courseList = {}
        for key in semList:
            currentSemester = self.semesters[key]
            courseList[key] = list(currentSemester.courses.keys())
        return courseList

    def getSections(self):
        pass

    def getAssignments(self):
        pass


class Semester:
    name = ''
    courses = {}
    startDate = ''
    endDate = ''
    def __init__(self,name):
        self.name = name

class Course:
    name = ''
    semester = ''
    sections = {}
    def __init__(self,name):
        self.name = name

class Section:
    name = ''
    weight = ''
    assignments = {}
    def __init__(self,name):
        self.name = name

class Assignment:
    name = ''
    grade = ''
    dueDate = ''
    def __init__(self,name):
        self.name = name

class userInput:
    string = ''
    def __init__(self):
        self.string = '' 

if __name__ == "__main__":
    main()
