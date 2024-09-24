import numpy as np

# Function to convert letter to number (A = 0, B = 1, ..., Z = 25)
def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

# Function to convert number to letter (0 = A, 1 = B, ..., 25 = Z)
def num_to_letter(num):
    return chr((num % 26) + ord('A'))

# Encrypt a block of plaintext using the key matrix
def encrypt_block(plain_block, key_matrix):
    plain_numbers = [letter_to_num(c) for c in plain_block]
    result = np.dot(key_matrix, plain_numbers) % 26
    return ''.join([num_to_letter(num) for num in result])

# Decrypt a block of ciphertext using the inverse key matrix
def decrypt_block(cipher_block, key_matrix_inverse):
    cipher_numbers = [letter_to_num(c) for c in cipher_block]
    result = np.dot(key_matrix_inverse, cipher_numbers) % 26
    return ''.join([num_to_letter(num) for num in result])

# Encrypt the entire plaintext using Hill Cipher
def hill_cipher_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]
    
    # Padding plaintext if necessary
    if len(plaintext) % block_size != 0:
        plaintext += 'X' * (block_size - len(plaintext) % block_size)
    
    ciphertext = ''
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        ciphertext += encrypt_block(block, key_matrix)
    
    return ciphertext

# Decrypt the entire ciphertext using Hill Cipher
def hill_cipher_decrypt(ciphertext, key_matrix):
    # Step 1: Compute the determinant of the key matrix
    determinant = int(np.round(np.linalg.det(key_matrix)))
    print(f"Determinant of the key matrix: {determinant}")
    
    # Step 2: Compute the modular inverse of the determinant modulo 26
    determinant_inverse = pow(determinant, -1, 26)
    print(f"Modular inverse of the determinant modulo 26: {determinant_inverse}")
    
    # Step 3: Compute the adjugate (adjoint) of the key matrix
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * determinant).astype(int)
    print(f"Adjugate matrix of the key matrix:\n{adjugate_matrix}")
    
    # Step 4: Compute the inverse of the key matrix modulo 26
    key_matrix_inverse = (determinant_inverse * adjugate_matrix) % 26
    print(f"Inverse key matrix modulo 26:\n{key_matrix_inverse}")
    
    block_size = key_matrix.shape[0]
    plaintext = ''
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        plaintext += decrypt_block(block, key_matrix_inverse)
    
    return plaintext

# Function to display the key matrix with corresponding alphabets
def display_key_matrix_alphabets(key_matrix):
    print("Corresponding alphabets of the key matrix numbers:")
    for row in key_matrix:
        row_alphabets = [num_to_letter(num) for num in row]
        print(" ".join(row_alphabets))

# Function to get key matrix from user input
def get_key_matrix(matrix_size):
    print(f"Enter the key matrix of size {matrix_size}x{matrix_size}..!!")
    key_matrix = []
    for i in range(matrix_size):
        row = list(map(int, input(f"Enter row {i+1} values separated by space: ").split()))
        key_matrix.append(row)
    key_matrix = np.array(key_matrix)
    
    display_key_matrix_alphabets(key_matrix)
    
    return key_matrix

# Main function to run the Hill Cipher encryption and decryption
def main():
    matrix_size = int(input("Enter the size of the key matrix : "))
    key_matrix = get_key_matrix(matrix_size)
    
    plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
    
    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"Encrypted text: {ciphertext}")
    
    decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
3
