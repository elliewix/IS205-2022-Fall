text = "a group of golden guppies are here"

words = text.split()

g_words = []
for w in words:
    # if w[0] == 'g':
    #     print(w)
    if w.startswith('g'):
        g_words.append(w)

print(g_words)
