# a program that generates pickup lines

# import markovify
import sys
sys.path.insert(0, "/usr/local/lib/python3.7/dist-packages/")
import markovify

# read pickup lines and make models
with open("pickup_lines.txt", encoding="utf8") as f:
    text = f.read()
pickup_model = markovify.Text(text, state_size=2)

with open("bojack_quotes.txt", encoding="utf8") as f:
    text = f.read()
bojack_model = markovify.Text(text, state_size=2)

with open("inspirational_quotes.txt", encoding="utf8") as f:
    text = f.read()
inspirational_model = markovify.Text(text, state_size=2)

# combine the models
model_combo = markovify.combine([pickup_model, bojack_model], [2,1])

# print 10 quotes using the new model
for i in range(15):
    print(i + 1, ">>", model_combo.make_sentence())
    print('\n')
