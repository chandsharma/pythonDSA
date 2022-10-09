import sys
sys.path.append(__file__.split('/Exercise')[0])  #added path of parent directory

from hashMaps_collisionHandling import HashMap

def load_data_as_dict(container):
    with open("nyc_weather.csv",'r') as file:
        csv_contents = file.readlines[1:]
        for content in csv_contents:
            container[content.split(',')[0]] = content.split(',')[1]

if __name__ == '__main__':
    f = open("nyc_weather.csv",'r')
    hm = HashMap()
    load_data_as_dict(hm)
    print(hm.arr)

