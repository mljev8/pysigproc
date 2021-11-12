import numpy as np

class Polynomial_Regression_Sweeper():

    # constructor
    def __init__(self, poly_orders=[0,1,2], N=512, n=49, step_size=1):

    # public
    def fit(self, y: np.ndarray):
    def plot_fit(self, y: np.ndarray):
    
    # protected methods (override upon inheritance)
    def _pretransform(self, y: np.ndarray): # z = f(y)
    def _map_model_parameters(self): # map beta coefs back to original domain 
    def _apply_constraints(self):
    def _eval_model(self):
    def _post_diagnosis(self):
    
    # private
    def __assert(self):
    def __setup_internals(self):