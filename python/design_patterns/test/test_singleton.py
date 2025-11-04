from design_patterns.singleton.singleton import PersonSingleton
import pytest


def test_initialize():
    person = PersonSingleton(name="John Doe", age=30)
    assert person.get_instance().name == "John Doe"
    assert person.get_instance().age == 30


def test_second_instance_exception():
    with pytest.raises(Exception) as excinfo:
        another_person = PersonSingleton(name="Jane Doe", age=25)

    assert "Singleton can't be instantiated more than ones!" in str(
        excinfo.value)


def test_print_data(capfd):
    person = PersonSingleton.get_instance()
    person.print_data()
    captured = capfd.readouterr()
    assert captured.out.strip() == f"Name: {person.name}, age: {person.age}"
