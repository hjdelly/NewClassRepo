def full_name(first, last):      #function called fullname with input arguments first and last
      return f'{first} {last}'   #if you want to pass the fullname around in the app use return NOT PRINT
                                 #when you call full name you aren't just printing to console just returns values


kristine = full_name('Kristine', 'Hudgens')  # stored function in a variable here

def greeting(name):                          # another method named greeting and name is argument
  print(f'Hi {name}!')                       # now print statement and format hi and pass in name


greeting(kristine)   # call the greeting function and pass in Kristine
