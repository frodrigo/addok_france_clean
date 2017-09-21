import re

def clean_query(q):
  q = str(q) # Hack, why I need this ?
  q = re.sub(r'\bb\.? ?p\.? ?[\d]*', '', q, flags=re.IGNORECASE) # Orverload
  q = re.sub(r'\bb(a|â)t(\.|iment)?\s*([0-9]+|[A-Z]\s+)', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bporte ?([0-9]+|[A-Z]\s+)', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bbureau ?([0-9]+|[A-Z]\s+)', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\b([eé]tage) ?[0-9]{1,2}', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bN[o°](?=[ 0-9])', '', q, flags=re.IGNORECASE)
  q = re.sub(r'\bl-?([0-9]{4})', '\\1', q, flags=re.IGNORECASE)
  q = re.sub('\(.*?\)', '', q, flags=re.IGNORECASE)
  return q
