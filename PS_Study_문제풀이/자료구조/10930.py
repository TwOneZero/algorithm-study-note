import hashlib

input_data = input()
encoded_data = input_data.encode() #바이트 객체로
result = hashlib.sha256(encoded_data).hexdigest()
print(result)