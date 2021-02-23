
def function_error():
    a = 5+7;
    try:
        return b
    except NameError:
        print("variable b has not been defined")
        
    
def main(b):
    c = b+3;
    if c == 15:
        return True
    else:
        return False


if __name__ == "__main__":
    b = function_error()
    sum_tot = main(b)
    print(sum_tot)
    
    
'''

def go_through_list(x):
    for i in range(10):
        try:
            print(x[i])
        except IndexError:
            break
'''
