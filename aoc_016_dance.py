

def swap(progs, p, q):
    progs[p], progs[q] = progs[q], progs[p]


def dance(progs):
    with open('016_input.txt','r') as f:
        for line in f:
            for move in line.strip().split(','):
                if move[0] == 's':
                    nprogs = int(move[1:])
                    progs = progs[-nprogs:] + progs[:-nprogs]

                elif move[0] == 'x':
                    moves = move.split('/')
                    p,q = int(moves[0][1:]), int(moves[1])
                    swap(progs, p, q)

                else:
                    moves = move.split('/')
                    p,q = progs.index(ord(moves[0][1:])-97), progs.index(ord(moves[1])-97)
                    swap(progs, p, q)

    return progs


progs = list(range(16))
progs = dance(progs)
final_progs = ''.join([chr(i+97) for i in progs])
print(final_progs)
