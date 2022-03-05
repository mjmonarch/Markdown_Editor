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
FORMATTERS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
              'ordered-list', 'unordered-list']
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


def list_():
    while True:
        try:
            num_of_rows = int(input("Number of rows: "))
            if num_of_rows <= 0:
                raise TypeError
        except TypeError:
            print("The number of rows should be greater than zero")
        else:
            break
    temp_list = []
    # for i in range(1, num_of_rows + 1):
    #     temp_list.append(input(f"Row #{i}: "))
    temp_list = [f"Row #{i}: " for i in range(1, num_of_rows + 1)]

    output.append(temp_list)


functions = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header, 'link': link,
             'inline-code': inline_code, 'new-line': new_line, 'ordered-list': list_,
             'unordered-list': list_}

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
