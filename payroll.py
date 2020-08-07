'''
    AUTHOR: VEYSEL BOYBAY
    STUDENT ID: 301115376
    FILE NAME: PAYROLL.PY
    DESCRIPTION: THIS PYTHON FILE READS OUTSOURCE DATA FILE AND PROMPTS IT.
'''

fileObject=open("data.txt","r")
contents=(fileObject.read())
fileObject.close()
newnew=contents.split(',')

#min_hour_salary indicates that workers makes $12 per hour
min_hour_salary=12

print("Emp-Num|-|LastFirst-Name|-|Hours-Worked|-|Description")
print("-----------------------------------------------")
#For loop below displays every worker data line by line
count=0
for i in range(10):
    for j in range(4):
        if count%4==3:
            print(newnew[count],end='')
        else:
            print("-"+newnew[count]+"---",end='')
        
        total_hours=0
        if count%4==3:
            total_hours=int(newnew[count])
            wage=total_hours*min_hour_salary
            print(f"===>{newnew[count-1]} {newnew[count-2]} has worked {newnew[count]} hours and made ${wage} this week.")
        count+=1
    print()


