import random

print("hello world!")
def mad(x):
    if x>=0.7:
        return "x｛｝ is big".format(x)
    else:
        return "x｛｝ is small".format(x)

if __name__ == '__main__':
    print(mad(random.random())
