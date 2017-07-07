def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1


chain_cache = {1: 1}


def chain_length_recursive(n):
    if n in chain_cache:
        return chain_cache[n]
    else:
        c = 1 + chain_length_recursive(collatz(n))
        chain_cache[n] = c
        return c


def chain_length_iterative(n):
    visited = []
    while True:
        if n in chain_cache:
            l = chain_cache[n]
            while len(visited) > 0:
                l += 1
                n = visited.pop()
                chain_cache[n] = l
            return l
        else:
            visited.append(n)
            n = collatz(n)


def chain_length(n):
    return chain_length_recursive(n)


def longest_chain_under(t):

    m = 0
    m_i = 0
    for n in range(1, t):
        c = chain_length(n)
        if c > m:
            m = c
            m_i = n
            print "New max is %d (from start %d)" % (m, m_i)
    print "Done: Start number %d produces chain %d long" % (m_i, m)
    return m_i
