#
#
#


#---Password Checker---#
password = input("type your password: ")
score = 0

#--Check the password for specific characters--
lowercase = False
uppercase = False
number = False
punctuation = False
#--check the password for specific charcters--
for charcter in password: 
    if charcter in 'abcdefghijklmnopqrstuvwxyz':
        lowercase = True 
    elif charcter in 'ABCDEFGHIJKLNOPQRSTUVWXYZ':
        uppercase = True
    elif charcter in '0123456789':
        number = True 
    else: 
        punctuation = True 
#--if password passes print text--
if lowercase == True:
    print('Your password contains at least one lowercase character.')
if uppercase == True: 
   print(' Your password contains at least one uppercase character.')
if number == True: 
   print(' Your password contains at least one number character.')
if punctuation == True: 
   print(' Your password contains at least one punctuation.')


#--If password passes add score--
if lowercase == True and uppercase == True: 
    score = score + 10

if number == True and (lowercase== True or uppercase==True): 
    score += 10

if punctuation == True:
    score += 5

if len(password) >= 8: 
    score += 5
    print('Your password is atleast 8 characters long.')



#--Show score--
print(f'\nScore: {str(score)}')