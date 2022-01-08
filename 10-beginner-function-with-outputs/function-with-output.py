# Functions with names

def format_name(fname, l_name):
   if f_name == "" or l_name == "":
      return "You didn't provide valid inputs."
   formatted_f_name = f_name.title()
   formatted_l_name = l_name.title()

   return(f"Result: {formatted_f_name} {formated_l_name}")
   
  
  formatted_string = format_name("MARTIN", "littlecott")
  print(formatted_string)
  
