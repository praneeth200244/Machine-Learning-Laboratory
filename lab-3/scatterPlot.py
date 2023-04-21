import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go 
from bokeh.plotting import figure,show 
from bokeh.models import ColumnDataSource

# Create some sample data
np.random.seed(1)
n=100
data = np.random.randn(n,4) 

# Create a scatter plot using matplotlib
plt.scatter(data[:,0],data[:,1])
plt.show()

# Create a box plot using seaborn
sns.boxplot(data=data)
plt.show()

#Create a heat map using seaborn
sns.heatmap(data)
plt.show()

# Create a contour plot using matplotlib
x=np.linspace(-3,3,100)
y=np.linspace(-3,3,100)
X,Y=np.meshgrid(x,y)
Z=np.exp(-(X**2+Y**2))
plt.contour(X,Y,Z)
plt.show()

# Create a 3D surface plot using plotly
fig = go.Figure(data=[go.Surface(z=Z)])
fig.show()

# Create a interactive scatter poot using bokeh
source=ColumnDataSource(data=dict(x=data[:,0],y=data[:,1]))
p=figure(tools="pan,wheel_zoom,box_zoom,reset,save",title="Scatter Plot")
p.scatter('x','y',source=source)
show(p)