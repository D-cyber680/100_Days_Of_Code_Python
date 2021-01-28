sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#Don't change code above 👆
#Write your code below:
#print(result)
import re
sentence_list = re.sub("[^\w]", " ",  sentence).split()

sentence_dict = {word:len(word) for word in sentence_list }
print(sentence_dict)
