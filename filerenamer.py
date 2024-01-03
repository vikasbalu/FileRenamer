import os

def main():
    i = 0
    path = "test/"
    for filename in os.listdir(path):
        my_dest = "file" + str(i) +".txt"
        my_source =path + filename
        print(my_source)
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()


