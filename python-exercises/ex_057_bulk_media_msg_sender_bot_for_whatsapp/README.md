### <img src="https://cdn-icons-png.flaticon.com/512/323/323329.png" width="15" height="15" alt="United Kingdom" /> [Click here to access the English version!](README-en.md)

<hr>

# Robô de envio em massa de mensagens multimídia para o WhatsApp

## Descrição:

- Bot de envio de mensagens em massa para WhatsApp utilizando os nomes dos seus contatos e/ou grupos. 🤖
- Mensagem de texto com opção de inclusão de imagem ou vídeo, além de personalização automática de cada mensagem usando o nome do contato e/ou grupo.
- O bot possui instruções claras e dicas de uso durante toda a sua execução. 📝
- Disponível em: <img src="https://cdn-icons-png.flaticon.com/512/197/197386.png" width="15" height="15" alt="Brazil" /> **portguês** e <img src="https://cdn-icons-png.flaticon.com/512/323/323329.png" width="15" height="15" alt="United Kingdom" /> **inglês**.

> _Recomendo enviar uma mensagem de teste para si mesmo(a) para entender bem como tudo funciona. Para quem não sabe, basta adicionar seu próprio número como contato em sua agenda e você poderá enviar mensagens para o seu próprio usuário do WhatsApp._

<hr>

## Vídeo de demonstração do aplicativo em execução:

**[Clique aqui](https://youtu.be/Ha-t__BuUs4)** para assistir a um vídeo no _YouTube_ do aplicativo em funcionamento.

<hr>

## Screenshots:
<table>
  <tr>
    <td>
       <img src="https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/blob/main/sample/screenshot_01.png" width="380" height="320" align="top" alt="Screenshot 01" />
     </td>
     <td rowspan="2">
        <img src="https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/blob/main/sample/screenshot_03.png" width="380" height="484" alt="Screenshot 03" />
     </td>
   </tr>
   <tr>
      <td> <img src="https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/blob/main/sample/screenshot_02.png" width="380" height="162" alt="Screenshot 02" />
      </td>
   </tr>
</table>

<hr>

## Sobre o projeto:

- Este é meu primeiro projeto pessoal de programação.
- Foi criado em **Python** 🐍 por hobby para aplicar e demonstrar as habilidades e conhecimentos que adquiri até aqui em vários tópicos da programação, como: _modularização, organização do código, programação orientada a objetos, herança, validação de inputs, tratamento de erros e exceções, automação_, dentre outros. E também explorar ao máximo o uso do terminal, tentando deixá-lo o mais agradável possível usando boa diagramação, além de animar e colorir os textos. Foi um processo bem "artesanal" para deixá-lo o mais intuitivo possível, mesmo sem o uso de uma interface gráfica.
- Fiz o melhor que pude para deixá-lo "redondinho", tratando todos os erros que pude encontrar. Se encontrar algum bug, me avise! 🧑‍🔧

> _Essa é uma ferramenta criada apenas para fins didáticos. Não me responsabilizo pelo uso indevido do app. Não abuse dela para enviar spam, nem incomode seus amigos. 😉_

<hr>

## Requerimentos:

- Windows 10/11
- Navegador Chrome
- Python 3.10+ (caso execute direto do código-fonte)

<hr>

## Como usar a partir do executável:

### Execute com um clique

- Baixe o executável **[aqui](https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/releases/tag/1.0)** e salve-o em seu computador.

> **Seu aplicativo está pronto para uso!**

<hr>

## Como usar a partir do código-fonte:

### Download do código-fonte

1. Baixe a pasta com o código-fonte **[aqui](https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/releases/tag/1.0)**.
2. Extraia o conteúdo do arquivo comprimido em seu computador.

### Instalação do Python

1. Visite o site oficial do **Python** em [python.org](https://www.python.org/downloads/) e faça o download da versão mais recente do Python para o seu sistema operacional.
2. Siga as instruções do instalador. Certifique-se de marcar a opção **"Add Python 3.xx to PATH"**.

### Instalação das dependências

1. Abra o seu Terminal ou PowerShell e navegue até o diretório do seu aplicativo extraído (substitua **"C:\LOCAL_DE_DOWNLOAD"** pelo local onde você extraiu o arquivo zip):
   ```
   cd C:\LOCAL_DE_DOWNLOAD\bot-whatsapp-bulk-media-msgs-sender
   ```
2. Use o código abaixo para instalar as dependências necessárias usando o pip:
   ```
   pip install -r requirements.txt
   ```

### Rodando o aplicativo

1. Ainda dentro da pasta, execute o arquivo principal do seu aplicativo:
   ```
   python main.py
   ```
2. Siga as instruções que aparecerão na tela para usar seu aplicativo.

<hr>

## 💡 Status e problemas conhecidos

- Eu pessoalmente só o testei no Windows 11 (CMD e PowerShell), mas teoricamente deve funcionar bem na maioria dos sistemas operacionais, incluindo Linux e MacOS.
- Se o usuário corrigir os inputs muitas vezes, o terminal pode começar a ficar mais lento. Sou amador, logo, qualquer dica a respeito disso será bem-vinda!
- O app não verifica corretamente se o usuário digitar um nome de contato ou grupo inexistente.
- Se algo não funcionar para você ou não fizer o que você espera, adoraria ouvir o seu feedback. Pode entrar em contato comigo por qualquer um dos meios abaixo.

<hr>

## 👨‍💻 Aos desenvolvedores:

- Espero que o código esteja bastante legível e que os comentários os ajudem a entendê-lo melhor.
- Vale lembrar que sites são reforumlados de tempos em tempos, logo, não sei se o bot estará funcionando perfeitamente quando você for testá-lo. Se você souber o básico de _webscraping_, basta atualizar as variáveis dos seletores CSS e XPATH do módulo **msg_sender.py** para os que o WhatsApp Web estiver usando no momento.
- Para que o WhatsApp Web não fique te pedindo para escanear o QR code toda vez que você usar o aplicativo, você pode "descomentar" este trecho do códigdo dentro da função **"init_webdriver()"** do modulo **"bot.py"** e substituir o diretório de instalação do meu Chrome pelo seu:
  ```
  options = webdriver.ChromeOptions()
  options.add_argument(
              r'--user-data-dir=C:\\Users\\ferna\\AppData\\Local\\Google\\Chrome\\User Data\\')
  self.driver = webdriver.Chrome(
              executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
  ```

<hr>

<img width="200" height="25" src="https://img.shields.io/tokei/lines/github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp?label=Total%20de%20linhas%20de%20c%C3%B3digo&logo=Python" alt="Linhas de código" />
