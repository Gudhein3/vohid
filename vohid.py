import evdev
import pygame
from typing import Dict, Tuple
from evdev.ecodes import *

devs = evdev.list_devices()

print("WARNING!!!!")
print("="*60)
print("You're about to show all input devices connected to this computer.")
print("This might lead to people begin know your HIDs.")
print("Press Enter to continue.")
print("="*60)

input()

def choose_device():
    for i, dev in enumerate(devs):
        print(f"({i}){evdev.InputDevice(dev).name}")

    device_index = -1
    while True:
        device_index = input("Please choose the input device that you wanna choose: ")
        if not device_index.isnumeric():
            continue
        device_index = int(device_index)
        if device_index < 0 or device_index >= len(devs):
            continue
        break

    return evdev.InputDevice(devs[device_index])

layout: Dict[str, Tuple[Dict[int, str], Dict[int, str], Dict[int, str]]] = {
    "us": (
        {
            KEY_0: '0', KEY_1: '1', KEY_2: '2', KEY_3: '3', KEY_4: '4', KEY_5: '5',
            KEY_6: '6', KEY_7: '7', KEY_8: '8', KEY_9: '9',
            KEY_A: 'a', KEY_B: 'b', KEY_C: 'c', KEY_D: 'd', KEY_E: 'e', KEY_F: 'f',
            KEY_G: 'g', KEY_H: 'h', KEY_I: 'i', KEY_J: 'j', KEY_K: 'k', KEY_L: 'l',
            KEY_M: 'm', KEY_N: 'n', KEY_O: 'o', KEY_P: 'p', KEY_Q: 'q', KEY_R: 'r',
            KEY_S: 's', KEY_T: 't', KEY_U: 'u', KEY_V: 'v', KEY_W: 'w', KEY_X: 'x',
            KEY_Y: 'y', KEY_Z: 'z',
            KEY_COMMA: ',',
            KEY_DOT: '.',
            KEY_SEMICOLON: ';',
            KEY_APOSTROPHE: '\'',
            KEY_SLASH: '\\',
            KEY_BACKSLASH: '/',
            KEY_LEFTBRACE: '[',
            KEY_RIGHTBRACE: ']',
            KEY_GRAVE: '`',
            KEY_MINUS: '-',
            KEY_EQUAL: '=',
        },
        {
            KEY_0: ')', KEY_1: '!', KEY_2: '@', KEY_3: '#', KEY_4: '$', KEY_5: '%',
            KEY_6: '^', KEY_7: '&', KEY_8: '*', KEY_9: '(',
            KEY_A: 'A', KEY_B: 'B', KEY_C: 'C', KEY_D: 'D', KEY_E: 'E', KEY_F: 'F',
            KEY_G: 'G', KEY_H: 'H', KEY_I: 'I', KEY_J: 'J', KEY_K: 'K', KEY_L: 'L',
            KEY_M: 'M', KEY_N: 'N', KEY_O: 'O', KEY_P: 'P', KEY_Q: 'Q', KEY_R: 'R',
            KEY_S: 'S', KEY_T: 'T', KEY_U: 'U', KEY_V: 'V', KEY_W: 'W', KEY_X: 'X',
            KEY_Y: 'Y', KEY_Z: 'Z',
            KEY_COMMA: '<',
            KEY_DOT: '>',
            KEY_SEMICOLON: ':',
            KEY_APOSTROPHE: '"',
            KEY_SLASH: '|',
            KEY_BACKSLASH: '?',
            KEY_LEFTBRACE: '{',
            KEY_RIGHTBRACE: '}',
            KEY_GRAVE: '~',
            KEY_MINUS: '_',
            KEY_EQUAL: '+',
        },
        {
            KEY_SPACE: ' ',
            KEY_ENTER: '\n',
        }
    ),

    "ru": (
        {
            KEY_0: '0', KEY_1: '1', KEY_2: '2', KEY_3: '3', KEY_4: '4', KEY_5: '5',
            KEY_6: '6', KEY_7: '7', KEY_8: '8', KEY_9: '9',
            KEY_A: 'ф', KEY_B: 'и', KEY_C: 'с', KEY_D: 'в', KEY_E: 'у', KEY_F: 'а',
            KEY_G: 'п', KEY_H: 'р', KEY_I: 'ш', KEY_J: 'о', KEY_K: 'л', KEY_L: 'д',
            KEY_M: 'ь', KEY_N: 'т', KEY_O: 'щ', KEY_P: 'з', KEY_Q: 'й', KEY_R: 'к',
            KEY_S: 'ы', KEY_T: 'е', KEY_U: 'г', KEY_V: 'м', KEY_W: 'ц', KEY_X: 'ч',
            KEY_Y: 'н', KEY_Z: 'я',
            KEY_COMMA: 'б',
            KEY_DOT: 'ю',
            KEY_SEMICOLON: 'ж',
            KEY_APOSTROPHE: 'э',
            KEY_SLASH: '\\',
            KEY_BACKSLASH: '.',
            KEY_LEFTBRACE: 'х',
            KEY_RIGHTBRACE: 'ъ',
            KEY_GRAVE: 'ё',
            KEY_MINUS: '-',
            KEY_EQUAL: '=',
        },
        {
            KEY_0: ')', KEY_1: '"', KEY_2: '"', KEY_3: '#', KEY_4: ';', KEY_5: '%',
            KEY_6: ':', KEY_7: '?', KEY_8: '*', KEY_9: '(',
            KEY_A: 'Ф', KEY_B: 'И', KEY_C: 'С', KEY_D: 'В', KEY_E: 'У', KEY_F: 'А',
            KEY_G: 'П', KEY_H: 'Р', KEY_I: 'Ш', KEY_J: 'О', KEY_K: 'Л', KEY_L: 'Д',
            KEY_M: 'Ь', KEY_N: 'Т', KEY_O: 'Щ', KEY_P: 'З', KEY_Q: 'Й', KEY_R: 'К',
            KEY_S: 'Ы', KEY_T: 'Е', KEY_U: 'Г', KEY_V: 'М', KEY_W: 'Ц', KEY_X: 'Ч',
            KEY_Y: 'Н', KEY_Z: 'Я',
            KEY_COMMA: 'Б',
            KEY_DOT: 'Ю',
            KEY_SEMICOLON: 'Ж',
            KEY_APOSTROPHE: 'Э',
            KEY_SLASH: '/',
            KEY_BACKSLASH: ',',
            KEY_LEFTBRACE: 'Х',
            KEY_RIGHTBRACE: 'Ъ',
            KEY_GRAVE: 'Ё',
            KEY_MINUS: '_',
            KEY_EQUAL: '+',
        },
        {
            KEY_SPACE: ' ',
            KEY_ENTER: '\n',
        }
    )
}


