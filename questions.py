from Crypto.Cipher import AES
import base64
cipher = AES.new('12345678abcdefgh',AES.MODE_ECB)

def hide(msg):
    newmsg = msg+"".join([" "]*(16-len(msg)%16))  
    print len(msg)
    print len(newmsg)
    encoded = base64.b64encode(cipher.encrypt(newmsg))
    return encoded

def unhide(text):
    decoded = cipher.decrypt(base64.b64decode(text))
    return decoded