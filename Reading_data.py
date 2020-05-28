import numpy as np
import pandas as pd
import matplotlib.pylab as mplt
from scipy import integrate

data_conf=pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
data_d=pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
data_R=pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

def dat(data_conf):
    data_conf=data_conf[data_conf['Country/Region']=='China']                 
    data_conf=data_conf[data_conf['Province/State']=='Hubei'] ##Se filtra solo la provincia de Hubei
    H_conf=data_conf.values[0][4:] ##Se toman los casos confirmados 
    return H_conf
H_conf=dat(data_conf)
H_d=dat(data_d)
H_R=dat(data_R)

H_activos=H_conf-(H_d+H_R)
H_out=H_d+H_R
t=np.arange(len(H_activos))
mplt.plot(t,H_activos)
mplt.plot(t,H_out)
mplt.grid()
mplt.show()