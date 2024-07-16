# language: pt
Funcionalidade: Testar funcionalidades do site

Cenário: Adicionando três itens ao carrinho
    Dado que o usuário está na página inicial do DemoBlaze
    Quando o usuário completa o processo de criação e login de conta
    E o usuário clica no botão Samsung galaxy s6 e coloca dentro do carrinho
    E o usuário clica no botão Nokia Sony vaio i5 e coloca dentro do carrinho
    E o usuário clica no botão Apple monitor 24 e coloca dentro do carrinho
    E clica no carrinho
    Então o usuario verifica que os três itens estão no carrinho
