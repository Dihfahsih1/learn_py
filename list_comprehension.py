

print(f"\n {'*' *20} BEAUTY OF LIST COMPREHENSION {'*' *20}")
print(f"\n {'*' *20} Square of only Even Numbers {'*' *20}")
print([x**2 for x in range(10,20, 1) if x%2==0])

print(f"\n {'*' *20} Upper casing only Alphabets {'*' *20}")
sentence="in 2023 python is really cool"
upper_case=[char.upper() for char in sentence if char.isalpha()]
print(upper_case)

print(f"\n {'*' *20} Length of the strings {'*' *20}")
my_list=['Alice', 'John', 'Walterson']
dict_length={name: len(name) for name in my_list if len(name) < 6 }
print(dict_length)

print(f"\n {'*' *20} Odd and Even Numbers {'*' *20}")
number_category={num: ('even' if num % 2==0 else 'odd') for num in range(2,20,1)}
print(number_category)

print(f"\n {'*' *20} Combining two lists {'*' *20}")
listx=[1,2,3]
listy=['a','b','c','d','e','f','g','h','i','j']
combined_lists=[(x,y)for x in listx for y in listy]
print(combined_lists)

