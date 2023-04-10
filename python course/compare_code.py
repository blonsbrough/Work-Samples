import re
import random
from timeit import repeat
def get_word():
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def green_glass_door_1():
    word = get_word()
    prev_letter = ''
    for letter in word:
        letter = letter.upper()
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False

def green_glass_door_2():
    word = get_word()
    pattern = re.compile(r'(.)\1')
    return pattern.search(word)

timepass1 = repeat(green_glass_door_1, number = 1000, repeat = 10)
timepass2 = repeat(green_glass_door_2, number = 1000, repeat = 10)

print(timepass1)
print(timepass2)
print("Comparison")
print(str(sum(timepass1)/sum(timepass2)*100)[:4]+'%')