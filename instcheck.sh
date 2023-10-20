#!/bin/bash


sudo apt update && sudo apt upgrade
sudo apt-get install dialog
sleep 7


# Verifica se o usuário é root
if [ "$EUID" -ne 0 ]
  then echo "Execute este script como superusuário (root)."
  exit
fi

# Atualiza o sistema
apt update
apt upgrade -y

# Instala dependências
apt-get install -y dialog python3-pip figlet

# Configura o fuso horário
echo "America/Sao_Paulo" > /etc/timezone
ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
dpkg-reconfigure --frontend noninteractive tzdata

# Instala o Flask
pip3 install flask

# Remove versões antigas, se existirem
rm /usr/lib/checkuser/atx.py
rm /bin/chuser
rm /bin/userscheck

# Baixa os arquivos necessários
cd /usr/lib/checkuser
wget https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/atx.py
chmod 777 atx.py

cd /bin
wget https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/chuser
wget https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/userscheck
chmod 777 chuser
chmod 777 userscheck

# Limpa o histórico do shell
cat /dev/null > ~/.bash_history
history -c

# Fim
echo "Instalação concluída. Comando principal: chuser"
