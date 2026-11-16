import sqlite3


def data_vault_spaguetti():
    # CONEXÃO DIRETA NO MEIO DO CÓDIGO
    conexao = sqlite3.connect('vault_original.db')
    cursor = conexao.cursor()

    # CRIAÇÃO DE TABELA MISTURADA COM A INTERFACE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suspeitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crime TEXT NOT NULL,
            periculosidade INTEGER NOT NULL
        )
    """)
    conexao.commit()

    while True:
        print("\n--- 🕵️ ARQUIVO MORTO (SISTEMA ANTIGO) ---")
        print("1. Cadastrar Suspeito")
        print("2. Listar Todos")
        print("0. Sair")

        escolha = input("O que deseja? ")

        if escolha == '1':
            # INTERFACE, VALIDAÇÃO E SQL COLADOS
            nome = input("Nome do meliante: ")
            crime = input("Delito: ")
            nivel = input("Nível de perigo (1-10): ")

            # INSERE DADOS NA TABELA
            cursor.execute(
                "INSERT INTO suspeitos (nome, crime, periculosidade) VALUES (?, ?, ?)",
                (nome, crime, int(nivel))
            )
            conexao.commit()
            print("Registro jogado na gaveta!")

        elif escolha == '2':
            # BUSCA E EXIBIÇÃO MISTURADAS
            cursor.execute("SELECT * FROM suspeitos")
            linhas = cursor.fetchall()
            print("\n--- FICHA CRIMINAL ---")
            for linha in linhas:
                print(f"ID: {linha[0]} | Suspeito: {linha[1]} | Crime: {linha[2]} | Perigo: {linha[3]}/10")

        elif escolha == '0':
            conexao.close()
            print("Desligando...")
            break
        else:
            print("Comando inválido!")


if __name__ == "__main__":
    data_vault_spaguetti()
