import pandas as pd
import numpy as np
import re

class definingAlgo(object):
    def __init__(self,filename,logger):
        self.__data=filename
        self.__logger=logger
        print(self.__data)
        
        
    @property
    def getfileName(self):
        '''
        Read File
        '''
        self.__data = pd.read_csv(self.__data,encoding='Latin-1')
        return self.__data
    
    
    def dataexploration(self):
        self.__logger.info('Going through the data {}'.format(self.getfileName))
     
    def cleandata(self):
        self.__data=.map(self.space)
        self.__data=['company_name'].str.replace('[^w s+]','')
        
    def space(self,a):
        try:
            if re.match('\s+',a):
                return np.nan
        except:
               return a
        
       