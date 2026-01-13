import tkinter as tk

def andmed():
    root = tk.Tk()
    root.title("Tulu/Kulu kalkulaator")
    root.geometry("600x600")
    
    label = tk.Label(root, text="Mida sa soovid teha?")
    label.pack(pady=10)
    
    load = tk.Button(root, text="Load file", command=lambda: newton())
    load.pack()
    
    root.mainloop()
    
def newton():
    new = tk.Tk()
    new.title("New Tulu/Kulu")
    new.geometry("600x600")
    
    label = tk.Label(new, text="blablalba")
    label.pack(pady=10)
    
    newt = tk.Button(new, text="iunno man", command=lambda: print("miskit")) 
    newt.pack()
    
    new.mainloop()

andmed()