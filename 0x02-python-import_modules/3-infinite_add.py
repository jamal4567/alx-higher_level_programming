#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv)-1
    if counter == 0:
        print(0)
    else:
        r = 0
        for i in range(counter):
            r += int(sys.argv[i+1])
        print("{}".format(r))
