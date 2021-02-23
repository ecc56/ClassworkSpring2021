## This program demonstrates "logging"

import logging

def fibonacci(fib_list):
    next_number = fib_list[-1] + fib_list[-2]
    #print("{} + {} + {}".format(fib_list[-1], fib_list[-2], next_number))
    logging.info("{} + {} + {}".format(fib_list[-1], fib_list[-2], next_number))
    fib_list.append(next_number)
    if next_number < 100:
        fibonacci(fib_list)
        
    else:
        logging.warning("reached end of list")
    return fib_list


def main():
    x = [0, 1]
    answer = fibonacci(x)
    print(answer)


if __name__ == "__main__":
    logging.basicConfig(filename="fib.txt", level=logging.INFO) #saves info/warning stuff to a text file
    main()


# logging.warning
# logging.info
# logging.debug
# logging.error
# logging.critical
