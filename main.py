from event import get_data

def agenda_formatada(selected_day, data):
    print("______________________________________________________________________")
    print(f"    {selected_day}")
    print("______________________________________________________________________")
    print(f"    Hour    -   Activity ")
    print("______________________________________________________________________")
    for d in data:
        print(f"{d['horario_inicio']} - {d['horario_fim']} | {d['titulo']}")
    print("______________________________________________________________________")

def main():
    while True:
        print(" ")
        print("______________________________________________________________________")
        print("     Escolha o dia de evento que você quer participar:")
        print("1. Monday")
        print("2. Tuesday")
        print("3. Wednesday")
        print("4. Thursday")
        print("5. Friday")
        print("6. Saturday")
        print("7. Sunday")
        print("0. Exit")

        choice = input("Selecione a opção equivalente de 0 a 7: ")

        if choice == '0':
            print("Saindo... Até mais!")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            selected_day = days[int(choice) - 1]
            data = get_data(selected_day)
            agenda_formatada(selected_day, data)
            break
        else:
            print("Escolha inválida. Por favor escolha um número de 0 a 7.")

if __name__ == "__main__":
    main()