class programmer:
    company = "Microsoft"
    Salary = 1000000
    def __init__(self, name, language, company , salary):
        self.name = name
        self.language = language
        self.company = company
        self.salary = salary
kunal = programmer("kunal", "python", "Microsoft", 1000000)
print(kunal.name,   kunal.language, kunal.company, kunal.salary)
rahul = programmer("rahul", "java", "Google", 2000000)
print(rahul.name, rahul.language, rahul.company, rahul.salary)