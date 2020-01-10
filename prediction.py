import numpy as np
from scipy.stats import norm
from scipy.optimize import bisect
from scipy import integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Prediction:
  def __init__(self):
    self.mean = 224.03
    self.stdev = 52.126

  def _p_t_over_t_total(self, t_total): # p(t | t_total)
    """一様分布と仮定"""
    try:
      return 1 / t_total
    except ZeroDivisionError:
      print("ZeroDivisionError!!")

  def _p_t_total(self, t_total): # p(t_total)
    """正規分布の確率密度関数"""
    return norm.pdf(x=t_total, loc=self.mean, scale=self.stdev)
  
  def _p_t_integrand(self, t_total):
    """p(t)の被積分関数"""
    return self._p_t_over_t_total(t_total)*self._p_t_total(t_total)

  def _p_t(self, t): # p(t)
    ans, _ = integrate.quad(self._p_t_integrand, t, np.inf)
    return ans

  def generate_t_star(self, t, lower_limit): # p(t*)
    """p(t_total | t)の確率密度関数をtから∞まで積分する"""
    """p(t_total|t)=0.5となるt*を求める。解析的には解けないので数値的に解く"""

    def _p_t_total_over_t(t_total): # p(t_total | t)
      return self._p_t_over_t_total(t_total) * self._p_t_total(t_total) / self._p_t(t)
    
    t_star = lower_limit
    min_value = 1
    flag = True
    while(flag) :
      value, _ = integrate.quad(_p_t_total_over_t, t_star, np.inf) #t_totalで積分
      if min_value > np.abs(value-0.5):
        min_value = np.abs(value-0.5)
        t_star += 1
      else:
        flag = False

    print('t: %d | t*: %d' %(t, t_star))
    return t_star

  def _questionnaire(self):
    """アンケート結果を集計してまとめているだけ"""

    q0_list = [240, 210, 210, 165, 220, 253, 200, 210, 210, 150, 210, 230, 140, 180, 210, 280, 150, 270, 200, 150, 240, 210, 120, 120, 140, 290, 160, 150, 210]
    q1_list = [220, 198, 120, 180, 130, 120, 150]
    q2_list = [30, 90, 90, 180]
    q3_list = [140, 80, 30, 60, 30, 20, 30]
    q4_list = [30, 30, 30, 20]
    q5_list = [30, 120, 120, 60, 15]

    q0_mean = np.median(q0_list)
    q1_mean = np.median(q1_list) + 60*1
    q2_mean = np.median(q2_list) + 60*2
    q3_mean = np.median(q3_list) + 60*3
    q4_mean = np.median(q4_list) + 60*4
    q5_mean = np.median(q5_list) + 60*5

    X = [0, 60, 120, 180, 240, 300]
    Y = [q0_mean, q1_mean, q2_mean, q3_mean, q4_mean, q5_mean]
    return X, Y

  def plot(self, file_name='prediction.png'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    T = np.arange(5, 305, 5)
    T_stars = []
    # generate_t_star関数は単調増加であることを利用し、計算量を削減している。
    previous_t_star = 210 # t=5でt_star=211のため
    for t in T:
      t_star = self.generate_t_star(t, previous_t_star)
      previous_t_star = t_star
      T_stars.append(t_star)
    
    plt.plot(T, T_stars)

    q_x, q_y = self._questionnaire()
    ax.scatter(q_x, q_y)
    ax.set_xlabel('t values')
    ax.set_ylabel('predicted t_total')
    ax.set_xticks(np.arange(0, 300 + 1, 60))
    ax.set_yticks(np.arange(0, 420, 60))
    plt.ylim(0, 420)
    plt.savefig(file_name)


if __name__ == "__main__":
    p = Prediction()
    p.plot()
    