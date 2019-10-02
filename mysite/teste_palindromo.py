def palindromo(numero_1, numero_2):
    # codigo
    for i in range(numero_1, numero_2 + 1):
        print(f"{i}")


def test_palindromo_um_a_vinte():
    numero_1 = 1
    numero_2 = 20
    resultado_esperado = [1,2,3,4,5,6,7,8,9,11]
    resultado = palindromo(numero_1, numero_2)
    assert resultado == resultado_esperado

def test_palindromo_tres_mil_a_tres_mill_e_dez():
    numero_1 = 3000
    numero_2 = 3010
    resultado_esperado = [3003]
    resultado = palindromo(numero_1, numero_2)
    assert resultado == resultado_esperado

