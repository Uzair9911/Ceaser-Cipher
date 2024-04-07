import tkinter as tk
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def on_encrypt():
    plaintext = entry_plaintext.get()
    shift = int(entry_shift.get())
    encrypted_text = encrypt(plaintext, shift)
    result_label.config(text="Encrypted text: " + encrypted_text)

def on_decrypt():
    ciphertext = entry_plaintext.get()  
    shift = int(entry_shift.get())
    decrypted_text = decrypt(ciphertext, shift)
    result_label.config(text="Decrypted text: " + decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher")

label_plaintext = tk.Label(root, text="Enter text:")
label_plaintext.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_plaintext = tk.Entry(root)
entry_plaintext.grid(row=0, column=1, padx=10, pady=5)

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_shift = tk.Entry(root)
entry_shift.grid(row=1, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=10, pady=5)

root.mainloop()
