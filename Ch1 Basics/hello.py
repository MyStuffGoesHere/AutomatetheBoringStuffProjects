# This Program Says Hello And Asks for your name.

print('Hello!')
print('What is your name?') # Asks for name

myName = input() # Takes input from user to get Name
print('It is good to meet you!, ' + myName)
print('The length of your name is:')
print(len(myName)) # Tells the length of the name given

print('what is your age?')
myAge = input()
print('you will be '+ str(int(myAge) + 2) + ' in 2 years!')
