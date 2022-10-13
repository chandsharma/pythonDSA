#program to count how many occurance a word have in a text file
from hashMaps_collisionHandling import HashMap

# hash_map = HashMap()
hash_map = dict()
with open(__file__.split("count_words.py")[0]+"road_not_taken.txt",'r') as file:
    data = file.read()
    for line in data.splitlines():
        for word in line.split(' '):
            cleaned_word = ''.join(letter for letter in word if letter.isalnum())
            if cleaned_word in hash_map:
                hash_map[cleaned_word] = hash_map[cleaned_word] + 1
            else:
                hash_map[cleaned_word] = 1

print(hash_map)