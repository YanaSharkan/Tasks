import math


class Triangle():
    def __init__(self, name, length1, length2, length3):
        self.name = name
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def __lt__(self, other):
        return self.countSquare() < other.countSquare()

    def countSquare(self):
        p = (self.length1 + self.length2 + self.length3) / 2
        return math.sqrt(p * (p - self.length1) * (p - self.length2) * (p - self.length3))


triangles = []


def sortTriangles():
    global triangles
    props = str(input('Please put in triangle properties: '))
    props_list = props.split(',')

    if (len(props_list) != 4):
        print('Triangle properties %s are not correct.' % props)
        exit()

    triangles.append(
        Triangle(
            props_list[0].strip(),
            float(props_list[1]),
            float(props_list[2]),
            float(props_list[3])
        )
    )

    continueCommand = input('Do you want to add a new triangle? ')
    if (continueCommand.strip().lower() == 'y' or continueCommand.strip().lower() == 'yes'):
        sortTriangles()
    else:
        triangles.sort(reverse = True)
        for ind in range(0, len(triangles)):
            print('%s. [%s]: %s cm' % (ind + 1, triangles[ind].name, round(triangles[ind].countSquare())))

if __name__ == '__main__':
    sortTriangles()