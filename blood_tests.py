def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9": #9 is in quotes because input returns a string
            return
        
interface()