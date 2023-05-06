import logging
w,h = [int(i) for i in input().split()]
image = [" " for i in range(h+10)]
code = input().split()
color = int(code[0]=='W')
BW='# '
code = [int(c) for c in code[1:][::2]]
R=0
w+=1
for c in code:
    image[R]+=BW[color%2]*c
    while len(image[R])>w:
        image[R+1]+=image[R][w:]
        image[R]=image[R][:w]
        R+=1
    color+=1

# logging.error('\n'.join(image))
image = list(filter(lambda x: len(x)>1, image))
# logging.error('\n'.join(image))
lines = []
I=0
while len(lines)==0:
    # logging.error(I)
    RI=[r[I] for r in image]
    # logging.error(''.join(RI))
    lines = []
    L1 = -1
    for i in range(len(RI)):
        if L1<0 and RI[i]=='#':
            L1=i
        elif L1>=0 and RI[i]==' ':
            lines+=[[L1-1,i]]
            L1=-1
    I+=1
I-=1
empty_row=[r[I] for r in image]
empty_6row=[i for i in empty_row]

line6=[lines[-1][0]+(lines[-1][0]-lines[-2][0])+1,lines[-1][1]+(lines[-1][1]-lines[-2][1])]

for i in range(lines[-1][0]+(lines[-1][0]-lines[-2][0])+1,lines[-1][1]+(lines[-1][1]-lines[-2][1])):
    empty_6row[i]='#'

# logging.error('\n'.join(''.join(image[y][x] if x%2==0 else empty_6row[y] for x in range(len(image[y]))) for y in range(len(image))))
# raise Exception()
cols = [[r[x] for r in image] for x in range(len(image[len(image)//2]))]
runs = []
for col in cols:
    L=0
    for x in col:
        if x==' ':
            runs+=[L]
            L=0
        else:
            L+=1
    runs+=[L]
runs = sorted(set(runs), reverse=True)
# logging.error(runs)
while runs[0]<runs[1]+lines[0][1]-lines[0][0]:runs=runs[1:]
# logging.error(runs)
staff_length=runs[0]
staff_cols=[]
for i in range(len(cols)):
    L=0
    for x in cols[i]:
        if x==' ':
            if L>=staff_length:
                staff_cols+=[i]
            L=0
        else:
            L+=1
    if L>=staff_length:
        staff_cols+=[i]

# logging.error(staff_cols)

# logging.error("START")


notePoints=[]
LS='\n'.join(image[L[0]]+"\n"+image[L[1]] for L in lines).split('\n')
for i in range(min(len(L) for L in LS)):
    # logging.error(''.join(L[i] for L in LS))
    if sum(int(L[i]=='#')for L in LS)>2:notePoints+=[i]

for i in range(len(notePoints))[::-1]:
    if notePoints[i]-1 in notePoints:
        notePoints=notePoints[:i]+notePoints[i+1:]
# logging.error("END")

def getNote(height, lines):
    if height < lines[0][0]:
        return 'G'
    elif height < lines[0][1]:
        return 'F'
    elif height < lines[1][0]:
        return 'E'
    elif height < lines[1][1]:
        return 'D'
    elif height < lines[2][0]:
        return 'C'
    elif height < lines[2][1]:
        return 'B'
    elif height < lines[3][0]:
        return 'A'
    elif height < lines[3][1]:
        return 'G'
    elif height < lines[4][0]:
        return 'F'
    elif height < lines[4][1]:
        return 'E'
    elif height < line6[0]:
        return 'D'
    elif height < line6[1]:
        return 'C'
    else:
        return 'B'

empty_sum = sum(int('#'==empty_row[i]) for i in range(len(empty_row)))
notes = list(filter(lambda x: sum(int('#'==r[x]) for r in image)!=0 and [r[x] for r in image]!=empty_row and [r[x] for r in image]!=empty_6row and (x not in staff_cols), range(len(image[lines[0][0]]))))
logging.error("Cols with Notes: "+str(notes))
temp_notes = []
TN1 = -1
for i in range(len(notes)):
    if i==0:
        TN1=i
        continue
    if abs(notes[i]-notes[i-1])>1:
        temp_notes+=[[TN1, i]]
        TN1=i
temp_notes+=[[TN1, len(notes)-1]]
if  abs(notes[-2]-notes[-1])>1:temp_notes += [[len(notes)-1, len(notes)-1]]
notes = [[notes[note[0]], notes[note[1]-1]+1]for note in temp_notes]
logging.error("Areas of Notes: "+str(notes))

temp_notes=[]
for note in notes:
    possible_y = list(filter(lambda i: not(True in [i>=line[0] and i<line[1]for line in lines]), range(len(image))))
    logging.error("Y: "+' '.join(str(i) for i in possible_y))
    logging.error('\n'+'\n'.join([''.join([image[y][x] for y in possible_y]) for x in range(note[0], note[1])]))
    points = [list(filter(lambda y: image[y][x]=='#', possible_y)) for x in range(note[0], note[1])]
    logging.error("Points: "+' || '.join(' '.join(str(y) for y in x) for x in points))
    points = [sum(x)/len(x) for x in points]
    logging.error("Point Avgs: "+' '.join(str(i) for i in points))
    height = sum(points)/len(points)
    color = [int('#'==image[i][(note[0]+note[1])//2]) for i in range(len(empty_row))]
    color = sum(color)-([1,2][height<lines[4][1]]*(lines[0][1]+lines[0][0]))>empty_sum
    color = ['H','Q'][color]
    temp_notes += [[getNote(height, lines), color]]
notes=temp_notes


# logging.error('\n'.join(image))
# logging.error("")
# logging.error('\n'.join(''.join(L[i]for i in notePoints) for L in LS))
logging.error(lines)
logging.error("")
logging.error(' '.join(str(i) for i in notePoints))
logging.error("")
print(' '.join(''.join(N) for N in notes))
