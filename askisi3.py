file = raw_input('Dwste arxeio: ')
with open(file,'r') as f:
    lines=f.readlines()

with open(file,'w') as f:
    for line in lines :
        if line.strip().startswith('#'):
            lines.remove(line)
    f.writelines(lines)

print 'Comments have been removed'
