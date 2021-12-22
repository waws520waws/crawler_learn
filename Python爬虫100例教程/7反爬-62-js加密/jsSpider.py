import execjs


def strdecode(autuurl):
    with open('base64dec.js', 'r', encoding='utf-8') as f:
        js = f.read()

    ctx = execjs.compile(js)

    for str_enc in autuurl:
        ctx.call('base64decode', str_enc)
        Gword = '21b5del6oIO57e01a'
        hn = 'ac.scmor.com'
        key = Gword + hn
        length = len(key)
        for i in range(len(str_enc)):
            k = i % length



def main():
    autourl = ["ZAM0RgYmLl0Ne3pZfjZxATgbMlcpJD8HKEMyGDdlfBVsMDcBbzgAf2xjJEhoDDBWYBkAFyE1eAghLA8M",
               "U3kwBQctIQAjMHZdVC1xRDs5LVQqURUfKxwQGjQACBZ5VysGVytwfmVgDQBVKSMZYRpbGwxAFhYOKl5JAWZRDw4EXzwWBwMT",
               "U3kwBQctIQAjMHZPbldbRQApNUc/DiMZEH1WBQ9bCV8=", "U3kwBQctIQAjMHZPbhwFRjg2VkUqNyAWP31WBQ8AARQ=",
               "U3kwBQctIQAjMHYGU1ZTRAMmD0cQDisWF31WBzRLBAhXDV1R",
               "U3kwBQctIQAjMHZdVC1xRDs5LVQqURUfKxwQGjQACBZ5VysGVytwfmVgDQBVKSBVYgpaXSMqfxYOOgdDLk8mEyNjIXg=",
               "U3kwBQctIQAjMHZdVC1xRDs5LVQqURUfKxwQGjQACBZ5VysGVytwfmVgDQBVKSBVYgpaBw41FxY1X3gAAH0yEyBbCzoVBw4TUkhUUQEdMhUIJz9bAic/RlMjCFk=",
               "U3kwBQctIQAjMHYBVBwFSzhSJRsRJCtcPkMtGQ9hCV8=",
               "U3kwBQctIQAjMHZPbldYRwMmJVc/DhUHEEM5Bw9cfw1RN1AGVAZxcg=="]

    strdecode(autourl)


if __name__ == '__main__':
    main()