from design_patterns.builder.builder import HouseBuilder
import pytest

def test_house_builder():
    house_builder = HouseBuilder()
    house_builder.windows = 4
    house_builder.doors = 2
    house_builder.rooms = 3
    house_builder.has_garage = True
    house_builder.has_garden = False

    house = house_builder.build()
    assert house.windows == 4
    assert house.doors == 2
    assert house.rooms == 3
    assert house.has_garage is True
    assert house.has_garden is False

def test_default_house_builder():
    house_builder = HouseBuilder()
    house = house_builder.build()
    assert house.windows == 0
    assert house.doors == 0
    assert house.rooms == 0
    assert house.has_garage is False
    assert house.has_garden is False