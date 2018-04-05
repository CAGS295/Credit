import pandas as pd
import numpy as np

from copy import deepcopy

# A tree is defined with this strucure:
# {'left': None, 'right': None, 'df': df, 'rss': 0}

def _residual_squared_sum(df, y):
    """
    Calculate the residual squared sum in R, defined
    by mask, using the target y.
    """
    yR = df[y].mean()
    RSS = (df[y] - yR)**2
    return RSS.sum(), yR

def _binary_splitting(df, y, x_j):
    """
    Find the best split using the predictor x_j. 
    """
    ss = df[x_j].unique()
    ss = sorted(ss)
    minimum = {'rss': float('inf')}
    for i in range(len(ss) - 1):
        s = (ss[i] + ss[i+1]) / 2
        df1 = df[df[x_j] < s]
        df2 = df[df[x_j] >= s]
        rss1, yR1 = _residual_squared_sum(df1, y)
        rss2, yR2 = _residual_squared_sum(df2, y)
        rss = rss1 + rss2
        if rss < minimum['rss']:
            minimum = {
                    'rss': rss,
                    's': s,
                    'left': {'df': df1, 'rss': rss1, 'yhat': yR1},
                    'right': {'df': df2, 'rss': rss2, 'yhat': yR2}
                    }
    return minimum

def _recursive_binary_splitting(df, y, predictors):
    """
    Select the best variable to reduce the
    residual square sum from predictors.
    """
    minimum = {'rss': float('inf')}
    for predictor in predictors:
        split = _binary_splitting(df, y, predictor)
        if split['rss'] < minimum['rss']:
            minimum = split
            minimum['x_j'] = predictor

    return minimum

def _grow_tree(tree, predictors, min_points_per_leaf=5):
    """
    Recursively divide tree using the split that
    minimize rss. It stops when the region have
    less than 5 elements.
    """
    df = tree['df']
    best_split = _recursive_binary_splitting(df, tree['y'], predictors)
    if best_split['rss'] >= tree['rss']:
        return

    left_tree = {'left': None, 'right': None,
                 'rss': best_split['left']['rss'],
                 'df': best_split['left']['df'],
                 'yhat': best_split['left']['yhat'],
                 'y': tree['y']
                }
    right_tree = {'left': None, 'right': None,
                  'rss': best_split['right']['rss'],
                  'df': best_split['right']['df'],
                  'yhat': best_split['right']['yhat'],
                  'y': tree['y']
                 }

    tree['left'] = left_tree
    tree['right'] = right_tree
    tree['x_j'] = best_split['x_j']
    tree['s'] = best_split['s']

    if len(left_tree['df']) > min_points_per_leaf:
        _grow_tree(left_tree, predictors)

    if len(right_tree['df']) > min_points_per_leaf:
        _grow_tree(right_tree, predictors)

def _make_tree(df, y):
    rss, yhat = _residual_squared_sum(df, y)
    return {'left': None, 'right':None, 
            'rss': rss,
            'yhat': yhat,
            'df': df,
            'y': y}

def _is_leaf(tree):
    return tree['left'] == None and tree['right'] == None

def _tree_rss(tree):
    if _is_leaf(tree):
        rss = tree['rss']
    else:
        rss = _tree_rss(tree['left']) + _tree_rss(tree['right'])
    return rss

def _is_last_branch(tree):
    return _is_leaf(tree['left']) and _is_leaf(tree['right'])

def _find_min_deltarss(tree):
    if _is_last_branch(tree):
        deltarss = tree['rss'] - (tree['left']['rss'] + tree['right']['rss'])
        return deltarss, tree
    else:
        if _is_leaf(tree['left']):
            return _find_min_deltarss(tree['right'])
        if _is_leaf(tree['right']):
            return _find_min_deltarss(tree['left'])
        min_deltarss, min_tree = _find_min_deltarss(tree['left'])
        right_deltarss, right_tree = _find_min_deltarss(tree['right'])
        if right_deltarss < min_deltarss:
            min_deltarss = right_deltarss
            min_tree = right_tree

        return min_deltarss, min_tree

def _count_leafs(tree):
    leafs = 0
    if _is_leaf(tree['left']):
        leafs += 1
    else:
        leafs += _count_leafs(tree['left'])
    if _is_leaf(tree['right']):
        leafs += 1
    else:
        leafs += _count_leafs(tree['right'])
    return leafs

def _prune_tree(tree, alpha):
    min_cost_complexity = _tree_rss(tree) + alpha * _count_leafs(tree)
    min_cc_tree = deepcopy(tree)

    while not _is_last_branch(tree):
        min_deltarss, min_tree = _find_min_deltarss(tree)
        min_tree['left'] = None
        min_tree['right'] = None

        cost_complexity = _tree_rss(tree) + alpha * _count_leafs(tree)

        if cost_complexity < min_cost_complexity:
            min_cost_complexity = cost_complexity
            min_cc_tree = deepcopy(tree)

    return min_cc_tree

def _evaluate(tree, event):
    if _is_leaf(tree):
        return tree['yhat']
    else:
        if event[tree['x_j']] < tree['s']:
            return _evaluate(tree['left'], event)
        else:
            return _evaluate(tree['right'], event)

class regression_tree:
    def __init__(self):
        self._tree = None

    def fit(self, df, y, predictors=None, alpha=1, min_points_per_leaf=5):
        if not predictors:
            predictors = set(df.columns) - set((y,))
        self._tree = _make_tree(df, y)
        _grow_tree(self._tree, predictors, min_points_per_leaf)
        self._tree = _prune_tree(self._tree, alpha)

    def predict(self, df):
        if self._tree:
            evaluate = lambda event: _evaluate(self._tree, event)
            return df.apply(evaluate, axis=1)
        else:
            print('Should train first. try fit() method')
            return

if __name__ == '__main__':
    df = pd.read_csv('../data/hitters.csv')
    df['LogSalary'] = np.log(df['Salary'])
    rt = regression_tree()
    rt.fit(df, 'LogSalary', predictors=['Years', 'Hits'])
    print(rt.predict(df))
