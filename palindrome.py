def palindromes(texts):
    with open(texts, "r") as text:
        for line in text:
            line = line.strip()
            line_2 = line[::-1]
            if line == line_2:
                print( line, " is palindromes")
            else:
                continue
text = "example.txt"
palindromes(text)