import math
import sys
from os import path

tasks_path = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(path.join(tasks_path, 'validator'))
import params_validator
from params_validation_error import ParamsValidationError


class Triangle:
    def __init__(self, name, length1, length2, length3):
        self.name = name
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()

    def calculate_area(self):
        p = (self.length1 + self.length2 + self.length3) / 2
        return math.sqrt(p * (p - self.length1) * (p - self.length2) * (p - self.length3))

    @staticmethod
    def validate(props_list):
        params_validator.validate_lst(props_list, 4)
        params_validator.validate_str(props_list[0])
        params_validator.validate_int_input(props_list[1])
        params_validator.validate_int_input(props_list[2])
        params_validator.validate_int_input(props_list[3])


def build_triangle(props_list):
    return Triangle(
        props_list[0].strip(),
        float(props_list[1]),
        float(props_list[2]),
        float(props_list[3])
    )


def check_continue(continue_cmd):
    return continue_cmd.strip().lower() == 'y' or continue_cmd.strip().lower() == 'yes'


def input_triangles(triangles):
    props = str(input('Please put in triangle properties: '))
    props_list = props.split(',')

    try:
        Triangle.validate(props_list)
        triangles.append(build_triangle(props_list))
    except ParamsValidationError as err:
        print(err)


def print_sorted_triangles(triangles_list):
    triangles_list.sort(reverse=True)
    for ind in range(len(triangles_list)):
        print('%s. [%s]: %s cm' % (ind + 1, triangles_list[ind].name,
                                   round(triangles_list[ind].calculate_area(), 2)))


if __name__ == '__main__':
    res_triangles = []
    while True:
        input_triangles(res_triangles)
        continue_command = input('Do you want to add a new triangle? ')
        if not check_continue(continue_command):
            print_sorted_triangles(res_triangles)
            break

