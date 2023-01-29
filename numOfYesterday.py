f = open("yesterday.txt" , "r")
yesterday_lyric = ""
'''
갯수를 나눠서 세는 프로그램
'''
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + '/n'
f.close()
n_of_yesterday = yesterday_lyric.count("yesterday")
n_of_YESTERDAY = yesterday_lyric.count("YESTERDAY")

print("Number of a Word 'yesterday'" , n_of_yesterday)
print("Number of a Word 'YESTERDAY'" , n_of_YESTERDAY)