import inspect
from types import FunctionType

def capture(f):
    try:
        frame = inspect.currentframe()
        fn_globals = {}
        fn_globals.update(f.__globals__)
        fn_globals.update(frame.f_back.f_locals)
        call_fn = FunctionType(getattr(f, "__code__"), fn_globals)
        return call_fn
    finally:
        del frame # See note at https://docs.python.org/3/library/inspect.html#the-interpreter-stack

if __name__ == "__main__":
    a = []
    SOMETHING_GLOBAL = 123
    for i in [1, 2]:
        a.append(capture(lambda: (SOMETHING_GLOBAL, i)))

    print(a[0](), a[1]())
