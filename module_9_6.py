def all_variants(text):
    while len(text) > 1:
        for i in range(1, len(text)):
            var = text[:i]
            yield var
        for i in range(len(text)):
            var = text[i:]
            yield var
        text = text[1:-1]


for x in all_variants('abcdefg'):
    print(x)
