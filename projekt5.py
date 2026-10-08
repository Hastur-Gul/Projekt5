# Ett program där man kan spela sten, sax, påse mot datorn
import random

val = ("sten", "sax", "påse")

try:
    användarens_val = input("Välj sten, sax eller påse (sten/sax/påse): ").lower()
    if användarens_val not in ("sten", "sax", "påse"):
        raise ValueError("Ogiltigt val. Välj sten, sax eller påse.")
except ValueError as e:
    while användarens_val not in ("sten", "sax", "påse"):
        print(e)
        användarens_val = input("Välj sten, sax eller påse (sten/sax/påse): ").lower()

datorns_val = random.choice(val)

print(f"Du valde: {användarens_val}")
print(f"Datorn valde: {datorns_val}")

# Bestäm vem som vinner och skriv ut resultatet
# Fråga användaren om de vill spela igen, om de svarar ja, starta om spelet, annars avsluta programmet