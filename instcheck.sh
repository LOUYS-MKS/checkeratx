#!/bin/bash


sudo apt update && sudo apt upgrade
sudo apt-get install dialog
sleep 7
echo "Aguarde..."
check_installed() {
    if [ -f "/usr/lib/chuser/atx.py" ]; then
        return 0  # Já instalado
    else
        return 1  # Não instalado
    fi
}
clear






dialog --infobox "Configurando o fuso horário..." 5 40
echo "America/Sao_Paulo" > /etc/timezone
ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime > /dev/null 2>&1
dpkg-reconfigure --frontend noninteractive tzdata > /dev/null 2>&1

clear
dialog --msgbox "INSTALAR CHECKUSER ATX TUNNEL" 7 40
dialog --msgbox "By @LOUYSZHX" 5 40

dialog --yesno "Pressione Sim para continuar ou Não para sair." 7 40
response=$?
if [ $response -eq 1 ]; then
    clear
    exit 1
fi

clear
dialog --infobox "Iniciando instalação. Aguarde..." 5 40
apt-get install figlet -y > /dev/null 2>&1
pip3 install flask > /dev/null 2>&1
rm /bin/chuser > /dev/null 2>&1
sleep 5
cd /bin || exit
wget https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/chuser > /dev/null 2>&1
wget https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/userscheck > /dev/null 2>&1
chmod 777 chuser > /dev/null 2>&1
chmod 777 userscheck > /dev/null 2>&1

clear
dialog --infobox "Concluindo a instalação..." 5 40
mkdir /usr/lib/checkuser > /dev/null 2>&1
cd /usr/lib/checkuser || exit
rm atx.py > /dev/null 2>&1
wget https://raw.githubusercontent.com/LOUYS-MKS/checkeratx/main/atx.py > /dev/null 2>&1
chmod 777 atx.py > /dev/null 2>&1

clear
dialog --msgbox "INSTALAÇÃO CONCLUÍDA" 5 40

clear
dialog --msgbox "Comando principal: chuser" 5 40

cat /dev/null > ~/.bash_history && history -c
