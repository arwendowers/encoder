# Arwen Dowers

def encode(password):                         # encodes inputted password
    encoded_password = ''                     # starts as an empty string
    for digit in password:                    # goes through each number of password
        new_digit = int(digit) + 3            # adds 3 to each digit
        if new_digit > 9:                     # if new digit is two digits,
            new_digit -= 10                   # subtracts 10 to roll digit over into one digit
        encoded_password += str(new_digit)    # adds new digits to encoded password string
    return encoded_password

def decode(encoded_password):
    decoded_password_list = []
    for number in encoded_password:
        number = int(number)
        if number <= 3:
            decoded_password_list.append((number + 10 - 3) % 10)
        else:
            decoded_password_list.append(number - 3)
    decoded_password = "".join(str(num) for num in decoded_password_list)
    return decoded_password

# takes an encoded password and decodes it

def main():
    option = 0
    password = 'none'  # prints 'none' statements if no password has been inputted when decoding
    encoded_password = 'none'
    while option != 3:  # option 3 is Quit
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        print()
        option = int(input('Please enter an option: '))
        while 1 <= option <= 2:
            if option == 1:  # Encode
                password = input('Please enter your password to encode: ')  # user inputs password
                encoded_password = encode(password)  # calls encode function, then stored in variable
                print('Your password has been encoded and stored!')
                print()
                break
            if option == 2:  # Decode
                password = decode(encoded_password) if password != 'none' else 'none'
                print(f'The encoded password is {encoded_password}, and the original password is {password}.')
                print()
                break


if __name__ == '__main__':
    main()
