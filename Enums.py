from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Thu)
print(Weekday['Thu'])
print(Weekday.Thu.value)
print(Weekday(3))
print(day1 == Weekday.Mon)

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
