from selenium import webdriver
from selenium.webdriver import chrome
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
#inicialização do driver 
chrome =  webdriver.Chrome(executable_path='C:\\webbot\\chromedriver') #o executable_path é utilizado principalmente no windows, para garantir que o chrome seja iniciado corretamente.

#Abrir uma janela e acessar uma pagina qualquer
chrome.get('https://www.google.com.br')

#Encontra um elemento via xpath
chrome.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')

#Encontra um elemento via id



chrome.find_element_by_name('q')

#Encontra um elemento via tag
chrome.find_element_by_tag_name('input')

#Escrever em um campo 
chrome.find_element_by_name('q').send_keys('Web Bot')
sleep(1)
#Pressiona a tecla enter em um elemento 
chrome.find_element_by_name('q').send_keys(u'\ue007')

#Executa um click
chrome.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a[1]/h3/div').click()
sleep(10)
#Fecha a janela
chrome.close()
exit()
