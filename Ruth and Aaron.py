def ruth_aaron(n):
    # Check if n is within the valid range
    if not (2 <= n <= 1000000):
        return None
    
    # Nested helper function to find all prime factors with multiplicity
    def get_prime_factors(num):
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors
    
    # Calculate prime factors once to avoid redundant computations
    factors_prev = get_prime_factors(n - 1)
    factors_curr = get_prime_factors(n)
    factors_next = get_prime_factors(n + 1)
    
    # Check first definition: sum of distinct prime factors
    with_prev_1 = sum(set(factors_prev)) == sum(set(factors_curr))
    with_next_1 = sum(set(factors_curr)) == sum(set(factors_next))
    
    # Check second definition: sum of prime factors with multiplicity
    with_prev_2 = sum(factors_prev) == sum(factors_curr)
    with_next_2 = sum(factors_curr) == sum(factors_next)
    
    # If n forms a pair with n+1 (n plays the role of Ruth) - CHECK THIS FIRST!
    if with_next_1 or with_next_2:
        if with_next_1 and with_next_2:
            return "Ruth-3"
        elif with_next_1:
            return "Ruth-1"
        else:
            return "Ruth-2"
    
    # If n forms a pair with n-1 (n plays the role of Aaron)
    if with_prev_1 or with_prev_2:
        if with_prev_1 and with_prev_2:
            return "Aaron-3"
        elif with_prev_1:
            return "Aaron-1"
        else:
            return "Aaron-2"
    
    # If no pair is found
    return "Not a Ruth-Aaron pair"
