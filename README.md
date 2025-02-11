# wpp-bot-ai

## Descrição
Este projeto é um bot de WhatsApp desenvolvido utilizando Flask. Ele recebe eventos via webhook e responde com um status de sucesso.

## Estrutura do Projeto
- `app.py`: Contém a aplicação Flask que define a rota do webhook e trata os eventos recebidos.

## Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
    ```bash
    pip install flask
    ```
3. Execute a aplicação:
    ```bash
    python app.py
    ```

## Uso
Envie uma requisição POST para a rota `/chatbot/webhook/` com um payload JSON. A aplicação irá imprimir o evento recebido e responder com um status de sucesso.

## Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença
Este projeto está licenciado sob a licença MIT.