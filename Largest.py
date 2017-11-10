# Finding the largest number in the given loop

largest=None
for num in [10,30,204,344,4523,5423,5665,121,454,656,75,678]:
    if largest is None:
        largest=num
    if num>largest:
        largest=num
print('Largest number',largest)
