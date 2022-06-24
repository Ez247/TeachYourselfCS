"""Pure Functions:
        0. Functions that have some input(an argument) and returns some output
           (a result) Eg abs function.
        1. Applying pure functions has no effects beyond returning a value.
        3. Why use pure functions:
            a. They are restricted in that they cannot have side effects.
            b. They tend to be simpler to test.
            c. They are essential for writing concurrent programs.
"""

#Pure Function
abs(-2)  # This evaluates to 2

"""Non-Pure Functions:
        0. They return a value and can generate side effects.
        1. Eg, generating additional output beyong the return value using print. 
"""

#Non-pure function Example

print(1, 2, 3)  # This evealuates to 1 2 3

print(print(1), print(2))  # This evealuates to 1 2 None None

two = print(2)

print(two)
