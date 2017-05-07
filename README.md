# python_learning

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for x in range(1,10):
    for y in range(1,x+1):
        # print(x, 'X',y,'=',x*y)
        print('%dx%d=%2s\t'%(x,y,x*y),end=' ')
    print()
