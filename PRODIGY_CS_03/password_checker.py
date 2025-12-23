import string

while True:
    password = input("\nEnter your password (or type exit): ")

    if password.lower() == "exit":
        print("Program ended.")
        break

    score = 0

    if len(password) >= 8:
        score += 1

    for ch in password:
        if ch.isupper():
            score += 1
            break

    for ch in password:
        if ch.islower():
            score += 1
            break

    for ch in password:
        if ch.isdigit():
            score += 1
            break

    for ch in password:
        if ch in string.punctuation:
            score += 1
            break

    if score <= 2:
        print("Password Strength: Weak")
    elif score <= 4:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")
