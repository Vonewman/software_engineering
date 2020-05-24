from nearest import nearest_square

nearest_5 = nearest_square(5)
print("Nearest square <= 5: returned {}, correct answer is 4.".format(nearest_5))
assert(nearest_5 == 4)

nearest_n12 = nearest_square(-12)
print("Nearest square <= -12: returned {}, correct answer is 0".format(nearest_n12))
assert(nearest_n12 == 0)

nearest_9 = nearest_square(9)
print("Nearest square <= 9: returned {}, correct answer is 9".format(nearest_square(9)))
assert(nearest_9 == 9)

nearest_23 = nearest_square(23)
print("Nearest square <= 23: returned {}, correct answer is 16.".format(nearest_23))
assert(nearest_23 == 16)