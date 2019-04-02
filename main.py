def transform(letter):
    letters = []
    a = """
      _
     /_\\
    /   \\
    """
    a = a.rstrip()

    b = """
     __
    |__]
    |__]
    """
    b = b.rstrip()

    c = """
     __
    |
    |__
    """
    c = c.rstrip()

    d = """
     __
    |  \\
    |__/
    """
    d = d.rstrip()

    e = """
     __
    |__
    |__
    """
    e = e.rstrip()

    f = """
     __
    |__
    |
    """
    f = f.rstrip("")

    newtext = ''
    for n in letter:
        if n.lower() == "a":
            n == a
            newtext += a
        elif n.lower() == "b":
            n == b
            newtext += b
        elif n.lower() == "c":
            n == c
            newtext += c
        elif n.lower() == "d":
            n == d
            newtext += d
        elif n.lower() == "e":
            n == e
            newtext += e
        elif n.lower() == "f":
            n == f
            newtext += f

    return newtext


letters = []
input_text = input("Please enter text:")
input_text = input_text.split()

for letter in input_text:
    letters.append(transform(letter))

for item in letters:
    print(item)