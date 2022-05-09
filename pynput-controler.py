from pynput import keyboard

kcontroler = keyboard.Controller()

def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

    if key == keyboard.Key.f1:
        global kcontroler
        kcontroler.press("a")
        kcontroler.release("a")


def on_release(key):
    print('Key released: {0}'.format(
        key))

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

