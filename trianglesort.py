def trianglesorter(a, b, c):
    '''Given three side lengths, a, b, c, return the type of the triangle.
    This must be one of 'Right angled', 'Equilateral', 'Isosceles', 'Scalene', 
    or 'Not a triangle'.'''
    sides = sorted([a, b, c])
    # The sides are now in order, reference them as sides[0], sides[1], sides[2]

    # Your code goes here

    return


if __name__ == '__main__':
    print(trianglesorter(3, 4, 7))
    print(trianglesorter(3, 4, 5))
    print(trianglesorter(3, 3, 3))
    print(trianglesorter(3, 3, 4))
    print(trianglesorter(3, 4, 6))
