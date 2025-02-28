# to find a missing number from a list/array

def missingNumber(numbers):
    n = len(numbers) + 1
    sum1 = n * (n+1) // 2
    total = sum(numbers)
    missing_number = sum1 - total 
    print(missing_number)

numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

missingNumber(numbers)