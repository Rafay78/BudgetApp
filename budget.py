class Category:
  
  def __init__(self,Category):
    self.category = Category
    self.ledger = []

  def deposit(self, amount, description=""):
    item = {"description": description, "amount": amount}
    self.ledger.append(item)

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else: 
      return False
  
  def withdraw(self, amount, description=""):
      if self.check_funds(amount):
        item = {"description": description, "amount": -(amount),}
        self.ledger.append(item)
        return True
      else:
          return False
  
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to "+category.category)
      category.deposit(amount, "Transfer from "+ self.category)
      return True
    else:
      return False

  def get_balance(self):
    total = 0  
    for i in self.ledger:
        for key, value in i.items():
            if key == "amount":
                total += value
    return total 
  
  def get_withdraw_bal(self):
    withdrawals = 0
    for i in self.ledger:
        for key, value in i.items():
            if key == "amount":
                if value < 0:
                    withdrawals += value
    return withdrawals   
  
  def __str__(self):
      final= ""
      strg = self.category
      strg = strg.center(30, '*')
      final += strg + "\n"
      for i in self.ledger:
        for key, value in i.items():
          if key == "description":
              if len(value) > 23:
                  value = value[:23]
              strg = value.ljust(23, ' ')
              final += strg
          elif key == "amount":
              final = final[0:-1] if (value < 0 and len(str(format(float(value), '.2f'))) >                 7) or len(str(format(float(value), '.2f'))) > 7 else final
              strg = str(format(float(value),'.2f')).rjust(7," ") + "\n"
              final += strg
      final += "Total: "    
      strg = str(format(self.get_balance(),'.2f'))  
      final += strg
      return final
    
def create_spend_chart(categories):
    # Calculate the total withdrawal amount for all categories
    total_withdrawals = sum(category.get_withdraw_bal() for category in categories)

    # Calculate the percentage spent in each category
    percentages = [category.get_withdraw_bal() / total_withdrawals * 100 for category in categories]
    # Round the percentage spent down to the nearest 10
    heights = [int(percentage // 10 * 10) for percentage in percentages]
    # Find the maximum bar height
    max_height = max(heights)

    # Create the chart title
    chart = "Percentage spent by category\n"

    # Create the bar chart
    for i in range(100, -10, -10):
        # Create the labels on the left side of the chart
        chart += "%3d|" % i

        # Add a bar for each category
        for height in heights:
            if height >= i:
                chart += " o "
            else:
                chart += "   "
      
        chart += " \n"

    # Add the horizontal line below the bars
    chart += "    " + "-" * ((len(categories) * 3) + 1) + "\n"

    # array = ["Food","Clothing","Auto"]

    # Find the maximum number of elements in any inner array
    max_elements = max(len(category.category) for category in categories)
    
    # Iterate over the elements in each inner array
    for i in range(max_elements):
        chart += "    "
        for category in categories:
            if i < len(category.category):
                # Print the element if it exists
                chart += " "+category.category[i]+" "
                # print(i)
            else:
                # Print a blank space if the element does not exist
                chart+="   "
        chart += " \n"
    chart = chart[:-1]    

    return chart