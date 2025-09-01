FBlist = list(range(1, 101))

for each in FBlist:
    if each % 5 == 0 and each % 3 == 0:
        print("fizzbuzz")
    elif each % 5 == 0:
        print("buzz")
    elif each % 3 == 0:
        print("fizz")
    else:
        print(FBlist[each])
