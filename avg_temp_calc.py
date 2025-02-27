#AVERAGE TEMPERATURE CALCULATOR

num_days = int(input("Enter the number of days:"))

total = 0
temp = []

for i in range(num_days):
    nextDay = int(input("Day " + str(i+1) + "'s temperature:"))
    temp.append(nextDay)
    total += temp[i]
    
average = round(total/num_days,2)
print("The average temperature is", average)

above = 0

for i in temp:
    if i > average:
        above += 1

print(str(above) + " day(s) above average")