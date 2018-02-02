import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
    #join argv list to a single string starting at 2nd index
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
