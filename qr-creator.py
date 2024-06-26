import qrcode
import os
# Dados que você deseja codificar no QR Code
while True:  
    data = input("Digite o que você quer transformar em QR Code: ")

    # Criação de uma instância de QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=200,
        border=1,
    )

    # Adicionando dados ao QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Criação de um objeto Image a partir do QR123 Code gerado
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salvando a imagem do QR Code
    nome = input("Digite o nome do arquivo: ")

    img.save(nome + ".png")

    os.system('cls')
    
    print("Arquivo salvo como: ", nome+".png")
