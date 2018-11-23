
import pickle



temp = {"day":1, "age":10, "name":"lpc"}

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()