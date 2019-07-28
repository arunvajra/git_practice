import string

alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
name = input("Enter a string \n") 
enc_or_dec = input("Do you want to Encrypt or Decrypt? \n").upper()
key = int(input("Enter the key \n"))
new_list = []
code_list = []

print(enc_or_dec + "ED")

for x in name:

    alpha_index = string.ascii_lowercase.index(x.lower()) #alphabetical index 
    int_alpha_index = int(alpha_index)

    if enc_or_dec == "ENCRYPT":
    
        list_add = new_list.append(int_alpha_index + key)

    else:

        list_add = new_list.append(int_alpha_index - key) 
    
# print(new_list)

for x in range(0,len(name)):
    code = new_list[x]
    string = alpha_list[code]
    code_list.append(string)

print(code_list)

# converting from list to string
final_string = ''.join(code_list)
print(final_string.upper())

    
  

