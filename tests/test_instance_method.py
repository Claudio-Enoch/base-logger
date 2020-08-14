import inspect


def test_args(capfd, obj):
    return_value = obj.instance_method("first", "last")
    stdout, stderr = capfd.readouterr()
    assert f"{obj.__class__.__name__}.instance_method" in stdout
    for parameter in inspect.signature(obj.instance_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout


def test_kwargs(capfd, obj):
    return_value = obj.instance_method(first_name="first", last_name="last")
    stdout, stderr = capfd.readouterr()
    assert f"{obj.__class__.__name__}.instance_method" in stdout
    for parameter in inspect.signature(obj.instance_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout


def test_default_kwargs(capfd, obj):
    return_value = obj.instance_method(first_name="Elie")
    stdout, stderr = capfd.readouterr()
    assert f"{obj.__class__.__name__}.instance_method" in stdout
    for parameter in inspect.signature(obj.instance_method).parameters.keys():
        assert parameter in stdout
    assert return_value in stdout
