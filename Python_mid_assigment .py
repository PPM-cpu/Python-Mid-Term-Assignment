class StudentDatabase:
    Student_list=[]
    @classmethod
    
    def add_student(claass,student):
        claass.Student_list.append(student)
        
class student:
    def __init__(self,student_id,name,department,is_enrolled=False):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=is_enrolled
        
        StudentDatabase.add_student(self)
        
    def get_student_id(self):
        return self.__student_id
    
    def enroll_student(self):
        if self.__is_enrolled:
            print("Student",self.__student_id,"is already enrolled.")
        else:
            self.__is_enrolled=True
            print("Student",self.__student_id,"has been enrolled.")
            
    def drop_student(self):
        if self.__is_enrolled==False:
            print("Student",self.__student_id,"is already dropped.")
        else:
            self.__is_enrolled=False
            print("Student",self.__student_id,"has been dropped.")
    
    def view_student_info(self):
        print(
             "ID:",self.__student_id,
             ", Name:",self.__name, 
             ", Department:",self.__department,
              ", Enrolled:",self.__is_enrolled 
        )
        
s1=student("001","Luffy","Food Engineering",True)
s2=student("002","Zoro","Software engineering",True)
s3=student("003","Robin","Archaeology",False)

while True:
    print("\n---Student Management Menu---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student") 
    print("4. Exit")
    
    choose =input("Enter your choice(1-4): ")
    
    if choose=='1':
        for student in StudentDatabase.Student_list:
            student.view_student_info()
            
    elif choose=="2":
        data=input("Enter Student ID to enroll:")
        
        get=False
        
        for student in StudentDatabase.Student_list:
            
            if student.get_student_id()==data:
                student.enroll_student()
                get=True
                break
            
        if get==False:
                print("Invalid Student ID.")
                
    elif choose=='3':
        data=input("Enter Student ID to drop: ")
        get=False
        
        for student in StudentDatabase.Student_list:
            if student.get_student_id()==data:
                student.drop_student()
                get=True
                break
        
        if get==False:
            print("Invalid Student ID. ")
            
    elif choose=='4':
        print("Program Ended. ")   
        break
    else:
        print("Invalid Choice. ")             