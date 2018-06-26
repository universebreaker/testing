

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

def list_counting(url):
    file_list = {}
    for link in url:
        file_name = link.rsplit('/',1)[-1]
        if file_name in file_list:
            file_list[file_name] += 1
        else:
            file_list[file_name] = 1
    count_list = {}
    for key, value in file_list.items():
        if value in count_list:
            count_list[value].append(key)
        else:
            count_list[value] = [key]
    c_out = list(reversed(list(set(count_list.keys()))))
    print_count = 0
    while print_count < 3:
        if len(c_out) == 0:
            return
        c = c_out.pop(0)
        count_list[c].sort()
        for name in count_list[c]:
            if print_count < 3:
                print(name + ' ' + str(c))
                print_count += 1

list_counting(urls)
