import rotor 
def encrypt(data):
  key_a = '!@#$%^&*' 
  key_b = 'abcdefgh' 
  key_c = '<>{}:"' 
  secret = key_a*4 + '|' + (key_b + key_a+key_c)*2 + '|' +key_b*2+'EOF'
  rot = rotor.newrotor(secret)
  return rot.decrypt(data)

def decrypt(data):
  key_a = '!@#$%^&*' 
  key_b = 'abcdefgh' 
  key_c = '<>{}:"' 
  secret = key_a*4 + '|' + (key_b + key_a+key_c)*2 + '|' +key_b*2+'EOF'
  rot = rotor.newrotor(secret)
  return rot.decrypt(data)

def dec(fileName):
  with open(fileName, mode='rb') as file: # b is important -> binary
    fileContent = file.read()
  return decrypt(fileContent)

print dec("encrypted_flag")
