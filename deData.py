from dataReader import DataReader as DR
pattern=''.center(20,'*')
print('Welcome to the muj Department electives 2021 visualizer.\n')
print(pattern+'\n\n')
choice=True
dataReader=None
while(choice):
    print('Select one of the options below\n')
    print(pattern+'\n\n')
    print('1>Visualize the class wise department elective chosen\n2>Number of students in each section of each department\n3>Exit the programme\n\n')
    optionSelected=int(input('Your choice : '))
    if optionSelected==3:
        break
    elif optionSelected>3 or optionSelected<1:
        print('Invalid option selected . Please enter again\n\n')
    else:
        if not dataReader:
            dataReader=DR()
            dataReader.readExcelFile('deData')
        if optionSelected==1:
            dataReader.plotGraphForDe()
        elif optionSelected==2:
            dataReader.plotGraphForStudents()
        else:
            print('Invalid Credential Entered\n\n')

        
        
        
