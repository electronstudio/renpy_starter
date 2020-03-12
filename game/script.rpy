define k = Character("Kieran")
define r = Character("Reena", who_color="#ff0000")

label start:
    scene bg school day
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
    k "We are in space now."
    "POW" with vpunch
    return
