# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

st = 'Но внеабв тут они заехали за почтиабв последний поворот'

st1 = st.split()
res = list(filter(lambda x: not 'абв' in x, st1))
res1 = ' '.join(res)

print(res1)
