import sys
for line in sys.stdin:
    for word in line.strip().split():
        print(word + '\t' + '1')
   
'''     
run in terminal: 
    - python mapper.py < textA.txt > results.txt
    - python mapper.py < textB.txt >> results.txt
'''