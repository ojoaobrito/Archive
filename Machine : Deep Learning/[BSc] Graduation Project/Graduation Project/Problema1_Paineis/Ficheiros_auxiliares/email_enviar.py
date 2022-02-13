import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os, natsort, sys, shutil

with open("run_atual.txt","r") as ficheiro:
    conteudo = (ficheiro.read()).split("\n")

path = "/home/socialab/Desktop/Projeto/BIODI/Gender/Debug/Gender_Disjoint_2_Iteration_1"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

escolhida = diretoria[len(diretoria)-1]
diretoria_final = os.listdir(path + "/" + escolhida)

for i in diretoria_final:
    if(i!="best_model.data-00000-of-00001"):
        shutil.copyfile(path + "/" + escolhida + "/" + i,"/home/socialab/Desktop/resultados/" + i)

shutil.make_archive("Resultados (" + conteudo[len(conteudo)-2] + ")", 'zip', "/home/socialab/Desktop/resultados")

email_user = 'jpedrocb98@gmail.com'
email_password = 'Dialga1998'
email_send = 'jpcruzbrito@hotmail.com'

subject = 'Resultados da aprendizagem'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = ''
msg.attach(MIMEText(body,'plain'))

filename='/home/socialab/Desktop/resultados.zip'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.quit()