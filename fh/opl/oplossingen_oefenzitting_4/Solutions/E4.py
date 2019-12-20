number = int(input('Enter a number: '))

if number == 0 or number == 1:
    is_prime = False
elif number == 2:
    is_prime = True
else:
    # The edge cases above are trivial, and follow the definition of prime numbers in math.
    # The algorithm below now checks for numbers > 2,
    # so that is what the correctness proof will be about as well.
    # The correctness proof, together with the two special cases above, entail a complete
    # correctness proof of the entire program, for any 'number' that is a natural number.

    # PRE: number is a natural number > 2

    is_prime = True
    i = 2

    # INVARIANT:
    #   1. is_prime is False if number is divisible by any number in S = {2, 3, ..., i - 1}
    #                     is True otherwise
    #   AND
    #   2. i <= number

    # AFTER INITIALISATION:
    #   1. there is no number in empty set S, so is_prime should be True - which it is.
    #   2. indeed, i <= number
    # So: INVARIANT holds after initialisation

    while (i < number and is_prime):
        # INVARIANT holds
        # and i < number
        # So:
        #       1. is_prime is False if number is divisible by any number in S = {2, 3, ..., i - 1}
        #                     is True otherwise
        #       AND
        #       2.     2 <= i < number

        if number % i == 0:
            is_prime = False
        # So:
        #       1. is_prime is False if number is divisible by any number in S = {2, 3, ..., i}
        #                     is True otherwise
        #       AND
        #       2.     2 <= i < number

        i += 1
        # So:
        #       1. is_prime is False if number is divisible by any number in S = {2, 3, ..., i-1}
        #                     is True otherwise
        #       AND
        #       2.     2 < i <= number
        # So, the INVARIANTS is MAINTAINED

    # TERMINATION
    #       Either when:
    #               i >= number: At that point S = {2, 3, ..., number - 1}, is_prime is false if number is not divisible by
    #                               any number in S and is true if it is divisible by at least one number in S
    #                           => POST CONDITION
    #       Or when:
    #               is_prime == False: At this point S = {2, 3, ..., i} and number is divisible by at least one number is S
    #                           => POST CONDITION

    # FINITENESS:
    # - VARIANT: `number` - `i`
    # - LOWER BOUND: `i` is at most equal to `number`,
    #   at that point the variant equals 0
    # - MONOTONIC DECREASE: at each iteration, `i` is increased by 1 and
    #   `number` is constant so the variant decreases by one at each iteration
    # - FINITE NUMBER OF DECREMENTS: since the variant decreases
    #   monotonically by one at each iteration and `number` is constant,
    #   the lower bound will be reached at which point the loop ends.

    # POST: S = {2, 3, ..., number - 1}; is_prime is false if number is divisible by at least one number in S, otherwise is_prime is true.

if is_prime:
    print(str(number) + ' is a prime number.')
else:
    print(str(number) + ' is not a prime number.')