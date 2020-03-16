---
title: "Renpy Tutorial"
listings-no-page-break: true
---

# Renpy Tutorial

The goal is write a good story, not to finish all the exercises.  If the intermediate exercises are too difficult,
work on making your story longer and better instead!

## Download

Download Renpy bundled with a copy of a the starter project here:
[https://github.com/electronstudio/renpy_starter/releases/download/1/renpy-coderdojo1.zip](https://github.com/electronstudio/renpy_starter/releases/download/1/renpy-coderdojo1.zip)

It is a big file and you will need 1 GB of free space on your computer.  If you don't have this you can delete the files in your Download directory
or uninstall some games.

On _Windows_ unzip the file to your Desktop and double click __renpy.exe__ to start.

On _Mac_ after you unzip you will need to type this in to Terminal:
```
xattr -r -d com.apple.quarantine Downloads/renpy-coderdojo1/renpy.app
xattr -r -d com.apple.quarantine Downloads/renpy-coderdojo1/editra/Editra-mac.app
```

On _Linux_ you can use Terminal commands to download and unzip:
```
wget https://github.com/electronstudio/renpy_starter/releases/download/1/renpy-coderdojo1.zip
unzip renpy-coderdojo1.zip
chmod +x renpy-coderdojo1/renpy.sh
rm -rf renpy-coderdojo1/editra/
```

Then to run Renpy:

```
renpy-coderdojo1/renpy.sh
```

## Basics (Beginner)

In Renpy, click __script.rpy__ to open the editor.  You will be given a choice of editors.  On Windows and Mac I recommmend you select __Editra__.
On Linux you are probably best with __System editor__.  There is also __Atom__ which is nice but very big so it will probably be slow to
download and run.  You can change your editor later in Renpy preferences.

The script has already been started for you.  Type the remaining lines.  Be careful to type indents with the tab key.  You can add
extra blank lines to make the script easier to read.

```renpy
label start:
    call basic
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
    play sound spacetrash1
    "POW" with vpunch
    k "We are in space now."
    return
```

Each time you change the script you should press __ctrl+S__ to save and then quit the game and click __Launch Project__ again.
(You can reload the game without quitting but things often do not work if you do that.)

### Backgrounds

`scene` changes the background.  You must follow it with the name of a file in your images directory.

### Characters

`show` shows a character.  You must follow it with the name of a file in your images directory.  You can change the position by
adding `at left`, `at right`, `at center`.

Character variables store the name and color of a character to save you from typing it every time the character speaks.
You `define` them at the top of the script.

Characters disappear automatically at the end of a scene, but you can also `hide` them if you need to.

### Transitions

Adding `with move` makes a character move.  You can also `with zoomin` or `with moveinright` when the character first appears.

There are several transitions for scenes:

`with fade`

`with vpunch`

`with dissolve`

`with pixellate`

### Tasks

1. Continue the conversation between Kieran and Reena.
2. Define another character and have him speak.
3. Change the expressions of the characters.
4. Change the scene background.
5. Write your own story.

## Flow control (Beginner)

Each example is separate but you can put them all in the same `script.rpy` file, so long as you remember to change
the `call` at the top to the label you are currently working on.

__IMPORTANT__: _On line 2, change `call basic` to `call flow`_.

Then add this code at the end of the program. (Line numbers shown here will __not__ match the line numbers in your program.)

```renpy
label flow:
    scene bg lake
    show kim smile with moveinright
    "Kim" "This is the lake"
    menu:
        "Where should we play our music?"
        "The Park":
            call park
        "The school":
            call boring
    scene bg lake
    "Back to the lake!"
    stop music
    return

label park:
    play music music4
    scene bg park
    "OK"
    return

label boring:
    play music music1
    scene bg school
    "OK"
    return
```

Renpy scripts are very similar to Python programs. You can even write Python commands in a Renpy script, but
it is easier to write Renpy commands because they are shorter.

`label` is similar to Python `def` for creating a function.  The first label must be called `start`.

After creating a label we use a colon and then everything is *indented* using the *tab key*, just like in a Python function.

To end the function/label we use `return` just like Python.  Unlike Python, Renpy does not return automatically return if you
leave it out.  I recommend you always return at the end of a label to avoid confusion.  When you return from the start label your game
will end.

To allow the player to choose what happens next in the story, use `menu`.

To go to a label we use `call` command, which is like `()` in Python.

### Tasks

1. Add another location to the menu.  Create a label for this location.
2. Write a story that has different choices.  Perhaps some choices lead to a good ending and other
choices lead to a bad ending.


## Input and conditionals (Intermediate)

_On line 2, change `call flow` to `call input`_.

Then add this new code at the end of the program. (Line numbers shown here will __not__ match the line numbers in your program.)

```renpy
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
```

Note the $ sign allows you to enter any python statement.  Mostly we use when we want to set a variable because
Renpy does not have a built in command for this.

### Tasks

1. Add additional `elif` statements for your name and your friend's name.

## Booleans (Intermediate)

_On line 2, change `call flow` to `call input`_.

Then add this new code at the end of the program. (Line numbers shown here will __not__ match the line numbers in your program.)

```renpy
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
```

## Sound and music

You can play a sound file with `sound play`.  You can play a loop of music with `music play`.
Look in the __audio__ directory to see what sounds are available.  You can record or download your own sounds.
They should be __.ogg__ or __.mp3__ format.

1. Add `play music music1` to somewhere in the script.
2. Add a sound effect of your choice to the script.

## Integers (Advanced)

_On line 2, change `call input` to `call booleans`_.

Then add this new code at the end of the program. (Line numbers shown here will __not__ match the line numbers in your program.)

```renpy
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
    play sound spacetrash2
    "A monster attacks" with hpunch
    if has_book:
        play sound laser1
        hide gravekeeper with zoomout
        "You use the book to cast a spell on the monster."
    else:
        scene bg black
        play sound game_over
        "Your sword is useless and the monster kills you." with vpunch
    return
```

### Tasks

1. Write a quiz where you get points for choosing the correct answer.
2. Add questions that use `renpy.input` to get the player to type an answer.

##  Integers (Advanced)

_On line 2, change `call booleans` to `call integers`_.

Then add this new code at the end of the program.  (Line numbers shown here will __not__ match the line numbers in your program.)

```renpy
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
        play sound congratulations
        "You win."
    else:
        play sound you_lose
        "You lose"
```

##  Your own artwork

You can draw your own backgrounds and characters using a graphics program, e.g. Krita.  You can also
download images from the web.  Backgrounds should be `1280x720` size.  Characters should be about `400x720`.  You might
have to load them into Krita and resize them.  You
must save them as `.png` or `.jpg` files in the `images` directory.

1. Draw or download your own background.
2. Draw or download your own character.