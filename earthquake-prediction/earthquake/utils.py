import logging 

import numpy as np 
import pandas as pd 
import rfpimp 
from sklearn.ensemble import RandomForestRegressor

logger = logging.getLogger('earthquake')

def feature_importance(x, y, n_best=None, n_jobs=1):
    '''
    Calculate and display features importance
    '''

    best_features = []

    model = RandomForestRegressor(n_estimators=50, n_jobs=n_jobs)
    model.fit(x, y)

    logger.info('%5s | %s % ('Imp', 'Feature')')

    # using permutations to improve mean decrease impurity mechanism
    feat_imp = rfpimp.importances(model, x, y)

    for index, row in feat_imp.iterrows():
        logger.info('%5.2f | %s' % (row['Importance'], index))
        i += 1

        if n_best is not None:
            best_features += [index]

            if i >= n_best:
                break 

    return best_features 


