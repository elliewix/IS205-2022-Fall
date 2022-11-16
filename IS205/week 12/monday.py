import string


def ngram_letters(name, num):
    # [n.strip(string.punctuation) for n in name.split()]
    components = name.split()
    cleaned_components = []
    for comp in components:
        clean_comp = comp.strip(string.punctuation)
        cleaned_components.append(clean_comp)
    return cleaned_components

results = ngram_letters("pikachu", 2)

print(results)
print(ngram_letters("mr.!!!      mime!:-)", 2))


# pause for discussion of recursive functions.....
#
#
# def fib(term):
#     f = [0, 1]
#     for now in range(2, term+1):
#         before = fib(now - 1)#f[now - 1]
#         before_before = fib(now - 2)#f[now -2]
#         # f.append(f[i-1] + f[i-2])
#         sum = before + before_before
#         f.append(sum)
#         # print(sum)
#     return f[term]
#
# print(fib(20))
#
# for i in range(4):
#     print(fib(i))
