from pycon_decorators import use_unit


class Runner:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    @use_unit("meters per second")
    def average_speed(self):
        return self.distance / self.duration


class Plane:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    @use_unit("km per hour")
    def average_speed(self):
        return self.distance / self.duration



bolt = Runner(100, 9.58)
osl_pit = Plane(6261, 9)

print(bolt.average_speed())
print(bolt.average_speed.unit)
print(osl_pit.average_speed())

ratio = osl_pit.average_speed() / bolt.average_speed()
print(ratio.to_base_units())


# def meters_per_second(func):
#     meters_per_second.ureg = pint.UnitRegistry()
#     unit = "meters per second"
#     def _meters_per_second(*args, **kwargs):
#         return func(*args, **kwargs) * meters_per_second.ureg(unit)
#     return _meters_per_second


# @meters_per_second
# def average_speed(distance, duration):
#     return distance / duration


# bolt = average_speed(100, 9.58)
# print(bolt)
# # 10.438.. <Unit('meter / second')>

# 2 * bolt

# bolt.to("km per hour")
