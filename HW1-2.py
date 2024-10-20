import dataclasses

@dataclasses.dataclass
class Employee:
    name: str
    age: int
    position: str
    salary: int

    def upgrade(self):
        self.salary = self.salary * 5
        return self.salary


if __name__ == '__main__':
    employee1 = Employee('Ivan', 25, "Developer", 1900)
    print(employee1.upgrade())
