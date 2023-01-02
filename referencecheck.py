import bibtexparser
import sys

def ty(e):
    return tuple(e.get(f).lower() for f in ("title", "year"))

with open(sys.argv[1]) as f:
    qgs = bibtexparser.load(f)

with open(sys.argv[2]) as f:
    other = bibtexparser.load(f)


#print(f'Quasi gold standard size {len(qgs.entries)}')

#for entry in qgs:
    #print(entry['ID'])


#print(f'Other size {len(other.entries)}')
missing = [e for e in qgs.entries if ty(e) not in (ty(o) for o in other.entries)]

for m in missing:
    print(m['author'], m['year'], m['title'])

print()
print(f'{sys.argv[2]} Missing {len(missing)}, recall {1-len(missing)/len(qgs.entries)}')

