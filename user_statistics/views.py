from django.shortcuts import render
from .utils import get_data_lists
from plotly.offline import plot
import plotly.graph_objs as graphs


def statistics(request):
    """ View to show visualizations of all the data on the website """

    # Get data and implement a chart to displays
    # the number of reviews per album
    albums, no_of_reviews = get_data_lists('reviews_per_album')
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=albums, y=no_of_reviews,
                             name='Reviews Per Genre',
                             marker=dict(size=20, color='red'))
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Album", yaxis_title="No. of Reviews",
                         paper_bgcolor='rgba(0, 0, 0, 0.85)',
                         font_color='whitesmoke', plot_bgcolor="rgba(0,0,0,1)")
    plot_html = plot(figure, output_type='div')

    # Get data and display a chart of reviews per user
    users, user_reviews = get_data_lists('reviews_per_user')
    figure1 = graphs.Figure()
    scatter1 = graphs.Scatter(x=users, y=user_reviews,
                              name='Reviews Per Genre',
                              marker=dict(size=20, color='gold'))
    figure1.add_trace(scatter1)
    figure1.update_layout(xaxis_title="Users", yaxis_title="No. of Reviews",
                          paper_bgcolor='rgba(0, 0, 0, 0.85)',
                          font_color='whitesmoke',
                          plot_bgcolor="rgba(0,0,0,1)")
    plot_html1 = plot(figure1, output_type='div')

    template = 'statistics.html'
    context = {
        'plot_html': plot_html,
        'plot_html1': plot_html1
    }
    return render(request, template, context)
