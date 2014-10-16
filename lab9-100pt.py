############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.



print 'What is your tempurature?'
userInput = int(raw_input())
print 'Have you been sick lately?'
userInput2 = raw_input()
print 'Have you been to Africa Lately?'
userInput3 = raw_input()
    
if userInput >= 105:
    print 'Go to the hospital'
else:
        if userInput2 == "yes" and userInput >= 102:
            print 'Go to the hospital'
        else:
            if (userInput > 105 or userInput2 == 'yes') and userInput3 == 'yes':
                print "Your fine go home'