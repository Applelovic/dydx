import numpy as np
import pandas as pd


def indi_w(
        vol,
        fee_rate,
        open_int,
        a,
):
    return (fee_rate * vol) ** a * open_int ** (1 - a)


class T1(object):

    def __init__(
            self,
            a,
            total_reward=150000,
            fee_rate=0.001,
    ):
        self.a = a
        self.fee_rate = fee_rate
        self.ttl_reward = total_reward
        self._vol = 0
        self._open_int = 0

    def set_vol(self, vol):
        self._vol = vol

    def set_open_int(self, open_int):
        self._open_int = open_int

    def get_vol(self):
        return self._vol

    def get_open_int(self):
        return self._open_int

    @staticmethod
    def indi_w_cal(
            vol,
            fee_rate,
            open_int,
            a,
    ):
        return (fee_rate * vol) ** a * open_int ** (1 - a)

    @property
    def indi_w(self):
        return indi_w(vol=self._vol, fee_rate=self.fee_rate, open_int=self._open_int, a=self.a)

    def indi_reward(self, other_w):
        return self.ttl_reward * self.indi_w / (other_w + self.indi_w)






if __name__ == '__main__':

    print('Done.')