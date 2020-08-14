import inspect


def test_args(capfd, cls):
    first_arg, second_hard = "first", "last"
    return_value = cls.class_method(*(first_arg, second_hard))

    stdout, stderr = capfd.readouterr()
    assert f"{cls.__name__}.class_method" in stdout
    for parameter in inspect.signature(cls.class_method).parameters.keys():
        assert parameter in stdout
    assert first_arg in stdout
    assert second_hard in stdout
    assert return_value in stdout


def test_kwargs(capfd, cls):
    kwargs = dict(first_name="first", last_name="last")
    return_value = cls.class_method(**kwargs)

    stdout, stderr = capfd.readouterr()
    assert f"{cls.__name__}.class_method" in stdout
    for parameter in inspect.signature(cls.class_method).parameters.keys():
        assert parameter in stdout
    for v in kwargs.values():
        assert v in stdout
    assert return_value in stdout


def test_default_kwargs(capfd, cls):
    kwargs = dict(first_name="Elie")
    return_value = cls.class_method(**kwargs)

    stdout, stderr = capfd.readouterr()
    assert f"{cls.__name__}.class_method" in stdout
    for parameter in inspect.signature(cls.class_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout
