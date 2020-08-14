from base_logger import BaseLogger, log_method


def test_property(capfd, obj):
    return_value = obj.property

    stdout, stderr = capfd.readouterr()
    assert f"{obj.__class__.__name__}.property" in stdout
    assert return_value in stdout


def test_nested_property(capfd):
    class Foo:
        def __init__(self):
            self.prop = property(lambda x: "str")
            setattr(self, "prop", log_method(getattr(self, "prop")))

    obj = Foo()
    return_value = obj.prop().fget(1)

    stdout, stderr = capfd.readouterr()
    assert f"lambda" in stdout
