from colorama import Fore
red = Fore.LIGHTGREEN_EX
green = Fore.RED
prime_counter = 0
print(
    "The numbers that are in green are the ones that are prime. The ones that are in red are not primes. PLS upvote if you think it is a good program (most of the credit should go to https://www.programiz.com/python-programming/examples/prime-number)"
)

# user input
bottem = int(input(Fore.GREEN + "Enter a low number (no negatives pls): "))
high = int(input(Fore.YELLOW + "Enter a high number: "))
show_factors = str(
    input(Fore.BLUE +
          "do you want to see the factors of all of the numbers? (y/n) "))
y_n_logging = str(input(Fore.BLUE + "do you want logging? (y/n)"))
if (y_n_logging == 'y'):
    logging_file = str(
        input(
            Fore.GREEN +
            "enter the name ofthe file that you want to log to (type none for no loging) "
        ))


# functions
def str_to_int(num_to_con):
    num_con = str(num_to_con)
    return num_con


def loging(ver_to_log):
    with open(logging_file, 'a') as x:
        x.write(ver_to_log)


# actual math
for num in range(bottem, high):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(green, num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                if (show_factors == 'y'):
                    print('lowest factor:', i)
                break
        else:
            print(red, num, "is a prime number")
            string = str_to_int(num)
            if (logging_file != 'none'):
                loging(str_to_int(num) + '\n')
            prime_counter = prime_counter + 1
            print('how many primes that i found:', prime_counter)
    else:
        print(green, num, "is not a prime number")
loging('number of primes found:' + str_to_int(prime_counter))
