# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        result = []

        for i in range(len(self.vector)):
            result.append(self.vector[i] + other.vector[i])

        return Vector(result)

    def __mul__(self, other):
        result = 0

        for i in range(len(self.vector)):
            result += self.vector[i] * other.vector[i]

        return result

    def __len__(self):
        return len(self.vector)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Addition:", (v1 + v2).vector)
print("Dot Product:", v1 * v2)
print("Dimension of v1:", len(v1))

