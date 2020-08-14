def test_property(capfd, obj):
    return_value = obj.property

    stdout, stderr = capfd.readouterr()
    assert f"{obj.__class__.__name__}.property" in stdout
    assert return_value in stdout
