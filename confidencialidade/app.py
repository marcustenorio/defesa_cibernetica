def cifra_cesar(texto, chave):
    resultado = ""

    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            deslocado = (ord(char) - base + chave) % 26
            resultado += chr(base + deslocado)
        else:
            resultado += char

    return resultado


def decifra_cesar(texto, chave):
    return cifra_cesar(texto, -chave)


def salvar_mensagem(mensagem_cifrada):
    with open("segredo.txt", "w") as f:
        f.write(mensagem_cifrada)


def ler_mensagem():
    try:
        with open("segredo.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


# ============================
# MENU PRINCIPAL
# ============================

def menu():
    while True:
        print("\n=== SISTEMA DE CONFIDENCIALIDADE ===")
        print("1 - Escrever mensagem secreta")
        print("2 - Ler mensagem secreta")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            mensagem = input("Digite a mensagem secreta: ")
            chave = int(input("Digite a chave: "))

            cifrada = cifra_cesar(mensagem, chave)
            salvar_mensagem(cifrada)

            print("\nMensagem armazenada com segurança (cifrada).")

        elif opcao == "2":
            chave = int(input("Digite a chave para leitura: "))

            mensagem_cifrada = ler_mensagem()

            if mensagem_cifrada is None:
                print("Nenhuma mensagem encontrada.")
                continue

            decifrada = decifra_cesar(mensagem_cifrada, chave)

            print("\nMensagem decifrada:")
            print(decifrada)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
