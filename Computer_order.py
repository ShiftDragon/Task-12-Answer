"""Builder Pattern: create a computer order step by step."""


class Computer:
    def __init__(self):
        self.cpu = "Not selected"
        self.memory = "Not selected"
        self.storage = "Not selected"

    def show(self):
        print("Computer order:")
        print(f"CPU: {self.cpu}")
        print(f"Memory: {self.memory}")
        print(f"Storage: {self.storage}")


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    # Each method builds one part and returns the same builder.
    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def add_memory(self, memory):
        self.computer.memory = memory
        return self

    def add_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer



computer = (
        ComputerBuilder()
        .add_cpu("Intel Core i5")
        .add_memory("16 GB")
        .add_storage("512 GB SSD")
        .build()
    )

computer.show()
