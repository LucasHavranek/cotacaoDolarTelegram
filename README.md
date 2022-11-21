# cotacaoDolarTelegram
### Notificações via telegram do dólar como parâmetro de verificação

### Passo a passo para configurar a notificação no aplicativo Telegram.

1. Criar e ativar um bot no telegram, mais informações no link a seguir (https://tecnoblog.net/responde/como-criar-um-bot-no-telegram/)
2. Identificar token do bot e o chat_id onde a notificação deve ser enviada, mais informações no link a seguir (https://weni.ai/blog/como-criar-um-chatbot-para-telegram/)
3. Em posse do token do bot, para identificar o chat ID acesse o endereço (https://api.telegram.org/bot"seutokenbot"/getUpdates) e em seguida envie uma mensagem no grupo ou conversa para que o chat_id seja atualizado na página.
4. Por fim edite o loop while de acordo com as suas preferencias, exemplo: recorrencia de execução 3600s equivalente a 1 hora, valor do dólar desejado 5 reais...