symbolization: Dict[str, Tuple[str, str]] = {
    "us": ("q","Q"),
    "ru": ("й","Й"),
}

layout_cycle = {
    "us": "ru",
    "ru": "us"
}

current_layout = "us"

device = choose_device()
device.grab()
shift = 0

WIDTH = 1000
HEIGHT = 420

TW_WIDTH = WIDTH-40
TW_HEIGHT = HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()

font = pygame.font.SysFont("noto", 60)

twx = 0
twy = HEIGHT-60

line = []

def break_line():
    global twx, twy, line
    line = []
    twy += 60
    twx = 0
    if twy >= TW_HEIGHT:
        twy = TW_HEIGHT-60
        screen.blit(screen, (0, -60))
        pygame.draw.rect(screen, (0, 0, 0), (0, TW_HEIGHT-60, TW_WIDTH, 60))

def print_char(char: str):
    global twx, twy
    if char == '\n':
        break_line()
        return
    serf = font.render(char, False, (255, 255, 255))
    screen.blit(serf, (twx, twy))
    w = serf.get_width()
    twx += w
    line.append(w)
    if twx >= WIDTH:
        break_line()

clock = pygame.time.Clock()

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit()
    pygame.draw.rect(screen, (0, 127, 127), (TW_WIDTH, 0,  WIDTH-TW_WIDTH, HEIGHT))
    pygame.draw.rect(screen, (0, 127, 127), (0, TW_HEIGHT, WIDTH,          HEIGHT-TW_HEIGHT))
    screen.fill((1,1,1), (0, 0, TW_WIDTH, TW_HEIGHT-60), special_flags=pygame.BLEND_RGB_SUB)
    while True:
        ev = device.read_one()
        if ev is None:
            break
        if ev.type == 1:
            key = ev.code
            if key == KEY_LEFTSHIFT:
                if ev.value != 2:
                    shift = ev.value
                continue
            if ev.value == 0:
                pass
            if ev.value == 1 or ev.value == 2:
                if key == KEY_BACKSPACE:
                    if len(line) != 0:
                        w = line.pop()
                        twx -= w
                        pygame.draw.rect(screen, (0, 0, 0), (twx, twy, w, 60))
                    continue
                elif key == KEY_F1:
                    current_layout = "us"
                    continue
                elif key == KEY_F2:
                    current_layout = "ru"
                    continue
                elif key == KEY_LEFTMETA:
                    current_layout = layout_cycle[current_layout]
                    continue
                if key in layout[current_layout][shift]:
                    print_char(layout[current_layout][shift][key])
                elif key in layout[current_layout][2]:
                    print_char(layout[current_layout][2][key])
                else:
                    print(f"Unknown key: {{{key}}}")
    serf = font.render(symbolization[current_layout][shift], True, (255, 255, 255))
    screen.blit(serf, (WIDTH-serf.get_width(), HEIGHT-60))
    pygame.display.flip()
    clock.tick(45)
