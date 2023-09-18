from types import FunctionType

def capture(f):
    try:
        # print(fn_globals["i"])
        # print(f.__closure__)
        # breakpoint()
        captured_cells = []
        if f.__closure__:
            for cell in f.__closure__:
                contents = cell.cell_contents
                captured_cell = (lambda: contents).__closure__[0]
                captured_cells.append(captured_cell)
        call_fn = FunctionType(
            code=f.__code__,
            globals=f.__globals__,
            name=f.__name__,
            argdefs=f.__defaults__,
            closure=tuple(captured_cells),
        )
        return call_fn
    finally:
        del frame # See note at https://docs.python.org/3/library/inspect.html#the-interpreter-stack
