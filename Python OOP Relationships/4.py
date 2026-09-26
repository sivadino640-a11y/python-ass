class employee:
    def show(self):
        print("I am an employee")
class manager(employee):
    def manage(self):
        print("I am a manager")
m = manager()
m.show()
m.manage()