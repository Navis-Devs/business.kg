import base64

def string_to_binary(text):
    binary_representation = ' '.join(format(ord(char), '08b') for char in text)
    return binary_representation

def binary_to_base64(binary_str):
    encoded_bytes = base64.b64encode(binary_str.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

text_input = input("your words: ")
binary_result = string_to_binary(text_input)
print("Binary result:", binary_result)

base64_result = binary_to_base64(binary_result)
print("Base64 result:", base64_result)
