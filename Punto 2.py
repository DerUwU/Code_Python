empresa = str(input("Ingrese nombre de la empresa: "))
num_talla_S = int(input("Ingrese cantidad de ropa talla S: "))
num_talla_M = int(input("Ingrese cantidad de ropa talla M: "))
num_talla_L = int(input("Ingrese cantidad de ropa talla L: "))

def calcula_metros(empresa: str, num_talla_S: int, num_talla_M: int, num_talla_L: int):
    metros_tela_S = 2
    metros_tela_M = 2.5
    metros_tela_L = 3

    total_metros = (num_talla_S * metros_tela_S) + (num_talla_M * metros_tela_M) + (num_talla_L * metros_tela_L)
    total_metros = str(total_metros)

    print(f"Para fabricar {num_talla_S} trajes talla S, {num_talla_M} trajes talla M, {num_talla_L} trajes talla L"
          f", para la empresa {empresa} se necesitan {total_metros} metros de tela.")


print(calcula_metros(empresa, num_talla_S, num_talla_M, num_talla_L))
