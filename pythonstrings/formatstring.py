# age = 36
# txt = "My name is John, I am " + age
# print(txt)

#But we can combine strings and numbers by using f-strings or the format() method!


age = 36
txt = f"My name is John, I am {age}"
print(txt)

car = "benz"
v = "my name is"
print(v + " " + car)


price = 59
txt = f"The price is {price} dollars"
print(txt)


cost = 6000
txt = f"the estimate is {cost} naira"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)
