import math


def dot_product(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    """
    Returns the dot product (scalar product) of two vectors.

    Args:
    a, b: tuple of 3 float numbers representing the vectors a and b.
    """
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def vector_norm(a: tuple[float, float, float]) -> float:
    """
    Returns norm or module of a vector a.

    Args:
    a: tuple of 3 float numbers representing the vector a.
    """
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)


def vector_angle(a: tuple[float, float, float], b: tuple[float, float, float]):
    """
    Returns the angle in degrees of two vectors a and b.

    Args:
    a, b: vectors represented by a tuple of 3 float numbers.
    """
    angle_rad = math.acos((dot_product(a, b)) / (vector_norm(a)*vector_norm(b)))
    return math.degrees(angle_rad)


# vectors
a = (0, 255, 0)
b = (255, 0, 0)

# 1) dot product
res_dot_product = dot_product(a, b)

# 2) vector norm
res_norm = vector_norm(a)

# 3) angle between vectors a and b
res_angle = vector_angle(a, b)

print(f"Vector a: {a}, vector b: {b}:\n")
print(f"The dot product of a, b is: {res_dot_product}")
print(f"The norm of a is: {res_norm}")
print(f"The angle between the vectors a and b is: {res_angle}°")
