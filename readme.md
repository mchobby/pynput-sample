# Pynput examples - Replace CTRL-C & CTRL-V on Linux machine
Thank to pynput, it is possible to capture keyboard even before the application catchs it.

Thank to this, we could capture alt+F1 & alt+F2 (if they are system free) trap the messages and replace them with ctrl+C & CTRL+V !

I had tested this during month on my Linux Mint. It's works great!

# Install pynput library
```
sudo apt-get install python3-dev

sudo pip3 install pynput
```

See the following article for more information:


https://www.delftstack.com/howto/python/python-detect-keypress/

# Free-up system assignment for combinations for F1 & F2 
On Linux Mint, deactivate <Alt>+<F1> showing the main  menu:
* Menu -> Preference -> CompizConfig Settings Manager
* General Section --> MATE Compatibility<br />Clear "display main menu" option (Afficher le menu principal)

On Linux Mint, deactivate the <Alt>+<F2> for Run command:
* Menu -> Preference -> Keyboard Shortcut (Raccourcis clavier)
* Under the "Desktop" section (Bureau)<br />remove the keyboard shortcut

# Run the Ctrl-C / Ctrl-V replacement

Once you add released the system assignment arount F1 & F2 then you can simply start the script with

```
python3 pynput-cv.py
```

It will catch the Alt+F1 & Alt+F2 and send the Ctrl+C & Ctrl+V keystroke instead.

# Additional recommandation

Replace the copy/paste shorcut in the terminal application.

On my Mate Terminal, I used F1 to copy & F2 to paste.

The final combination of graphical Apps shortcut and terminal shorcut is just kindly useful. I use them every days.

Cheers,
Dominique
