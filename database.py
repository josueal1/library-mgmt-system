from replit import db

def getDB(q=None):
  if (db and q):
    filtered_db_copy = {}

    for k,info in db.items():
      # every metadata in a book info
      for md in info.values():
        q = q.lower()
        md = md.lower()

        # mentioned at least once in any field
        if (q in md) or (md in q):
          filtered_db_copy[k] = info
          # skip the rest of md, move to next book
          break

    return filtered_db_copy
    
  else:
    return db
    

def delete(item:'str'):
  bid_deleted = db.pop(str(item))
  return bid_deleted


def insert(isbn, metadata) -> 'bool':
  # separate isbn and metadata
  try:
    success_entry = True
    db[isbn] = metadata
  except Exception as e:
    return False
  else:
    return True
