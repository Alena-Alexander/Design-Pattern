from dataclasses import dataclass, field
from abc import ABC, ABCMeta
from datetime import date, datetime, timedelta


@dataclass
class Person:
    name: str
    dob: date
    age: str = field(init=False)

    def __post_init__(self):  # Our lazy init function
        if self.dob is not None:
            self.age = str(date.today().year - self.dob.year)
            print(f"Age is: {self.age}")


if __name__ == "__main__":
    person_instance = Person(name="John", dob=date(year=2004, month=9, day=4))
    print(person_instance)
