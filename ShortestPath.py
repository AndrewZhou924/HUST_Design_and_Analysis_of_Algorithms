import numpy as np
import sys

maxNum = sys.maxsize

def findroad(distant, begin, end, path, map):
    if distant == 0 and begin == end:
        return True, np.delete(path, path.shape[0] - 1)
    if begin == end:
        return False, path
    for i in range(5):
        if i == begin or map[begin, i] == maxNum or i in path:
            continue
        else:
            flag, p = findroad(distant - map[begin, i], i, end, np.append(path, i), map)
            if flag:
                return flag, p
    return False, path


def spfa(map=None, begin=0):
    distant = np.array([maxNum, maxNum, maxNum, maxNum, maxNum])
    distant[begin] = 0
    line = np.array([0, 0, 0, 0, 0])
    line[0] = begin
    len_line = 1
    flag = np.zeros(shape=(5,))
    flag[begin] = 1
    while len_line != 0:
        n = line[len_line - 1]
        flag[n] = 0
        len_line -= 1
        for i in range(5):
            if i == n:
                continue
            elif map[n, i] != maxNum and map[n, i] + distant[n] < distant[i]:
                distant[i] = map[n ,i] + distant[n]
                if flag[i] == 0:
                    line[len_line] = i
                    len_line += 1
                    flag[i] = 1
    return distant


def floyd(map):
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if map[i, k] == maxNum or map[k, j] == maxNum:
                    continue
                if map[i, j] > map[i, k] + map[k, j]:
                    map[i, j] = map[i, k] + map[k, j]
    return map


class SPFA():
    def __init__(self, n):
        self.map = np.array([[0, 6, maxNum, 7, maxNum],
                             [maxNum, 0, 5, 8, -4],
                             [maxNum, -2, 0, maxNum, maxNum],
                             [maxNum, maxNum, -3, 0, 9],
                             [2, maxNum, 7, maxNum, 0]])
        self.dicts = {0:"s", 1:"t", 2:"x", 3:"y", 4:"z"}
        for i in range(n):
            self.distant = spfa(self.map, i)
            print(self.distant)
            print(self.dicts.get(i) + "点为起点的最短路路径：")
            for j in range(5):
                if j == i:
                    continue
                _, path = findroad(self.distant[j], i, j, np.array([]), self.map)
                str = self.dicts.get(i) + " -> "
                for k in path:
                    str += self.dicts.get(k) + " -> "
                str += self.dicts.get(j)
                print(str)
        print("\n")




class Floyd():
    def __init__(self):
        self.map = np.array([[0, 3, 8, maxNum, -4],
                             [maxNum, 0, maxNum, 100, 7],
                             [maxNum, 4, 0, maxNum, maxNum],
                             [2, maxNum, -5, 0, maxNum],
                             [maxNum, maxNum, maxNum, 6, 0]])
        for i in range(5):
            self.distant = spfa(self.map, i)
            print(self.distant)
            print(str(i) + "点为起点的最短路路径：")
            for j in range(5):
                if j == i:
                    continue
                if self.distant[j] == maxNum:
                    print("没有从%d到%d这条路"%(i, j))
                _, path = findroad(self.distant[j], i, j, np.array([]), self.map)
                string = str(i) + " -> "
                for k in path:
                    string += str(int(k)) + " -> "
                string += str(j)
                print(string)
            print("")


if __name__ == "__main__":
    OnePoint = SPFA(1)

    AllPoint = Floyd()
