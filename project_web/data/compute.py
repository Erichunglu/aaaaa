from numpy import exp, cos, linspace
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time, glob
import pandas as pd
import matplotlib.dates as md
import urllib
from pandas import Series
from matplotlib.widgets import Cursor

globmax = 0
globmin = 0
globmean = 0

def getline(s,s2,f,f2):
    start_time = s+' '+s2
    finish_time = f+' '+f2
    print start_time
    print finish_time
    return collect(start_time,finish_time)

def collect(time1, time2):
	global globmax
	global globmin
	global globmean
	start = int(time.mktime(time.strptime(time1, '%Y-%m-%d %H:%M:%S')))
	start = str(start)
	end = int(time.mktime(time.strptime(time2, '%Y-%m-%d %H:%M:%S')))
	end = str(end)
	url = "http://172.17.18.152:8080/render?from="+start+"&now="+end+"&target=QwQ.node1.monster.memory.*.used&rawData=%22true%22"
	testfile = urllib.URLopener()
	testfile.retrieve(url,"mydata_test.csv")
	df = pd.read_csv('mydata_test.csv',header=None)
	df = df.T
	df= df.convert_objects(convert_numeric=True)
	StartTime=df.iloc[1]
	EndTime=df.iloc[2]
	df = df.drop(df.index[[0,1,2,3]])
	df.rename(columns={0:'Value'}, inplace=True)
	row_num=len(df.index)
	timeintervall=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(StartTime))
	timestamp = pd.date_range(timeintervall, periods=row_num+4, freq='min')
	df['time'] = Series(timestamp)
	df.reindex(index=timestamp)
	plt.figure()  # needed to avoid adding curves in plot
	fig,ax= plt.subplots()
	plt.subplots_adjust(bottom=0.2)
	plt.xticks( rotation=75 )
	plt.ylabel("GB",fontsize=16)
#	plt.yticks(range(),fontsize=14)
	ax=plt.gca()
	y_mean = [df.Value.mean() for i in df.time]
	mean_line = ax.plot(df.time,y_mean, label='Mean', linestyle='--', color='red')
	xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
	ax.xaxis.set_major_formatter(xfmt)
	max_index=df.Value.idxmax()-4
	min_index=df.Value.idxmin()-4
	markers_on = [max_index,min_index]
	data_line = ax.plot(df.time,df.Value,'-bD',markevery=markers_on,label='Data')
	Cursor(plt.gca(), horizOn=True, color='r', lw=1)
	legend = ax.legend(loc=(1,0.85))
	globmax = df.Value.max()
        globmin = df.Value.min()
        globmean = df.Value.mean()
	plt.show()
	plt.grid(True)
	plt.title('Memory Usage',fontsize=18)
	if not os.path.isdir('static'):
        	os.mkdir('static')
    	else:
        	# Remove old plot files
        	for filename in glob.glob(os.path.join('static', '*.png')):
            	    os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    	plotfile = os.path.join('static', str(time.time()) + '.png')
    	plt.savefig(plotfile)
#	os.remove('mydata_test.csv')
   	return plotfile

def showdata():
    a = globmax/1000000000
    b = globmin/1000000000
    c = globmean/1000000000
    print(globmax)
    return  """show data  <table border=1>    <tr><td> max     </td><td>%.6f GB</td></tr>    <tr><td> min     </td><td>%.6f GB</td></tr>    <tr><td> mean     </td><td>%.6f GB</td></tr>  """%(a,b,c)



def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    print os.getcwd()
    t = linspace(0, T, resolution+1)
    y = damped_vibrations(t, A, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, y)
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile

if __name__ == '__main__':
    print collect(0, 0, 0, 0)
