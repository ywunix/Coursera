import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
text = fh.read()

domains = re.findall(r'From:\s+?\S+@(\S+)', text)
sync_tick = 0
for domain in domains:
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))

    sync_tick += 1
    if sync_tick > 50:
        conn.commit()
        sync_tick = 0
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 21'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()