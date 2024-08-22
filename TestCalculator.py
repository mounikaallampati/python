from Calulator import  square
def main():
    test_Square()
"""
def test_Square():
    if  square(3)!=9:
        print("3 Square is not 9")
    if  square(6)!=36:
        print("6 Square is not 36")
        """
def test_Square():
    assert square(3)==9
    assert square(6)==36

if __name__=="__main__":
    main()


