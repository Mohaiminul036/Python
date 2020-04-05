from matplotlib import pyplot as plt
import numpy as np

def func1(x):
    return 0.6*x + 0.3

def func2(x):
    return 0.4*x*x + 0.1*x + 0.2

def find_curve_intersects(x,y1,y2):
    d = y1 - y2
    idx = np.where(d[:-1]*d[1:]<=0)[0]
    x1,x2 = x[idx],x[idx+1]
    d1,d2 = d[idx],d[idx+1]
    return -d1*(x2-x1)/(d2-d1)+ x1

x = np.linspace(-3,3,100)
f1 = func1(x)
f2 = func2(x)
fig,ax = plt.subplots(figsize=(10,5))
ax.plot(x,f1)
ax.plot(x,f2)

x1,x2 = find_curve_intersects(x,f1,f2)
ax.plot(x1,func1(x1),"o")
ax.plot(x2,func1(x2),"o")
ax.fill_between(x,f1,f2,where=f1>f2,facecolor="g",alpha=0.5)

from matplotlib import transforms
trans = transforms.blended_transform_factory(ax.transData,ax.transAxes)
ax.fill_between([x1,x2],0,1,transform=trans,alpha=0.1)

plt.rcParams["font.family"] = "SimHei"
a = ax.text(0.05,0.95,"直线与二次曲线的交点",transform=ax.transAxes,verticalalignment="top",fontsize=18)
arrow = {"arrowstyle":"fancy,tail_width=0.6","facecolor":"gray","connectionstyle":"arc3,rad=-0.3"}
ax.annotate("交点",xy=(x1,func1(x1)),xycoords="data",xytext=(0.05,0.5),textcoords="axes fraction",arrowprops = arrow)
ax.annotate("交点",xy=(x2,func1(x2)),xycoords="data",xytext=(0.05,0.5),textcoords="axes fraction",arrowprops = arrow)

plt.show()