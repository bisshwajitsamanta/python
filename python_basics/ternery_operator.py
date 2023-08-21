ask_price = 100
a = 20
b = 10

volume = 60 if ask_price > 50 else 80
print(volume)

distance = a - b if a >= b else b + a
print(distance)

# Another Example
current_value = -999
running_total = 15000
running_count = 125

# We are going to use Ternary operator only when the base remains the same only the condition changes
# if the condition satisfies then it will go to Left Hand Side else Right Hand side
clean_value = 0 if current_value == -999 else current_value
running_total = running_total + clean_value
print(running_total)
