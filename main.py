# Author: Aleks Gondek alg6177@psu.edu
# Collaborator: Yash Raj yqr5113@psu.edu
# Collaborator: Logan Sund lms7078@psu.edu
# Collaborator: Kyle MacLeay kfm5670@psu.edu
# Section: 12R
# Breakout: 5

def getLetterGrade(grade):
  if (grade >= 93.0):
    return("Your letter grade for CMPSC 131 is A.")
  elif (grade >= 90.0):
    return("Your letter grade for CMPSC 131 is A-.")
  elif (grade >= 87.0):
    return("Your letter grade for CMPSC 131 is B+.")
  elif (grade >= 83.0):
    return("Your letter grade for CMPSC 131 is B.")
  elif (grade >= 80.0):
    return("Your letter grade for CMPSC 131 is B-.")
  elif (grade >= 77.0):
    return("Your letter grade for CMPSC 131 is C+.")
  elif (grade >= 70.0):
    return("Your letter grade for CMPSC 131 is C.")
  elif (grade >= 60.0):
    return("Your letter grade for CMPSC 131 is D.")
  else:
    return("Your letter grade for CMPSC 131 is F.")
  return 0

def run():
  gvar = float(input("Enter your CMPSC 131 grade: "))
  print(getLetterGrade(gvar))

if __name__ == "__main__":
  run()