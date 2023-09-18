# scope\_capture

**WARNING**: I haven't tested it on older Python versions, "3.8" is only a requirement because I'm lazy! Please, if you can afford testing this on older Python versions, send a pull request, it will be very appreciated.

This library will allow you to capture surrounding scopes of functions and closures and freeze them with the callable object itself.

## The problem

In Python, variables from closures are not saved when the closure is reached, but instead they are always retrieved by their name from the surrounding scope. This leads to problems like this one:

```py
a = []
for i in [1, 2]:
    a.append(lambda: i)
for f in a:
    print(f())
```

The code above will output "2" twice, because it's not the value of the variable that was captured, the only thing that was really captured was the name, and it is only resolved when the closure is called. The last value that is associated with the name - "2" - is thus used.

## The solution

My library allows the user to freeze closures with their surrounding scope:

```py
from scope_capture import capture

a = []
for i in [1, 2]:
    a.append(lambda: i)
for f in a:
    print(f())
```

This code will print "1" and then "2", because the contexts of these lambdas were frozen with them.

This library can work with functions too.

## Examples

If you want to see examples, check out the `test_scope_capture.py` file.

## Installation

`pip install scope_capture`
