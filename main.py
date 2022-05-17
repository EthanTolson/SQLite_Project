from display import display

def main():
    #Create a window object
    display1 = display()
    display1.drawInterface()
    display1.window.mainloop()

if __name__ == "__main__":
    main()