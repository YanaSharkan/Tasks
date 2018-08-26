from params_validation_error import ParamsValidationError


def validate_lst(lst, params_number):
    if not isinstance(lst, (list, tuple)) or len(lst) != params_number:
        raise ParamsValidationError('Not enough arguments specified')


def validate_float_input(num):
    try:
        float(num)
    except ValueError:
        raise ParamsValidationError('Argument must be a float greater then 0')


def validate_str(st):
    if not isinstance(st, str) or st.strip() == '':
        raise ParamsValidationError('Argument must be non-empty string')


def validate_length_of_side_triangle(props_list):
    props_list.sort(key=lambda s: float(s), reverse=True)
    max_length = float(props_list[0])
    if max_length >= float(props_list[1]) + float(props_list[2]):
        raise ParamsValidationError('Sum of two sides of triangle must be greater then the biggest side')



