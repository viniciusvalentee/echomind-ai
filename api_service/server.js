// server.js

// 1. Importa o framework Fastify. O 'require' é como o 'import' do Python.
const fastify = require('fastify')({
  logger: true // Liga os logs para vermos as requisições no terminal
});

// 2. Declara uma rota (ou "endpoint"). Esta é a nossa primeira URL.
//    - 'GET' é o método HTTP (quando você acessa uma URL no navegador, é um GET).
//    - '/' é o caminho da URL (a raiz do nosso site).
//    - 'async (request, reply) => { ... }' é a função que será executada
//      quando alguém acessar esta rota.
fastify.get('/', async (request, reply) => {
  // O objeto 'reply' é usado para enviar uma resposta de volta ao usuário.
  // Aqui, estamos enviando um objeto JSON.
  return { status: 'ok', message: 'Bem-vindo à API do EchoMind AI!' };
});

// 3. Inicia o servidor para que ele comece a "ouvir" por requisições.
const start = async () => {
  try {
    // Faz o servidor "ouvir" na porta 3000.
    // O endereço será http://localhost:3000
    await fastify.listen({ port: 3000 });
  } catch (err) {
    // Se a porta 3000 já estiver em uso, ele registrará um erro e sairá.
    fastify.log.error(err);
    process.exit(1);
  }
};

// Chama a função para iniciar o servidor.
start();