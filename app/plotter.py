import matplotlib.pyplot as plt
import base64
from io import BytesIO

class Plotter:

    def __init__(self, data):
        self.data = data

    def plot_html(self):
        self.fig = plt.figure()
        plt.plot(*self.data)
        encoded = self.encode()
        plot_html = self.format_html(encoded)
        return plot_html

    def encode(self):
        tmpfile = BytesIO()
        self.fig.savefig(tmpfile, format='png')
        return base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    @staticmethod
    def format_html(encoded):
        return '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

