import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("amritashish1221@gmail.com","7376735800")
msg="Hi How are you"
s.sendmail("amritashish1221@gmail.com","avinashshekar12345@gmail.com",msg)
s.quit()
