import time
import webbrowser

i = input()

server_name = i.split(' ')[1]

time.sleep(1)

print(server_name+'\'s password:')

i = input()

time.sleep(2)
print()
print('Welcome to susnet. Geoff is indeed sus.')

f = open('among_us.txt', 'r')
lines = f.readlines()

time.sleep(2)

for line in lines:
    print(line, end='')
    time.sleep(0.03)

print('Opening Susnet\'s homepage.')

webbrowser.open('https://www.alexlwyen.com/')

# i = input()

