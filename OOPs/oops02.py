from datetime import datetime, date

class Human():
    def __init__(self, name, gender, dob):
        if gender not in ['M', 'F']:
            raise ValueError("Gender must be 'M' or 'F'")


        self.name = name
        self.dob = dob
        self.gender = gender
        self.age = self.calculate_age() 
    
    
    def calculate_age(self):
        try:
            birth_date = datetime.strptime(self.dob, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("DOB must be in YYYY-MM-DD format")
        
        today = date.today()

        age = today.year - birth_date.year 

        if(today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age
    
    def display(self):
        print(self.name, self.gender, self.age, self.dob)


print("\nHuman Class\n")

name = input("Enter name: ")
gender = input("\nEnter gender(M/F): ").upper()
dob = input("\nEnter DOB(YYYY-MM-DD): ")


try:
    person = Human(name, gender, dob)
    print("")
    person.display()
except ValueError as e:
    print("Error: " , e)




        