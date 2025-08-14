loja1 = {'iPhone 14 Pro', 'Galaxy S23', 'Huawei P50', 'Motorola Edge 40'}
loja2 = {'iPhone 14 Pro', 'Galaxy S23', 'Xiaomi 13', 'LG Velvet'}

uni = loja1 | loja2
print("Todos os modelos disponiveis nas lojas:", uni)

inter = loja1 & loja2
print("Modelos disponiveis em ambas as lojas: ", inter)
