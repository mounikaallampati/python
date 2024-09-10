def main():

    fb_series=fib()
    for fb in fb_series:

        print(fb)
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
main()