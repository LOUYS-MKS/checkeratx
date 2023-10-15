#!/bin/bash

check_installed() {
    if [ -f "/usr/lib/checkuser/atx.py" ]; then
        return 0  # Já instalado
    else
        return 1  # Não instalado
    fi
}

if check_installed; then
    echo "Desinstalando o Checkuser..."
    pkill -f atx.py  # Parar o processo atx.py
    rm -f /usr/lib/checkuser/atx.py  # Remover o arquivo atx.py
    rm -f /usr/bin/chuser  # Remover o script chuser
    rm -f /usr/bin/userscheck  # Remover o script userscheck
    rmdir /usr/lib/checkuser  # Remover o diretório /usr/lib/checkuser
    echo "Checkuser desinstalado com sucesso."
else
    echo "O Checkuser não está instalado."
fi
