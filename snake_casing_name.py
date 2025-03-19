# Allow users to input
full_name = input("Enter your full name: ")

# Make it snake casing
snake_casing = "_".join(full_name.lower().split())

# Print result
print(snake_casing)