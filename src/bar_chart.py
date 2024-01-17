'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio
from template import THEME
from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN
from hover_template import get_hover_template

def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    
    fig = go.Figure()
    
    
    
   
    fig.update_layout(template="simple_white")

    custom_template = pio.templates['custom']
    fig.update_layout(
        title={
            'text': 'Lines per Act',
            'xanchor': 'left',
            'yanchor': 'top'
        },
        font=custom_template.layout.font,  # Appliquez la police personnalisée
        paper_bgcolor=custom_template.layout.paper_bgcolor,  # Appliquez la couleur de fond personnalisée
        plot_bgcolor=custom_template.layout.plot_bgcolor,  # Appliquez la couleur de fond du tracé personnalisée
        hoverlabel=custom_template.layout.hoverlabel,  # Appliquez les étiquettes au survol personnalisées
        colorway=custom_template.layout.colorway,  # Appliquez la palette de couleurs personnalisée
        dragmode=False,
        barmode='relative'
    )
    return fig
   



def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
   
    fig = go.Figure(fig)
     # TODO : Update the figure's data according to the selected mode
    
    column_name = "LineCount" if mode == "Count" else "PercentCount"
    
    fig = update_y_axis(fig,mode)
    
    fig.data =[]
    color_map = {player: THEME['bar_colors'][i % len(THEME['bar_colors'])] for i, player in enumerate(data['Player'].unique())}
    
    # Create a bar for each player using the color map
    for player in data['Player'].unique():
        player_data = data[data['Player'] == player]
        fig.add_trace(go.Bar(
            x=player_data['Act'],
            y=player_data[column_name], 
            name=player,
            marker=dict(color=color_map[player])  ,
            hovertemplate= get_hover_template(player,mode)
        ))
     
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    fig = go.Figure(fig)
   
    y_axis_label = "Lines (Count)" if mode == "Count" else "Lines (%)"

    fig.update_layout(yaxis_title=y_axis_label)

    return fig