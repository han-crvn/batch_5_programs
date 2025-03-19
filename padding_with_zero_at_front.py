# Allow users to input number
numbers = (input("Enter the number: "))

# Check number if 0-1000
if 0 < int(numbers) <= 1000:
    
    # Add zeros to the front
    print(numbers.zfill(6))

else:
    print("Number must be 0-1000.")