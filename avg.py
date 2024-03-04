class Student:
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.average = self.avg()

    def avg(self):
        print(int(self.sub1 + self.sub2 + self.sub3)/3)


Student(1,2,3)



