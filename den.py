'''
Created on 19 Haz 2013

@author: administrator
'''
import os

file = open("text","r")
text = (file.read())
array = text.replace(',',' ').replace(';', ' ').replace('.',' ').replace('!',' ').replace('?',' ').replace('"',' ').replace("'",' ').replace('/',' ').replace('&',' ').replace(':',' ').replace('%',' ').split()
file.close()
writable_file = open("normal","w")
for i in range(0,len(array)):
    writable_file.write(array[i]+"\n")

writable_file = open("normal","r")  
t = writable_file.read()            
writable_file.close()               
writable_file = open("normal","w")  
                                  
while(os.path.getsize('normal') < 2147483648): 
    writable_file.write(t+"\n")              
    print(os.path.getsize('normal'))         

writable_file.close()




#lines = file.readlines()
#file.close()
#print (lines.split(','))
#print(file.name)

