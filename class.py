class Student():
    Name="Avinandan"                                                         #property
    Age=18
X=Student()                                                                   #object creation
print(X.Name,X.Age)
Y=Student()
print(Y.Name,Y.Age)                                                               #object oriented 
Y.Name  
Y.Name='Khanda'
print(Y.Name)                                                             
class Person():
    fname="yoo"
    lname="hoo"
    def get_full_name(self):
        print(self.fname,self.lname)
new=Person()
new.get_full_name()