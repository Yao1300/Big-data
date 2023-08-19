def est_numerque(chaine):
  reponse=True
  for a in chaine:
     if a in ['0','1','2','3','4','5','6','7','8','9']:
        continue
     else:
        reponse=False
        break
  return reponse
print(est_numerque('3'))
print(est_numerque('b'))