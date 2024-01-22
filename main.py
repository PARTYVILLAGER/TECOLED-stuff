print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()
media_keys = MediaKeys()

keyboard.modules = [layers, encoder_handler, media_keys]

keyboard.tap_time = 250
keyboard.debug_enabled = True

CHANGE = KC.NO
______ = CHANGE
PRV = KC.TRNS

keyboard.keymap = [
    #Base Layer
    [
        KC.ESC,      ______,  KC.F1,   KC.F2,  KC.F3,  KC.F4,  ______,   KC.F5,  KC.F6,  KC.F7,    KC.F8,   ______,   KC.F9,   KC.F10,    KC.F11,   KC.F12,    ______,    KC.MPLY, 
        KC.TILDA,    KC.N1,   KC.N2,   KC.N3,  KC.N4,  KC.N5,  KC.N6,    KC.N7,  KC.N8,  KC.N9,    KC.N0,   KC.MINUS, KC.EQL,  KC.BSPC,   ______,   KC.INSERT, KC.HOME,   KC.PGUP, 
        KC.TAB,      KC.Q,    KC.W,    KC.E,   KC.R,   KC.T,   KC.Y,     KC.U,   KC.I,   KC.O,     KC.P,    KC.LBRC,  KC.RBRC, KC.BSLS,   ______,   KC.DEL,    KC.INSERT, KC.PGDN,
        KC.CAPSLOCK, ______,  KC.A,    KC.S,   KC.D,   KC.F,   KC.G,     KC.H,   KC.J,   KC.K,     KC.L,    KC.SCLN,  KC.QUOT, ______,    KC.ENTER, ______,    ______,    ______, 
        KC.LSHIFT,   ______,  KC.Z,    KC.X,   KC.V,   KC.V,   KC.B,     KC.N,   KC.M,   KC.COMMA, KC.DOT,  KC.SLASH, ______,  KC.RSHIFT, ______,   ______,    KC.UP,     ______, 
        KC.LCTRL,    KC.LWIN, KC.LALT, ______, ______, ______, KC.SPACE, ______, ______, ______,   KC.RALT, KC.RWIN,  KC.A,    KC.RCTRL,  ______,   KC.LEFT,   KC.DOWN,   KC.RIGHT, 
    ],
    #Function Layer
    [
        PRV, PRV,    KC.F13, KC.F14, KC.F15, KC.F16, PRV,    KC.F17, KC.F18, KC.F19, KC.F20, PRV,    KC.F21, KC.F22, KC.F23, KC.F24, PRV, PRV, 
        PRV, KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, PRV,    PRV,    PRV,    PRV, PRV,
        PRV, PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV, PRV,
        PRV, PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV, PRV,
        PRV, PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV, PRV, 
        PRV, PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV,    PRV, PRV,
    ]
]                                      

encoder_handler.pins = ((board.GP27, board.GP28, None))      
encoder_map = [
    [
        (KC.VOLD, KC.VOLU, 1),
        (KC.PGUP, KC.PGDN, 1),
    ]
]

if __name__ == '__main__':
    keyboard.go()