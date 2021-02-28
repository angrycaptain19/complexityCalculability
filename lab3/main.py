# Subject: Empirical analysis of algorithms for obtaining Eratosthenes Sieve.

import algorithms

if __name__ == "__main__":
    while True:
        num = int(input("What's the range of primes?\n"))
        print("Welcome to the menu\n"
              "1. Re-choose the range\n"
              "2. Choose the algorithm\n"
              "3. Exit")
        n = int(input())

        if n == 1:
            num = int(input("How many primes do you want printed?\n"))

        if n == 2:
            choice = int(input("Choose the algorithm:\n"
                               "1.\n2.\n3.\n4.\n5.\n"))
            if choice == 1:
                algorithms.firstAlgorithm(num)
            elif choice == 2:
                algorithms.secondAlgorithm(num)
            elif choice == 3:
                algorithms.thirdAlgorithm(num)
            elif choice == 4:
                algorithms.fourthAlgorithm(num)
            elif choice == 5:
                algorithms.fifthAlgorithm(num)
            else:
                print("Wrong choice, try again!")

        elif n == 3:
            break

        else:
            print("Wrong choice, try again!")

