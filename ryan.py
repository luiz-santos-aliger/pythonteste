
from typing import List

def obter_dados_aluno():
    """
    Função com EFEITO COLATERAL (interage com o usuário).
    Pede o nome e as notas do aluno.
    - Demonstra: 'input()', loop 'while', 'try/except' e retorno de TUPLA.
    - Retorna: Uma tupla contendo (nome_do_aluno, lista_de_notas).
    """
    print("--- Cadastro de Aluno ---")
    nome = input("Digite o nome do aluno: ")
    
    notas = []
    while True:
        nota_str = input(f"Digite uma nota para {nome} (ou 'fim' para parar): ")
        
        if nota_str.lower() == 'fim':
            break # Quebra o loop 'while'
            

        nota_valida = validar_nota(nota_str)
        
        if nota_valida is not None:
            notas.append(nota_valida)
            print(f"Nota {nota_valida} adicionada.")
        else:
            print(f"'{nota_str}' não é uma nota válida (use 0 a 10).")

    return nome, notas

def validar_nota(nota_str: str):
    """
    Função AUXILIAR (Helper Function).
    Tenta converter uma string em uma nota válida (float de 0 a 10).
    - Demonstra: 'try/except' e retorno condicional ('float' ou 'None').
    """
    try:
        nota = float(nota_str)
        if 0 <= nota <= 10:
            return nota
        else:
          
            return None
    except ValueError:
    
        return None

def calcular_media(lista_de_notas: List[float]) -> float:
    """
    Função PURA (sem efeitos colaterais).
    Recebe uma lista de números e retorna a média.
    - Demonstra: Parâmetro (list), retorno (float), 'sum()' e 'len()'.
    """
    if not lista_de_notas: 
        print("Aviso: Nenhuma nota foi inserida. Média será 0.")
        return 0.0
        
    total = sum(lista_de_notas)
    media = total / len(lista_de_notas)
    return media

def verificar_status(media: float, media_aprovacao: float = 6.0) -> str:
    """
    Função PURA.
    Determina se o aluno foi aprovado ou reprovado.
    - Demonstra: Parâmetro com VALOR PADRÃO ('media_aprovacao=6.0').
    - Demonstra: Operador Ternário (if/else em uma linha).
    """
  
    status = "Aprovado" if media >= media_aprovacao else "Reprovado"
    return status

def exibir_relatorio(nome: str, notas: List[float], media_final: float, status: str):
    """
    Função com EFEITO COLATERAL (imprime na tela).
    Não retorna nada (implicitamente retorna 'None').
    - Demonstra: Recebendo múltiplos parâmetros e formatando 'print'.
    """
    print(f"\n--- Relatório Final do Aluno ---")
    print(f"Nome:   {nome}")
    print(f"Notas:  {notas}")

    print(f"Média:  {media_final:.2f}") 
    print(f"Status: {status}")


def main():
    """
    Função principal que organiza e executa o fluxo do programa.
    Ela CHAMA todas as outras funções na ordem correta.
    """
   
    nome_aluno, lista_de_notas = obter_dados_aluno()

    media_calculada = calcular_media(lista_de_notas)

    status_final = verificar_status(media_calculada)
    
    exibir_relatorio(nome_aluno, lista_de_notas, media_calculada, status_final)

if __name__ == "__main__":
    main()