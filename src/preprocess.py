'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN
import numpy as np

def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    
    counts = my_df.groupby(['Act','Player']).size().reset_index(name='LineCount')
    
    tot_lines = counts.groupby(['Act']).sum().reset_index()
    tot_lines = tot_lines.rename(columns={'LineCount': 'TotalLines'})
    new_df = pd.merge(counts, tot_lines, on=['Act'])

    new_df['PlayerPercent'] = (new_df['LineCount'] / new_df['TotalLines']) * 100
    
    return new_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    
    top_players = my_df.groupby('Player')['LineCount'].sum().nlargest(5).index
    
    # Other
    other_players = my_df[~my_df['Player'].isin(top_players)]
    others_grouped = other_players.groupby('Act').agg({'LineCount': 'sum', 'PlayerPercent': 'sum'}).reset_index()
    others_grouped['Player'] = 'OTHER'

    # Join
    top_players_df = my_df[my_df['Player'].isin(top_players)]
    new_df = pd.concat([top_players_df, others_grouped], ignore_index=True)
    new_df = new_df.drop(columns=["TotalLines"])
    
    # Sort
    new_df.sort_values(by=['Act', 'Player'], ascending=[True, True], inplace=True)
    new_df.reset_index(drop=True, inplace=True)
    
    return new_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    players = my_df["Player"]
    players = players.apply(name_changed)
    my_df["Player"] = players
    
    return my_df

def name_changed(name):
    
    name = name.lower()
   
    name = name[0].upper() + name[1:]

    return name
