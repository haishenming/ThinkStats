import math

import matplotlib.pyplot as pyplot

from libs import thinkstati
from Chapter1.first_ import *

pumkins = [1, 1, 1, 2, 2, 591]


def Pumpkin(pumkins):
    """ 计算重量 """
    print("mean:", thinkstati.Mean(pumkins))
    print("variance:", thinkstati.Var(pumkins))
    print("Standard deviation", math.sqrt(thinkstati.Var(pumkins)))


def Summarize(data_dir):
    """Prints summary statistics for first babies and others.

    Returns:
        tuple of Tables
    """
    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)

    print('Standard deviation of first', math.sqrt(thinkstati.Var(
        firsts.lengths)))
    print('Standard deviation of others', math.sqrt(thinkstati.Var(
        others.lengths)))


if __name__ == '__main__':
    # Pumpkin(pumkins)
    # Summarize(".")
    pyplot.pie([1, 2, 3, 4])
    pyplot.show()
