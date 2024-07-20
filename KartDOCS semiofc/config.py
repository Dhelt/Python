import os
import time
def linha():
    print()
def tempo():
    time.sleep(2)

from bancodedados import usuarios
def verificar_login(user, senha):
    if user in usuarios and usuarios[user] == senha:
        return True
    return False

import pyfiglet
text = pyfiglet.figlet_format(text='KartDOCS', font='poison')
