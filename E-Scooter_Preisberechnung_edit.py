import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Berechnung vom Preis pro Minute als Funktion
def berechne_preis_dauer(dauer, grundgebuehr, preis_pro_minute):
    return grundgebuehr + (preis_pro_minute * dauer)

# Berechnung von Preis pro Kilometer als Funktion
def berechne_preis_strecke(strecke, grundgebuehr, preis_pro_km):
    return grundgebuehr + (preis_pro_km * strecke)

# Berechnung basierend auf der Auswahl des User
def berechne_preis():
    try:
        grundgebuehr = float(entry_grundgebuehr.get())
        preis_pro_minute = float(entry_preis_pro_minute.get())
        preis_pro_km = float(entry_preis_pro_km.get())
        
        # Überprüfung ob die Checkbox Nutzungsdauer ausgewählt wurde
        if var.get() == 1:
             # Berechnung des Preis pro Minute basierend auf die Eingabe des Users
            dauer = float(entry.get())
            preis = berechne_preis_dauer(dauer, grundgebuehr, preis_pro_minute)
            messagebox.showinfo("Preisberechnung", f"Der Fahrpreis beträgt: {preis:.6f} Euro")
            
        # Überprüfung ob die Checkbox Nutzungsstrecke ausgewählt wurde
        elif var.get() == 2:
        
            # Berechnung des Preis pro Strecke basierend auf die Eingabe des Users
            strecke = float(entry.get())
            preis = berechne_preis_strecke(strecke, grundgebuehr, preis_pro_km)
            messagebox.showinfo("Preisberechnung", f"Der Fahrpreis beträgt: {preis:.6} Euro")
            
         # Falls der User keine Checkbox ausgewählt hat, wird folgende Fehlermeldung angezeigt:
        else:
            messagebox.showerror("Fehler", "Bitte eine Berechnungsmethode auswählen.")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

# Definieren des Interface Namens und Titels
app = tk.Tk()
app.title("E-Scooter Preisberechnung")

# Erstellung einer Variabel für die Checkbox
var = tk.IntVar()

# Erstellung eines Labels
tk.Label(app, text="E-Scooter Preisberechnung", font=("Arial", 16)).pack(pady=10)

# Erstellung eine Eingabebox für die Grundgebühr
tk.Label(app, text="Grundgebühr (in Euro):").pack(pady=3)
entry_grundgebuehr = tk.Entry(app)
entry_grundgebuehr.pack(pady=6)

# Erstellung eine Eingabebox für den Preis pro Min
tk.Label(app, text="Preis pro Minute (in Euro):").pack(pady=3)
entry_preis_pro_minute = tk.Entry(app)
entry_preis_pro_minute.pack(pady=6)

# Erstellung eine Eingabebox für den Preis pro KM
tk.Label(app, text="Preis pro Kilometer (in Euro):").pack(pady=3)
entry_preis_pro_km = tk.Entry(app)
entry_preis_pro_km.pack(pady=6)

# Erstellung der Checkboxen für Nutzungsdauer und Nutzungsstrecke inklusive Zuweisung und Definitons der Variablen
tk.Radiobutton(app, text="Nutzungsdauer (in Minuten)", variable=var, value=1).pack(pady=5)
tk.Radiobutton(app, text="Nutzungsstrecke (in Kilometern)", variable=var, value=2).pack(pady=5)

# Erstellung eines Labels
tk.Label(app, text="Eingabe:").pack(pady=5)
entry = tk.Entry(app)
entry.pack(pady=5)

# Erstellung und benneung des Berechnungsbuttons
tk.Button(app, text="Berechnen", command=berechne_preis).pack(pady=20)

# Einfügen des Scooteq Logos
image_path = "F:\programming\ScooTec3.png"
img = PhotoImage(file=image_path)
image_label = tk.Label(app, image=img)
image_label.pack(pady=10)


app.mainloop()
