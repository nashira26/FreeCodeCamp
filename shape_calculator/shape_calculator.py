class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  #setter function for width
  def set_width(self, width):
    if width > 0:
      self.width = width
    else:
      raise ValueError

  #setter function for height
  def set_height(self, height):
    if height > 0:
      self.height = height
    else:
      raise ValueError

  #get area of shape
  def get_area(self):
    return (self.width * self.height)

  #get perimeter of shape
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  #get diagonal of shape
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  #get picture
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      return ("*"*self.width + "\n") * self.height
      
  #string rep of the object
  def __str__(self):
      return f"Rectangle(width={self.width}, height={self.height})"

  #get no.of shapes can be fit inside the given shape
  def get_amount_inside(self, shape):
    return int(self.width / shape.width) * int(self.height / shape.height)
    
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    self.width = side
    self.height= side
  
  def set_width(self, side):
    self.width = side

  def set_height(self, side):
    self.height = side

  #setter function for side
  def set_side(self, side):
    if side < 0:
      raise ValueError
    else:
      self.set_width(side)
      self.set_height(side)

  #string rep of the object
  def __str__(self):
      return f"Square(side={self.width})"
  
