import numpy as np

left = 0
right = np.pi/2
step = np.pi/36
points = []


def simpson_method(right_end, num_of_pieces):
    local_step = (right_end-left)/num_of_pieces
    print(local_step)
    array_of_even = [] #парні х
    array_of_odd = [] #непарні х
    i = 0
    temp = left
    while i < num_of_pieces-1:
        temp = temp + local_step
        if i % 2 == 0:
            array_of_odd.append(temp)
        else:
            array_of_even.append(temp)
        i = i + 1
    print(array_of_even)
    print(array_of_odd)

    sum_for_even = 0
    for e in array_of_even:

        sum_for_even += 2*func(e)
        print(f"for x = {e} func is {4*func(e)}")

    sum_for_odd = 0
    for o in array_of_odd:
        sum_for_odd += 4*func(o)
        print(f"for x = {o} func is {4*func(o)}")

    return local_step/3 * (func(left) + func(right_end) + sum_for_odd + sum_for_even)


def func(x):
    return np.log(np.cos(x))


def fill_points():
    i = left
    while i <= right:
        points.append(i)
        i = i + step
    print(points)


if __name__ == '__main__':
    fill_points()
    print(simpson_method(np.pi/4, 18))
