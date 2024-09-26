def luhn_algorithm(card_number):
    total_sum = 0
    length = len(card_number)

    for i in range(length - 1, -1, -1):
        digit = int(card_number[i])

        if (length - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9

        total_sum += digit

    return total_sum % 10 == 0

def identify_card_type(card_number):
    length = len(card_number)

    if length == 15 and card_number.startswith(('34', '37')):
        return "AMEX"
    elif length == 16 and card_number.startswith(('51', '52', '53', '54', '55')):
        return "MASTERCARD"
    elif (length == 13 or length == 16) and card_number.startswith('4'):
        return "VISA"
    else:
        return "INVALID"

def main():
    card_number = input("Enter credit card number: ")

    if not card_number.isdigit():
        print("INVALID")
        return

    if luhn_algorithm(card_number):
        card_type = identify_card_type(card_number)
        print(card_type)
    else:
        print("INVALID")

if __name__ == "__main__":
    main()
