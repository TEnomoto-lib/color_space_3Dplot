import plotly.express as px
import pandas as pd

class plot3DColorSpace:
    red = []
    green = []
    blue = []
    name = []

    step = 4
    eye_x = -1
    eye_y = 2.25
    eye_z = 1.75

    arrayLength = 0

    def __init__(self, red, green, blue, name=[]):
        self.red = red
        self.green = green
        self.blue = blue
        self.name = name

        if((len(self.red)!=len(self.green)) or (len(self.green)!=len(self.blue))):
            raise Exception("All arrays must be of the same length.")
        
        self.arrayLength = len(self.red)

    def plot(self,fileName=""):
        mark_color = []

        for i in range(self.arrayLength):
            mark_color.append("#"+format(self.red[i],'02x')+format(self.green[i],'02x')+format(self.blue[i],'02x'))

        color_data = None
        fig = None

        if(len(self.name)==0):
            color_data = pd.DataFrame({
                'Red':self.red,
                'Green':self.green,
                'Blue':self.blue,
                'mark_color':mark_color})

            fig = px.scatter_3d(
                color_data, 
                x="Red", 
                y="Green", 
                z="Blue", 
                color="mark_color",
                color_discrete_map="identity")
        else:
            color_data = pd.DataFrame({
                'Red':self.red,
                'Green':self.green,
                'Blue':self.blue,
                'name':self.name,
                'mark_color':mark_color})

            fig = px.scatter_3d(
                color_data, 
                x="Red", 
                y="Green", 
                z="Blue", 
                color="mark_color",
                text="name",
                color_discrete_map="identity")
            
        fig.update_layout(title=dict(text="RGB Color Space",
            font=dict(size=26,color='grey')),
            scene=dict(
                camera=dict(
                    center=dict(x=0,y=0,z=0),
                    eye=dict(x=self.eye_x,y=self.eye_y,z=self.eye_z)),
                xaxis=dict(
                    title=dict(text="Red",font=dict(size=20,color='red')),
                    dtick=self.step),
                yaxis=dict(
                    title=dict(text="Green",font=dict(size=20,color='green')),
                    dtick=self.step),
                zaxis=dict(
                    title=dict(text="Blue",font=dict(size=20,color='blue')),
                    dtick=self.step)))

        fig.show()

        if(not fileName.isspace()):
            with open(fileName, 'w') as f:
                f.write(fig.to_html(include_plotlyjs='cdn',full_html=False))