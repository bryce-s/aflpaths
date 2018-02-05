import sys
import csv
import matplotlib.pyplot as plt


class csvParser(object):
    def addCSV(self, csvs):
        csvs.pop(0)
        self.csvFile = csvs
        self.len = len(self.csvFile)

    def __getTime(self, index):
        return self.csvFile[index][0]

    def __getPath(self, index):
        return self.csvFile[index][2]

    def returnTimePath(self):
        """returns time in list[0], path in list[2]"""
        timePath = [[], []]
        for time in self.csvFile:
            timePath[0].append(time[0])
        for path in self.csvFile:
            timePath[1].append(path[3])
        return timePath


def aflPaths():
    if len(sys.argv) != 2:
        print("usage: aflpaths plot_data")

    parser = csvParser()

    with open(sys.argv[1]) as inFile:
        csvs = csv.reader(inFile)
        csvList = list(csvs)
        parser.addCSV(csvList)

    timePath = parser.returnTimePath()
    plt.figure('time x paths')
    print(timePath[0])
    print(timePath[1])
    plt.scatter(timePath[0], timePath[1], label='time',
                color='k', marker='*', s=10)
    plt.xlabel('time')
    plt.ylabel('paths_total')
    plt.legend()
    plt.show()


aflPaths()
