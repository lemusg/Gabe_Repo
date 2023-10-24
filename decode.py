#Sebastian Dion

def decode(password):
    decopass = ''
    for i in password:
        if int(i) -3 == -3:
            decopass += '7'
        elif int(i) - 3 == -2:
            decopass += '8'
        elif int(i) - 3 == -1:
            decopass += '9'
        else:
            decopass += str((int(i) - 3))
    return decopass