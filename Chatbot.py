# Chat Bot em Python
# Bibliotecas 
import unicodedata
import nltk

# Baixando os pacotes do NLTK necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#  Dicionário de respostas do chatbot com mais interações úteis
respostas = {
    
    "feliz": "Que bom saber disso! 😊 Como posso ajudar hoje?",
    "triste": "Poxa, espero que seu dia melhore! Se quiser conversar, estou aqui. 😢",
    "python": "Python é uma ótima linguagem de programação! Precisa de ajuda com sintaxe, bibliotecas ou lógica?",
    "ajuda": "Claro! Posso te ajudar com Python, lógica de programação ou até dar recomendações de estudo. Pergunte à vontade!",
    "tchau": "Até mais! Se precisar de algo, estarei por aqui. 👋",
    "erro": "Erros são normais na programação! Qual erro você encontrou? Talvez eu possa te ajudar a resolvê-lo. 🧐",
    "curso": "Se quer aprender programação, recomendo Coursera, Udemy, Alura ou YouTube. Qual linguagem você quer aprender?",
    "biblioteca": "Python tem várias bibliotecas incríveis! Quer saber sobre qual? Algumas populares são Pandas, NumPy e Requests.",
    "carreira": "Se quer entrar no mercado de TI, uma dica é aprender lógica de programação e versionamento com Git. Posso sugerir cursos!",
    "html": "HTML é a base da web! Se quiser aprender mais, recomendo MDN Web Docs e cursos gratuitos na W3Schools.",
    "css": "CSS deixa os sites bonitos! Quer aprender mais sobre estilos, flexbox ou animações?",
    "javascript": "JavaScript é essencial para desenvolvimento web! Você quer saber sobre manipulação de DOM, APIs ou frameworks?",
    "inteligencia artificial": "IA está crescendo muito! Algumas bibliotecas famosas para IA em Python são TensorFlow e Scikit-learn.",
    "dados": "Se quer aprender sobre ciência de dados, sugiro estudar Pandas e Matplotlib para análise e visualização!",
    "github": "GitHub é essencial para programadores! Você já sabe como criar um repositório e fazer commits?",
    "seguranca": "Segurança é fundamental! Você quer saber sobre criptografia, ataques comuns ou como proteger seu código?",
    "banco de dados": "Bancos de dados armazenam informações. Você quer aprender SQL ou NoSQL?",
    "algoritmos": "Algoritmos resolvem problemas! Quer aprender busca binária, ordenação ou estruturas de dados?",
    "estrutura de dados": "Filas, pilhas, listas e árvores são essenciais! Sobre qual estrutura você quer saber mais?",
    "logica de programacao": "Lógica de programação é a base para qualquer desenvolvedor. Quer dicas sobre condicionais, loops ou funções?"

} #final do dicionário Respostas

#  Função para remover acentos
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn') 

#  Processamento de texto: remove acentos e stopwords
def processar_texto(texto):
    texto = remover_acentos(texto.lower())  # Normalizar acentos e colocar tudo em minúsculas
    palavras = word_tokenize(texto)  # Tokenizar texto
    stop_words = set(stopwords.words('portuguese'))  # Stopwords em português
    palavras_filtradas = [p for p in palavras if p.isalnum() and p not in stop_words]  # Remover stopwords e caracteres especiais

    return palavras_filtradas  # Agora retornamos apenas palavras-chave filtradas

#  Função para responder com base no input processado
def responder(usuario_input, primeira_interacao):
    palavras_chave = processar_texto(usuario_input)

    if primeira_interacao:
        return "Olá! Sou um chatbot. Como posso ajudar você hoje?"

    for palavra in palavras_chave:
        for chave in respostas:
            chave_sem_acento = remover_acentos(chave)  # Remover acentos das chaves do dicionário
            if palavra in chave_sem_acento:  # Verifica se a palavra do usuário está na chave do dicionário
                return respostas[chave]
        
    return "Desculpe, não entendi. Você pode reformular a pergunta? 🤔"

#  Início do chatbot
def iniciar_chat():
    print("🤖 Chatbot iniciado! Digite 'sair' para encerrar.")
    primeira_interacao = True

    while True:
        entrada = input("Você: ")
        if entrada.lower() == "sair":
            print("Chatbot: Até logo! 👋")
            break

        resposta = responder(entrada, primeira_interacao)
        primeira_interacao = False
        print(f"Chatbot: {resposta}")

# Iniciar o chat
iniciar_chat()
