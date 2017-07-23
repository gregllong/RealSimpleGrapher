'''
Configuration settings for Grapher gui
'''
import pyqtgraph as pg
pg.setConfigOption('background', 'k')
pg.setConfigOption('foreground', 'y')

class traceListConfig():
    def __init__(self, background_color = 'white'):
        self.background_color = background_color

class graphConfig():
    def __init__(self, name, ylim=[0,1], isScrolling=False, max_datasets = 20,
                 show_points = True, grid_on = False, scatter_plot=False,
                 plot_only_new_data=False):
        self.name = name
        self.ylim = ylim
        self.isScrolling = isScrolling
        self.isImages = False
        self.max_datasets = max_datasets
        self.graphs = 1 # just a single graph
        self.plot_only_new_data = plot_only_new_data
        self.show_points = show_points
        self.grid_on = grid_on
        self.scatter_plot = scatter_plot

class gridGraphConfig():
    def __init__(self, tab, config_list):
        self.tab = tab
        self.config_list = config_list[0::3]
        self.row_list = config_list[1::3]
        self.column_list = config_list[2::3]

        self.graphs = len(self.config_list)


tabs =[
    gridGraphConfig('current', [graphConfig('current', max_datasets = 1), 0, 0]),
    gridGraphConfig("MOT_and_ML_pulses", [
        graphConfig('total_counts', isScrolling=True, max_datasets = 1, show_points = False), 0, 0]),
    gridGraphConfig("MOT_and_ML_pulses", [
        graphConfig('tagged_photons', isScrolling=False, max_datasets = 1, show_points = False, plot_only_new_data=True), 0, 0]),
    gridGraphConfig('PowerCalibration', [graphConfig('PowerCalibration', ylim=[0,.1], isScrolling=True, max_datasets = 5, show_points = False), 0, 0]),
    gridGraphConfig(
        'RabiFlopScan', [graphConfig('RabiFlopScan', isScrolling=True,
                                     max_datasets=10, scatter_plot=True,
                                     show_points=True, ylim=[0, .1]), 0, 0])
]

#    gridGraphConfig('testgrid',
#        [
#            graphConfig('fig1'), 0, 0,
#            graphConfig('fig2'), 0, 1,
#            graphConfig('fig3'), 2, 2,
#            graphConfig('fig4'), 1, 2
#        ]),
#    gridGraphConfig('testgrid2',
#        [
#            graphConfig('fig1123'), 0, 0,
#        ])
