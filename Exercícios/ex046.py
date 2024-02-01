from time import sleep
import emoji
print('\033[1;33m-=' * 20)
print('\033[1;34mCONTAGEM REGRESSIVA')
print('\033[1;33m-=' * 20)
for r in range(10, -1, -1):
    print('\033[36m', r)
    sleep(1)
for c in range(0, 19):
    print(emoji.emojize('\033[31m:fireworks:\033[32m:fireworks:\033[34m:fireworks:', use_aliases=True), end='')
print(' FELIZ 2021!')
