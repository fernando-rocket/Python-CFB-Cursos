import urllib.request

pagina = urllib.request.urlopen("http://cfbcursos.com.br/modelocursopython.html")

texto = pagina.read().decode("utf8")

dado = texto[0:15]

produto_posicao_inicial = texto.find("Mouse")
preco = texto[produto_posicao_inicial+26:produto_posicao_inicial+26+7]

print(dado)
print(produto_posicao_inicial)
print(preco)
