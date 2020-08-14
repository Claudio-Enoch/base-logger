import inspect


def test_args(capfd, cls):
    return_value = cls.static_method("first", "last")
    stdout, stderr = capfd.readouterr()
    assert f"{cls.__name__}.static_method" in stdout
    for parameter in inspect.signature(cls.static_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout


def test_kwargs(capfd, cls):
    return_value = cls.static_method(first_name="first", last_name="last")
    stdout, stderr = capfd.readouterr()
    assert f"{cls.__name__}.static_method" in stdout
    for parameter in inspect.signature(cls.static_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout


def test_default_kwargs(capfd, cls):
    return_value = cls.static_method(first_name="Elie")
    stdout, stderr = capfd.readouterr()
    assert f"{cls.__name__}.static_method" in stdout
    for parameter in inspect.signature(cls.static_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout
