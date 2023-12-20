import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')


from matplotlib import patches
from scipy.spatial import ConvexHull
import warnings; warnings.simplefilter('ignore')
sns.set_style("white")

import moviepy.editor as mpy # версия 1.0.3
import matplotlib.pyplot as plt #3.3.4

import glob
import os
import shutil

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")


df = pd.read_excel('фут.xlsx')

dir_name = 'pngs2'
max_sum  = 100
path_script = os.getcwd()

os.mkdir(os.path.join(path_script, dir_name))

gif_name = 'anim_var4.gif'

for i in range(0,len(df.index)):

    ax = df[['Забитые голы', 'Удары', 'Владение мячом, %']].iloc[:i+1].plot(figsize = (12,8), linewidth = 2, color= ['b','g','r'])
    ax.set_xlim(0, i+1)
    ax.set_ylim(0, max_sum)
    ax.legend(['Забитые голы', 'Удары', 'Владение мячом, %'], loc = 'upper left', frameon = False)
    # убираем ненужные оси
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # линии сетки по оси Х
    ax.grid(axis = 'x')
    # отрисовываем данные на холсте
    fig = ax.get_figure()
    # сохраняем холст в файл
    fig.savefig(os.path.join(path_script, dir_name) + f'/{i}.png')
# задаем частоту кадров в секунду
fps = 1
# создаем список файлов-кадров из ранее созданной папки
file_list = glob.glob(os.path.join(path_script, dir_name) + '/*')
# создаем анимацию из списка файлов
clip = mpy.ImageSequenceClip(file_list, fps = fps)
# сохраняем анимацию в формате GIF в папку со скриптом
clip.write_gif(path_script + '/{}'.format(gif_name), fps = fps)
# удаляем папку с файлами кадров
shutil.rmtree(os.path.join(path_script, dir_name))