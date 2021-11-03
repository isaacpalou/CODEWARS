from math import floor


def loose_change(cents):
    result = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

    # PRECONDICIONES
    if not isinstance(cents, int) and not isinstance(cents, float):
        return result
    if cents < 1:
        return result
    if isinstance(cents, float):
        cents = floor(cents)
    # FUNCIÓN:
    result['Quarters'] = cents // 25
    cents %= 25
    result['Dimes'] = cents // 10
    cents %= 10
    result['Nickels'] = cents // 5
    cents %= 5
    result['Pennies'] = cents // 1

    return result


if __name__ == '__main__':
    assert(loose_change(29) == {'Nickels': 0,
           'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
    assert(loose_change(91) == {'Nickels': 1,
           'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
    assert(loose_change(0) == {'Nickels': 0,
           'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert(loose_change(-2) == {'Nickels': 0,
           'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert(loose_change(3.9) == {'Nickels': 0,
           'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
