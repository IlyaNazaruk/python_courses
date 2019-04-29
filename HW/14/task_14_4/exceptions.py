class MathException(Exception):
   def __init__(self, message='Calculator Error'):
       super().__init__(message)