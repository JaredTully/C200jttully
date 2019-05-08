def hex_dec(hex):
    if hex:
        return int(hex[0], 16) * (16 ** (len(hex) -1)) + hex_dec(hex[1::])
    else:
        return 0

hex = input("Hex: ")

print(hex_dec(hex))