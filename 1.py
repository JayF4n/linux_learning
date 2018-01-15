#!/usr/bin/env python3


class Config(object):
    def __init__(self,configfile):
        self.configfile = configfile
    def get_config(self):
        with open(self.configfile) as configraw:
            self._configDetail = {}
            for arg in configraw:
                configlist = arg.split(' = ')
                self._configDetail[configlist[0]] = float(configlist[1])
        configdict = {}
        configdict['JiShuH'] = self._configDetail['JiShuH']
        configdict['JiShuL'] = self._configDetail['JiShuL']
        configdict['FeiLv'] = self._configDetail['YangLao'] + self._configDetail['YiLiao'] + self._configDetail['ShiYe'] +self._configDetail['GongShang'] + self._configDetail['ShengYu'] + self._configDetail['GongJiJin']
        self.configdict = configdict
        return configdict

class UserData(object):
    def __init__(self,usrdatafile):
        self.usrdatafile = usrdatafile
    def get_usrdata(self):
        JiShuH = Config(configfile).get_config()['JiShuH']
        JiShuL = Config(configfile).get_config()['JiShuL']
        FeiLv = Config(configfile).get_config()['FeiLv']
        with open(self.usrdatafile) as usrdataraw:
            for arg in usrdataraw:
                salarylist = arg.split(',')
                staffNo = int(salarylist[0])
                salary  = int(salarylist[1])
                if  salary <= JiShuL :
                    insurance = JiShuL * FeiLv
                elif JiShuL < salary < JiShuH:
                    insurance = salary * FeiLv
                else:
                    insurance = JiShuH *FeiLv
                tax = salary - insurance - 3500
                if tax <= 0:
                        tax_to_pay = 0
                elif tax >0 and tax <= 1500:
                        tax_to_pay = tax * 0.03
                elif tax > 1500 and tax <= 4500:
                    tax_to_pay = tax * 0.10 -105
                elif tax > 4500 and tax <= 9000:
                    tax_to_pay = tax * 0.20 - 555
                elif tax > 9000 and tax <= 35000:
                    tax_to_pay = tax * 0.25 -1005
                elif tax > 35000 and tax <= 55000:
                    tax_to_pay = tax * 0.30 - 2755
                elif tax > 55000 and tax <= 80000:
                    tax_to_pay = tax * 0.35 - 5505
                else:
                    tax_to_pay = tax *0.45 -13505
                salaryFinal = salary - insurance - tax_to_pay

                infolist =[str(staffNo),str(salary),'%.2f' % insurance,'%.2f' % tax_to_pay,'%.2f' % salaryFinal]
                self.infolist = infolist
                self.outputfile = outputfile
                with open(self.outputfile,'a') as file:
                    file.write(self.infolist[0])
                    file.write(",")
                    file.write(self.infolist[1])
                    file.write(",")
                    file.write(self.infolist[2])
                    file.write(",")
                    file.write(self.infolist[3])
                    file.write(",")
                    file.write(self.infolist[4])
                    file.write("\n")
        

if __name__ == '__main__':
    import sys
    try:
        args = sys.argv[1:]
        configfile = args[(args.index('-c'))+1]
        usrdatafile = args[(args.index('-d'))+1]
        outputfile =  args[(args.index('-o'))+1]
        UserData(usrdatafile).get_usrdata()
    except :
        print("File_Path Error or File_Format Error")
        exit()