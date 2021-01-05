import pyautogui
import time

def from_command_line():
    msg = input( "Enter the text you want to spam: " )
    num = int(input( "How many times do you want to spam the message: " ))
    print( "You have 5 seconds to place your cursor in the text box ")
    time.sleep( 5 )
    for i in range(num):
        pyautogui.write( msg )
        pyautogui.press( 'enter' )
        time.sleep( 0.1)
    print( "Spammed " + msg + " " + str(num) + " times")
    print( "Thank you for using this program, have a good day!")

def from_file():
    file = open( r"input.txt", "r")
    print( "Reading from input.txt" )
    print( "You have 5 seconds to place your cursor in the text box" )
    time.sleep( 5 )
    lines = file.readlines()
    for i in lines:
        pyautogui.write( i )
        pyautogui.press( 'enter' )
        time.sleep(0.1)
    print( "Spammed the contents in input.txt")
    print( "Thank you for using this program, have a good day!")

print( "Enter 1 to input a custom phrase" )
print( "Enter 2 to read from the input.txt file" )
inp = int(input("Input: "))
if( inp == 1 ):
    from_command_line()
elif( inp == 2 ):
    from_file()
else:
    print( "Invalid input, please run this program again" )
