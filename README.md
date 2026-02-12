Nome: ClimaTodoDia

Descrisão: Programa criado com o intuito de fortalecer conhecimentos na linguagem Python além de explorar novos sistemas e funcionalidades.

COMO USAR: 
O progrmama foi feito interamente pela linguagem Python, então você precisa da linguagem instalada no seu sistema. O programa serve como uma unidade de processamento de dados climaticos. 


PASSO A PASSO: 
Com o seu editor OU IDE preferida, clone este repositorio usando o comando: git clone https://github.com/ItsDrue157/ClimaTodoDi, na pasta você vera um arquivo chamado "app.py", execute ele. 
Este progrma foi idealizado para ser uma forma de você conseguir dados rapidos sobre o clima diretamente no WhatsSap. Para se comunicar, o programa se utliza de um serviço chamado twilio, no qual tem um plano gratuito. 

Crie uma conta no site: https://www.twilio.com/pt-br, depois vá até a url: https://console.twilio.com/?frameUrl=/console, onde você vera um painel na esquerda, clique em develop => Messaging => Try it out => Send a WhatsApp message.
na tela tera duas abas, 'SandBox' e 'SandBox settings', a primeira sera onde devera mandar a entrada dos dados no whatsapp, a segunda voce colocara um link que (veremos a seguir) em 'when a message comes in'.

Para se comunicar, precisamos de uma 'ponte' entre o programa e o twilio. Portanto usaremos o ngrok (https://ngrok.com/) baixe-o e execute, nele abrira um Terminal e voce digitara: 'ngrok http 5000' e precionar enter. 
Com isso voce vera no terminal alguma informações, a que nos interessa é a "Forwarding", o link dela sera nossa ponte. copie-o e salve. 

Vamos agora voltar a aba no twilio 'sandbox settings' na opcao 'when a message comes in' copie o link nela e acione no final '/bot' e salve. pronto nosso sistema estara pronto para se comunicar.

Na versao 1.0 o sistema ainda é simples portanto depois de voce iniciar no whatsapp e enviar a mensagem pré definida voce entrara no modo para se comunicar.
nele voce ja pode digitar o nome de alguma cidade e receber os dados. 



Se voce leu até o final, obrigado, se puder, deixe sua estrela e sua sugestão, elas vão ser muito bem vindas. 

links importantes:
'Ponte' https://ngrok.com/
instalador do python, versao utilizada é a 3.14.3: https://www.python.org/downloads/ 
twilio: https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

APIs de clima: 
https://open-meteo.com/en/docs?forecast_days=1&hourly=&timezone=auto&latitude=-22.9064&longitude=-43.1822&bounding_box=-90,-180,90,180&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max#settings

APIs de Geocoding: 
https://open-meteo.com/en/docs/geocoding-api?name=&language=pt&count=1

Frameworks Utilziados: 
Flask: https://flask.palletsprojects.com/en/stable/installation/

bibilotecas utilizadas: 
requests: python -m pip install requests (no terminal)

IA utlizada: GEMINI no modo aprendizado guiado. 

Disclaimer: ia foi utilizada neste codigo para consultas, aprendizado e de forma secundaria (não foi utulizada no forma de criação primaria de codigo), e na verificacao de erros (que teve muitos rs).   





