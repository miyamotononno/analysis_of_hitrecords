import csv
import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Gaussian_Fitting:
  def __init__(self):
    self.X = []
    self.Y = []
    self.mean = 0
    self.stdev = 0
    self.fitting = None
    self.r_squared = 0

  def read_csv(self):
    """csvの読み込み"""

    df_tracks= pd.read_csv('./data.csv', header=0)
    track_info = df_tracks.values.tolist()
    track_durations = sorted([item[3] for item in track_info])
    return track_durations
    
  def set_mean_and_stdev(self, data, width=60, range=[0, 600]):
    """dataの平均と標準偏差をセットする"""

    hist_1, bins = np.histogram(data, width, range=(range[0],range[1]))
    bins = bins[:-1]
    param = norm.fit(data)
    self.X = bins
    self.Y = hist_1
    self.mean = param[0]
    self.stdev = param[1]

  def _gaussian_func(self, x, a, mu, sigma):
    """ガウス関数"""
    return a*np.exp(-(x-mu)**2/(2*sigma**2))

  def curve_fitting(self):
    """データ分布を関数でフィッティングする"""

    param_ini = [80,self.mean, self.stdev]
    popt, _ = curve_fit(self._gaussian_func, self.X, self.Y, p0=param_ini)
    fitting = self._gaussian_func(self.X, popt[0],popt[1],popt[2])
    self.fitting = fitting

  def set_residuals(self):
    """残差のセット"""

    residuals =  self.Y - self.fitting
    rss = np.sum(residuals**2)#residual sum of squares = rss
    tss = np.sum((self.Y-np.mean(self.Y))**2)#total sum of squares = tss
    self.r_squared = 1 - (rss / tss)

  def plot(self, file_name='graph.png'):
    """fileにプロットする"""

    plt.rcParams['font.size'] = 14
    _, ax = plt.subplots()
    ax.bar(self.X,self.Y,width=3,align='edge')
    ax.plot(self.X,self.fitting,'k')
    ax.annotate("μ="+str(np.round(self.mean,3)), xy=(0.6, 0.8), xycoords='axes fraction')
    ax.annotate("σ="+str(np.round(self.stdev,3)), xy=(0.6, 0.7), xycoords='axes fraction')
    ax.annotate("$R^2$="+str(np.round(self.r_squared,3)), xy=(0.6, 0.6), xycoords='axes fraction')
    ax.set_xlabel('time duration(s)')
    ax.set_ylabel('count')
    ax.set_xticks(np.arange(0, 540 + 1, 60))
    plt.savefig(file_name)

if __name__ == "__main__":
    gf = Gaussian_Fitting()
    data = gf.read_csv()
    gf.set_mean_and_stdev(data)
    gf.curve_fitting()
    gf.set_residuals()
    gf.plot('graph.png')

