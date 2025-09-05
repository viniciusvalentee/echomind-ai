# process_audio.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Carrega as variáveis de ambiente do arquivo .env
# Agora ele vai carregar a GOOGLE_API_KEY
load_dotenv()

# Transcrição
podcast_transcript = """
Olá e bem-vindos ao Futuro Digital. Hoje, vamos mergulhar fundo no conceito de
Inteligência Artificial Generativa. Vimos um boom de ferramentas como DALL-E para imagens,
e claro, modelos de linguagem como o GPT-4 que podem escrever, resumir e até programar.
A questão não é mais 'se' a IA vai mudar nossas vidas, mas 'como' e 'quando'.
Uma das maiores discussões é o impacto no mercado de trabalho. Tarefas repetitivas
estão sendo automatizadas, mas novas profissões focadas em engenharia de prompt e
curadoria de IA estão surgindo. Empresas que adotam essa tecnologia cedo estão vendo
ganhos massivos em produtividade. Falaremos também sobre os desafios éticos, como
vieses nos dados de treinamento e o uso indevido da tecnologia. Fiquem ligados.
"""

# 2. Apontamos para o modelo do Google
# O LangChain automaticamente usará a GOOGLE_API_KEY do nosso .env
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

# 3. A Engenharia de Prompt.
prompt = f"""
Você é um especialista em marketing digital e SEO, especializado em conteúdo de podcasts.
Sua tarefa é criar 3 sugestões de títulos para um episódio de podcast com base na transcrição fornecida.

Regras:
- Os títulos devem ser curtos, impactantes e otimizados para buscas (SEO-friendly).
- Devem despertar curiosidade.
- Devem refletir o conteúdo principal da transcrição.

Transcrição do episódio:
---
{podcast_transcript}
---

Gere os 3 títulos, separados por uma nova linha.
"""

# Este é o poder do LangChain: a interface é consistente.
print("--- 🧠 Conectando com a IA do Google Gemini para gerar títulos... ---")

message = HumanMessage(content=prompt)
response = llm.invoke([message])

print("--- ✨ Títulos Gerados com Sucesso! ✨ ---")
print(response.content)
print("------------------------------------------")