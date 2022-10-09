import sys
sys.path.append(__file__.split('/Exercise')[0])  #added path of parent directory

from hashMaps_collisionHandling import HashMap

def load_data_as_dict(container):
    with open('/home/chand/Desktop/pythonDSA/HashMaps/Exercise/nyc_weather.csv','r') as file:
        csv_contents = file.readlines()[1:]
        for content in csv_contents:
            container[content.split(',')[0]] = int(content.split(',')[1])

def load_data_as_list():
    with open('/home/chand/Desktop/pythonDSA/HashMaps/Exercise/nyc_weather.csv','r') as file:
        csv_contents = file.readlines()[1:]
        data = []
        for content in csv_contents:
            data.append(int(content.split(',')[1]))
        return data

if __name__ == '__main__':
    hm = HashMap()
    load_data_as_dict(hm)
    # data = load_data_as_list()
    # print(data)
    # print(sum(data[:7])/len(data[:7]))
    # print(max(data[:10]))
    print(hm['Jan 9'])
    print(hm['Jan 4'])

