def shift_encrypt(text, clicks):
    encrypted_text = ""

    # 1~10,000 범위로 각 문자를 시프트
    for i, char in enumerate(text):
        shift_value = (i + 1 + clicks) % 10000  # clicks에 따라 시프트 값 조정
        shifted_char = chr((ord(char) + shift_value) % 1114112)  # 유니코드 전체 범위에서 순환
        encrypted_text += shifted_char

    return encrypted_text

def shift_decrypt(encrypted_text, clicks):
    decrypted_text = ""

    # 1~10,000 범위로 각 문자를 역 시프트
    for i, char in enumerate(encrypted_text):
        shift_value = (i + 1 + clicks) % 10000  # clicks에 따라 시프트 값 조정
        shifted_char = chr((ord(char) - shift_value) % 1114112)  # 유니코드 전체 범위에서 순환
        decrypted_text += shifted_char

    return decrypted_text

# 원본 플래그
plaintext = "MJSEC{}"

# 10,000번 암호화 실행
clicks = 0  # 초기 클릭 수
encrypted_text = plaintext  # 초기화

for _ in range(10000):
    encrypted_text = shift_encrypt(encrypted_text, clicks)
    clicks += 1  # 클릭 수 증가

# 암호화된 결과 출력
print(f"Encrypted text after 10,000 encryptions: {encrypted_text}")

# 10,000번 복호화 실행
decrypted_text = encrypted_text  # 초기화
clicks = 0  # 클릭 수 초기화

for _ in range(10000):
    decrypted_text = shift_decrypt(decrypted_text, clicks)
    clicks += 1  # 클릭 수 증가

# 복호화된 결과 출력
print(f"Decrypted text after 10,000 decryptions: {decrypted_text}")

# 암호화된 텍스트를 파일로 저장하는 코드
file_path = "encrypted_text.txt"

# UTF-8 인코딩으로 파일 저장
with open(file_path, "w", encoding="utf-8") as file:
    file.write(encrypted_text)

print(f"Encrypted text saved to {file_path}")
