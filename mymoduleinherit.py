import Classobj as cl

class demo(cl.employee):
    
    def __init__(self):
        super().__init__()
        print("Inherited successfully")



d = demo()
d.exit()
d.run()
        

