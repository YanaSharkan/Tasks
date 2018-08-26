class ParamsValidationError(Exception):
    def __init__(self, message):
        super(ParamsValidationError, self).__init__(message)

