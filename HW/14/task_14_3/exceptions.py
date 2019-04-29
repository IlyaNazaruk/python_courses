class MathException(Exception):
   def __init__(self, message='Math Error'):
       super().__init__(message)


class NumberException(Exception):
    def __init__(self, message='Number Error'):
        super().__init__(message)

