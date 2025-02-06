from utils.limpeza_menu_e_exibir_titulo import limpeza_e_exibicao
from menu.menu_principal import menu_principal

def escolha_menu_principal():
    try:
        numero_escolha = int(input('Qual parte deseja escolher? '))

        if numero_escolha == 1:
            print('Criação personagem em criação')
        elif numero_escolha == 2:
            print('Rolagem de dados em criação')
        elif numero_escolha == 3:
            limpeza_e_exibicao('Saindo da aplicação')
    except:
        limpeza_e_exibicao('Opção invalidada, voltando ao menu principal')
        menu_principal()

