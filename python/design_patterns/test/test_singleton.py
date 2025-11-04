from design_patterns.singleton.singleton import Singleton
import pytest

def test_singleton_instance():
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()
    assert singleton1 is singleton2, "Both instances should be the same"

