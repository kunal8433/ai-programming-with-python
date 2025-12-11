
class Employees  :
    language = "python"
    Salary = 1200000
    def __init__(self):
        print("jaat on top")
    def wish(self):
        print("GM")
    def getInfo (self):
        print(f"the language is {self.language}, the salary is {self.Salary}")

kunal = Employees ()
kunal.wish()
kunal.getInfo()