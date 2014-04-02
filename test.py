from tinywebdb import TinyWebDB
import config

# 'host' might be "berea.edu"
# 'path' might be "tinywebdb"
# 'db' might be 'mattdb' (or anything you desire)
# Note that 'db' is an optional parameter, and is not supported
# by most TinyWebDB instances.

tdb = TinyWebDB(config.host, config.path, config.db)

print tdb.getURL()
print tdb.getvalue("fish")

for i in range(3):
  print "SET: " + str(tdb.setvalue("counter", i))
  print "GET: " + str(tdb.getvalue("counter"))

