#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
import time

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def progr():
    pole = []
    for i in xrange(8):
        pole.append([1,2,3,4,5,6,7,8])
    recursia(pole)
    return 0

def n_eq_one(pole, v):
    def dlt(a, b):
        try:
            print "Удаляется элемент {0} из {1}".format(b, a)
            if b in a: a.remove(b)
        except ValueError:
            print "Не удалось удалить элемент {0} из {1}".format(b, a)

    rezerv = pole
    v -= 1
    if len(pole[v])>0:
        h = pole[v][0]
        print "Вертикаль № {0}, ячейка № {1}".format(v + 1, h)
        s = v + 1
        if s < 9:
            pl = h + v
            mi = h - v
            while s < 8:
                k = pl - s; dlt(pole[s], k)
                k = h;      dlt(pole[s], k)
                k = mi + s; dlt(pole[s], k)
                s += 1
                
        print "После удаления элементов массив выглядит так:"
        for i in pole:
            print i
        print
        result = -1 # Таблица заполнена. Можно печатать
        if v + 1 < 9: result = len(pole[v + 1])
        if not result: pole = rezerv
    else: result = 0
    return result

def prn(x):
    print x
    
def recursia(pole, n = 1, v = 1):
    print "Подпрограмма recursia. n = {0}, v = {1}".format(n, v)
    if n == 1:
        z = n_eq_one(pole,v)

    if z > 0: recursia(pole, 1 , v + 1)
    if z == -1: prn(pole)
    sys.exit(0)
    #recursia(pole)
    return 1

def other_variant(pole):
    for i in xrange(len(pole)):
        s = pole[i]
    


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        progr()
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
