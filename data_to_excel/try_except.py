import os
def open_data(f_name):
    try:
        with open(f_name) as file:
            return file.readlines()
    except:
        print('ewihwbfiew')
        exit()
def msum(lines):
    summ = 0
    print(lines)
    for i in lines:
        try:
            el = int(i.strip())
            summ += el
        except Exception:
            pass
    return summ
def main():
    fname = 't.cpp'
    data = open_data(fname)
    print(msum(data))

main()
