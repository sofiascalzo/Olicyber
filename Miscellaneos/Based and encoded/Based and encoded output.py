def octal_to_ascii(octal_array):
    ascii_string = ""
    for octal in octal_array:
        decimal = int(str(octal), 8)
        character = chr(decimal)
        ascii_string += character
    return ascii_string


numeri = [47, 173, 144, 63, 143, 60, 144, 63, 137, 164, 150, 61, 163, 137, 60, 156, 137, 146, 60, 162, 137, 163, 61, 172, 63, 137, 155, 162, 137, 142, 60, 156, 144, 1]  # Array di numeri ASCII
flag = octal_to_ascii(numeri)
print(flag)

#flag{d3c0d3_th1s_0n_f0r_s1z3_mr_b0nd}