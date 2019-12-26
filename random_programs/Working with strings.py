# printing out a string
print("lol")
# printing out a space betwin them (\n)
print("Hello\nWorld")
# if you want to put a (") inside do this:
print("Hello\"World\"")
# if you want to put a (\) inside just type:
print("Hello\World")
# you can also print a variable like this;
lol = "Hello World"
print(lol)
# you can also do something called cencatenation who is putting a string whit some text like this;
lol = "Hello World"
print(lol + " Hello World")
# you can also use fonctions to change info or to know info about a sring. exemple of fonctions;
lol = "Hello World"
# puts every thing small or decapitelize
print(lol.lower())
# capitelize everything
print(lol.upper())
# boolean is it all cap.
print(lol.isupper())
# 2 same time
print(lol.upper().isupper())
# tells you lhe length
print(len(lol))
# this fonction shows a letter of the string(0 for "H", 1 for "e" exetera).
lol = "Hello World"
print(lol[0])
print(lol[1])
# you can return the index (the position of a letter)by doing this:
print(lol.index("d"))
# you can also replace a word in your string like this:
print(lol.replace("World", "dude"))
