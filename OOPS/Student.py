class Student:
    def __init__(self,name,house,petronus):
        if not name:
            raise ValueError('Name cannot be empty')
        if not house:
            raise ValueError('House cannot be empty')
        if not petronus:\
            raise ValueError('Petronus cannot be empty')
        self.name = name
        self.house = house
        self.petronus = petronus
    def __str__(self):
        return f'{self.name} from {self.house}'
    def charm(self):
        if self.petronus=='stag':
            return "horse"
        elif self.petronus=='otter':
            return "bear"
        elif self.petronus=='jack russel':
            return "dog"
        else:
            return '/'
def get_Student():
    name=input('Enter your name:')
    house=input('Enter your house:')
    petronus=input('Enter your petronus:')
    return Student(name,house,petronus)

def main():
    st=get_Student()
    st.house="no 4"
    print(st)
    print(st.charm())

if __name__ == '__main__':
    main()
