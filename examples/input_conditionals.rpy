define player = Character("[name]")
define jen = Character("Jen", who_color="#00ff00")

label start:
    scene bg forest
    show jen normal with zoomin
    $ name = renpy.input("What is your name?")
    player "My name is [name]."
    jen "Hi [name]"
    if name == "Richard":
        jen "That is a good name."
    elif name == "Nick":
        jen "That is a silly name."
    else:
        jen "I don't know you."
    return