import cmd
import os
import gradeClass as gc


# Todo:
# Reformat the list command to print more similar to the ls command in terminal

class gradeCalculator(cmd.Cmd):
    """Main Shell of Python code"""
    gcFile = 'gradesData.pickle'
    data = gc.Data(gcFile)          # Create Data Object
    userInput = gc.userInput()      # Create User Input Object
    prompt = '(Cmd) $ '             # Setting the initial prompt
    # Initializing the initial varibale to determine the selection.
    Selection = {'Semester':[None,None],
                'Course':[None,None],
                'Section':[None,None],
                'Assigment':[None,None]}
    currentSelection = None         # Selection

    def __init__(self):
        cmd.Cmd.__init__(self)

    def do_ls(self,line):
        pass
        if line.lower() == 'courses':
            for key in self.data.semesters.keys():
                pass
        # Re - write
        if self.currentSelection == None:
            self.printHeader()
            print('Semesters')
            print('\t'.join(list(self.data.semesters.keys())))
        else:
            self.printHeader()
            argsIndex = list(self.Selection.keys()).index(self.currentSelection)+1  # Gets the index of the name of the list
            print(''.join([list(self.Selection.keys())[argsIndex],'s']))            # Prints the name of the list being printed
            if self.Selection[self.currentSelection][1] == None:
                print('None')
            else:
                if len(self.Selection[self.currentSelection][1]) > 0:
                    print('\t'.join(list(self.Selection[self.currentSelection][1].keys()))) 

    def do_rename(self,line):
        # line format = (Cmd) $ rename newName oldName
        if line.__len__() == 1:
            # If the length of line is 1, then the user only specified a newName
            newName = line
            # oldName is the name of the previous selection

        #   If oldName is not specified, rename the current section to the new name
        #   
        
        pass 
    
    def do_select(self,line):
        # If no input was entered reset the selection
        # If ./ was entered, keep the first selections else, reset the selection

        # Protection needs to be enable to ensure that the user is entering the correct names into the system.
        # 
        if line == '':
            self.Selection = {'Semester':[None,None],
                'Course':[None,None],
                'Section':[None,None],
                'Assigment':[None,None]}
            self.currentSelection = None

        # Finnaly print a string detailing the current selections
        args = line.lower().split(' ')
        kargs = []
        # If the ./ command is given
        if args[0] == './':
            args.remove('./')
            for key in self.Selection.keys():
                if self.Selection[key][0] != None:
                    kargs.append(self.Selection[key][0].name)
            for string in args:
                kargs.append(string)
            args = kargs     
        # Setting the Current Semester
        if not args[0] in self.data.semesters:     
            # Creating a new semester if the enter             
            self.data.semesters[args[0]] = gc.Semester(args[0])     
        self.Selection['Semester'][0] = self.data.semesters[args[0]]
        self.Selection['Semester'][1] = self.Selection['Semester'][0].courses
        self.currentSelection = 'Semester'      
        # Setting the Current Course               
        if len(args) > 1:
            if not args[1] in self.Selection['Semester'][0].courses:
                self.Selection['Semester'].courses[args[1]] = gc.Course(args[1])
            self.Selection['Course'][0] = self.Selection['Semester'][0].courses[args[1]]
            self.Selection['Course'][1] = self.Selection['Course'][0].sections
            self.currentSelection = 'Course'
        # Setting the Current Section
        if len(args) > 2:
            if not args[2] is self.Selection['Course'][0].sections:
                self.Selection['Course'][0].sections[args[2]] = gc.Section(args[2])
            self.Selection['Section'][0] = self.Selection['Course'][0].sections[args[2]]
            self.Selection['Section'][0] = self.Selection['Section'][0].assignments
            self.currentSelection = 'Section'
        # Setting the Current Assignment
        if len(args) > 3:
            if not args[3] is self.Selection['Section'][0].assignments:
                self.Selection['Section'][0].assignments[args[3]] = gc.Assignment(args[3])
            self.Selection['Assignment'][0] = self.Selection['Section'][0].assignments[args[3]]
            self.Selection['Assignment'][1] = self.Selection['Assignment'][0].grade
            self.currentSelection = 'Assignment'
        # Displaying the current selection to the user Write a new function for this


    def do_quit(self, line):
        """Quits the Program"""
        # self.data.write()
        return True

    # Class Functions


    def findSelection(self)->list:
        pass
    # Prints header
    def printHeader(self):
        print('========================================')



def main():
    gradeCalculator().cmdloop()

if __name__ == '__main__':
    main()