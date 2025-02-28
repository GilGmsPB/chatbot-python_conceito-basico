#Chat Bot em Python- Nível Iniciante 

import  unicodedata

# Função para converte caracteres com acentos em caracteres base
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn') 

# Função para automatizar a remoção de acentos
def chatbot_respostas(pergunta):
    pergunta_sem_acentos = remover_acentos(pergunta)    # Remove os acentos da entrada 
    pergunta_processada = pergunta_sem_acentos.lower()  # Converte tudo para minúsculas para facilitar a comparação

    #Respostas pré-definidas usando estruturas de controles (if e elif);
    if "ola" in pergunta_processada or "oi" in pergunta_processada:
        return "Olá, Como posso ajudar?"
    
    elif "como vai" in pergunta_processada:
        return "Estou bem, obrigado por perguntar! E você?"
    
    elif "nao" in pergunta_processada or "mal" in pergunta_processada:
        return "Sinto muito em saber, mas as coisas irão melhorar!"
    
    elif "bem" in pergunta_processada or "bom" in pergunta_processada:
        return "Fico muito feliz em saber!"

    elif "tchau" in pergunta_processada:
        return "Tchau! Foi uma prazer!"
    
    else:
        return "Desculpe, não entendi a sua pergunta. Pode reformular?"
    
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