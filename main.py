# Author: Aleks Gondek alg6177@psu.edu
# Collaborator: Yash Raj yqr5113@psu.edu
# Collaborator: Logan Sund lms7078@psu.edu
# Collaborator: Kyle MacLeay kfm5670@psu.edu
# Section: 12R
# Breakout: 5

def getLetterGrade(grade):
  if (grade >= 93.0):
    return("A")
  elif (grade >= 90.0):
    return("A-")
  elif (grade >= 87.0):
    return("B+")
  elif (grade >= 83.0):
    return("B")
  elif (grade >= 80.0):
    return("B-")
  elif (grade >= 77.0):
    return("C+")
  elif (grade >= 70.0):
    return("C")
  elif (grade >= 60.0):
    return("D")
  else:
    return("F")
  return

def run():
  gvar = float(input("Enter you CMPSC 131 grade: "))
  print(getLetterGrade(gvar))

if __name__ == "__main__":
  run()