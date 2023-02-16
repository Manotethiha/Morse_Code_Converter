MORSE_CODE = {
  'a': ".-",
  'b': "-...",
  'c': "-.-.",
  'd': "-..",
  'e': ".",
  'f': "..-.",
  'g': "--.",
  'h': "....",
  'i': "..",
  'j': ".---",
  'k': "-.-",
  'l': ".-..",
  'm': "--",
  'n': "-.",
  'o': "---",
  'p': ".--.",
  'q': "--.-",
  'r': ".-.",
  's': "...",
  't': "-",
  'u': "..-",
  'v': "...-",
  'w': ".--",
  'x': "-..-",
  'y': "-.--",
  'z': "--..",
  '1': ".----",
  '2': "..---",
  '3': "...--",
  '4': "....-",
  '5': ".....",
  '6': "-....",
  '7': "--...",
  '8': "---..",
  '9': "----.",
  '0': "-----",
}

while True:
  option = input("Would you like to encrypt or decrypt morse code? : ")
  option = option.lower()
  if option == "encrypt":
    
    user_message = input("\nWhat is your message? : ")
    user_message = user_message.lower()
    encrypt_message = ""
    
    for word in user_message:
      if word in MORSE_CODE:
        encrypt_message += MORSE_CODE[word] + " "
  
      elif word == " ":
        encrypt_message += "|" + " "
        
      else:
        print(f"\nCan't encrypt for '{word}'. It'll display as '*'\n")
        encrypt_message += "*" + " "

    print("\n  * Space between words is encrypted as '|'\n")
    print(f"The morse code for your message :\n{encrypt_message}\n")
    
  
  elif option == "decrypt":

    print("\n  * Seperate with space between codes\n  * Enter '|' for space between words\n  * Example: .... . .-.. .-.. --- | .-- --- .-. .-.. -.. >>> hello world\n  * The output will be lower case\n")
    user_code = input("What is your code? : ")
    split_code = user_code.split(" ")
    
    decrypt_message = ""  
    
    for code in split_code:
      if code == "|":
          decrypt_message += " "
  
      else:
        for key,value in MORSE_CODE.items():
          if code == value:
            decrypt_message += key

          elif code == key:
            print(f"\nCan't decrypt for '{code}'. It'll display as '*'")
            decrypt_message += "*"
          
          else:
            continue   

    print(f"\nThe decode message of your code :\n{decrypt_message}\n")

  elif option == "exit" or option == "e":
    break
  
  else:
    print("\nSorry, it's not available!\n")


    
  


