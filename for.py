
import math

# x = float(input("insert your var"))
talaii = (1+math.sqrt(5))/2
radical5 = math.sqrt(5)

for x in range(100):
    f = (float(talaii**x)-float((1-talaii)**x))/radical5
    print(f)