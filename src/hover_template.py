'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''
    # TODO: Generate and return the over template
    
    # Data infos 
    if mode == 'Count':
        ligne_info = f"<br><br><i>%{{y}} lignes</i>"
    else :
        ligne_info = f"<br><br><i>%{{y:.2f}}% des lignes</i>"
    
    #Text + style
    hover_template = f'<span style="font-family: Grenze Gotish; font-size: 24px; color: black;">{name}{ligne_info}</span>'
    
    return hover_template  + "<extra></extra>" # To get rid of the default behavior
    
