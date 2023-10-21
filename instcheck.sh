#!/bin/bash

# Atualiza os pacotes e faz upgrade
sudo apt update && sudo apt upgrade

# Instala o pacote "dialog"
sudo apt-get install dialog

# Aguarde 7 segundos
sleep 7

# Configura o fuso horário
echo "Configurando o fuso horário..."
echo "America/Sao_Paulo" > /etc/timezone
ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
dpkg-reconfigure --frontend noninteractive tzdata

# Verifica se o arquivo "/usr/lib/chuser/atx.py" existe
check_installed() {
    if [ -f "/usr/lib/chuser/atx.py" ]; then
        return 0  # Já instalado
    else
        return 1  # Não instalado
    fi
}

# Limpa a tela
clear

# Exibe mensagens usando "dialog"
dialog --infobox "INSTALAR CHECKUSER ATX TUNNEL" 7 40
dialog --msgbox "By @LOUYSZHX" 5 40

dialog --yesno "Pressione Sim para continuar ou Não para sair." 7 40
response=$?
if [ $response -eq 1 ]; then
    clear
    exit 1
fi

# Continua com a instalação
clear
dialog --infobox "Iniciando instalação. Aguarde..." 5 40

# Instala pacotes adicionais
apt-get install figlet -y
pip3 install flask
rm /bin/chuser

# Aguarda 5 segundos
sleep 5

# Move para a pasta /bin e baixa arquivos
cd /bin || exit
wget -q https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/chuser
wget -q https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/userscheck
chmod 777 chuser
chmod 777 userscheck

# Continua com a instalação
clear
dialog --infobox "Concluindo a instalação..." 5 40

# Cria uma pasta e baixa o arquivo atx.py
mkdir -p /usr/lib/checkuser
cd /usr/lib/checkuser || exit
rm atx.py
wget -q https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/atx.py
chmod 777 atx.py

# Finaliza a instalação
clear
dialog --msgbox "INSTALAÇÃO CONCLUÍDA" 5 40
dialog --msgbox "Comando principal: chuser" 5 40

# Limpa o histórico do bash
cat /dev/null > ~/.bash_history && history -c
