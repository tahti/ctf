import rotor

def encrypt(data):
  key_a = '!@#$%^&*' 
  key_b = 'abcdefgh' 
  key_c = '<>{}:"' 
  secret = "aa"
  rot = rotor.newrotor(secret)
  return rot.decrypt(data)

