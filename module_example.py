from blood_calculator import *
from numpy import *
from matplotlib import *
import analysis

print("This is the database module and python calls it {}"
      .format(__name__))

check_HDL()

numpy.check_HDL()


def function():
    print("one")


def function():
    print("two")


HDL_value = 55

classification = check_HDL(HDL_value)

print("55 is {}".format(classification))
x = check_LDL(200)
