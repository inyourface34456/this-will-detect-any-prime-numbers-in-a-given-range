from colorama import Fore
red = Fore.LIGHTGREEN_EX
green = Fore.RED
prime_counter = 0
print(
    "The numbers that are in green are the ones that are prime. The ones that are in red are not primes."
)
bottem = int(input(Fore.GREEN + "Enter a low number (no negatives pls): "))
high = int(input(Fore.YELLOW + "Enter a high number: "))
for num in range(bottem, high):
    if num  > 0:
        for i in range(2, num):
            if (num % i) == 0:
                print(green, num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(red, num, "is a prime number")
            prime_counter = prime_counter + 1
            print('how many primes that i found:', prime_counter)

    else:
        print(green, num, "is not a prime number")