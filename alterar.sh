#!/bin/bash

cont=0
for FILENAME in temp/* ; do
    cont=$((cont=cont+1))
    mv $FILENAME "imagens/imagem-$cont.jpg"
done

ls imagens