nlist= [1,2,3,4,5,6,7,8,9,10]
for a in nlist:
    print(a)
nlist.insert(0,0)
print(nlist)
text="hello,World"
text_list=list(text)                                      #list is a function           Use to convert a string into a list
print(text_list)
text_split=text.split(",")                                #split is a function           use to divide a string into a list
print(text_split)
my_email='avinandankhanda2001@gmail.com'
email_provider=my_email.split("@")
print(email_provider)

text_string=" ".join(text_list)                           #join is a function         use to merge the elaments of list into a string 
print(text_string)