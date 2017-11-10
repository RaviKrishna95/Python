# To find the average of some given numbers

sum=0
count=0
avg=0
for thing in [10,30,204,344,4523,5423,5665,121,454,656,75,678]:
    count=count+1
    sum=sum+thing
avg=sum/count
print('Average:',avg)
