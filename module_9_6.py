def all_variants(text):
    for i in range(len(text)):
        var = text[i]
        yield var
    for i in range(len(text)-1):
        var = text[i:i+2]
        yield var
    for i in range(len(text)-2):
        var = text[i:]
        yield var
    for i in range(3, len(text)):
        var = text[:i]
        yield var


for x in all_variants('abcde'):
    print(x)
