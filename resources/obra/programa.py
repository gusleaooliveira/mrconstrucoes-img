from PIL import Image
from resizeimage import resizeimage

minimo = 200
menor = 320
medio = 480
maior = 640
gigante = 800
xgigante = 1400


for i in range(0, 29):
    lista = [ 
        f"minimo/imagem{i}-{minimo}x{minimo}.jpg",
        f"menor/imagem{i}-{menor}x{menor}.jpg",
        f"medio/imagem{i}-{medio}x{medio}.jpg",
        f"maior/imagem{i}-{maior}x{maior}.jpg",
        f"gigante/imagem{i}-{gigante}x{gigante}.jpg",
        f"xgigante/imagem{i}-{xgigante}x{xgigante}.jpg"
    ]
    origem = f"imagem{i}.jpg"

    print(f"imagem{i}=[")
    for cont, item  in enumerate(lista):
        if  cont == 0:
            tamanho=menor
        elif cont == 1: 
            tamanho=menor
        elif cont == 2:
            tamanho=medio
        elif cont == 3:
            tamanho=maior
        with open(origem, 'r+b') as arquivo:
            with Image.open(arquivo) as imagem:
                cover = resizeimage.resize_cover(imagem, [tamanho, tamanho])
                cover.save(item, imagem.format)
                print(f"\t{item}=>tamanho:{tamanho}x{tamanho}")
    print("]")

