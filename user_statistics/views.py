from django.shortcuts import render
from .utils import get_lists_of_albums_and_no_of_reviews
from plotly.offline import plot
import plotly.graph_objs as graphs


def statistics(request):

    albums, no_of_reviews = get_lists_of_albums_and_no_of_reviews()

    figure = graphs.Figure()
    scatter = graphs.Scatter(x=albums, y=no_of_reviews,
                             name='Reviews Per Genre',
                             marker=dict(size=20, color='red'))
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Album", yaxis_title="No. of Reviews")
    plot_html = plot(figure, output_type='div')

    template = 'statistics.html'
    context = {
        'plot_html': plot_html
    }
    return render(request, template, context)
