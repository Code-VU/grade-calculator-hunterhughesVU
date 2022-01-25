def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try:
        score = float(input("Enter score:"))

        if(score >= 0.9 and score <= 1.0):
            grade = 'A'
        elif(score >= 0.8 and score < 9.0):
            grade = 'B'
        elif(score >= 0.7 and score < 8.0):
            grade = 'C'
        elif(score >= 0.6 and score < 7.0):
            grade = 'D'
        elif(score < 0.6 and score >= 0.0):
            grade = 'F'
        else:
            grade = "Score is out of range! (0.0 - 1.0)"

    except: grade = 'Invalid input!'

    
    print(grade)
        


    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateGrade()