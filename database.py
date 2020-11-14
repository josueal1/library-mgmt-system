from replit import db

def showDB():
  for k,v in db.items():
    print(k,v)
    print()


def delete(item:'str'):
  del db[item]
