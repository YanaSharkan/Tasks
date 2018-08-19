from params_validation_error import ParamsValidationError


def validate_lst(lst, params_number):
    if (type(lst) != list and type(lst) != tuple) or len(lst) != params_number:
        print(lst)
        raise ParamsValidationError('Not enough arguments specified')


def validate_int_input(num):
    if type(num) != str or not num.isdigit() or int(num) < 1:
        raise ParamsValidationError('Argument should be a positive int')


def validate_positive_int(num):
    if type(num) != int or num < 1:
        raise ParamsValidationError('Argument should be a positive int')


def validate_str(st):
    if type(st) != str or st.strip() == '':
        raise ParamsValidationError('Argument should be non-empty string')
