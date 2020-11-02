from colorama import Fore
# To take input from the user
red = Fore.LIGHTGREEN_EX
green = Fore.RED
print("The numbers that are in green are the ones that are prime. The ones that are in red are not primes.")
bottem = int(input(Fore.GREEN + "Enter a low number (no negatives pls): "))
high = int(input(Fore.YELLOW + "Enter a high number: "))
# prime numbers are greater than 1
for num in range(bottem,high):
  if num > 1:
    # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            print(green, num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(red, num, "is a prime number")
        
  # if input number is less than
  # or equal to 1, it is not prime
  else:
    print(green, num, "is not a prime number")