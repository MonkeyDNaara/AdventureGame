



UNKNOWN_SYMBOL = "□"
TORCH_LIGHT_RADIUS = 1


DEFAULT_MAZE = [
    "IIIIIIIIIIIIIIIIIIII",     #0
    "IX  I I     I S I  I",     #1
    "Ip    I IIIII   I II",     #2
    "I   I I     I   I II",     #3
    "IIIII IIIII III I II",     #4
    "I     I     I      I",     #5
    "I IIIII II IIIIIII I",     #6
    "I        I         I",     #7
    "IIIIIIII IIII III II",     #8
    "I      I  I I I I  I",     #9
    "I II I II I I I    I",     #10
    "I  I I  I I I IIII I",     #11
    "IIII II I          I",     #12
    "I     I I III IIII I",     #13
    "IFIII III I I   I  I",     #14
    "I   I     I   I I  I",     #15
    "I I I I IIIIIII I  I",     #16
    "I I I I IE      II I",     #17
    "I●I!I I  IBI   I   I",     #18
    "IIIIIIIIIIAIIIIIIIII",     #19
]


HIDDEN_ROOM = [
    "IIIIIIIIII",   #0
    "I●  I   !I",   #1
    "III I IIII",   #2
    "I   I    I",   #3
    "I IIII I I",   #4
    "I      I I",   #5
    "I IIIIII I",   #6
    "I M  XII I",   #7
    "IIIIIIx  I",   #8
    "IIIIIIIIII",   #9
]


DIRECTIONS = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1),
}


ITEM_TILES = {
    "F": {"type": "torch"},
    "p": {"type": "potion", "name": "small_potion"},
    "P": {"type": "potion", "name": "big_potion"},
    "S": {"type": "weapon", "name": "rusty_sword"},
    "x": {"type": "key", "key": "x"},
}


ENEMY_TILES = {
    "e": 1,
    "E": 2,
    "m": 3,
    "M": 4,
    "B": 10,
}
