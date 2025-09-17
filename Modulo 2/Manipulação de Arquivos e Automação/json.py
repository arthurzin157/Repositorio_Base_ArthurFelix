import json

dados_json = '{"produto":"carne", "preco": 12.5, "estoque": 30}'
 
#converte json para dicionario
dados_dict = json.loads(dados_json)

#acessa e json e imprime os valores
print("produto:",dados_dict["produto"])
print("preço:",dados_dict["preco"])
