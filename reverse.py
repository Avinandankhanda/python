# name="level madam kayak radar rotor"
name = "JHARGRAM"
reverse_name=""
reverse_name_list = []
for b in name:
    reverse_name = b + reverse_name

for b in name:
    reverse_name_list.insert(0, b)

print(reverse_name)
print(''.join(reverse_name_list))