label start:
    call basic
    call flow
    call input
    call booleans
    call integers
    return

define k = Character("Kieran")
define r = Character("Reena", who_color="#ff0000")

label basic:
    scene bg school
    "I am the narrator."
    show kieran normal
    "Kieran" "I am Kieran."
    show kieran at left
    k "Defined as 'k' for short."
    show reena normal
    r "I am Reena and my colour is red."
    show reena at right with move
    r "I can move my position."
    scene bg space with fade
    show kieran angry
    "POW" with vpunch
    k "We are in space now."
    return

label flow:
    scene bg lake
    show kim smile with moveinright
    "Kim" "This is the lake"
    menu:
        "Where should we go?"
        "The Park":
            call fun
        "The school":
            call boring
    scene bg lake
    "Back to the lake!"
    return

label fun:
    scene bg park
    "OK"
    return

label boring:
    scene bg school
    "OK"
    return


define player = Character("[name]")
define jen = Character("Jen", who_color="#00ff00")

label input:
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


define has_book = False

label booleans:
    scene bg lake
    show malucy serious
    "Malucy" "Knowledge is power."
    menu:
        "Choose one item to take."
        "Book":
            show item book
            $ has_book = True
        "Sword":
            show item sword
    "You take the item"
    scene bg lake night with fade
    show gravekeeper
    "A monster attacks" with hpunch
    if has_book:
        hide gravekeeper with zoomout
        "You use the book to cast a spell on the monster."
    else:
        "Your sword is useless and the monster kills you." with vpunch
        scene bg black
    "The End."
    return

define points = 0

label integers:
    scene bg stars
    show mustafa crying
    "Mustafa" "I am sad because I do not have any friends."
    menu:
        "I will be your friend.":
            $points = points + 1
        "That is because you are fat.":
            $points = points - 10
    scene black
    "You scored [points] kindness points."
    if points > 0:
        "You win."
    else:
        "You lose"