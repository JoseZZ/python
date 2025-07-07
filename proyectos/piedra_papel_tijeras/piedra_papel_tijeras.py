import random


def play():
    user_choice = input("Elige R para piedra, P para papel o T para tijeras: ").upper()
    while user_choice not in ['R', 'P', 'T']:
        user_choice = input("Entrada inválida. Elige R para piedra, P para papel o T para tijeras: ").upper()
    computer_choice = random.choice(['R', 'P', 'T'])
    values = {'R': 'Piedra', 'P': 'Papel', 'T': 'Tijeras'}

    # Comprobar el resultado
    if user_choice == computer_choice:
        print(f"Ambos eligieron {values[user_choice]}. ¡Es un empate!")
    elif (user_choice == 'R' and computer_choice == 'T' or user_choice == 'P' and computer_choice == 'R' or
          user_choice == 'T' and computer_choice == 'P'):
        print(f"Tú eliges {values[user_choice]} y la computadora elige {values[computer_choice]}. ¡Tú ganas!")
    else:
        print(
            f"Tú eliges {values[user_choice]} y la computadora elige {values[computer_choice]}. ¡La computadora gana!")


continuar = 'S'
while continuar.upper() == 'S':
    play()
    continuar = input("¿Quieres jugar de nuevo? (S/N): ")
