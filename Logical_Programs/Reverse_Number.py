orgNum = 123
rev = 0      #321
while orgNum>0:    #0>0
   rem=orgNum%10       #1%10=1            #get last digit
   rev=rev*10+rem      #320 + 1=321                   #Append last digit to rev num
   orgNum =orgNum//10     #1//10=0            #remove last digit
print(rev)




num = 1997
rev = 0
while num>0:
    rem = num%10  # get last digit
    rev = rev*10+rem
    num = num//10
print(rev)