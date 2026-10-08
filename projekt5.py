# Ett program där man kan spela sten, sax, påse mot datorn
import random

val = ("sten", "sax", "påse")

while True:
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

    if användarens_val == datorns_val:
        print("Oavgjort!")
    elif \
    (användarens_val == "sten" and datorns_val == "sax") or \
    (användarens_val == "sax" and datorns_val == "påse") or \
    (användarens_val == "påse" and datorns_val == "sten"):
        print("Du vinner!")
    else:
        print("Datorn vinner!")

    spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
    while spela_igen not in ("ja", "nej"):
        print("Ogiltigt svar. Välj ja eller nej.")
        spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
    if spela_igen == "nej":
        print("Tack för att du spelade!")
        break
    else:
        continue
