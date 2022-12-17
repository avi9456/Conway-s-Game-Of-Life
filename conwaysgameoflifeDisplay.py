import ConwaysGameOfLife as game
import matplotlib.pyplot as plt
import numpy as np

def init_select(size):
    count=game.init_count(size)
    color = np.array(["white", "black"])
    x=np.array([[j for j in range(size)] for i in range(size)])
    y=np.array([[i for j in range(size)] for i in range(size)])
    return x,y,count,color
def init(size):
    z=game.create_matrix(size)
    count=game.init_count(size)
    color = np.array(["white", "black"])
    x=np.array([[j for j in range(size)] for i in range(size)])
    y=np.array([[i for j in range(size)] for i in range(size)])
    return z,x,y,count,color

def colors(dead,alive):
    return np.array([dead, alive])

def setDisplay(size):
    fig=plt.figure()
    fig.set_figheight(size)
    fig.set_figwidth(size)
    return fig

def show(repet,z,x,y,size,count,color,fig):
    for k in range(repet):
        z=game.update_matrix(z,game.count_alive(z,count))
        plt.axis("off")
        for i in range(size):
            for j in range(size):
                plt.scatter(x[i][j],-y[i][j],s=500,c=color[z[i][j]])
        if (z==0).all():
            print("all dead")
            plt.close()
            return
        plt.show(block=False)
        plt.pause(1)
        fig.clear(True)