from mean_var_std import calculate

# Test valid input
print(calculate([0,1,2,3,4,5,6,7,8]))

# Test invalid input
try:
    print(calculate([1,2,3]))
except ValueError as e:
    print(e)
