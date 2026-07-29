class TeamMember():
    """docstring for TeamMember"""
    def __init__(self, name,uid):
        self.name = name
        self.uid = uid

class Employee():
    """docstring for Employee"""
    def __init__(self, paid,jobtitle):
        self.paid = paid
        self.jobtitle = jobtitle

class Programmer(TeamMember, Employee):
    def __init__(self, name, uid, paid, jobtitle, prLanguage, workExp):
        self.workExp = workExp
        self.prLanguage = prLanguage
        TeamMember.__init__(self, name, uid)
        Employee.__init__(self, paid, jobtitle)

    def showInfo(self):
        print(f'''''Programmer Information--> name: {self.name} | uid: {self.uid} | paid: {self.paid} | jobTitle: {self.jobtitle} | programming language: {self.prLanguage} | work experience: {self.workExp}''')

Programmer1 = Programmer('Mobin', '12035', '1500000', 'Programmer', 'Python', '5')
Programmer1.showInfo()

Programmer2 = Programmer('Fariborz', '12135', '50000', 'Programmer', 'Python', '14')
Programmer2.showInfo()

