name=input("Enter your name: ")
match name:
    case "monika"|"sahi":
        print("banglore")

    case "malndeep":
        print("guntur")
    case _:
        print("who?...")
# match is a keyword which acts switch case in other languages