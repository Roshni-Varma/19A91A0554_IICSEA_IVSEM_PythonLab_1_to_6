# Implement a python script add.py that takes 2 numbers as command line arguments and perform arithmetic operations on them.
import sys 
a=int(input(sys.argv[1]))#sys.argv-It returns a list of command line arguments passed to a python script
b=int(input(sys.argv[2]))
c=a+b 
print('sum is: ',c)

"""output:
          2
          3
          sum is:  5"""


'''Implement a python script add.py that takes 2 numbers as command line arguments
and perform arithmetic operations on them.(using putty)'''
import sys as s
print(int(s.argv[1])+int(s.argv[2]))

OUTPUT:
 [19A91A0554@Linux ~]$ vi cmd.py
[19A91A0554@Linux ~]$ python3 cmd.py 2 3
5
