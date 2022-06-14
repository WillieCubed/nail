def load_data_from_file(filename: str):
    pass


class Program:
    def __init__(self, inital_data=None, program_data=None):
        self._initial_data = inital_data
        self._program_data = program_data

    def evaluate(self, *args):
        pass

    def __call__(self, *args):
        self.evaluate(args)

    @classmethod
    def from_file(cls, filename: str):
        try:
            data = load_data_from_file(filename)
            return cls(program_data=data)
        except:
            # TODO: Log, obviously
            pass


if __name__ == '__main__':
    # We can load programs from memory using a serialized file format
    classify_dog = Program.from_file('./dog-classifier.pt')

    import numpy as np

    dog_image = np.random((3, 128, 128))
    dog_breed = classify_dog(dog_image)

    # TODO: Figure out how we train these programs
    # Working idea is that each program maintains and manipulates an active
    # neural and symbolic component. Maybe a symbolic component is only
    # "extracted" on-demand?