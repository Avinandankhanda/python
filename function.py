def washing_machine(company):
    print('turn on',company)
    print('washing is under process')
    print('please collect the clothes')
washing_machine('whirlpool')
washing_machine('lg')
washing_machine('janina')
def air_conditionar(company):
    print('turn on',company)
    print('mentain your suitable temperature')
    print('increase fan speed')
    print('turn off')
air_conditionar("daikin")
air_conditionar('voltas')
air_conditionar('whirlpool')


def age_calculator():
    yob=input('enter your dob')
    yob=int(yob)
    curren_year=2019
    current_age=curren_year-yob
    print(current_age)
age_calculator()