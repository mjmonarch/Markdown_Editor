# ----------------------- 1 --------------------------------------------
#
# print("""# John Lennon
# or ***John Winston Ono Lennon*** was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# * Imagine
# * Norwegian Wood
# * Come Together
# * In My Life
# * ~~Hey Jude~~ (that was *McCartney*)""")

# # ----------------------- 2 --------------------------------------------
# FORMATTERS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list',
#               'unordered-list', 'new-line']
# SP_COMMANDS = ['!help', '!done']
#
# while True:
#     print("Choose a formatter:", end='')
#     formatter = input()
#     if formatter not in FORMATTERS and formatter not in SP_COMMANDS:
#         print("Unknown formatting type or command")
#         continue
#     if formatter == '!done':
#         break
#     if formatter == '!help':
#         print(f"Available formatters:", *FORMATTERS)
#         print(f"Special commands:", *SP_COMMANDS)

# ----------------------- 3 --------------------------------------------
FORMATTERS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line']
SP_COMMANDS = ['!help', '!done']


def plain():
    text = input("Text: ")
    output.append(text)


def bold():
    text = input("Text: ")
    output.append(f"**{text}**")


def italic():
    text = input("Text: ")
    output.append(f"*{text}*")


def header():
    while True:
        try:
            level = int(input("Level: "))
            if not 1 <= level <= 6:
                raise TypeError
        except TypeError:
            print("The level should be within the range of 1 to 6")
        else:
            break
    text = input("Text: ")
    output.append(f"{'#' * level} {text}\n")


def link():
    label = input("Label: ")
    url = input("URL: ")
    output.append(f"[{label}]({url})")


def inline_code():
    text = input("Text: ")
    output.append(f"`{text}`")


def new_line():
    output.append("\n")


def _help():
    print(f"Available formatters:", *FORMATTERS)
    print(f"Special commands:", *SP_COMMANDS)


functions = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header, 'link': link,
             'inline-code': inline_code, 'new-line': new_line}

global output
output = []

while True:
    print("Choose a formatter:", end='')
    formatter = input()
    if formatter not in FORMATTERS and formatter not in SP_COMMANDS:
        print("Unknown formatting type or command")
        continue
    if formatter == '!done':
        break
    if formatter == '!help':
        _help()
    else:
        functions[formatter]()
        print(*output, sep='')
