def add_time(start, duration, day = ""):
  #acquiring the time values from inputs
  hr_min, t = start.split()
  [hr, min] =  [int(x) for x in hr_min.split(":")]
  [dur_hr, dur_min] = [int(x) for x in duration.split(":")]

  #finding the minutes portion of the time
  new_min = min + dur_min
  if new_min >= 60:
    new_min -= 60
    hr += 1
    
  #adding hours to the time
  new_hr = hr + dur_hr

  #adding day portion
  new_day = ""


  if new_hr < 12:
    new_t = t
    if day != "":
      new_day = ", " + day
    
  elif new_hr < 24 and t == "AM":
    new_t = "PM"
    if new_hr != 12:
      new_hr -= 12
    if day != "":
      new_day = ", " + day
      
  elif new_hr < 24 and t == "PM":
    new_t = "AM"
    if new_hr != 12:
        new_hr -= 12
    new_day = " (next day)"

  else:
    days = round(new_hr / 24)
    new_hr = new_hr % 24
    
    if new_hr >= 12 and t == "AM":
      if new_hr != 12:
        new_hr -= 12
      new_t = "PM"
    elif new_hr >= 12 and t == "PM":
      if new_hr != 12:
        new_hr -= 12
      new_t = "AM"
    else:
      new_t = t

    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    if day != "":
      id = days_list.index(day.lower())
      if id + days > 6:
        id = ((id+1 + days) % 7) - 1
      else:
        id = id + days
      new_d = days_list[id]
      
      if days == 1:
        new_day =f", {new_d.title()} (next day)"
      else:
        new_day =f", {new_d.title()} ({days} days later)"
        
    elif days == 1:
      new_day =" (next day)"
      
    else:
      new_day =f" ({days} days later)"

  new_time = f"{new_hr}:{new_min:02} {new_t}{new_day}"
  return new_time
