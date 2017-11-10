# Finding the smallest number in the given loop

smallest=None
for num in [30,204,344,4523,5423,5665,10,121,454,656,75,678]:
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
print('Smallest number',smallest)
