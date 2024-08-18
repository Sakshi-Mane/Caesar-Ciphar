alphabets = ['a' , 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','@','#','$',
             '2','5', '9','%','&','1','4','7','*','^','/','3','6','8' ]
# print(len(alphabets))
def caesarCiphar(original_text, shift_amount, encode_decode):
    output_text=""
    if encode_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabets)
            output_text+=alphabets[shifted_position]
    print(f"Here is your cipher:{output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesarCiphar(original_text=text, shift_amount=shift, encode_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")

    if restart == "no":
        should_continue = False
        print("See you!")





