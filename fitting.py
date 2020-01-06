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
    df_tracks= pd.read_csv('./data.csv', header=0)
    track_info = df_tracks.values.tolist()
    track_durations = sorted([item[3] for item in track_info])
    return track_durations
    
  def get_mean_and_stdev(self, data, width=40, range=[0, 600]):
    hist_1, bins = np.histogram(data, width, range=(range[0],range[1]))
    bins = bins[:-1]
    param = norm.fit(data)
    self.X = bins
    self.Y = hist_1
    self.mean = param[0]
    self.stdev = param[1]

  def _gaussian_func(self, x, a, mu, sigma):
      return a*np.exp(-(x-mu)**2/(2*sigma**2))

  def curve_fitting(self):
    param_ini = [80,self.mean, self.stdev]
    popt, _ = curve_fit(self._gaussian_func, self.X, self.Y, p0=param_ini)
    fitting = self._gaussian_func(self.X, popt[0],popt[1],popt[2])
    self.fitting = fitting

  def residuals(self):
    residuals =  self.Y - self.fitting
    rss = np.sum(residuals**2)#residual sum of squares = rss
    tss = np.sum((self.Y-np.mean(self.Y))**2)#total sum of squares = tss
    self.r_squared = 1 - (rss / tss)

  def plot(self):
    plt.rcParams['font.size'] = 14
    _, ax = plt.subplots()
    ax.bar(self.X,self.Y,width=100/100,alpha=0.5,color='m',align='edge')
    ax.plot(self.X,self.fitting,'k')
    ax.annotate("$R^2$="+str(np.round(self.r_squared,3)), xy=(0.6, 0.6), xycoords='axes fraction')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.savefig('graph.png')

if __name__ == "__main__":
    gf = Gaussian_Fitting()
    gf.read_csv()
    data = gf.read_csv()
    gf.get_mean_and_stdev(data)
    gf.curve_fitting()
    gf.residuals()
    gf.plot()

