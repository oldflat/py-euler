# Amicable numbers
#
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from utilities.divisors import get_divisors
from utilities.primes import prime_factors


def main():
    print(prime_factors(12))

    print(get_divisors(7200))

    sum_of_amicable_numbers = 0
    amicable_lookup = [0] * 20000
    for num1 in range(10000):
        if amicable_lookup[num1] != 0:
            num2 = amicable_lookup[num1]
        else:
            num2 = sum(get_divisors(num1))
            amicable_lookup[num1] = num2
        if num1 % 100 == 0:
            print("sum of divisors of " + str(num1) + " = " + str(num2))
        if num2 < len(amicable_lookup) and amicable_lookup[num2] != 0:
            amicable_test_for_num1 = amicable_lookup[num2]
        else:
            amicable_test_for_num1 = sum(get_divisors(num2))
            if num2 < len(amicable_lookup):
                amicable_lookup[num2] = amicable_test_for_num1
        if amicable_test_for_num1 == num1 and num1 != num2:
            sum_of_amicable_numbers += num1
            print("amicable numbers " + str(num1) + " and " + str(num2))

    print("The Answer to Project Euler 021")
    print("The sum of amicable numbers under 10000 is {0}".format(str(sum_of_amicable_numbers)))


if __name__ == "__main__":
    main()
