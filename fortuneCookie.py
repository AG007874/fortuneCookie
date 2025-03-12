import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,4)

fortune_text =''

if fortune_number == 1:
  fortune_text = 'You will have a great day!'

if fortune_number == 2:
  fortune_text = 'Today will be tough...but worth it.'

if fortune_number == 3:
  fortune_text = 'You will get marrried this year!'
  
if fortune_number == 4:
  fortune_text = 'You will get your dream job!"

print(f'{fortune_text} Your lucky number is:',lucky_number)
