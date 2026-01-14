import tkinter as tk
from tkinter import messagebox
import raha  # Importing your raha.py file

# The 4 fixed categories
KATEGOORIAD = ["toit", "transport", "meelelahutus", "muu"]

def clear_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

def peamenüü(root):
    clear_screen(root)
    stats = raha.arvuta_kategooriad(raha.kirjed)
    kokku = sum(stats.values())
    
    tk.Label(root, text="Rahahaldur", font=("Arial", 16, "bold")).pack(pady=10)
    
    tk.Button(root, text="Lisa Tulu", width=20, bg="#d4edda", command=lambda: lisa_vaade(root, "tulu")).pack(pady=5)
    tk.Button(root, text="Lisa Kulu", width=20, bg="#f8d7da", command=lambda: lisa_vaade(root, "kulu")).pack(pady=5)
    tk.Button(root, text="Vaata ajalugu / Eemalda", width=20, command=lambda: ajaloo_vaade(root)).pack(pady=5)

    tk.Label(root, text=f"Hetkeseis: {kokku:.2f} €", font=("Arial", 12, "bold")).pack(pady=20)
    
    tk.Label(root, text="Kategooriate kaupa:").pack()
    for kat, summa in stats.items():
        tk.Label(root, text=f"{kat}: {summa:.2f} €").pack()

def lisa_vaade(root, tyyp):
    clear_screen(root)
    tk.Label(root, text=f"Lisa uue {tyyp} sisestus", font=("Arial", 12)).pack(pady=10)
    
    # 1. Summa sisestus
    tk.Label(root, text="Summa:").pack()
    ent_summa = tk.Entry(root)
    ent_summa.pack(pady=5)
    
    # 2. KATEGOORIA MENU (Dropdown)
    tk.Label(root, text="Vali kategooria:").pack()
    valitud_kat = tk.StringVar(root)
    valitud_kat.set(KATEGOORIAD[0]) # Sea vaikeväärtus (toit)
    
    kat_menu = tk.OptionMenu(root, valitud_kat, *KATEGOORIAD)
    kat_menu.pack(pady=5)
    
    # 3. Kirjeldus
    tk.Label(root, text="Kirjeldus:").pack()
    ent_kirjeldus = tk.Entry(root)
    ent_kirjeldus.pack(pady=5)

    def salvesta():
        try:
            s = float(ent_summa.get())
            k = valitud_kat.get() # Grab value from dropdown
            d = ent_kirjeldus.get()
            
            raha.lisa_kulu_tulu(s, k, d, tyyp)
            peamenüü(root)
        except ValueError:
            messagebox.showerror("Viga", "Summa peab olema number!")

    tk.Button(root, text="Salvesta", command=salvesta, bg="lightgreen").pack(pady=10)
    tk.Button(root, text="Tagasi", command=lambda: peamenüü(root)).pack()

def ajaloo_vaade(root):
    clear_screen(root)
    tk.Label(root, text="Kõik kanded", font=("Arial", 14)).pack(pady=10)
    
    # Create a canvas and scrollbar for history if it gets too long
    for i, kirje in enumerate(raha.kirjed):
        frame = tk.Frame(root)
        frame.pack(fill="x", padx=20, pady=2)
        
        tekst = f"{kirje['tyyp'].upper()}: {kirje['summa']}€ - {kirje['kategooria']} ({kirje['kirjeldus']})"
        tk.Label(frame, text=tekst, anchor="w").pack(side="left")
        
        tk.Button(frame, text="Kustuta", fg="white", bg="red", font=("Arial", 8),
                  command=lambda idx=i: eemalda_kirje(root, idx)).pack(side="right")
        
    if not raha.kirjed:
        tk.Label(root, text="Ajalugu on tühi.").pack()

    tk.Button(root, text="Tagasi", command=lambda: peamenüü(root)).pack(pady=20)

def eemalda_kirje(root, index):
    if messagebox.askyesno("Kinnita", "Kas soovid selle kande kustutada?"):
        raha.kirjed.pop(index)
        ajaloo_vaade(root)

# --- START ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tulu/Kulu Manager")
    root.geometry("450x550")
    peamenüü(root)
    root.mainloop()