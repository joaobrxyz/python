import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;31mO site PUDIM não está acessível no momento.')
else:
    print('\033[1;32mConsegui acesssar o site PUDIM com sucesso.')
    print(site.read())
