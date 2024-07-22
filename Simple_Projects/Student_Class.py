class Student :
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.id = 0
        self.grade = 0

    def student_name(self):
        self.name = str(input("What's Your Name : "))
        return self.name 

    def lastname(self):
        self.last_name = str(input("What's Your Last Name : "))
        return self.last_name

    def id_number(self):
        self.id = int(input("Enter Your Student Id Number : "))
        return self.id

    def student_grade(self):
        self.grade = int(input("Enter Your Grade Point Average : "))
        print("------------------------------------------------------------")
        return self.grade

    def classification(self,l):
        self.dict_group = {"A" : 0 , "B" : 0 , "C" : 0 , "D" : 0}
        self.lst = l
        for k in range(len(self.lst)) :
           if 18 < self.lst[k] <= 20 :
               self.dict_group["A"] = self.dict_group.get("A")+1
           elif 15 < self.lst[k] <= 18 :
               self.dict_group["B"] = self.dict_group.get("B")+1 
           elif 12 < self.lst[k] <= 15 :
               self.dict_group["C"] = self.dict_group.get("C")+1  
           elif 10 < self.lst[k] <= 12 :
               self.dict_group["D"] = self.dict_group.get("D")+1
        for k,v in self.dict_group.items():
                    print("Number Of Student In Group",k , ":" , v)
    def show(self,d):
        self.dic = d
        self.tmp = 0
        print(" |--------------------------------------------------------|")
        print(f" |             Recorded Students Specifications           |")
        print(" |--------------------------------------------------------|")
        for key,value in self.dic.items() :
            print(  key , ":" , value)
            self.tmp += 1
            if self.tmp == 4 :
                print("------------------------------------------------------------")
                self.tmp = 0  

#---------------------------------------------- The End Of Class Defintion --------------------------------------------------

di = dict()
ls = []
ob = Student()
for i in range(2) :
    Student_name = ob.student_name()
    last_name = ob.lastname()
    Student_id = ob.id_number()
    grade = ob.student_grade()
    di.update({f"{i+1} ) Student_Name" : Student_name , f"{i+1} ) Student_Last_Name" : last_name , f"{i+1} ) Student_Id" : Student_id , f"{i+1} ) Student_Grade" : grade})
    ls.append(grade)
    # {i+1} , it show that this information is for multiple students

ob.show(di)
ob.classification(ls)
