import os
import re

import xlrd, xlwt

import matlab
import matlab.engine

class AISSig():
    def createAISSig(self):
        path = "../devops/AISSig"
        signum = 10;
        conflictNum = 2;
        totalratio = 1;
        channelnum = 1;
        os.chdir('../ais_testmodule/')
        eng = matlab.engine.start_matlab()
        for powdiff in range(0, 15):
            for EbN0 in range(13, 17):
                try:
                    #sig.create(float(powdiff), float(signum), float(conflictNum), float(totalratio), float(channelnum), float(EbN0), path)
                    eng.test(float(powdiff), float(signum), float(conflictNum), float(totalratio), float(channelnum), float(EbN0), path)
                except Exception as exp:
                    print "powdiff: %s  EbN0: %s" %(powdiff, EbN0)
                    print exp
                #eng.test(powdiff, signum, conflictNum, totalratio, channelNum, EbN0, path)
        eng.quit()
        os.chdir('../devops/')
sig = AISSig()

class Demo():
    def antDemo(self):
        file_list = os.listdir('./AISSig')
        current = os.getcwd()
        aissig = os.path.join(current, './AISSig')
        os.chdir('../singleantv2.0.1/')
        eng = matlab.engine.start_matlab()
        for file_name in file_list:
            if file_name == '.' or file_name == '..' or file_name == '.DS_Store':
                continue
            sigpath = os.path.join(aissig, file_name)
            eng.Main(sigpath)
        eng.quit()
        os.chdir('../devops/')
demo = Demo()

def getdataparam(filename):
    pattern = re.compile(r'^AIS(Data)_h\d+_t\d+_v\d+_e(\d+)_p(\d+)')
    match = pattern.match(filename)
    print filename
    if match:
        return match.groups()
    return None

class Analysis():
    def check(self):
        res = {}
        file_list = os.listdir('./AISSig')
        current = os.getcwd()
        aissig = os.path.join(current, './AISSig')
        os.chdir('../checkprob/conflictcheck')
        eng = matlab.engine.start_matlab()
        for file_name in file_list:
            if file_name == '.' or file_name == '..' or file_name == '.DS_Store':
                continue
            sigpath = os.path.join(aissig, file_name) + '/'
            resultpath = os.path.join(sigpath, 'demodResult_1ant/')
            filename = os.listdir(sigpath)
            for k in filename:
                data = getdataparam(k)
                if not data or not data[0]:
                    continue
                dataname = os.path.join(sigpath, k)
                prob = eng.detectProbability(resultpath, k, sigpath)
                if not res.has_key(int(data[1])):
                    res[int(data[1])] = {}
                if not res[int(data[1])].has_key(int(data[2])):
                    res[int(data[1])][int(data[2])] = prob
        eng.quit()
        os.chdir('../../devops/')
        print res
        return res
anay = Analysis()

def genXlsFormat(result):
    """
    TODO: from txt gen xls
    """
    ft = open('./result.txt', 'w+')
    #for eb, value in result.iteritems():
    #    for po, pr in value.iteritems():
    items = result.items()
    items.sort()
    for eb, v in items:
        it = v.items()
        it.sort()
        for po, pr in it:
            context = str(eb) + " " + str(po) + " " + str(pr) + '\n'
            ft.write(context)
            print eb, po, pr
            

if __name__ == '__main__':
    #sig.createAISSig()
    #demo.antDemo()
    res = anay.check()
    genXlsFormat(res)
