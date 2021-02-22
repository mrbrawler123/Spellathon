import nltk
import time
nltk.download("words")
nltk.download("wordnet")
print("\033[2J\033[H")
print("SPELLATHON")
time.sleep(2)
print(
    "This is where you can form words. First enter one or more compulsory letters. Then you can enter other letters which can be in the word. I will tell you all the possible words that can be made."
)
time.sleep(1)
from nltk.corpus import words
from nltk.corpus import wordnet
words_list = words.words() + list(wordnet.words())
rp = input("Enter the compulsory letters (Comma Separated): ")
r = rp.replace(" ", "")
compulsory_letter1 = r.split(",")
compulsory_letter = []
for dj in compulsory_letter1:
	dj = dj.lower()
	compulsory_letter.append(dj)
time.sleep(1)
me = input("Enter the optional letters (Comma Separated): ")
s = me.replace(" ", "")
optional_letters1 = s.split(",")
optional_letters = []
for dkj in optional_letters1:
	dkj = dkj.lower()
	optional_letters.append(dkj)
final_words = []
index_list = []
var = 0
for x in words_list:
	var = 0
	x = x.lower()
	x_list = list(x)
	if len(x_list) < 4:
		continue
	for randomletter in compulsory_letter:
		if randomletter in x_list:
			var = var + 1
	if var != len(compulsory_letter):
		continue
	for z in range(len(x_list)):
		for al in compulsory_letter:
			if al == x_list[z]:
				index_list.append(z)
				continue
		for y in optional_letters:
			if y == x_list[z]:
				index_list.append(z)
	if len(index_list) == len(x_list):
		final_words.append(x)
	index_list = []
if len(final_words) == 0:
	print("No words can be formed.")
else:
	print(f"Here are the words that can be formed: {final_words}")