assentos = [[0 for _ in range(8)] for _ in range(5)]

# Exibir o mapa de assentos
def exibir_assentos():
    print("Mapa de assentos (0 = livre, 1 = reservado):")
    for i in range(5):
        print(assentos[i])
    print()  # linha em branco pra separar

# Reservar um assento
def reservar_assento(fileira, numero):
    if assentos[fileira-1][numero-1] == 0:
        assentos[fileira-1][numero-1] = 1
        print(f"Assento ({fileira},{numero}) reservado com sucesso!")
    else:
        print(f"Assento ({fileira},{numero}) já está reservado.")

# Cancelar reserva
def cancelar_reserva(fileira, numero):
    if assentos[fileira-1][numero-1] == 1:
        assentos[fileira-1][numero-1] = 0
        print(f"Reserva do assento ({fileira},{numero}) cancelada.")
    else:
        print(f"Assento ({fileira},{numero}) já está livre.")

# Procedimento experimental
reservar_assento(1, 3)
reservar_assento(2, 5)
reservar_assento(4, 7)

cancelar_reserva(2, 5)

exibir_assentos()

