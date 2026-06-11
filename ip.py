vermelho = "\033[91m"
reset = "\033[0m"

import requests
import os
import webbrowser
import ipaddress

os.system("cls" if os.name == "nt" else "clear")

asci_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣤⣒⣒⡾⢭⡩⠉⢰⢖⣖⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⢷⣫⠤⢲⠄⠀⠀⠧⡵⠀⡛⠉⢂⢄⣀⢻⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⣏⡽⢿⣿⣜⢲⡀⡼⠃⠀⡠⢻⣓⣄⢹⣼⢪⠇⢠⠉⠞⠋⠉⠢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠏⠀⢠⠴⢾⡽⣥⡟⡃⢙⡤⢤⡱⣈⠤⡍⣄⣞⠛⣒⣼⣲⠀⠀⠀⠀⠈⢢⡀⠀⠀⠀
⠀⠀⢠⡞⠁⠀⠀⠳⡤⡼⠀⠋⠱⣔⢄⡎⠭⠕⠁⠸⢹⠛⢯⣦⠊⠉⠁⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀
⠀⢠⡟⠀⠀⠀⠀⠀⠛⠀⠀⢤⣶⡸⡼⠸⡀⠀⠀⠸⢸⢠⠈⠃⡠⠤⣲⣄⢀⣗⣷⡄⢷⡀⠘⡄⠀
⠀⣮⠃⠀⠀⠀⠀⠀⢀⡠⠞⠛⠁⠈⠑⡣⠃⠀⠀⢰⢈⠈⡢⠶⠕⠒⣜⡋⣻⣟⢦⠀⠘⠃⠀⢱⡀
⢸⢻⠀⠀⠀⠀⠀⢀⡼⣘⡕⠀⠀⠀⠈⠀⠀⠀⢀⢇⢎⡜⠁⠀⠀⠀⢀⠈⠈⠉⠉⣄⠀⠀⠀⡀⡇
⡟⡎⡄⠀⡖⠒⢲⢣⠌⡎⠀⠀⠀⠀⠀⠀⠀⠀⡜⡜⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⢠⠟⣼
⡿⡔⢝⣄⢇⢶⠀⠽⢲⠁⠀⠀⠀⠀⠀⠀⠀⠀⢇⢇⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣶⡇⠀⣿
⣷⠈⠢⣈⠉⡪⣧⡂⠌⠒⠄⠀⠀⠀⠀⠀⠀⠀⠘⢎⠪⡓⠤⠠⠤⠲⡄⠀⠀⠀⠀⠀⠀⣰⢱⢡⢻
⢸⡄⠀⠀⠙⢎⡎⡎⠑⠒⠲⣄⡀⠀⢦⡀⠀⠀⠀⠀⠑⠢⠄⠀⡄⡇⢧⠀⠀⠀⠀⠀⠞⢡⠃⡠⡇
⠈⣷⠀⠀⠀⠘⣇⠇⠀⠀⠀⠀⠹⢂⣂⡀⠉⠲⡄⠀⠀⠀⠀⠀⠁⠠⢸⠀⠀⠀⠀⢸⢀⡹⡀⢱⠁
⠀⠘⣧⠀⠀⢰⢇⢆⠀⠀⠀⠀⠀⠀⠀⠈⡵⡀⡅⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⠀⠰⢳⢫⢣⢣⠇⠀
⠀⠀⠘⣧⠀⠀⠳⣗⢳⢤⠀⠀⠀⠀⠀⠸⣰⢱⠁⠀⠀⠀⠀⠀⠀⠀⢹⠀⢀⠜⠁⠓⡣⣣⠏⠀⠀
⠀⠀⠀⠈⢷⣄⠀⠈⢣⢏⡇⠀⠀⠀⡔⣊⢜⡎⠀⠀⠀⠀⠀⠀⢆⠰⣘⣺⠕⣀⠤⢀⡴⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⣄⠀⢫⠘⡄⢀⡞⡝⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠒⠊⢁⡴⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣧⡘⢾⣜⠰⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠿⢤⣌⣀⣀⣀⣀⣀⣠⡤⠤⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(vermelho + asci_art + reset)

# NOVA FUNÇÃO MAPS (
def abrir_maps(dados):
    lat = dados.get("lat")
    lon = dados.get("lon")
    cidade = dados.get("city")
    estado = dados.get("regionName")
    pais = dados.get("country")

    endereco = f"{cidade}, {estado}, {pais}".replace(" ", "+")

    url = f"https://www.google.com/maps?q={lat},{lon} ({endereco})"

    print("Abrindo localização detalhada no Maps...")

    try:
        if os.name == "posix":
            os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
        else:
            webbrowser.open(url)
    except:
        webbrowser.open(url)


def localizar_ip():
    ip = input("Digite o IP: ")

    try:
        ip_obj = ipaddress.ip_address(ip)

        #  DETECTA IP PRIVADO
        if ip_obj.is_private:
            print(" IP privado (não rastreável na internet)")
            return

    except ValueError:
        print("IP inválido.")
        return

    try:
        resposta = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        dados = resposta.json()
    except:
        print("Erro ao conectar.")
        return

    if dados["status"] == "success":
        print("\n===== INFORMAÇÕES DO IP =====")
        print("IP:", dados.get("query"))
        print("Região:", dados.get("regionName"))
        print("ASN:", dados.get("as"))
        print("Organização:", dados.get("org"))
        print("País:", dados.get("country"))
        print("Cidade:", dados.get("city"))
        print("Latitude:", dados.get("lat"))
        print("Longitude:", dados.get("lon"))

        escolha = input("\nAbrir no Maps? (y/n): ").lower()
        if escolha == "y":
            abrir_maps(dados)

    else:
        print("IP inválido.")


def localizar_cep():
    cep = input("Digite o CEP: ").replace("-", "")

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido.")
        return

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        dados = resposta.json()
    except:
        print("Erro ao conectar.")
        return

    if "erro" in dados:
        print("CEP não encontrado.")
        return

    print("\n===== INFORMAÇÕES DO CEP =====")
    print("CEP:", dados.get("cep"))
    print("Rua:", dados.get("logradouro"))
    print("Bairro:", dados.get("bairro"))
    print("Cidade:", dados.get("localidade"))
    print("Estado:", dados.get("uf"))

    escolha = input("\nAbrir no Maps? (y/n): ").lower()
    if escolha == "y":
        endereco = f"{dados.get('logradouro')}, {dados.get('bairro')}, {dados.get('localidade')}, {dados.get('uf')}"
        url = f"https://www.google.com/maps/search/{endereco.replace(' ', '+')}"

        try:
            if os.name == "posix":
                os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
            else:
                webbrowser.open(url)
        except:
            webbrowser.open(url)


def menu():
    while True:
        print("\n[1] Localizar IP")
        print("[2] Localizar CEP")
        print("[0] Sair")

        op = input("Escolha: ")

        if op == "1":
            localizar_ip()
        elif op == "2":
            localizar_cep()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

