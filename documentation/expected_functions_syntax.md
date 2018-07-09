When initialising the validator, you must supply a list of tuples.
Each tuple should be the name of the function and then a list of the function arguments.

In practice this looks like the following:
```
expected_functions = [('function_a', [20, 30]),
                      ('function_b', [10, 10, 10]),
                      ('function_a', [5, 5])]
my_validator = Validator(expected_functions)
```

The above is equivalent to a user script of the following form:
```
import instrument_controls as IC
IC.function_a(20, 30)
IC.function_b(10, 10, 10)
IC.function_a(5,5)
```
