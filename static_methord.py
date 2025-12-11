class Employees  :
    language = "python"
    Salary = 1200000
    @staticmethod
    def wish():
        print("GM")
    def getInfo (self):
        print(f"the language is {self.language}, the salary is {self.Salary}")

kunal = Employees ()
kunal.wish()
kunal.getInfo()