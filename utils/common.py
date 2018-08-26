from itertools import product


def get_year_and_quarter(start, end, quarters=[1, 2, 3, 4]):
    years = range(start, end)
    return list(product(years, quarters))
