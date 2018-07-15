import yaml
import logging
import re
import numpy as np
from DefiningAlgo import definingAlgo



if __name__=='__main__':
    
    with open('config.yml','rt') as f:
        config=yaml.safe_load(f)
        
    logging.basicConfig(format='%(asctime)s %(message)s',level='INFO')
    logger=logging.getLogger('Startup')
    print(config['Startup']['filename'])    
    obj= definingAlgo(config['Startup']['filename'],logger)
    obj.dataexploration()



