#!/usr/bin/env python3

import sys
try:
    tax = int(sys.argv[1]) - 3500
except ValueError:
    print("Parameter Error")
    exit()

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

print(format(tax_to_pay,".2f"))

