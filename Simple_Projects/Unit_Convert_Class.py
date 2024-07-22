from time import sleep
class convert :
    def sqm_to_hec_and_rev(self) :
        self.entered_number = float(input("Enter A Number : "))
        self.calculate = self.entered_number * 10000
        self.rcalculate = self.entered_number / 10000
        print(f"The Result Of Convert Sequare Meteres To Hectares : {self.rcalculate} Hec")
        print(f"The Result Of Convert Hectares To Sequare Meteres  : {self.calculate} Sm")

    def inch_to_centi_and_rev(self) :
        self.entered_number = float(input("Enter A Number : "))
        self.calculate = self.entered_number * 2.54
        self.rcalculate = self.entered_number / 2.54
        print(f"The Result Of Convert Inches To Centimeters : {self.calculate} Cm")
        print(f"The Result Of Convert Centimeters To Inches : {self.rcalculate} In")
    
    def feet_to_meters_and_rev(self) :
        self.entered_number = float(input("Enter A Number : "))
        self.calculate = self.entered_number * 0.3048
        self.rcalculate = self.entered_number / 0.3048
        print(f"The Result Of Convert Feet To Meters : {self.calculate} M")
        print(f"The Result Of Convert Meters To Feet : {self.rcalculate} Ft")

    def lit_to_gallons_and_rev(self) :
        self.entered_number = float(input("Enter A Number : "))
        self.calculate = self.entered_number * 0.26
        self.rcalculate = self.entered_number / 0.26
        print(f"The Result Of Convert Liters To Gallons : {self.calculate} Ga")
        print(f"The Result Of Convert Gallons To Liters : {self.rcalculate} Li")

    
#---------------------------------------------- The End Of Class Defintion --------------------------------------------------

ob = convert()
while True :
    question_text = """
Which Operation Do You Want To Do ?
    1) Sequare Meteres To Hectares & rev.
    2) Inches To Centimeters & rev.
    3) Feet To Meters & rev.
    4) Liters To Gallons & rev.
    5) Exit
    """

    print(question_text)
    selected_operation = int(input("Enter The Opertion Number : "))
    if selected_operation == 1 :
        ob.sqm_to_hec_and_rev()
        sleep(3)
    elif selected_operation == 2 :
        ob.inch_to_centi_and_rev()
        sleep(3)
    elif selected_operation == 3 :
        ob.feet_to_meters_and_rev()
        sleep(3)
    elif selected_operation == 4 :
        ob.lit_to_gallons_and_rev()
        sleep(3)
    elif selected_operation == 5 :
        print("The End Of Operation")
        sleep(3)
        break
    else : 
        print("!!! Invalid The Operation Number , Please Enter Currect Nummber !!!")
        sleep(5)
