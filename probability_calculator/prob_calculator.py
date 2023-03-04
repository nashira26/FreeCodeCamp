import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, val in kwargs.items():
      for _ in range(val):
        self.contents.append(key)

  #function to draw balls out
  def draw(self, count):
    #drawn balls count exceeding available balls
    if count > len(self.contents):
      return self.contents
    else:
      balls = []
      #randomly drawing balls
      for _ in range(count):
        ball = random.choice(self.contents)
        self.contents.remove(ball)
        balls.append(ball)
      return balls
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for _ in range(num_experiments):
    #create a copy of hat
    hat_new = copy.deepcopy(hat)
    drawn_balls = hat_new.draw(num_balls_drawn)
    
    #initiate a var to find if the expected balls are there
    present = False

    #check if the balls are there iterating through each color
    for key, val in expected_balls.items():
      try:
        if drawn_balls.count(key) >= val:
          present = True
        else:
          present = False
          break
      except KeyError:
        present = False
        break
     
    if present:
      M += 1
   
  return M / num_experiments
