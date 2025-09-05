// server.js

const fastify = require('fastify')({ logger: true });
// Importa o módulo 'spawn' para criar processos filhos
const { spawn } = require('child_process');
const path = require('path'); // Módulo para lidar com caminhos de arquivos

// Rota de status
fastify.get('/', async (request, reply) => {
  return { status: 'ok', message: 'Bem-vindo à API do EchoMind AI!' };
});

// Nova rota para processar o áudio
fastify.post('/process-audio', async (request, reply) => {
  try {
    // Pega a transcrição do corpo da requisição POST
    const { transcript } = request.body;
    if (!transcript) {
      return reply.status(400).send({ error: 'A transcrição (transcript) é obrigatória.' });
    }

    // Caminho para o executável Python DENTRO do ambiente virtual
    // const pythonExecutable = path.resolve(__dirname, '../ia_service/.venv/bin/python'); // Para macOS/Linux
    const pythonExecutable = path.resolve(__dirname, '../ai_service/.venv/Scripts/python.exe'); // Para WINDOWS

    const scriptPath = path.resolve(__dirname, '../ai_service/process_audio.py');

    // Usa uma Promise para lidar com o processo assíncrono do Python
    const result = await new Promise((resolve, reject) => {
      // Inicia o processo Python
      const pythonProcess = spawn(pythonExecutable, [scriptPath]);

      let dataOutput = '';
      let errorOutput = '';

      // Envia a transcrição para o stdin do script Python
      pythonProcess.stdin.write(transcript);
      pythonProcess.stdin.end();

      // Captura a saída (stdout) do script
      pythonProcess.stdout.on('data', (data) => {
        dataOutput += data.toString();
      });

      // Captura os erros (stderr) do script
      pythonProcess.stderr.on('data', (data) => {
        errorOutput += data.toString();
      });

      // Finaliza a promise quando o processo terminar
      pythonProcess.on('close', (code) => {
        fastify.log.info(`Logs do script Python: ${errorOutput}`);
        if (code !== 0) {
          reject(new Error(`Script Python finalizou com erro: ${errorOutput}`));
        } else {
          resolve(dataOutput);
        }
      });
    });

    // Retorna o resultado gerado pela IA
    return { titles: result.trim() };

  } catch (error) {
    fastify.log.error(error);
    return reply.status(500).send({ error: 'Erro interno ao processar o áudio.' });
  }
});

// Função de inicialização do servidor (continua a mesma)
const start = async () => {
  try {
    await fastify.listen({ port: 3000 });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();