def charFrequency(input):
    charset = {}

    for char in input:
        if char in charset:
            charset[char] += 1
        else:
            charset[char] = 1

    counted_charset = sorted(charset.items(), key=lambda item: item[1], reverse=True)

    print(f"Sentence inputted = {input}\nCharacter counts in the sentence are:")
    for i in range(len(counted_charset)):
        print(f"{counted_charset[i]}")

charFrequency("Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech.")