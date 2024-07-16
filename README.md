Projeto de Teste BDD com Selenium para o DemoBlaze
Este projeto utiliza Behave para BDD (Behavior Driven Development) com Selenium para automação de testes no site DemoBlaze.

Pré-requisitos
Python 3.6+
Pip (Python package installer)
Webdriver para o navegador que você deseja usar (ex: ChromeDriver para o Chrome)
Instalação
Clone o repositório:

bash
git clone https://github.com/PedroSanchesFigueiredo/Desafio-Brivia.git
cd seu-repositorio
Crie um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # Para Linux/MacOS
.\venv\Scripts\activate  # Para Windows
Instale as dependências:

bash
pip install -r requirements.txt
requirements.txt:

behave
selenium
faker
Certifique-se de ter o webdriver instalado e disponível no seu PATH.

Estrutura do Projeto
.
├── features
│   ├── steps
│   │   └── steps.py
│   └── teste.feature
├── README.md
└── requirements.txt
features/steps/steps.py: Arquivo com a implementação dos steps do Behave.
features/teste.feature: Arquivo de feature que contém os cenários de teste.
requirements.txt: Arquivo com as dependências do projeto.