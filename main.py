from matplotlib import pyplot as plt
import numpy as np


left = 0
right = np.pi/2 - 0.00001
step = np.pi/36
#1.570796326794896
#1.570796326794896
points = []
eps = 0.00001
prev_approx = 2
a = 0
b = 0


def runge_rule(right_end):
    global prev_approx
    print(prev_approx)
    pieces = prev_approx
    global a
    global b
    a = simpson_method(right_end, pieces)
    b = simpson_method(right_end, pieces / 2)
    print("in")
    while np.abs(a - b)/15 >= eps:
        #print(1/15 * np.abs(a - b))
        pieces += 2
        a = simpson_method(right_end, pieces)
        b = simpson_method(right_end, pieces/2)
    print("out")
    prev_approx = pieces
    return a


def simpson_method(right_end, num_of_pieces):
    print(f"Right end = {right_end}, num = {num_of_pieces}" )
    local_step = (right_end-left)/num_of_pieces
    #print(local_step)
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
    #print(array_of_even)
    #print(array_of_odd)

    sum_for_even = 0
    for e in array_of_even:

        sum_for_even += 2*func(e)
        #print(f"for x = {e} func is {4*func(e)}")

    sum_for_odd = 0
    for o in array_of_odd:
        sum_for_odd += 4*func(o)
        #print(f"for x = {o} func is {4*func(o)}")

    return local_step/3 * (func(left) + func(right_end) + sum_for_odd + sum_for_even)


def func(x):
    return np.log(np.cos(x))


def func1(x):
    return (-1) * np.log(np.cos(x))


def do_staff():
    res = {}
    resv = []
    for ele in points:
        k = (-1)*runge_rule(ele)
        resv.append(k)
        res[ele] = k

    print(res)
    # functional_table = np.append(functional_table, [[points, resv]], axis=0)
    # print(f"{functional_table=}")
    # # x, y = functional_table.T
    plt.plot(points, resv)
    plt.show()


def fill_points():
    i = left + step
    print(right)
    while i < right:
        points.append(i)
        i = i + step
    print(points)


if __name__ == '__main__':
    fill_points()
    #print(simpson_method(np.pi/2-0.001, 2230))
    do_staff()
