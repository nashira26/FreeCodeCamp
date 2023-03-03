class Category:
  def __init__(self, name, ledger =[]):
    self.ledger = []
    self.name = name
    self.funds = 0
    
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def check_funds(self, amount):
    for i in self.ledger:
      self.funds += i["amount"]
    if self.funds > amount:
      return True
    return False

  def withdraw(self, amount, description =""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
  
  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i["amount"]
    return balance

  def transfer(self, amount, budget_new):
    if self.withdraw(amount, description = f"Transfer to {budget_new.name}"):
      budget_new.deposit(amount, description = f"Transfer from {self.name}")
      return True
    return False

  def __str__(self):
    s = self.name.center(30, "*") + "\n"
    for i in self.ledger:
      desc = i["description"][:23]
      s = s + desc + f'{i["amount"]:.2f}'.rjust(30-len(desc), " ") + "\n"
    s += f"Total: {self.get_balance()}"
    return s

def create_spend_chart(categories):
  #adding the spent money of each categories to a dictionary
  balances = dict()
  for i in categories:
    balances[i.name] = 0
    for j in i.ledger:
      if j["amount"] < 0:
        balances[i.name] += abs(j["amount"])
  total = sum(list(balances.values()))

  #getting the percentage spent by each category
  for key, val in balances.items():
     balances[key] = int((val / total) * 100)

  #initiating output
  output = "Percentage spent by category"

  #adding the y axis(percentage column)
  for i in range(100, -1 ,-10):
    output += ("\n" + str(i).rjust(3, " ") + "| ")
    #adding the plot data
    for key, val in balances.items():
      if val >= i:
        output += "o  "
      else:
        output += "   "
        
  #the horizontal line  
  output += ("\n" + (" "*4) + ("-" * ( len(balances)*3+1) ))  
  l = max(list(len(i.name) for i in categories))

  #adding x axis(categories)
  for i in range(l):
    output += ("\n" + " "*5)
    for key in balances:
      try:
        output += f"{key[i]}  "
      except IndexError:
        output += "   "
        
  return output