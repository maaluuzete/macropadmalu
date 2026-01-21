import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
PINS = [board.D1, board.D2, board.D3, board.D4, board.D5, board.D6]
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.Macro(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), KC.MACRO("code\n")),# Abrir VS Code
        KC.Macro(Press(KC.LCTRL), Press(KC.LSHIFT), Tap(KC.B), Release(KC.LSHIFT), Release(KC.LCTRL)), # Rodar código (Ctrl+Shift+B)
        KC.MACRO("int t; cin >> t;\nwhile (t--) {\n\n}\n"),# while(t--) template
        KC.Macro(Press(KC.LCTRL), Tap(KC.F), Release(KC.LCTRL)),# Buscar (Ctrl+F)
        KC.MACRO("#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    ios::sync_with_stdio(false);\n    cin.tie(NULL);\n\n    return 0;\n}\n"),  # Template C++ CP
        KC.MACRO("for(int i=0; i<n; i++){\n    \n}\n"),# For loop rápido
    ]
]

if __name__ == '__main__':
    keyboard.go()
