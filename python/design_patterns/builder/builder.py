import dataclasses


class House(object):
    def __init__(self, builder):
        self.windows = builder.windows
        self.doors = builder.doors
        self.rooms = builder.rooms
        self.has_garage = builder.has_garage
        self.has_garden = builder.has_garden

@dataclasses.dataclass
class HouseBuilder:
    windows: int = 0
    doors: int = 0
    rooms: int = 0
    has_garage: bool = False
    has_garden: bool = False


    def build(self):
        return House(self)
    