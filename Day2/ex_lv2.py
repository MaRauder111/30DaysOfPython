import ex_lv1

first_name = ex_lv1.first_name
last_name = ex_lv1.last_name

print(type(first_name))

print(len(first_name))

len_first = len(first_name)
len_last = len(last_name)

if(len_first == last_name):
    print("Same length")
else:
    print("Not same")

num_one = 5
num_two = 4

print(num_one + num_two)
print(num_one - num_two)
print(num_one*num_two)
print(num_one/num_two)
remainder = num_one%num_two
print(remainder)
print((num_one)**num_two)

floor_division = num_one // num_two
print(floor_division)

rad = 30
area_of_circle = 3.14*(rad**2)
print(area_of_circle)

circum_of_circle = 2 * 3.14 * rad
print(circum_of_circle)

rad_input = int(input("Enter the rad "))


area_of_circle = 3.14*(rad_input**2)
print(area_of_circle)

circum_of_circle = 2 * 3.14 * rad_input
print(circum_of_circle)

first_name_input = input("Enter the first name ")
last_name_input = input("Enter the last name ")
country_input = input("Enter the country name ")

print(first_name_input, last_name_input, country_input)

help("keywords")