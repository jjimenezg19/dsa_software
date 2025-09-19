
##### Big O: O(n)     Proportional
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

#### Big O: Drop Constants
# 0(2n) se puede simplificar como 0(n)
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)


###### Big O: O(n^2)     Loop within a loop
# O(n^2 + n) se puede simplificar como O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

#### Big O: Drop Non_dominants
#
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

print_items(10)

#### Big O: O(1) The most efficient BigO     Constant
def add_items(n):
    return n + n + n


## Big O: O(log n)    Divide and conquer
### 2^3 = 8 --> log 2^8 = 3


### Big O: Different Terms to Inputs
# O(a) + O(b) = O(a + b)
def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# O(a) * O(b) = O(a * b)
def print_items(a, b):
    for i in range(a):
        print(i)
        for j in range(b):
            print(j)


### Big O: List
# adding or removing at the end is always = O(1)
# adding or removing at the beginning is always = O(n)
my_list = [11, 3, 23, 7, 13]
my_list.append(17)
my_list.pop(0)
my_list.insert(0, 11)


#### Big O: Wrap Up
