from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

fake = Faker()

def acessar_site(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.demoblaze.com")

def verificar_titulo(context, titulo):
    elemento_a = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nava"))
    )
    titulo_elemento = elemento_a.text.strip()
    assert titulo == titulo_elemento, f"Título esperado '{titulo}', mas encontrado '{titulo_elemento}'"

def clicar_botao_sign_up(context):
    botao_sign_up = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign up"))
    )
    botao_sign_up.click()
    time.sleep(2)

def preencher_nome_usuario(context):
    nome_usuario = fake.user_name()
    campo_usuario = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "sign-username"))
    )
    campo_usuario.clear()
    campo_usuario.send_keys(nome_usuario)
    context.nome_usuario = nome_usuario

def preencher_senha(context, senha):
    campo_senha = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "sign-password"))
    )
    campo_senha.clear()
    campo_senha.send_keys(senha)

def clicar_botao_login(context):
    botao_login = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#signInModal > div > div > div.modal-footer > button.btn.btn-primary'))
    )
    botao_login.click()
    time.sleep(2)

def aceitar_popup_confirmacao(context):
    alert = WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    alert.accept()
    time.sleep(1)

def clicar_botao_log_in(context):
    botao_log_in = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    botao_log_in.click()

def preencher_nome_usuario_login(context):
    campo_login_usuario = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    campo_login_usuario.clear()
    campo_login_usuario.send_keys(context.nome_usuario)

def preencher_senha_login(context, senha):
    campo_login_senha = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    campo_login_senha.clear()
    campo_login_senha.send_keys(senha)

def clicar_botao_login_modal(context):
    botao_login_modal = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#logInModal > div > div > div.modal-footer > button.btn.btn-primary'))
    )
    botao_login_modal.click()
    time.sleep(2)

def verificar_botao_logout(context):
    botao_logout = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout2"))
    )
    assert botao_logout.is_displayed(), "Botão 'Log out' não encontrado"

def adicionar_item_ao_carrinho(context):
    # Aqui você pode adicionar o código para encontrar e clicar no botão para adicionar um item ao carrinho
    pass

@given('que o usuário está na página inicial do DemoBlaze')
def step_impl(context):
    acessar_site(context)

@when('o usuário completa o processo de criação e login de conta')
def step_impl(context):
    acessar_site(context)
    verificar_titulo(context, "PRODUCT STORE")
    clicar_botao_sign_up(context)
    preencher_nome_usuario(context)
    preencher_senha(context, "Po22lty.@")
    clicar_botao_login(context)
    aceitar_popup_confirmacao(context)
    clicar_botao_log_in(context)
    preencher_nome_usuario_login(context)
    preencher_senha_login(context, "Po22lty.@")
    clicar_botao_login_modal(context)

@then('o usuário deve visualizar o botão "Log out"')
def step_impl(context):
    verificar_botao_logout(context)
    context.driver.quit()

@when('o usuário clica no botão Samsung galaxy s6 e coloca dentro do carrinho')
def step_impl(context):
    link_samsung = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Samsung galaxy s6'))
    )
    link_samsung.click()

    # Aguardar o botão "Add to cart" e clicar
    botao_add_to_cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@onclick="addToCart(1)"]'))
    )
    botao_add_to_cart.click()

    # Aguardar o popup de confirmação e clicar em "OK"
    WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    alert.accept()

    # Clicar no link "Home"
    link_home = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link" and @href="index.html"]'))
    )
    link_home.click()

@when('o usuário clica no botão Nokia Sony vaio i5 e coloca dentro do carrinho')
def step_impl(context):
    link_laptops = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="itemc" and @onclick="byCat(\'notebook\')"]'))
    )
    link_laptops.click()
    # Clicar no link "Sony vaio i5"
    link_sony_vaio = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="prod.html?idp_=8"]'))
    )
    link_sony_vaio.click()

    # Aguardar o botão "Add to cart" e clicar
    botao_add_to_cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@onclick="addToCart(8)"]'))
    )
    botao_add_to_cart.click()

    # Aguardar o popup de confirmação e clicar em "OK"
    WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    alert.accept()

    # Clicar no link "Home"
    link_home = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link" and @href="index.html"]'))
    )
    link_home.click()

    


@when('o usuário clica no botão Apple monitor 24 e coloca dentro do carrinho')
def step_impl(context):
    link_monitors = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="itemc" and @onclick="byCat(\'monitor\')"]'))
    )
    link_monitors.click()

    # Clicar no link "Apple monitor 24"
    link_apple_monitor = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="prod.html?idp_=10" and @class="hrefch"]'))
    )
    link_apple_monitor.click()

    # Aguardar o botão "Add to cart" e clicar
    botao_add_to_cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@onclick="addToCart(10)"]'))
    )
    botao_add_to_cart.click()

    # Aguardar o popup de confirmação e clicar em "OK"
    WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    alert.accept()

    # Clicar no link "Home"
    link_home = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link" and @href="index.html"]'))
    )
    link_home.click()

@when('clica no carrinho')
def step_impl(context):
    elemento_navegacao = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#navbarExample > ul > li:nth-child(4) > a'))
    )
    elemento_navegacao.click()
    time.sleep(2)

@then('o usuario verifica que os três itens estão no carrinho')
def step_impl(context):
    itens_esperados = ["Samsung galaxy s6", "Sony vaio i5", "Apple monitor 24"]
    for item in itens_esperados:
        elemento_item = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//td[text()="{item}"]'))
        )
        assert elemento_item.text == item, f"Item '{item}' não encontrado no carrinho."

@then('o usuario clica no botão "Delete" e verifico')
def step_impl(context):
    # Encontrar todos os elementos de linha na tabela
    rows = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//tbody[@id="tbodyid"]/tr'))
    )
    
    item_deleted = False
    
    # Iterar sobre cada linha para encontrar o item "Apple monitor 24" e deletá-lo
    for row in rows:
        # Verificar se o texto da segunda coluna (Title) é "Apple monitor 24"
        if "Apple monitor 24" in row.find_element(By.XPATH, './td[2]').text:
            # Encontrar e clicar no link "Delete" na quarta coluna (td[4])
            delete_link = row.find_element(By.XPATH, './td[4]/a')
            delete_link.click()
            item_deleted = True
            break  # Interromper o loop assim que o item for deletado

    elemento_navegacao = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#navbarExample > ul > li:nth-child(4) > a'))
    )
    elemento_navegacao.click()
    time.sleep(3)

    itens_esperados = ["Samsung galaxy s6", "Sony vaio i5"]
    for item in itens_esperados:
        elemento_item = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//td[text()="{item}"]'))
        )
        assert elemento_item.text == item, f"Item '{item}' não encontrado no carrinho."
    

