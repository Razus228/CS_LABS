def encrypt_text(plaintext,n):
    ans = ""
    
    for i in range(len(plaintext)):
        ch = plaintext[i]

        if ch==" ":
            ans+= ch.replace(" ", "") 

        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
            
      
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
            ans = ans.upper()
    
    return ans

def decrypt_text(plaintext, n):
    answer = ""

    for j in range(len(plaintext)):
        cz = plaintext[j]

        if cz==" ":
            answer+= cz.replace(" ", "")

        elif (cz.isupper()):
            answer += chr((ord(cz) - n-65) % 26 + 65)
            
      
        else:
            answer += chr((ord(cz) - n-97) % 26 + 97)
            answer = answer.upper()
    return answer

def print_menu():
    print ('1 -- Encrypt' )
    print ('2 -- Decrypt' )
    
            

plaintext = input("Enter text : ")
n = input("Enter key : ")
n = int(n)
while(True):
    print_menu()
    option = ''
    try:
        option = int(input("Enter your choice : "))
    except:
        print("Wrong input ")
    if option == 1:
        encrypt_text(plaintext, n)
        print("Plain Text is : " + plaintext)
        print("Shift pattern is : " + str(n))
        print("Cipher Text is : " + encrypt_text(plaintext,n))
        exit()
    elif option == 2:
        decrypt_text(plaintext, n)
        print("Plain Text is : " + plaintext)
        print("Shift pattern is : " + str(n))
        print("Decipher Text is : " + decrypt_text(plaintext,n))
        exit()


