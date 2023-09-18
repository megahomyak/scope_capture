import inspect
from types import FunctionType

def _make_cell(value):
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]

def capture(f):
    try:
        frame = inspect.currentframe()
        fake_globals = {}
        fake_globals.update(f.__globals__)
        fake_globals.update(frame.f_back.f_locals)
        captured_cells = []
        if f.__closure__:
            for cell in f.__closure__:
                captured_cells.append(_make_cell(cell.cell_contents))
        print(captured_cells, fake_globals["i"])
        call_fn = FunctionType(
            code=f.__code__,
            globals=fake_globals,
            name=f.__name__,
            argdefs=f.__defaults__,
            closure=tuple(captured_cells),
        )
        return call_fn
    finally:
        del frame
