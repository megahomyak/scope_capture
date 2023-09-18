from scope_capture import capture


def test_capturing_in_a_lambda():
    a = []
    SOMETHING_GLOBAL = 123
    for i in [1, 2]:
        a.append(capture(lambda: (SOMETHING_GLOBAL, i)))
    assert [f() for f in a] == [(123, 1), (123, 2)]


def test_accepting_arguments():
    assert capture(lambda a: a + 2)(2) == 4
    assert capture(lambda a=3: a + 2)() == 5
    assert capture(lambda a: a + 2)(a=4) == 6


def test_capturing_in_a_function():
    a = []
    SOMETHING_GLOBAL = 256
    for i in [3, 4]:
        def f():
            return (SOMETHING_GLOBAL, i)
        a.append(capture(f))
    assert [f() for f in a] == [(256, 3), (256, 4)]


def test_capturing_nested_scopes():
    functions = []
    for i in [1, 2]:
        def a():
            def b():
                def c():
                    functions.append(lambda: i)
                c()
            b()
        a()
    assert [f() for f in functions] == [1, 2]
