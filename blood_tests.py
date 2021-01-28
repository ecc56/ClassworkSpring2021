def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9": #9 is in quotes because input returns a string
            return


def HDL_driver():   
    # Get data
    # Analyze data
    # Output data
    data1 = input("Enter HDL value: ")
    data = int(data1)
    if data >= 60:
        print("Normal")
    elif data < 40:
        print("Low")
    else:
        print("Borderline Low")


        
interface()

HDL_driver()


