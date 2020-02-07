class classex:
    empcnt=0
    def __init__(self,ename,sal):
        self.ename = ename
        self.sal = sal
        classex.empcnt += 1


    def display(self):
        print("name:",self.ename,"salary:")

class manager(classex):
            def __init__(self,n,s):
                classex.init(self,n,s)

            employee1=classex("alek",1000)
            employee2=classex("sru",2000)
            employee2=classex("mohi",3000)
            employee2=classex("char",4000)
            employee1.display()
            print("total employees",classex.empcnt)