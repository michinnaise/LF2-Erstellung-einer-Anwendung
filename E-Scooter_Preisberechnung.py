import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def berechne_preis_dauer(dauer, grundgebuehr, preis_pro_minute):
    return grundgebuehr + (preis_pro_minute * dauer)

def berechne_preis_strecke(strecke, grundgebuehr, preis_pro_km):
    return grundgebuehr + (preis_pro_km * strecke)

def berechne_preis():
    try:
        grundgebuehr = float(entry_grundgebuehr.get())
        preis_pro_minute = float(entry_preis_pro_minute.get())
        preis_pro_km = float(entry_preis_pro_km.get())
        
        if var.get() == 1:
            dauer = float(entry.get())
            preis = berechne_preis_dauer(dauer, grundgebuehr, preis_pro_minute)
            messagebox.showinfo("Preisberechnung", f"Der Fahrpreis beträgt: {preis:.6f} Euro")
        elif var.get() == 2:
            strecke = float(entry.get())
            preis = berechne_preis_strecke(strecke, grundgebuehr, preis_pro_km)
            messagebox.showinfo("Preisberechnung", f"Der Fahrpreis beträgt: {preis:.6} Euro")
        else:
            messagebox.showerror("Fehler", "Bitte eine Berechnungsmethode auswählen.")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")

app = tk.Tk()
app.title("E-Scooter Preisberechnung")

var = tk.IntVar()

tk.Label(app, text="E-Scooter Preisberechnung", font=("Arial", 16)).pack(pady=10)

tk.Label(app, text="Grundgebühr (in Euro):").pack(pady=3)
entry_grundgebuehr = tk.Entry(app)
entry_grundgebuehr.pack(pady=6)

tk.Label(app, text="Preis pro Minute (in Euro):").pack(pady=3)
entry_preis_pro_minute = tk.Entry(app)
entry_preis_pro_minute.pack(pady=6)

tk.Label(app, text="Preis pro Kilometer (in Euro):").pack(pady=3)
entry_preis_pro_km = tk.Entry(app)
entry_preis_pro_km.pack(pady=6)

tk.Radiobutton(app, text="Nutzungsdauer (in Minuten)", variable=var, value=1).pack(pady=5)
tk.Radiobutton(app, text="Nutzungsstrecke (in Kilometern)", variable=var, value=2).pack(pady=5)

tk.Label(app, text="Eingabe:").pack(pady=5)
entry = tk.Entry(app)
entry.pack(pady=5)

tk.Button(app, text="Berechnen", command=berechne_preis).pack(pady=20)

image_path = "F:\programming\ScooTec3.png"
img = PhotoImage(file=image_path)
image_label = tk.Label(app, image=img)
image_label.pack(pady=10)


app.mainloop()
