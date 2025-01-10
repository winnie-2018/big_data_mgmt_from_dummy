import sys
for line in sys.stdin:
    fields = line.strip().split(',')
    print('salary', '\t', fields[-1])
    
'''
Run in terminal: 
    - python mapper.py < employees.csv | python reducer.py
'''