from trianglesort import trianglesorter

def test_not_a_triangle():
    '''Test for invalid triangle'''
    assert trianglesorter(3, 4, 7) == 'Not a triangle'

def test_right_angled():
    '''Test for a right-angled triangle'''
    assert trianglesorter(3, 4, 5) == 'Right angled'

def test_equilateral():
    '''Test for an equilateral triangle'''
    assert trianglesorter(3, 3, 3) == 'Equilateral'

def test_isosceles():
    '''Test for an isosceles triangle'''
    assert trianglesorter(3, 3, 4) == 'Isosceles'

def test_scalene():
    '''Test for a scalene triangle'''
    assert trianglesorter(3, 4, 6) == 'Scalene'

if __name__ == '__main__':
    test_not_a_triangle()
    test_right_angled()
    test_equilateral()
    test_isosceles()
    test_scalene()
    print('All tests pass')
