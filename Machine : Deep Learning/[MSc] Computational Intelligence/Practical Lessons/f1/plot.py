# ----------------------------------------------------------------------------------
# API CLASS USED TO DRAW ONE OR MORE PLOTS IN THE SAME FIGURE (ON TOP OF EACH OTHER)
# ----------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import warnings
import time

warnings.filterwarnings("ignore")

class Plot:

    def __init__(self,axis,title,x_label,y_label): # class constructor
        
        '''
        SHOULD BE CALLED LIKE THIS:
        variable_name = Plot([
        [ [0], [0], "r-", "line_1" ], # an example plot (i.e. x_axis, y_axis, line_color, line_label)
        ...
        ], "title", "x_axis_label", "y_axis_label")
        '''
        
        plt.ion()
        self.axis = axis
        self.lines = []
        
        # plot configurations
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        # save the plot(s)
        for i in range(len(self.axis)):
            self.lines.append(self.ax.plot(self.axis[i][0],self.axis[i][1],self.axis[i][2],label=self.axis[i][3]))
        
        # set the axis limits
        self.ax.set_xlim([min(list(map(lambda x : min(x[0]),self.axis))),max(list(map(lambda x : max(x[0]),self.axis)))])
        self.ax.set_ylim([min(list(map(lambda x : min(x[1]),self.axis))),max(list(map(lambda x : max(x[1]),self.axis)))])
        
        self.ax.set_title(title)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.legend()

        # show the initial plot
        plt.grid()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def update_plot(self,new_values): # update the plot(s)

        '''
        SHOULD BE CALLED LIKE THIS:
        variable_name.update_plot([(plot1_new_x_value,plot1_new_y_val), ...])
        '''

        plt.ion()
        
        # add the new data to the axis
        for i in range(len(new_values)):
            self.axis[i][0].append(new_values[i][0])
            self.axis[i][1].append(new_values[i][1])

        # update the plot
        for i in range(len(self.axis)):
            self.lines[i][0].set_data(self.axis[i][0],self.axis[i][1])
        
        # set the axis limits
        self.ax.set_xlim([min(list(map(lambda x : min(x[0]),self.axis))),max(list(map(lambda x : max(x[0]),self.axis)))])
        self.ax.set_ylim([min(list(map(lambda x : min(x[1]),self.axis))),max(list(map(lambda x : max(x[1]),self.axis)))])

        # wait some time
        plt.pause(1)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def keep_plot(self): # keep the plot(s) on the screen
        
        '''
        SHOULD BE CALLED LIKE THIS:
        plot.keep_plot()
        '''

        plt.ioff()
        plt.show()

# -------
# EXAMPLE
# -------
'''
plot = Plot([
    [ [0], [0], "r-x", "line_1" ], # line number 1 (in red)
    [ [0], [0], "g-x", "line_2" ]  # line number 2 (in green)
    ],"TITLE", "X AXIS", "Y AXIS"
    )

for i in range(10):
    plot.update_plot([(i+1,i*2.4),(i+1,(i*2.4)+1)])

plot.keep_plot()'''