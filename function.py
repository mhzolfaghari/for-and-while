from math import sqrt

talaii = (1+sqrt(5))/2
radical5 = sqrt(5)
def fibunacci (x):
    f = (float(talaii**x)-float((1-talaii)**x))/radical5
    return f

print(fibunacci(2))
