import sys
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Função principal que encapsula a lógica
def generate_titles(transcript):
    """
    Usa o Google Gemini para gerar títulos de podcast com base em uma transcrição.
    """
    load_dotenv()

    # Inicializa o modelo Gemini-2.0-flash com temperatura 0.7
    # Ajuste a temperatura conforme necessário para variar a criatividade
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    # O prompt permanece o mesmo
    prompt = f"""
    Você é um especialista em marketing digital e SEO, especializado em conteúdo de podcasts.
    Sua tarefa é criar 3 sugestões de títulos para um episódio de podcast com base na transcrição fornecida.

    Regras:
    - Os títulos devem ser curtos, impactantes e otimizados para buscas (SEO-friendly).
    - Devem despertar curiosidade.
    - Devem refletir o conteúdo principal da transcrição.

    Transcrição do episódio:
    ---
    {transcript}
    ---

    Gere os 3 títulos, cada um em uma nova linha, sem numeração ou marcadores.
    """

    # Invoca o modelo e retorna o conteúdo da resposta
    message = HumanMessage(content=prompt)
    response = llm.invoke([message])
    return response.content

if __name__ == "__main__":
    # 1. Lê a transcrição da entrada padrão (stdin)
    #    Isso permite que o Node.js envie dados para este script.
    transcript_from_input = sys.stdin.read()

    # 2. Escreve logs na saída de erro padrão (stderr)
    #    Isso evita que mensagens de log se misturem com o resultado final.
    print("--- 🐍 Script Python Recebeu a Transcrição 🐍 ---", file=sys.stderr)

    # 3. Chama a função principal com os dados recebidos
    generated_titles = generate_titles(transcript_from_input)

    # 4. Imprime o resultado final na saída padrão (stdout)
    #    É SÓ ISSO que o Node.js irá capturar como resultado.
    print(generated_titles)