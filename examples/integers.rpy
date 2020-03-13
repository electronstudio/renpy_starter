define points = 0

label start:
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