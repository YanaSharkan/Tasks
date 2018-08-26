from params_validation_error import ParamsValidationError


def validate_int_input(num):
    if not isinstance(num, str) or not num.isdigit() or int(num) < 1:
        raise ParamsValidationError('Argument must be an int greater then 0')
