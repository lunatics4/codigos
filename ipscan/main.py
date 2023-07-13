import os # Trabalhar com o SO
import platform # Utilizada para identificar o tipo SO
import subprocess, threading # Criação e Manipulacao de Threads
import ipaddress

class IPScan:
    def __init__(self):
        self.comm='' # Comando enviado ao SO
        self.output='' # Redirecionamento da Saída do comm
        self.address = input('Digite IP/Mask:')
        self.ips = ipaddress.ip_network(self.address,False).hosts()
        self.checkSO()
        # Verificacao de Cada host encontrado
        for ip in list(self.ips): # Para cada ip
            # Criar uma Thread para testar
            th = threading.Thread(target=self.checkIP, args=(ip,))
            th.start()
    
    def checkSO(self):
        so = platform.system()
        if so == 'Windows':
            self.comm = 'ping -n 1 '
            self.output = ' > null'
        elif so == 'Linux':
            self.comm = 'ping -c 1 -W 1 '
            self.output = ' >/dev/null 2>&1'

    def checkIP(self, ipaddress):
        # Envia o comando pela SystemCall do SO e recebe a resposta
        response = os.system(self.comm + str(ipaddress) + self.output)
        if response == 0:
            print('IP:', ipaddress, ' esta ativo')


# Corpo do Programa
if __name__ == '__main__':
    ip = IPScan()