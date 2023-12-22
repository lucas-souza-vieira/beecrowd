# Leio a quantidade de participantes e crio um dicionario
n = int(input())
d = {}


# Leio o nome do participante e os presentes desejados e os adiciono ao dicionarios
for i in range(n):
    nome, p1, p2, p3 = input().split()
    d.update({nome: [p1, p2, p3]})


while True:
    # Leio o nome o presente pro teste
    try:
        chave, presente = input().split()
        # Se o presente tiver dentro da lista da pessoas eu printo a primeira mensagem se não printo o tente novamente
        try:
            print("Uhul! Seu amigo secreto vai adorar o/") if presente in d[chave] else print("Tente Novamente!")
        # Se não receber o input de forma certa printo o tente novamente
        except: print("Tente Novamente!")
            
    except EOFError:
        break
