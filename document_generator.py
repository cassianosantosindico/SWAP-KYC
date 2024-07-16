import requests

URL = 'https://www.4devs.com.br/ferramentas_online.php'
HEADERS = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

TARGET = ['gerar_cpf', 'gerar_cnpj', 'gerar_cep']


def get_first_digit_for_kyc_status(desired_status):
    status_mapping = {
        "Automaticamente Aprovado": [0, 1, 2, 3, 4],
        "Automaticamente Reprovado": [5, 6],
        "Em Análise Manual - Aprovado Manualmente": [7],
        "Em Análise Manual - Reprovado Manualmente": [8],
        "Em Análise - Qualquer Status Final": [9]
    }
    for status, digits in status_mapping.items():
        if status == desired_status:
            return digits
    return []


def get_kyc_status(document_number):
    first_digit = int(document_number[0])

    if first_digit <= 4:
        return "Automaticamente Aprovado"
    elif 5 <= first_digit <= 6:
        return "Automaticamente Reprovado"
    elif first_digit == 7:
        return "Em Análise Manual - Aprovado Manualmente"
    elif first_digit == 8:
        return "Em Análise Manual - Reprovado Manualmente"
    elif first_digit == 9:
        return "Em Análise - Qualquer Status Final"
    else:
        return "Status Desconhecido"


option = int(input("""
=================
[ 0 ] - CPF
[ 1 ] - CNPJ
[ 2 ] - CEP
=================
>>> """))

if option != 2:
    kyc_options = [
        "Automaticamente Aprovado",
        "Automaticamente Reprovado",
        "Em Análise Manual - Aprovado Manualmente",
        "Em Análise Manual - Reprovado Manualmente",
        "Em Análise - Qualquer Status Final"
    ]

    print("\nSelecione o status KYC desejado:")
    for i, status in enumerate(kyc_options):
        print(f"[ {i} ] - {status}")

    kyc_choice = int(input(">>> "))
    desired_status = kyc_options[kyc_choice]
    valid_first_digits = get_first_digit_for_kyc_status(desired_status)

    found_valid_document = False
    while not found_valid_document:
        response = requests.post(
            url=URL,
            headers=HEADERS,
            data={'acao': TARGET[option], 'pontuacao': 'N'},
        )
        response = response.content.decode('utf-8')
        if int(response[0]) in valid_first_digits:
            found_valid_document = True
            final_response = response
            kyc_status = get_kyc_status(final_response)
else:
    response = requests.post(
        url=URL,
        headers=HEADERS,
        data={'acao': TARGET[option], 'pontuacao': 'N',
              'cep_estado': '', 'cep_cidade': ''},
    )
    response = response.content.decode('utf-8')
    final_response = response
    kyc_status = "N/A para CEP"

print('TARGET:', TARGET[option])
print('RESPONSE:', final_response)
print('KYC STATUS:', kyc_status)
