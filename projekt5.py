# Ett program där man kan spela sten, sax, påse mot datorn

try:
    användarens_val = input("välj sten, sax eller påse (sten/sax/påse): ").lower()
    if användarens_val not in ["sten", "sax", "påse"]:
        raise ValueError("Ogiltigt val. Välj sten, sax eller påse.")
except ValueError as e:
    print(e)
    exit()

# Datorn ska slumpa fram ett val(Sten, sax eller påse)
# Visa användarens val och datorns val
# Bestäm vem som vinner och skriv ut resultatet
# Fråga användaren om de vill spela igen, om de svarar ja, starta om spelet, annars avsluta programmet