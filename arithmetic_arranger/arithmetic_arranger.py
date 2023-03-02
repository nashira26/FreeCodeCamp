def arithmetic_arranger(problems, arg = False):
  first_row = []
  second_row = []
  third_row= []
  fourth_row = []
  
  #error if problems count is more than 5
  if  len(problems) > 5:
    return "Error: Too many problems."
  
  else:
    for problem in problems:
      
      #error if operator is not + or -
      if (problem.split())[1] not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
        break
        
      #error if inputs are not numbers
      elif not ((problem.split())[0].isnumeric() and (problem.split())[2].isnumeric()):
        return "Error: Numbers must only contain digits."
        break
        
      #error if the input numbers are more than 4 digits in length
      elif len((problem.split())[0]) > 4 or len((problem.split())[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
            break
      else:
        n , oper ,m = problem.split() 
        size = 2 + max([len(n), len(m)])
        first_row.append(n.rjust(size, " "))
        second_row.append(oper + m.rjust(size-1, " "))
        third_row.append("-" * size)
        
        if oper == '+':
          fourth_row.append(str(int(n)+int(m)).rjust(size, " "))
        else:
          fourth_row.append(str(int(n)-int(m)).rjust(size, " "))
    #specify the output format according to second argument      
    if arg:
      arranged_problems = "    ".join(first_row) + "\n" + "    ".join(second_row) + "\n"+ "    ".join(third_row) + "\n" + "    ".join(fourth_row)
    else:
      arranged_problems = "    ".join(first_row) + "\n" + "    ".join(second_row) + "\n"+ "    ".join(third_row)
    return arranged_problems