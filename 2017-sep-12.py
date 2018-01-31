x = int(input("Enter a number..."))
if x%2 == 0:
    if x%3 == 0:
        print("It's a multiple of 2 and 3.")
    else:
        print("It's a multiple of 2 only.")
else:
    print("It's a multiple of 3 only.")

