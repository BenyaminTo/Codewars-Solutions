# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:51:14 2026

@author: Benyamin
"""
def dig_pow(n, p):
    num = n
    dig = []
    while num > 0:
        dig.append(num % 10)
        num = num // 10
    
    dig.reverse()
    sum_n = 0
    for d in dig:
        sum_n += d**p
        p += 1

    if sum_n % n == 0:
        k = sum_n / n
    else:
        k = -1
        
    return k
#------------------------------------------------------------------------------
# Test cases: (n, p, expected_output)
tests = [
    (89, 1, 1),
    (92, 1, -1),
    (695, 2, 2),
    (46288, 3, 51),
    (135, 1, 1),
    (1, 1, 1),
    (9, 1, 1),
    (567, 4, -1),
]

def run_tests():
    passed = 0
    for i, (n, p, expected) in enumerate(tests, 1):
        result = dig_pow(n, p)
        if result == expected:
            print(f"Test {i}: ✔ PASSED")
            passed += 1
        else:
            print(f"Test {i}: ✘ FAILED (n={n}, p={p}) → expected {expected}, got {result}")

    print(f"\nSummary: {passed}/{len(tests)} tests passed.")

if __name__ == "__main__":
    run_tests()