import random

avail_choice = ["stone","paper","scissor"]

class Win_loss:
  pc_score = 0
  end_usr_score = 0
  @classmethod
  def stone_choosed(self):
    if pc_choice == "stone":
      print("match draw")
      print(f"your score : {self.end_usr_score}")
      print(f"pc score : {self.pc_score}")
    elif pc_choice == "paper":
      print("you loose:")
      self.end_usr_score= self.end_usr_score - 1
      print(f"your score : {self.end_usr_score}")
      self.pc_score = self.pc_score + 1
      print(f"pc score : {self.pc_score}")
    elif pc_choice == "scissor":
      print("you win")
      self.end_usr_score= self.end_usr_score + 1
      print(f"your score : {self.end_usr_score}")
      self.pc_score = self.pc_score
      print(f"pc score : {self.pc_score}")
  
  @classmethod
  def paper_choosed(self):
    if pc_choice == "stone":
      print("match win")
      self.end_usr_score= self.end_usr_score + 1
      print(f"your score : {self.end_usr_score}")
      print(f"pc score : {self.pc_score}")
    elif pc_choice == "paper":
      print("match draw")
      print(f"your score : {self.end_usr_score}")
      print(f"pc score : {self.pc_score}")
    elif pc_choice == "scissor":
      print("you loose")
      print(f"your score : {self.end_usr_score}")
      self.pc_score = self.pc_score + 1
      print(f"pc score : {self.pc_score}")  
  @classmethod
  def scissor_choosed(self):
    if pc_choice == "stone":
      print("you loose")
      print(f"your score : {self.end_usr_score}")
      self.pc_score = self.pc_score + 1
      print(f"pc score : {self.pc_score}")  
    elif pc_choice == "paper":
      print("match win")
      self.end_usr_score= self.end_usr_score + 1
      print(f"your score : {self.end_usr_score}")
      print(f"pc score : {self.pc_score}")
    elif pc_choice == "scissor":
      print("match draw")
      print(f"your score : {self.end_usr_score}")
      print(f"pc score : {self.pc_score}")

# finally calling all class functions..

print("stone = paper = scissor")
print("Enter St for stone\nEnter p for paper\nEnter s for scissor\n")

while True:
  ran_no = random.randint(0,2)
  pc_choice = str(avail_choice[ran_no])
  usr_inp = str(input("Enter your choice..!\n"))
  if usr_inp == "st":
    Win_loss.stone_choosed()
  elif usr_inp == "p":
    Win_loss.paper_choosed()
  elif usr_inp == "s":
    Win_loss.scissor_choosed()
  elif usr_inp == "e":
    break

print(f"your final score is {Win_loss.end_usr_score}")
print(f"the PC final score is {Win_loss.pc_score}")
if Win_loss.end_usr_score > Win_loss.pc_score:
  print("you win..!")
elif Win_loss.end_usr_score == Win_loss.pc_score:
  print("the match ended in a draw")
else:
  print("you loose..!") 