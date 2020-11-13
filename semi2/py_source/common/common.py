import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import send_file

def data_frame(df):
    return [df.to_html(classes='data', header="true")]

def seaborn(fig):
    canvas=FigureCanvas(fig)
    img = io.BytesIO()
    canvas.print_png(img)
    fig.savefig(img)
    img.seek(0)
    return send_file(img,mimetype='img/png')

def pyplot(plt):
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)
    return send_file(img, mimetype='img/png')
