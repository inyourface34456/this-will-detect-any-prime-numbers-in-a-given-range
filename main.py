from colorama import Fore
red = Fore.LIGHTGREEN_EX
green = Fore.RED
# orange = Fore.PURPLE
prime_counter = 0
print(
    "The numbers that are in green are the ones that are prime. The ones that are in red are not primes. PLS upvote if you think it is a good program"
)
print(str(10))
# print(float('inf'))
# bottem = 0
# high = float('inf')
def str_to_int(num_to_con):
  num_con = str(num_to_con)
  return num_con
bottem = int(input(Fore.GREEN + "Enter a low number (no negatives pls): "))
high = int(input(Fore.YELLOW + "Enter a high number: "))
show_factors = str(input(Fore.BLUE + "do you want to see the factors of all of the numbers? (y/n) "))
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
            with open('primes.txt', 'w') as x:
              x.write(str_to_int(num))
            x.close()
            prime_counter = prime_counter + 1
            print('how many primes that i found:', prime_counter)

    else:
        print(green, num, "is not a prime number")