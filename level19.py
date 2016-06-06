import array,wave
import email

mail=email.message_from_file(open('19.txt'))
for part in mail.walk():
  if part.get_content_maintype()=='audio':
    audio=part.get_payload(decode=1)
    open('19_indian.wav', 'wb').write(audio)
wi = wave.open('19_indian.wav','rb')
wo = wave.open('19_indian_inv.wav', 'wb')
wo.setparams(wi.getparams())
a = array.array('i')
a.fromstring(wi.readframes(wi.getnframes()))
a.byteswap()
wo.writeframes(a.tostring())
wi.close(),wo.close()
