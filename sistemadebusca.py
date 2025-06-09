docs = {
    1: "Psicologo",
    2: "Voluntarios",
    3: "Casas de Apoio",
    4: "Escolas"
}

while True:
    # Pede o termo para buscar
    termo = input("Buscar por: ").lower()
   
    # Se digitar 'sair', encerra
    if termo == 'sair':
        break
   
    # Procura o termo em cada documento
    print("\nResultados:")
    encontrou = False
    for id, texto in docs.items():
        if termo in texto.lower():
            print(f"Doc {id}: {texto}")
            encontrou = True
   
    if not encontrou:
        print("Nada encontrado")
