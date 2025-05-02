# 1. Construck questions
# 2. Put them in listing
# 3. Set the Answers
# 4. Re-arrange
score = 0
name = input("What is you name?")

#This is my list of questions
questions_list = [" Q1. What is the name of the youngest sibling of the four?",\
"Q2. What year does this movie come out?",\
"Q3. What is the author\'s name who made the books based on this movie?",\
"Q4. Reepicheep the character is a horse?",\
"Q5. What religion is this movie based on?",\
"Q6. Where do the Pevensie Children magically teleport from to go to narnia?",\
"Q7. The character Aslan is a lion?",\
"Q8. What island was it filmed in (north or south)?",\
"Q9. What is the name of the cove in NZ where they teleport to?",\
"Q10. What evil character returns?"]


print("Welcome to my quiz {}, this quiz is about the movie," .format(name))
print ("The Chronicles of Narnia, Prince Caspian")
print ("All of your answers will be A, B, C or D")
print("Lets get started!") 


#Q1

#this prints the first question on list above.
print(questions_list[0])
#possable answers
print("  A. Peter B. Susan C. Edmund D. Lucy")
#Where you make your guess
Q1_answer = input("Your answer- \n")

#Answer replys

if Q1_answer == "d":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))

#and continues through the code

#Q2


print(questions_list[1])
print("  A.2008  B.2007  C.2009  D.2010 ")
Q2_answer = input ("Your answer-  \n")

# Answer

if Q2_answer == "a":
    print("Correct 10 points!")
    score += 10
else:
    print("Sorry that is wrong no points!")
    score += 0

print("Your score is now: {} points \n".format(score))

#Q3

print(questions_list[2])
print("  A. C.S Lewis  B. Clive Staples Lewis ")
Q3_answer = input ("Your answer-  \n")

# Answer

if Q3_answer == "A":
    print("Trick question it is both!")
    score += 10
    
else:
    print("Trick question it is both!")
    score += 10
    
print("Your score is now: {} points".format(score))

#Q4

print(questions_list[3])
print("  A. True  B. False")
Q4_answer = input("Your answer- \n")

#Answer

if Q4_answer == "b":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))


#Q5

print(questions_list[4])
print("  A. Judaism  B. Islam  C. Christianity")
Q5_answer = input("Your answer- \n")

#Answer

if Q5_answer == "c":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))


#Q6
print(questions_list[5])
print("  A. Beach  B. Shop  C. Bedroom  D. Train Station")
Q6_answer = input("Your answer- \n")

#Answer

if Q6_answer == "d":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))

#Q7

print(questions_list[6])
print("  A. True  B. False")
Q7_answer = input("Your answer- \n")

#Answer

if Q7_answer == "a":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))

#Q8

print(questions_list[7])
print("  A. North  B. South")
Q8_answer = input("Your answer- \n")

#Answer

if Q8_answer == "a":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))

#Q9

print(questions_list[8])
print("  A. Coverton  B. Akarua  C. Cathedral")
Q9_answer = input("Your answer- \n")

#Answer

if Q9_answer == "c":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
print("Your score is now: {} points\n".format(score))

#Q10

print(questions_list[9])
print("  A. Caspian  B. Sea Witch  C. Lava Witch D. Ice Witch")
Q10_answer = input("Your answer- \n")

#Answer

if Q10_answer == "d":
 print ("Correct 10 points!")
 score += 10
else:
 print("Sorry that is wrong no points!")
 score += 0
 
 
#Ending
  
print("\n")
print("Well done!")
print("Your final score is: {} points\n".format(score))
print("Thank you for playing")
