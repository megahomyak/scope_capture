import inspect
from types import FunctionType

def capture(f):
    try:
        frame = inspect.currentframe()
        fn_globals = {}
        fn_globals.update(f.__globals__)
        fn_globals.update(frame.f_back.f_locals)
        call_fn = FunctionType(
            code=f.__code__,
            globals=fn_globals,
            name=f.__name__,
            argdefs=f.__defaults__,
            closure=f.__closure__,
        )
        return call_fn
    finally:
        del frame # See note at https://docs.python.org/3/library/inspect.html#the-interpreter-stack
