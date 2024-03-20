caesar="tqjzfxfdemcplvespwlhozteezdptkpazhpctylwwzespcnldpdzmdpcgptetnlxptdlhtnzybfpcpotetdmpeepcezncplepeslyezwplcyncpletyrtdesppddpynpzqtqpldlcfwpxpyhzccjxzcplmzfehsleespjnlyedppeslylmzfehsleespjnlytetdpldtpcezqtyoxpyhszhtwwgzwfyeppcezotpeslyezqtyoeszdphszlcphtwwtyrezpyofcpaltyhtesaletpyn"
shift=int(input("Enter the shift value: "))
def salad(caesar,shift):
    result=""
    for ch in caesar:
        if ch.isalpha():
            soup = ord(ch) - shift
            if soup < ord('a'):
                soup += 26
            fL = chr(soup)
            result+= fL
    print(result)
    return result
salad(caesar,shift)