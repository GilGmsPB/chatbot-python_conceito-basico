#Chat Bot em Python- Nível Iniciante 

import unicodedata, random, re

# Função para remover acontos
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn') 

# Função para remover pontuação
def remover_pontuacao(texto):
    return re.sub(r'[^\w\s]','',texto)# Remove tudo que não for letra ou espaço

# Função para automatizar a remoção de acentos
def chatbot_respostas(pergunta):
    pergunta_sem_acentos = remover_acentos(pergunta)    # Remove os acentos da entrada 
    pergunta_processada = pergunta_sem_acentos.lower()  # Converte tudo para minúsculas para facilitar a comparação

    #Palavras pré-definidas
    saudacoes= ["ola","ola","oi","oi","bom dia","boa noite","boa tarde"]
    despedidas = ["tchau","adeus","ate mais","ate logo"]
    sentimentos_bem = ["bem","bom","otimo","maravilhoso","maravilhosa","boa","na paz"]
    sentimentos_mal = ["mal","ruim","triste","pessimo","nao muito bem","mais ou menos"]
    agradecimentos = ["obrigado","obrigada","valeu","vlw","agradeço"]


    #Respostas pré-definidas usando estruturas de controles (if e elif);
    if any(saudacao in pergunta_processada for saudacao in saudacoes):
        return random.choice(["Olá, como posso ajudar?","Oi! Como você está?","Olá! O que posso fazer por você hoje?"])
    
    elif any(sentimento in pergunta_processada for sentimento in sentimentos_mal):
        return random.choice(["Sinto muito em saber, mas as coisas irão melhorar!","Lamento ouvir isso, espero que melhore logo."])
    
    elif any(sentimento in pergunta_processada for sentimento in sentimentos_bem):
        return random.choice(["Fico muito feliz em saber!","Que bom que você está bem!"])

    elif any(despedida in pergunta_processada for despedida in despedidas):
        return random.choice(["Tchau! Até logo!", "Até mais! Foi um prazer!", "Até a próxima"])
    
    elif any(agradecimento in pergunta_processada for agradecimento in agradecimentos):
        return random.choice (["De nada!", "Sempre à disposição!", "Fico feliz em ajudar!"])
    
    else:
        return random.choice(["Desculpe, não entendi a sua pergunta. Pode reformular?", "Não consegui entender, tente de novo!"])
    
def iniciar_chat():
    print("Bem-vindo ao Chatbot! Digite 'tchau' para encerrar a conversa.")
    while True:
        pergunta = input("Você: ")
        if "tchau" in remover_acentos(pergunta).lower():
            print("Chatbot: Tchau! Até logo!")
            break
        resposta = chatbot_respostas(pergunta)
        print(f"Chatbot: {resposta}")

# Iniciar o chatbot
iniciar_chat()