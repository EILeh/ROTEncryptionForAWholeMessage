"""
ROT-Encryption for a whole message

Program reads the encrypted message from the user as a whole (the message is
ended by entering an empty row). After this, the message is printed as
encrypted. The program performs the ROT13 transformation for a line.
It can be assumed that the parameter is always a character, i.e., a string
consisting of a single character.

Writer of the program: EILeh

"""

def read_message():
    """
    Reads given message and checks if it is empty or not. If it isn't empty,
    function adds message to a list otherwise breaks the loop.
    :return: str, parameter if it is not empty row
    """

    input_text = ""
    msg = []
    not_empty_row = True

    # As long as row is not empty, the program will ask an input.
    while not_empty_row:
        input_text = input()

        # If user input is not empty, a new text is added to the list msg.
        if input_text:
            msg.append(input_text)

        # If input is empty, the variable not_empty_row value will be changed
        # to False.
        else:
            not_empty_row = False

    # Calls the function row_encryption with the input_text as its' parameter.
    row_encryption(input_text)

    # Returns the list msg.
    return msg


def encrypt(current_letter_at_text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param current_letter_at_text: char,  char to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    is_found = False
    capitalized_text = current_letter_at_text.lower()
    capitalized_encrypted_text = ""
    empty_string = ""
    wanted_encrypted_index = ""

                    #   0    1    2    3    4    5    6    7    8    9    10
    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                    #  11   12   13   14   15   16   17   18   19   20    21
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                    #  22   23   24   25
                       "w", "x", "y", "z"]


                    #   0    1    2    3    4    5    6    7    8    9    10
    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                    #  11   12   13   14   15   16   17   18   19   20    21
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                    #  22   23   24   25
                       "j", "k", "l", "m"]

    # Checks that current_letter_at_text is found in regular chars.
    if current_letter_at_text in regular_chars:
        is_found = True

        if is_found:
            # Initializes a new variable to get the index of the current letter.
            wanted_index = regular_chars.index(current_letter_at_text)

            # Initializes a new variable to get the encrypted letter.
            wanted_encrypted_index = encrypted_chars[wanted_index]

        # Returns the encrypted char.
        return wanted_encrypted_index

    # Checks that capitalized_text is found in regular chars.
    if capitalized_text in regular_chars:
        is_found = True

        if is_found:
            # Initializes a new variable to get the index of the current letter.
            wanted_index = regular_chars.index(capitalized_text)

            # Initializes a new variable to get the encrypted letter.
            wanted_encrypted_index = encrypted_chars[wanted_index]

            # Initializes a new varibale to get the uppercase letters correctly.
            capitalized_encrypted_text = wanted_encrypted_index.upper()

        # Returns the encrypted char.
        return capitalized_encrypted_text

    # If current char is not found in regular chars.
    if current_letter_at_text not in regular_chars:
        is_found = True

        if is_found:

            # Initializes a new variable that stores the information of the
            # char that is not found in regular chars.
            no_index = current_letter_at_text

        # Returns the char as it is.
        return current_letter_at_text

    # Checks if the currents char is space.
    if current_letter_at_text == empty_string:

        # Returns the variable empty_string as it is.
        return empty_string


def row_encryption(text):
    """
    Encrypts the entire list.
    :param text: given text that is being ecrypted
    :return: string_line
    """

    string_line = ""
    text_length = 0
    text_length = len(text)

    # Starting from zero, stays in the loop for the length of the text.
    for char in range(0, text_length, 1):
        # Calls the function encrypt at every char and adds the value gotten
        # from the encryption function to the variable string_line.
        string_line += encrypt(text[char])

    # return the formed variable string_line.
    return string_line


def main():

    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()
    msg_at_current_index = 0
    msg_length = 0
    msg_length = len(msg)

    print("ROT13:")

    # As long as the variable msg_at_current_index is smaller that the
    # variable msg_length, loop is done.
    while msg_at_current_index < msg_length:
        
        input_text = msg[msg_at_current_index]

        print(row_encryption(input_text))

        msg_at_current_index += 1

if __name__ == "__main__":
    main()