class Students:
    def __init__(self):
        self.course = ""
        self.group = ""
        self.firstName = ""
        self.secondName = ""
        self.middleName = ""
        self.certName = ""
        self.certDate = ""
        self.curDate = ""
    def addInfo(self, course, group, firstName, secondName, middleName, certName, certDate, curDate):
        self.course = course
        self.group = group
        self.firstName = firstName
        self.secondName = secondName
        self.middleName = middleName
        self.certName = certName
        self.certDate = certDate
        self.curDate = curDate
    def getCourse(self):
        return self.course
    def getGroup(self):
        return self.group
    def getFirst(self):
        return self.firstName
    def getSecond(self):
        return self.secondName
    def getMiddle(self):
        return self.middleName
    def getCertName(self):
        return self.certName
    def getCertDate(self):
        return self.certDate
    def getCurDate(self):
        return self.curDate
    def debug(self):
        print(self.course, self.group, self.firstName, self.secondName, self.middleName, self.certName, self.certDate, self.curDate)