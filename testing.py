import dictionaries.weapon_skills as ws

# 
def test2():
    '''Name strip test'''
    mystring = 'ferocious Bear'
    if not mystring.startswith('Dead'):
        if len(mystring.split(' ')) < 2:
            mystring = 'Dead %s' % mystring
        else:
            no_variation = mystring.split(' ', 1)
            print(no_variation)
            mystring = no_variation[1]
            print(mystring)
            mystring = '{} {}'.format('Dead', mystring)    
    print(mystring)

def main():
    pass

if __name__ == '__main__':
    main()
