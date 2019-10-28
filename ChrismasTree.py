def ChrismasTree(s,N):
    for i in range(N):
        char_ = ""
        for j in range(N-i):
            char_ = char_ + 'x'
        for j in range(i-1):
            if i > 0:
                char_ = char_ + 'c'
                char_ = char_ + 'x'
        char_ = char_ + 'c'
        for j in range(N-i):
            char_ = char_ + 'x'
        print(char_)
if __name__ == '__main__':
    tree = ChrismasTree('c',5)