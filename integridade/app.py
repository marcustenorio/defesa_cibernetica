import hashlib
import os


ARQUIVO_MENSAGEM = "mensagem.txt"
ARQUIVO_HASH = "hash.txt"


def calcular_hash(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def salvar_mensagem():
    mensagem = input("Digite a mensagem a ser protegida: ")

    with open(ARQUIVO_MENSAGEM, "w", encoding="utf-8") as f:
        f.write(mensagem)

    hash_mensagem = calcular_hash(mensagem)

    with open(ARQUIVO_HASH, "w", encoding="utf-8") as f:
        f.write(hash_mensagem)

    print("\nMensagem salva com sucesso.")
    print("Hash SHA-256 gerado:")
    print(hash_mensagem)


def verificar_integridade():
    if not os.path.exists(ARQUIVO_MENSAGEM) or not os.path.exists(ARQUIVO_HASH):
        print("\nErro: mensagem ou hash não encontrados.")
        return

    with open(ARQUIVO_MENSAGEM, "r", encoding="utf-8") as f:
        mensagem_atual = f.read()

    with open(ARQUIVO_HASH, "r", encoding="utf-8") as f:
        hash_original = f.read().strip()

    hash_atual = calcular_hash(mensagem_atual)

    print("\nHash original :", hash_original)
    print("Hash atual    :", hash_atual)

    if hash_original == hash_atual:
        print("\nIntegridade confirmada: a informação não foi alterada.")
    else:
        print("\nAlerta: a informação foi alterada!")


def menu():
    while True:
        print("\n=== SISTEMA DE INTEGRIDADE ===")
        print("1 - Salvar mensagem e gerar hash")
        print("2 - Verificar integridade da mensagem")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            salvar_mensagem()
        elif opcao == "2":
            verificar_integridade()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
