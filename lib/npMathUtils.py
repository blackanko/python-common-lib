# coding:utf-8
import numpy as np


def vectorRotate(pointVector, deg):
    rad = -np.deg2rad(deg)
    matrix = np.array([[np.cos(rad), -np.sin(rad)],[np.sin(rad), np.cos(rad)]])
    result = np.dot(matrix, np.array(pointVector))
    return [round(result[0], 3), round(result[1], 3)]


class RandomMachine():

    def __init__(self):
        self.refreshFlag = True
        self.ret = None

    def _formatFloat(self, strList):
        return map(lambda x: float(x), strList)


    def new(self, l, p, num):
        self.reset()
        return self.random(l, p, num)

    def random(self, l, p, num):
        if self.refreshFlag:
            plist = np.array(self._formatFloat(p))
            plist /= plist.sum()
            self.ret = np.random.choice(l, num, p=plist, replace=False)
            self.refreshFlag = False

        return self.ret

    def reset(self):
        self.refreshFlag = True

    def lock(self):
        self.refreshFlag = False
