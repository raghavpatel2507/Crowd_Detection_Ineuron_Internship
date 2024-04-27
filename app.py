from Crowd_Detection.logger import logging
from Crowd_Detection.exception import AppException
import sys

try:
    a=3 /'a'
except Exception as e:
    raise AppException(e, sys)