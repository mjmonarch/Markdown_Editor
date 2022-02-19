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

# ----------------------- 2 --------------------------------------------
FORMATTERS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list',
              'unordered-list', 'new-line']
SP_COMMANDS = ['!help', '!done']

while True:
    print("Choose a formatter:", end='')
    formatter = input()
    if formatter not in FORMATTERS and formatter not in SP_COMMANDS:
        print("Unknown formatting type or command")
        continue
    if formatter == '!done':
        break
    if formatter == '!help':
        print(f"Available formatters:", *FORMATTERS)
        print(f"Special commands:", *SP_COMMANDS)
