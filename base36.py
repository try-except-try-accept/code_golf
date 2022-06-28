def conv(num, base):
    c=1
    last=c
    while base**c < num:
        last = c
        c += 1

    c=last

    out = ""

    while c>=0:

        fits = num // base**c
        out += str(fits) if fits < 10 else chr(fits+55)
        this_col_val = fits*(base**c)
        if fits > 0:
            num = num % this_col_val
 
        c -= 1
    return out
