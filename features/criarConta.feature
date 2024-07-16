# language: pt
Funcionalidade: Preencher senha após preencher nome de usuário

Cenário: criação de conta
    Dado que o usuário está na página inicial do DemoBlaze
    Quando o usuário completa o processo de criação e login de conta
    Então o usuário deve visualizar o botão "Log out"
