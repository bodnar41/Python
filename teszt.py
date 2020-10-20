import threading, paramiko, subprocess, time

ip = 'localhost' #input('[*]Enter Server IP Address :')
usr = 'Márk' #input('[*]Enter Username :')
passwd = '****' #input('[*]Enter Password :')
cmd = 'wmic cpu get status'

def ssh_comm(ip, usr, passwd, cmd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=usr, password=passwd)
        ssh_session = client.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(cmd)
            time.sleep(2)
            outout = ssh_session.recv(650000)

            with open("info.txt", "a") as f:
                k = str(outout)
                f.write(k)
                print(outout)
                client.close()
        return


#cmd = 'wmic cpu get name, status, virtualizationfirmwareenabled, manufacturer, description, processorid '  #input('[*]Enter Command :')

ssh_comm(ip, usr, passwd, cmd)




