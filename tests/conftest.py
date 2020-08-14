import pytest

from base_logger import BaseLogger


class Class(BaseLogger):
    @staticmethod
    def static_method(first_name: str, last_name: str = "Last Name") -> str:
        return first_name + last_name

    @property
    def property(self) -> str:
        return "Property"

    def instance_method(self, first_name, last_name="Last Name") -> str:
        return self.__class__.__name__ + first_name + last_name

    @classmethod
    def class_method(cls, first_name, last_name: str = "last name") -> str:
        return cls.__name__ + first_name + last_name


@pytest.fixture(scope="session")
def cls() -> type(Class):
    return Class


@pytest.fixture(scope="session")
def obj() -> Class:
    return Class()
