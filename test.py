#!/usr/bin/env python3

import sys


args = sys.argv[1:]

userdataargs = args.index('-d')
userdatafile = args[userdataargs+1]

outputargs = args.index('-o')
outputfile = args[outputargs+1]


class Config(object):
    def __init__(self,configfile):
        configfile = args[(args.index('-c'))+1]
        with (open(configfile).split(' = ')) as configraw:
            for (a,b) in configraw:
                self._config = {a,b}
    




if __name__ == '__main__':
    if len(sys.argv) == 6:
        pass
    else:
        print("Parameter Error")
        print(sys.argv[0], "-c configfile -d usrfile -o outputfile")
        sys.exit(-1)
    sys.exit(0)

salary,'%.2f' % insurance,'%.2f' % tax_to_pay,'%.2f'% salaryFinal