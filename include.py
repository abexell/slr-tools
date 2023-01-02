import bibtexparser
import sys

def ask(e):
    print()
    print(e.get('title'))
    print(e.get('abstract'))
    print(e.get('author_keywords'))
    return input(sys.argv[1] + '> ')

with open(sys.argv[2]) as f:
    refs = bibtexparser.load(f)

for ref in refs.entries:
    if not ref.get(sys.argv[1]):
        ref[sys.argv[1]] = ask(ref)
    with open(sys.argv[2], 'w') as f:
        bibtexparser.dump(refs, f)

