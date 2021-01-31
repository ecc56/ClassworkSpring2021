def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter an option: ")
        if choice == "9": #9 is in quotes because input returns a string
            return
        elif choice == "1":
            HDL_driver()

#Need to add functions that:            
    # Get data
    # Analyze data
    # Output data

def HDL_driver():  
    HDL = get_HDL_input()
    analysis = analyze_HDL(HDL)
    output_HDL(HDL, analysis)

def get_HDL_input(): #input function
    HDL = input("Enter HDL Level: ")
    return int(HDL)
    
def analyze_HDL(HDL): #analyze data
    if HDL >= 60:
        print("Normal")
    elif HDL < 40:
        print("Low")
    else:
        print("Borderline Low")
        
def output_HDL(HDL,analysis):
    print("The HDL entered was {}".format(HDL))
    print("The level is {}".format(analysis))      

        
interface()
HDL_driver()
get_HDL_input()
analyze_HDL()
output_HDL()


