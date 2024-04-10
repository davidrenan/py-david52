# Função para calcular o dígito verificador do CPF parcial
def calcular_digito_verificador(cpf_parcial):
    soma = 0
    multiplicador = len(cpf_parcial) + 1  # Define o multiplicador inicial

    # Itera sobre cada dígito do CPF parcial
    for digito in cpf_parcial:
        soma += int(digito) * multiplicador  # Soma o produto do dígito pelo multiplicador
        multiplicador -= 1  # Decrementa o multiplicador

    resto_divisao = soma % 11  # Calcula o resto da divisão
    if resto_divisao < 2:
        return '0'  # Se o resto da divisão for menor que 2, retorna '0'
    else:
        return str(11 - resto_divisao)  # Caso contrário, retorna o dígito verificador calculado


# Função para verificar se o CPF é válido
def verificar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # Remove os pontos e traços do CPF

    # Verifica se o CPF tem 11 dígitos e se são todos números
    if len(cpf) != 11 or not cpf.isdigit():
        return False  # Retorna False se o CPF não tiver 11 dígitos ou conter caracteres não numéricos

    cpf_parcial = cpf[:9]  # Obtém os nove primeiros dígitos do CPF

    digito1 = calcular_digito_verificador(cpf_parcial)  # Calcula o primeiro dígito verificador
    cpf_parcial += digito1  # Adiciona o primeiro digito verificador ao CPF parcial

    digito2 = calcular_digito_verificador(cpf_parcial)  # Calcula o segundo dígito verificador
    cpf_calculado = cpf_parcial + digito2  # Adiciona o segundo digito verificador ao CPF parcial

    return cpf == cpf_calculado  # Retorna True se o CPF original for igual ao CPF calculado com os dígitos verificadores


# Função principal
def main():
    cpf = input("Digite o CPF (apenas números): ")  # Solicita ao usuário que insira o CPF

    if verificar_cpf(cpf):  # Verifica se o CPF é válido
        print("CPF válido!")  # Se for válido, exibe essa mensagem
    else:
        print("CPF inválido")  # Se não for válido, exibe essa mensagem


if __name__ == "__main__":
    main()  # Chama a função principal ao executar o script
