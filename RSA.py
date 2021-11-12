from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


def generatekeys():
    key = RSA.generate(2048)
    pubKey = key.public_key().exportKey('PEM').decode()
    publicKeyFile = open('publicKey.pem', 'w')
    publicKeyFile.write(pubKey)
    publicKeyFile.close()
    print("CLE PUBLIQUE OK\n")

    privKey = key.exportKey('PEM').decode()
    privateKeyFile = open('privateKey.pem', 'w')
    privateKeyFile.write(privKey)
    privateKeyFile.close()
    print("CLE PRIVÉE OK\n")

    return 0


def encryptdata(message):
    key_text = open(input("Entrez le nom du fichier contenant la clé publique du destinataire : "), "rb").read()
    public_key = RSA.importKey(key_text)
    cipher = PKCS1_v1_5.new(public_key)
    message = message.encode()
    encrypted_bytes = cipher.encrypt(message)
    return base64.b64encode(encrypted_bytes)


def decryptdata(ciphertext):
    key_text = open(input("Entrez le nom du fichier contenant votre clé privée : "), "rb").read()
    private_key = RSA.importKey(key_text)
    cipher = PKCS1_v1_5.new(private_key)
    text = base64.b64decode(ciphertext)
    return cipher.decrypt(text, "ERREUR")


print("#############################################")
print("##### CHIFFREMENT - DECHIFFREMENT RSA #######")
print("#############################################")
print("\nBienvenue dans cet outil développé par K3RM1T, que souhaitez vous faire ?\n")
print("   1: Générer une paire de clés privée/publique")
print("   2: Chiffrer un message")
print("   3: Déchiffrer un message\n")
resultChoice = int(input("Entrez votre choix : "))

if resultChoice == 2:
    dataEncrypted = encryptdata(input("Entrez votre message à chiffrer : "))
    print(dataEncrypted.decode())
if resultChoice == 3:
    dataDecrypted = decryptdata(input("Entrez le message à déchiffrer : "))
    print(dataDecrypted.decode())
if resultChoice == 1:
    generatekeys()