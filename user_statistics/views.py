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
    scatter = graphs.Scatter(y=albums, x=no_of_reviews,
                             name='Reviews Per Genre',
                             mode='markers',
                             marker=dict(size=15, color='red'))
    figure.add_trace(scatter)
    figure.update_layout(yaxis_title="Album", xaxis_title="No. of Reviews",
                         paper_bgcolor='rgba(0, 0, 0, 0.85)',
                         font_color='whitesmoke', plot_bgcolor="rgba(0,0,0,1)")

    # Fade the grid lines to make the grid more distinguishable
    figure.update_xaxes(gridcolor='rgba(255, 255, 255, 0.3)')
    figure.update_yaxes(gridcolor='rgba(255, 255, 255, 0.3)')
    plot_html = plot(figure, output_type='div')

    # Get data and display a chart of reviews per user
    users, user_reviews = get_data_lists('reviews_per_user')
    figure1 = graphs.Figure()
    scatter1 = graphs.Scatter(y=users, x=user_reviews,
                              name='Reviews Per Genre',
                              marker=dict(size=20, color='gold'))
    figure1.add_trace(scatter1)
    figure1.update_layout(yaxis_title="Users", xaxis_title="No. of Reviews",
                          paper_bgcolor='rgba(0, 0, 0, 0.85)',
                          font_color='whitesmoke',
                          plot_bgcolor="rgba(0,0,0,1)")

    # Fade the grid lines to make the 2nd graph more distinguishable
    figure1.update_xaxes(gridcolor='rgba(255, 255, 255, 0.3)')
    figure1.update_yaxes(gridcolor='rgba(255, 255, 255, 0.3)')

    plot_html1 = plot(figure1, output_type='div')

    template = 'statistics.html'
    context = {
        'plot_html': plot_html,
        'plot_html1': plot_html1
    }
    return render(request, template, context)
