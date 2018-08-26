import math
import params_validator
from params_validation_error import ParamsValidationError

CONTINUE_CONFIRM_SHORT = 'y'
CONTINUE_CONFIRM_FULL = 'yes'


class Triangle:
    def __init__(self, name, length1, length2, length3):
        self.name = name
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def get_area(self):
        p = (self.length1 + self.length2 + self.length3) / 2
        return math.sqrt(p * (p - self.length1) * (p - self.length2) * (p - self.length3))

    @staticmethod
    def validate(props_list):
        params_validator.validate_lst(props_list, 4)
        params_validator.validate_str(props_list[0])
        params_validator.validate_float_input(props_list[1])
        params_validator.validate_float_input(props_list[2])
        params_validator.validate_float_input(props_list[3])
        params_validator.validate_length_of_side_triangle(props_list[1:4])


def check_continue(continue_cmd):
    return continue_cmd.strip().lower() in (CONTINUE_CONFIRM_SHORT, CONTINUE_CONFIRM_FULL)


def get_input():
    return str(input('Please put in triangle properties (name, length1, length2, length3): '))


def input_triangle(triangles):
    props = get_input()
    props_list = props.split(',')

    Triangle.validate(props_list)  # Validates properties of triangle
    triangles.append(Triangle(  # Adds each triangle into triangles
        props_list[0].strip(),
        float(props_list[1]),
        float(props_list[2]),
        float(props_list[3])
    ))


def print_triangle_line(triangle, line_number):
    print('%s. [%s]: %s cm' % (line_number, triangle.name,
                               round(triangle.get_area(), 2)))


def print_sorted_triangles(triangles_list):  # Sorts triangles in list and prints each triangle
    triangles_list.sort(reverse=True)
    for ind in range(len(triangles_list)):
        print_triangle_line(triangles_list[ind], ind + 1)



if __name__ == '__main__':
    res_triangles = []  # List of triangles for sorting
    while True:
        try:
            input_triangle(res_triangles)  # Adding each entered triangle into common list
        except ParamsValidationError as err:
            print(err)
        continue_command = input('Do you want to add a new triangle? ')
        if not check_continue(continue_command):
            print('============= Triangles list: =============')
            print_sorted_triangles(res_triangles)
            break
