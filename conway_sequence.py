# Your last iavaScript (Node) code is saved below:
# // Using the following pattern..
# 1  -> [1]
# 2  -> [1, 1]
# 3  -> [2, 1]
# 4  -> [1, 2, 1, 1]
# 5  -> [1, 1, 1, 2, 2, 1]
# 6  -> [3, 1, 2, 2, 1, 1]
# 7  -> [1, 3, 1, 1, 2, 2, 2, 1]
# 8  -> [1, 1, 1, 3, 2, 1, 3, 2, 1, 1]
# 9  -> [3, 1, 1, 3, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1]
# 10 -> [1, 3, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 1, 1]
# // []
# //
# // Implement a function called `hearsay` to return the nth row
# //
# // hearsay(2) = [1, 1]
# // hearsay(4) = [1, 2, 1, 1]


def conway(depth):

    last_lvl = [] # Initial empty last lelvel
    for _ in range(depth):
        lvl = [] # Initial current level

        if last_lvl: # Check if there are not prev levels
            count = 1 # Initial count
            N = len(last_lvl) # Get number of items in prev level
            for i in range(N): # for each element in the array
                a = last_lvl[i] # Current value
                if i < N-1: # Check against last value in arr
                    b = last_lvl[i+1] # Next Value
                    if a == b: # Compare current and next value
                        count += 1 # Increment count
                        continue # move to next value
                lvl.append(count)
                lvl.append(a)
                count = 1 # Reset after insertion

        else: # Just insert 1 for first level
            lvl.append(1)

        last_lvl = lvl # Store last just created level

    return last_lvl 


# print(conway(1) == [1])
# print(conway(2) == [1, 1])
# print(conway(3) == [2, 1])
# print(conway(4) == [1, 2, 1, 1])
# print(conway(5) == [1, 1, 1, 2, 2, 1])
# print(conway(6) == [3, 1, 2, 2, 1, 1])
# print(conway(7) == [1, 3, 1, 1, 2, 2, 2, 1])
# print(conway(8) == [1, 1, 1, 3, 2, 1, 3, 2, 1, 1])
# print(conway(9) == [3, 1, 1, 3, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1])
# print(conway(10) == [1, 3, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 1, 1])
print(conway(11))
