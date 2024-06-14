'''write a code such that filtered_list has the values of x which are even but should not present in y'''

'''x=[2,4,6,8,10]
filtered_list=[]
y=[3,5,7,9,10,12]
for i in x:
      if(i not in y):
            if(i%2==0):
               filtered_list.append(i)
      else:
           pass       

print(filtered_list) '''

'''------------------------------------or[using inline method]-------------------------------------------'''

x=[2,4,6,8,10]
y=[3,5,7,9,10,12] 
filtered_list=[i for i in x if i not in y and i%2==0]
print(filtered_list)              