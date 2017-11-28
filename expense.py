##################################################################
# Monthly Expense Calculator
#
##################################################################
#!/usr/bin/python
import argparse
import re 

# Argument parser
parser = argparse.ArgumentParser()

parser.add_argument('-F', action='store', dest='file_name',
                    help='filename')

f_name = parser.parse_args()
fname = f_name.file_name

class monthlyExpense():
    def __init__(self, fname):
        file=open('%s' %(fname), 'r')
        data=file.readlines()
        file.close()
        data=str(data)
        amt=re.findall(r'\-*[\d.-]+,?[\d.-]+', data)
        amt = [word.replace(',','') for word in amt]
        total=[]
        for i in amt:
            m = re.search("-.*?[\d.-]+" , i)
            if m:
                 total.extend([m.group(0)])
        total = [word.replace('-','') for word in total]
        total = [word.replace('112017','0') for word in total]
        print total
        total_amount_spent=sum(float(i) for i in total)
        print "Total amount spent this month = %s" %(total_amount_spent)
        
obj=monthlyExpense(fname)
