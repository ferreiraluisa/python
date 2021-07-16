import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url) #requisicao

# print(req.status_code) #ver se o codigo de status ta td certo, tem que dar 200

dados = req.json() #pega os dados que esta na api e transforma em um dict4

#print(dados)

valor_reais = float(input('Informe o valor, em reais: R$'))

cotacao = dados['rates']['BRL']

#print(cotacao)

print('R${:.2f} corresponde a U${:.2f}'.format(valor_reais,(valor_reais/cotacao)))