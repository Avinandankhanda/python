class Cricketer():
    def __init__(self,team,name):
        self.team=team
        self.name=name
aa=Cricketer("india",'m.s')
ab=Cricketer('bangladesh','r.s')
ac=Cricketer('england','s.s')
print(aa.team)
print(aa.name)
print(ab.name)
print(ab.team)
print(ac.team)
print(ac.name)
class Batsman(Cricketer):
    pass
ad=Batsman('rd radha','amazon')
acc=Batsman('md pagol','lodha')
print(ad.name)
print(ad.team)
print(acc.name)
print(acc.team)
o