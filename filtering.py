import numpy as np

class AR_filter():

    def __init__(self, feedback_coefs=[2/9,1/9]):
        self.p = len(feedback_coefs)
        self.feedback_coefs = np.array(feedback_coefs)
        self.buffer = np.zeros(self.p)
        self.a0 = 1. - self.feedback_coefs.sum()
        assert self._stability_check(self.feedback_coefs), 'UNSTABLE FILTER'

    @staticmethod
    def _stability_check(coefs):
        return True

    def init(self, Y0):
        self.buffer[:] = Y0
        
    def filter(self, Yt):
        Y = self.a0 * Yt
        Y += self.feedback_coefs.dot(self.buffer)
        self.buffer[:] = np.roll(self.buffer[:], shift=1)
        self.buffer[0] = Yt
        return Y

    def predict(self, k=1):
        return 0.