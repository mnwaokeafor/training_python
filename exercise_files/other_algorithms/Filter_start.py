def main():
  chores = int(input("Enter number of chores done in a month: "))
  if chores == 0:
    print("You earned 0 cookies.")
  elif chores == 2:
    print("You earned 5 cookies.")
  elif chores == 4:
    print("You earned 15 cookies.")
  elif chores == 6:
    print("You earned 30 cookies.")
  elif chores >= 8:
    print("You earned 50 cookies.")
  else:
    print("Invalid number of chores.")
    
main()
