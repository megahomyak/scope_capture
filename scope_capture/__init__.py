from types import FunctionType

def _make_cell(value):
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]

def capture(f):
    # print(fn_globals["i"])
    # print(f.__closure__)
    # breakpoint()
    captured_cells = []
    if f.__closure__:
        for cell in f.__closure__:
            captured_cells.append(_make_cell(cell.cell_contents))
    call_fn = FunctionType(
        code=f.__code__,
        globals=f.__globals__,
        name=f.__name__,
        argdefs=f.__defaults__,
        closure=tuple(captured_cells),
    )
    return call_fn
