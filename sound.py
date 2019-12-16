import os
import webbrowser

def music():
    os.system('mpg123 music.mp3')

def voice():
    os.system('mpg123 final.mp3')

os.system("open final.mp3")
os.system('mpg123 music.mp3')
