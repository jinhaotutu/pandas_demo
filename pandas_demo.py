import pandas as pd
import numpy as np
import csv


def main():
    filename = open("test.csv", encoding="gbk")
    data = pd.read_csv(filename)
    print(data)


def pandas_start():
    data2 = pd.read_csv("test.csv", encoding="gbk")
    print(data2)
    #X = data2[1]
    #Y = data2[1]
    #print(X, Y)

if __name__ == '__main__':
    print("start pandas demo")
    main()
    pandas_start()

    while True:
        pass
