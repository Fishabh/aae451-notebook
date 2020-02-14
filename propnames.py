import prop_uiuc
import subprocess as sb

prop_db = prop_uiuc.parse_database(False)

names = []
for prop_name in prop_db.keys():
    names.append(prop_name)

names = sorted(names)
f = open('names.txt', 'w')
for name in names:   
    sb.call(["echo", name],stdout=f)