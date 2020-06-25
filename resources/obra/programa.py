from PIL import Image
from resizeimage import resizeimage

minimo = 200
menor = 320
medio = 480
maior = 640
gigante = 800
xgigante = 1040





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
            tamanho=minimo
            t="minimo"
        elif cont == 1: 
            tamanho=menor
            t="menor"
        elif cont == 2:
            tamanho=medio
            t="medio"
        elif cont == 3:
            tamanho=maior
            t="maior"
        elif cont == 4:
            tamanho=gigante
            t="gigante"
        elif cont == 5:
            tamanho=xgigante
            t="xgigante"
        with open(origem, 'r+b') as arquivo:
            with Image.open(arquivo) as imagem:
                cover = resizeimage.resize_cover(imagem, [tamanho, tamanho])
                cover.save(item, imagem.format)
                print(f"\t{item}=>tamanho:{tamanho}x{tamanho}")
              
                file = open(f"{t}.json", "a")
                file.write("{")
                file.write(f'"tamanho": "{t}",')
                file.write(f'"imagem": "https://gusleaooliveira.github.io/mrconstrucoes-img/resources/obra/{item}"')
                file.write("}")
                file.write("\n")
                file.close()

    print("]")

file.close()

