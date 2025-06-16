import streamlit as st
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from mplsoccer import VerticalPitch

st.title("Individual Player Statistics in the Champions League Season 2025")


df = pd.read_excel("UCL_playerstats_orig.xlsx")


competitions = df['Competitions'].dropna().unique()
competition_selected = st.selectbox("Choose Competition", sorted(competitions), index=None)


if competition_selected:
    teams_in_comp = df[df['Competitions'] == competition_selected]['Team'].dropna().unique()
    team_selected = st.selectbox("Choose the Team", sorted(teams_in_comp), index=None)


    if team_selected:
        players_in_team = df[
            (df['Competitions'] == competition_selected) &
            (df['Team'] == team_selected)
        ]['Player'].dropna().unique()
        player_selected = st.selectbox("Select Player", sorted(players_in_team), index=None)


        if player_selected:
            player_stats = df[
                (df['Competitions'] == competition_selected) &
                (df['Team'] == team_selected) &
                (df['Player'] == player_selected)
            ].iloc[0]

            st.subheader(f"Player: {player_selected}")
            st.markdown(f"**Age:** {player_stats['Age']}")
            st.markdown(f"**Position:** {player_stats['Position']}")
            st.markdown(f"**Team:** {player_stats['Team']}  |  **Competition:** {player_stats['Competitions']}")


            stat_columns = [
                'Goals', 'Assists', 'Rating', 'DistanceCovered(km)',
                'Value10^6',
                'Total_attempts', 'Chances_Created', 'Dribbles', 'Match_played','Minutes_played',
                'Tackles_Won', 'Tackles_Lost', 'Saves', 'Goals_Conceded',
                'Clean_Sheets', 'MOTM_Awards', 'Balls_recovered',
            ]

            selected_stats = st.multiselect(
                "Choose which statistics you want to display:",
                stat_columns,
                default=[]
            )

            if selected_stats:
                st.markdown("## Selected statistics")
                for stat in selected_stats:
                    st.write(f"**{stat}:** {player_stats[stat]}")
            else:
                st.info("Select at least one statistic to see the value.")


            with st.expander("Show all statistics"):
                st.dataframe(player_stats.to_frame(name="Vlera").rename_axis("Statistika"))