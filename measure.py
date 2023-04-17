import numpy as np


def point_to_line(p1, p2, p3):
    """_summary_

    Args:
        p1 (_type_): 直线的一个点
        p2 (_type_): 直线的另外一个点
        p3 (_type_): 待求点

    Returns:
        _type_: _description_
    """
    return np.linalg.norm(np.cross(p2 - p1, p1 - p3)) / np.linalg.norm(p2 - p1)


def npa(x: list):
    return [np.array([x[0], x[1]]), np.array([x[2], x[3]])]


previous = [
    [0, 63, 893, 63],
    [0, 62, 893, 62],
    [0, 66, 893, 66],
    [0, 65, 893, 65],
    [27, 61, 881, 61],
    [0, 64, 893, 64],
    [0, 67, 893, 67],
    [464, 68, 893, 68],
]

now = [
    [0, 204, 893, 204],
    [0, 203, 893, 203],
    [0, 202, 893, 202],
    [0, 205, 893, 205],
    [0, 206, 893, 206],
    [65, 201, 893, 201],
    [188, 200, 893, 200],
    [0, 207, 893, 207],
    [0, 208, 452, 208],
]

end = [
    [  0, 392, 893, 392],
[  0 ,391, 893, 391],
[ 63, 388, 893, 388],
[  0 ,389, 893 ,389],
[  0 ,390, 893 ,390],
[164 ,387, 893 ,387],
[  0 ,393, 888 ,393],
[343, 386, 893 ,386],
[  0 ,394, 818 ,394]
]

cnt = 0
sum = 0

for p1 in now:
    for p2 in previous:
        cnt += 2
        sum += point_to_line(npa(p1)[0],npa(p1)[1], npa(p2)[0])
        sum += point_to_line(npa(p1)[0],npa(p1)[1], npa(p2)[1])


# 5 cm
sum = sum / cnt

num = 0
cnt = 0
for p1 in end:
    for p2 in now:
        cnt += 2
        num += point_to_line(npa(p1)[0],npa(p1)[1], npa(p2)[0])
        num += point_to_line(npa(p1)[0],npa(p1)[1], npa(p2)[1])

num = num / cnt

print(num / sum * 5, "cm")
