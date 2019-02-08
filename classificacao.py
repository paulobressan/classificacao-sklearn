# classificação, ele é gordinho? ele tem perna curta? ela faz au au(late)?
from sklearn.naive_bayes import MultinomialNB
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# Dizer que é porco = 1, cachorro = -1.
#  Seguindo a sequencia do array de dados, exemplo, porco1 é porco? Sim = 1, Não = -1
marcacoes = [1, 1, 1, -1, -1, -1]

# elemento a ser identificado
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
teste = [misterioso1, misterioso2]

# do pacote sklearn.naive_bayers vamos importar o algoritimo MultinomialNB
# O naive_bayers é os algoritimos mais simples de identificação

# Criando um modelo
modelo = MultinomialNB()
# Treinar o algoritmo com os dados e as marcações
modelo.fit(dados, marcacoes)
# Prever se misterioso é cachorro(-1) ou porquinho(1)
# resultado é [-1, 1] porque o misterioso1 é um cachorro e o misterioso2 é um porco
print(modelo.predict(teste))
