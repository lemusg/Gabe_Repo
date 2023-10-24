from Labs.encode import encode
from Labs.decode import decode


def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    user = input('Please enter an option: ')
    return int(user)


password = ''

if __name__ == '__main__':
    while True:
        user_input = main()
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif user_input == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
            print()
        elif user_input == 3:
            exit()
        else:
            continue
