from cryptography.fernet import Fernet

# Gerar uma chave a partir de uma senha personalizada
def formata_chave_personalizada(senha):
    import hashlib, base64
    chave = hashlib.sha256(senha.encode()).digest()
    return base64.urlsafe_b64encode(chave)

# Criptografar uma mensagem e converter para hexadecimal
def criptografar_mensagem(mensagem, chave_personalizada):
    senhaformatada = formata_chave_personalizada(chave_personalizada)
    fernet = Fernet(senhaformatada)
    mensagem_encriptada = fernet.encrypt(mensagem.encode())
    # Converter a mensagem criptografada para hexadecimal
    return mensagem_encriptada.hex()

# Descriptografar a mensagem a partir do hexadecimal
def descriptografar_mensagem(mensagem_encriptada, chave_personalizada):
    fernet = Fernet(formata_chave_personalizada(chave_personalizada))
    # Converter o hexadecimal de volta para bytes
    mensagem_encriptada_bytes = bytes.fromhex(mensagem_encriptada)
    mensagem_descriptografada = fernet.decrypt(mensagem_encriptada_bytes).decode()
    return mensagem_descriptografada


