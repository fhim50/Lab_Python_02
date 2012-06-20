#Q5


theInput = input("Enter an integer: ")
#Your code here
 #int(theInput)

if theInput%2==0:
    print 'even'
else:
    print 'odd'
   
print '----------------------------------------------------'

#Q6

primarySchoolAge= 4
legalVotingAge =18
agePresident = 40
officialRetirementAge= 60
personAge= input('Enter your Age:  ')

if personAge < 4:
    print ('Too young')
elif personAge > 17:
    print 'Remember to vote'

    if personAge>= 40 :
        if personAge>60:
            print "You can't b president"
            print "Too old"
        else:
            print 'vote for me'

#else:
#print'Too old'


print '------------------------------------------------------'
#Q7


i=40
while i>0:
    i-=1
    
    if i%3== 0:
         print i 

print '---------------------------------------------------------'
# Q8

for i in range(7,30):
    if i%2!=0 and i%3!=0 and i%5!=0:
        print i
        
print '---------------------------------------------------------'

# Q9
n= 1
while n>0:
    n+=1
    if 79*n%97==1:
        print n
        if n%2==0:
            break


        
        
        

    
