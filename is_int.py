def is_int():
    while True:
      try:
         enter_val = int(input("Enter Value: "))       
      except ValueError:
         continue
      else:
         return enter_val




