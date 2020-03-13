define has_book = False

label start:
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
