import copy


class Vector:
    VECTOR = []

    def __int__(self, ):
        pass

    def push_back(self, element):
        self.VECTOR.append(element)

    def pop_back(self):
        self.VECTOR.remove(len(self.VECTOR) - 1)

    def at(self, index):
        if index in self.VECTOR:
            return self.VECTOR[index]
        raise IndexError

    def back(self):
        return self.VECTOR[len(self.VECTOR) - 1]

    def front(self):
        return self.VECTOR[0]

    def isempty(self):
        if (len(self.VECTOR)) == 0:
            return True
        return False

    def isfull(self):
        if (len(self.VECTOR) - 1) == len(self.VECTOR) - 1:
            return True
        return False

    def insert_at(self, index, value):
        if index not in self.VECTOR:
            raise IndexError
        self.VECTOR.index(index, value)

    def size_of_vector(self):
        count = 0
        for _ in self.VECTOR:
            count += 1
        return count

    def print_vector(self):
        print(self.VECTOR)

    def copy_vector(self, other):
        self.VECTOR = copy.deepcopy(other)