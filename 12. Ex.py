# Que: sentence="This is a common interview question"
# Find the most repeated character in this text.
# We will take a dictionary and store the char and it's frequency as key value pairs.

sentence = "This is a common interview question"
genz = {}
for char in sentence:
    if char in genz:
        genz[char] += 1
    else:
        genz[char] = 1

sorted_freq = sorted(
    genz.items(), key=lambda kv: kv[1], reverse=True)

print(sorted_freq[0])
print(genz)
