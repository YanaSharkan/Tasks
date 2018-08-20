from params_validation_error import ParamsValidationError


def validate_lst(lst, params_number):
    if (not isinstance(lst, list) and not isinstance(lst, tuple)) or len(lst) != params_number:
        raise ParamsValidationError('Not enough arguments specified')


def validate_int_input(num):
    if not isinstance(num, str) or not num.isdigit() or int(num) < 1:
        raise ParamsValidationError('Argument should be a positive int')


def validate_positive_int(num):
    if not isinstance(num, int) or num < 1:
        raise ParamsValidationError('Argument should be a positive int')


def validate_str(st):
    if not isinstance(st, str) or st.strip() == '':
        raise ParamsValidationError('Argument should be non-empty string')
