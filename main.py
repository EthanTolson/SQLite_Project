from display import display

def main():
    #Create a window object
    window = display()
    window.drawInterface()
    window.window.mainloop()

if __name__ == "__main__":
    main()