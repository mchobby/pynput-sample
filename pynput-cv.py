#!/usr/bin/env python3
from pynput import keyboard


last_pressed = None
kb_controller = keyboard.Controller()

def on_press(key):
    global last_pressed 
    #try:
    #    print('Alphanumeric key pressed: {0} '.format(key.char))
    #except AttributeError:
    #    print('special key pressed: {0}'.format(key))

    if (key == keyboard.Key.f1) or (key == keyboard.Key.f2) or (key == keyboard.Key.scroll_lock):
        last_pressed = key
    else:
        last_pressed = None

def on_release(key):
    global last_pressed
    global kb_controller
    # print('Key released: {0}'.format(key))
    if key == keyboard.Key.alt:
        if last_pressed != None: # if F1 or F2 have been pressed
            if last_pressed == keyboard.Key.f1:
                # Send Copy KeyStroke
                kb_controller.press( keyboard.Key.ctrl )
                kb_controller.press( 'c' )
                kb_controller.release( 'c' )
                kb_controller.release( keyboard.Key.ctrl )
            elif last_pressed == keyboard.Key.f2:
                # Send Paste KeyStroke
                kb_controller.press( keyboard.Key.ctrl )
                kb_controller.press( 'v' )
                kb_controller.release( 'v' )
                kb_controller.release( keyboard.Key.ctrl )
            elif last_pressed == keyboard.Key.scroll_lock:
                return False # Stop listener
        last_pressed = None

    #if key == keyboard.Key.esc:
    #    # Stop listener
    #    return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


