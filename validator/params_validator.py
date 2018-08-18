from params_validation_error import ParamsValidationError


def validate_lst(lst, params_number):
    if type(lst) != list or len(lst) != params_number:
        raise ParamsValidationError('Argument should be a list')


def validate_positive_int(num):
    if type(num) != str or not num.isdigit() or int(num) < 1:
        raise ParamsValidationError('Argument should be a positive int')


def validate_str(st):
    if type(st) != str or st.strip() == '':
        raise ParamsValidationError('Argument should be non-empty string')
