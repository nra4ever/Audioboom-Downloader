import requests, re, os

print("Audioboom Downloader by nra4ever v1")
print("Enter audioboom channel URL: ")
curl = input()
ddir = input("Enter the desired download directory: ")
assert os.path.exists(ddir), "I did not find the directory at, "+str(ddir)
ldata = []
d = 0
page = 0

print("Finding channel page amount...")

for i in range(1000):
    r = requests.get(curl + '?page=' + str(i + 1))
    texty = r.text.splitlines()
    for line in texty:
        if line == '<p>This podcast has no episodes yet</p>':
            page = i
            break
        else:
            continue
    else:
        continue
    break

print("Channel has " + str(page) + " pages.")
print("Fetching and parsing download links...")

for i in range(page):
    r = requests.get(curl + '?page=' + str(i + 1))
    texty = r.text.splitlines()
    for line in texty:
        if re.search('oom.com/posts', line):
            lnk = line[line.find('https'):]
            url = ''.join(lnk.partition('"')[0:2])
            data = url.rstrip('"') + ".mp3"
            ldata.append(data)
            print("found episode " + data)

dlinks = set(ldata)
print("Downloading Episodes...")

for url in dlinks:
    fnstr = url[url.find('posts/'):][14:]
    print("Downloading " + fnstr)
    s = requests.get(url)
    with open(ddir + fnstr, 'wb') as f:
        f.write(s.content)
        d = +1
print("Finished, downloaded " + str(d) + " files.")
