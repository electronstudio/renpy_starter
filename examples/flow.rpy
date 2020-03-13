label start:
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




