import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit_lottie
from typing import Union, Optional, Literal
from streamlit_lottie import st_lottie
import json
# df_club = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\clubs.csv")
# df_competition = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\competitions.csv")
# df_game_event = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\game_events.csv")
# df_game = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\games.csv")
# df_player_valuation = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\player_valuations.csv")
# df_players = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\players.csv")
# df_appearances = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\appearances.csv")
# df_club_games = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\club_games.csv")
df_foot_n1 = pd.read_csv("D:\\correct_data1.csv")
df_foot_n3 = pd.read_csv("D:\\correct_data2.csv")
df_graph2 = pd.read_csv("D:\\df_graph2.csv")
df_graph1 = pd.read_csv("D:\\df_graph1.csv")
df_game1 = pd.read_csv("D:\\df11.csv")
df_pie = pd.read_csv("D:\\df_pie.csv")
df_new_p = pd.read_csv('D:\\folder\\df_new_p.csv')
df4 = pd.read_csv("D:\\folder\\df4.csv")
df1 = pd.read_csv('D:\\folder\\df1.csv')
dff = pd.read_csv("D:\\Games_chart.csv")
d_comp = pd.read_csv("D:\\df_c_new.csv")
# df_game2 = pd.read_csv("D:\\df22.csv")

import preprocess,helper
def load_lottiefile(filepath : str):
    with open(filepath,'r') as f:
        return json.load(f) 
# df = preprocess.preprocessor()
lottie_coding = load_lottiefile("D:\\animation_llfazi8j.json")
lottie_coding1 = load_lottiefile("D:\\football_team1.json")
lottie_coding2 = load_lottiefile("D:\\football_team2.json")
lottie_coding3 = load_lottiefile("D:\\football_team.json")
lottie_football4 = load_lottiefile("D:\\football.json")
lottie_finish5 = load_lottiefile("D:\\finish.json")
st.sidebar.title("Football Analysis")
with st.sidebar:
    st_lottie(lottie_football4,height=180,width=250)
user_menu = st.sidebar.radio(
    "Select an Option",
    ("Analysis for Clubs","Analysis for Players","Analysis for Games","Analysis for Competition")
)

hide_st_style = """
<style>
footer {visibility : hidden;}
</style>
"""

st.markdown(hide_st_style,unsafe_allow_html=True)
if user_menu == 'Analysis for Clubs':
    st.title("Football Clubs Analysis")
    c1,c2 = st.columns(2)
    with c1:
        st_lottie(lottie_coding,height = 180,width=400)
    with c2:
        st_lottie(lottie_coding1,height = 180,width=400)
    # c_n,h_n = preprocess.club()
    c_n = df_new_p['name'].unique().tolist()
    c_n.insert(0,"All Data")
    h_n =df4['hosting'].unique().tolist() 
    h_n.insert(0,"All Data")
    A_f = st.sidebar.selectbox('Search Club',c_n)
    H_f = st.sidebar.selectbox('Matches on',h_n)
    goal = helper.fetch_goals1(df_new_p,H_f,A_f)
    goal_tally = helper.fetch_goals2(df4,df1,H_f,A_f)
    # goal_tally = helper.goal_tally(df_club,df_club_games)
    if A_f == 'All Data' and H_f == 'All Data':
        st.header('Information for All Club')
    if A_f != 'All Data' and H_f == 'All Data':
        st.header('Information of ' + A_f +' Club')
    if A_f == 'All Data' and H_f != 'All Data':
        st.header('Information for All Club')
    if A_f != 'All Data' and H_f != 'All Data':
        st.header('Information of ' + A_f + " Club")
    st.table(goal)
    # st.header("Information of Most Goals")
    if A_f == 'All Data' and H_f == 'All Data':
        st.header('Information of Most Goals')
    if A_f != 'All Data' and H_f == 'All Data':
        st.header('Information of ' + A_f +' Club')
    if A_f == 'All Data' and H_f != 'All Data':
        st.header('Information for All Club at ' + H_f + " Hosting")
    if A_f != 'All Data' and H_f != 'All Data':
        st.header('Information of ' + A_f + " Club at " + H_f +' Hosting')
    st.table(goal_tally)
    if(A_f != 'All Data' and H_f == 'All Data'):
        pie_club1 = helper.pl_pie_Club(df1,A_f)
        p_na = np.array(['Total Wins','Total Goals','Total Opponent Goals'])
        figure = px.pie(names = p_na,values = pie_club1,title = 'Club ('+ A_f + ') Result',hole = 0.5,color = p_na,color_discrete_map={
            'Total Wins':'lightgreen','Total Goals':'cyan','Total Opponent Goals':'darkred'
        })
        st.plotly_chart(figure)
    if(A_f != 'All Data' and H_f != 'All Data'):
        pie_club2 = helper.pl_pie_club1(df4,A_f,H_f)
        p_na1 = np.array(['Total Wins','Total Goals','Total Opponent Goals'])
        figur = px.pie(names = p_na1,values = pie_club2,title = 'Club ('+ A_f + ') Result at ' + H_f,hole = 0.5,color = p_na1,color_discrete_map={
            'Total Wins':'lightgreen','Total Goals':'cyan','Total Opponent Goals':'darkred'
        })
        st.plotly_chart(figur)
    st_lottie(lottie_finish5,height=250,width=400)
if user_menu == "Analysis for Players":
    st.title("Top Statistics")
    player_name = df_foot_n1['player_name'].unique().shape[0]
    country_name = df_foot_n1['country_of_citizenship_x'].unique().shape[0]
    club_name = df_foot_n1['current_club_name'].unique().shape[0]
    
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.header('Players')
        st.header(player_name)
    with col2:
        st.header('Countries')
        st.header(country_name)
    with col3:
        st.header('Clubs')
        st.header(club_name)
    with col4:
        st_lottie(lottie_coding3,height=180,width=250)
    st.header("Goals and Red card vs Players from Football Club Chart")
    fig1= px.line(df_graph2,y = 'current_club_name',x = ['Sum of Total Goals','Sum of Total Red Card'])
    st.plotly_chart(fig1)
    st.header("Assist and Yellow Card vs Players from Football Club Chart")
    fig2 = px.line(df_graph2,y='current_club_name',x=['Sum of Total Yellow card','Sum of Total Assist'])
    st.plotly_chart(fig2)
    st.header("Goals and Red card vs Players from Country Chart")
    fig3 = px.line(df_graph1,y= 'country_of_citizenship_x',x = ['Sum of Total Goals','Sum of Total Red Card'])
    st.plotly_chart(fig3)
    st.header("Assist and Yellow card vs Players from Country Chart")
    fig4 = px.line(df_graph1,y= 'country_of_citizenship_x',x = ['Sum of Total Yellow card','Sum of Total Assist'])
    st.plotly_chart(fig4)
    coun_pl= preprocess.player1(df_foot_n1)
    c_pl = st.sidebar.selectbox('Select Country of Players',coun_pl)
    cn_pl=preprocess.player2(df_foot_n1,c_pl)
    cl_pl = st.sidebar.selectbox('Select Club of Players',cn_pl)
    na_pl =  preprocess.player3(df_foot_n1,c_pl,cl_pl)
    n_pl = st.sidebar.selectbox('Select Player',na_pl)

    if n_pl == 'Select above first' and c_pl == 'Select' and cl_pl == 'Select':
        st.header("Please Select to get the Data")
        st_lottie(lottie_coding2,height= 300,width=400)
        
    # if n_pl != 'Select above first' and c_pl == 'Select' and cl_pl == 'Select':
    #     st.subheader("Please Select")
    if n_pl == 'Select' and c_pl != 'Select' and cl_pl == 'Select':
        st_lottie(lottie_coding2,height= 300,width=400)
        st.subheader("Players which belongs to the " + c_pl+" Country")
        player1 = helper.player_info1(n_pl,c_pl,cl_pl,df_foot_n1)
        st.table(player1)
        
    if n_pl == 'Select' and c_pl == 'Select' and cl_pl != 'Select':
        st_lottie(lottie_coding2,height= 300,width=400)
        st.subheader("Players which belongs to the " + cl_pl +" Club")
        player1 = helper.player_info1(n_pl,c_pl,cl_pl,df_foot_n1)
        
        st.table(player1)
    if n_pl == 'Select' and c_pl != 'Select' and cl_pl != 'Select':
        st_lottie(lottie_coding2,height= 300,width=400)
        st.subheader("Players which belongs to " +c_pl + " Country and " + cl_pl +" Club")
        player1 = helper.player_info1(n_pl,c_pl,cl_pl,df_foot_n1)
        st.table(player1)
    if n_pl != 'Select' and c_pl != 'Select' and cl_pl == 'Select':
        st_lottie(lottie_coding2,height= 300,width=400)
        st.subheader("Players " +n_pl + " from Country " + c_pl)
        player1 = helper.player_info1(n_pl,c_pl,cl_pl,df_foot_n1)
        st.table(player1)
    if n_pl != 'Select' and c_pl == 'Select' and cl_pl != 'Select':
        st_lottie(lottie_coding2,height= 300,width=400)
        st.subheader("Players " +n_pl + " from Club " + cl_pl)
        player1 = helper.player_info1(n_pl,c_pl,cl_pl,df_foot_n1)
        st.table(player1)
    if n_pl != 'Select' and c_pl != 'Select' and cl_pl != 'Select':
        st_lottie(lottie_coding2,height= 300,width=400)
        st.subheader("Player name "+n_pl+ " which belongs to " +c_pl + " Country and " + cl_pl +" Club")
        player1 = helper.player_info1(n_pl,c_pl,cl_pl,df_foot_n1)
        
        st.table(player1)
    
    
    if n_pl == 'Select above first' and c_pl == 'Select' and cl_pl == 'Select':
        pass
    # if n_pl != 'Select above first' and c_pl == 'Select' and cl_pl == 'Select':
    #     st.header("Here's the info of")
    if n_pl == 'Select' and c_pl != 'Select' and cl_pl == 'Select':
        st.subheader("Players which belongs to the " + c_pl + " Country")
        player2 = helper.player_info2(n_pl,c_pl,cl_pl,df_foot_n3)
        st.table(player2)
    if n_pl == 'Select' and c_pl == 'Select' and cl_pl != 'Select':
        st.subheader("Players which belongs to the " + cl_pl +" Club")
        player2 = helper.player_info2(n_pl,c_pl,cl_pl,df_foot_n3)
        st.table(player2)
    if n_pl == 'Select' and c_pl != 'Select' and cl_pl != 'Select':
        st.subheader("Players which belongs to " +c_pl + " Country and " + cl_pl +" Club")
        player2 = helper.player_info2(n_pl,c_pl,cl_pl,df_foot_n3)
        st.table(player2)
    if n_pl != 'Select' and c_pl != 'Select' and cl_pl == 'Select':
        st.subheader("Player " +n_pl+" from country "+c_pl)
        player2 = helper.player_info2(n_pl,c_pl,cl_pl,df_foot_n3)
        st.table(player2)
    if n_pl != 'Select' and c_pl == 'Select' and cl_pl != 'Select':
        st.subheader("Players " +n_pl + " from Club " + cl_pl)
        player2 = helper.player_info2(n_pl,c_pl,cl_pl,df_foot_n1)
        st.table(player2)
    if n_pl != 'Select' and c_pl != 'Select' and cl_pl != 'Select':
        st.subheader("Player name "+n_pl+ " which belongs to " +c_pl + " Country and " + cl_pl +" Club")
        player2 = helper.player_info2(n_pl,c_pl,cl_pl,df_foot_n3)
        st.table(player2)
    
    if(n_pl != 'Select' and c_pl != 'Select'):
        st.subheader("Chart for Player (" +n_pl+")")
        pie3 = helper.pl_pie(df_foot_n3,n_pl,c_pl)
        p_name = np.array(['Total Assist','Total Red Card','Total Yellow Card','Total Goals'])
        fig1 = px.pie(names = p_name,values = pie3,hole = 0.5)
        st.plotly_chart(fig1)
        st_lottie(lottie_finish5,height= 250,width=400)
    elif(n_pl == 'Select' and c_pl != 'Select'):
        st.subheader('Please Select Player Name for Chart')
        st_lottie(lottie_coding2,height= 250,width=400)
    elif(n_pl != 'Select' and c_pl == 'Select'):
        st.subheader('Please Select Player and Country for Chart')
        st_lottie(lottie_coding2,height= 250,width=400)
    else:
        st.subheader('Please Select Player Name and Country for Chart')
        st_lottie(lottie_coding2,height= 250,width=400)
if user_menu == "Analysis for Games":
    st.title('Analysis for Football Clubs Matches') 
    col1,col2,col3= st.columns(3)
    with col1:
        st.header('Total Clubs')
        st.header('420')
    with col2:
        st.header('Matches')
        st.header('31111')
    with col3:
        st_lottie(lottie_coding3,height=180,width=300)
    game1_pl = preprocess.game1(df_game1)
    game2_pl = st.sidebar.selectbox('Select Competition',game1_pl)
    round1_pl = preprocess.game2(df_game1,game2_pl)
    round2_pl = st.sidebar.selectbox('Select Round',round1_pl)
    match1_pl = preprocess.game3(df_game1,game2_pl,round2_pl)
    match2_pl = st.sidebar.selectbox('Select Match',match1_pl)
    date1_pl = preprocess.game4(df_game1,game2_pl,round2_pl,match2_pl)
    date2_pl = st.sidebar.selectbox("Select Date",date1_pl)
    if(game2_pl == 'Select' and round2_pl == 'Select'):
        st.subheader("Select Competition and Round for Histogram chart(Goals vs Club)")
    if(game2_pl != 'Select' and round2_pl == 'Select'):
       st.header('Select Round please! for Histogram Chart(Goals vs Club)')
    if(game2_pl == 'Select' and round2_pl != 'Select'):
        st.header('Select Competition please! for Histogram Chart(Goals vs Club)')
    if(game2_pl != 'Select' and round2_pl != 'Select'):
        st.subheader("Team1 in " + game2_pl+" Competition and round "+round2_pl+" Team1 vs Goals Histogram Chart")
        dff_x = dff.groupby(['competition_type','round','home_club_name','away_club_name']).sum()[['home_club_goals','away_club_goals']].reset_index()
        fig11 = px.histogram(y = preprocess.game_line1(dff_x,game2_pl,round2_pl)['home_club_name'],x = preprocess.game_line1(dff_x,game2_pl,round2_pl)['home_club_goals'])
        fig12 = px.histogram(y = preprocess.game_line2(dff_x,game2_pl,round2_pl)['away_club_name'],x = preprocess.game_line2(dff_x,game2_pl,round2_pl)['away_club_goals'])
        st.plotly_chart(fig11)
        st.subheader("Team2 in " + game2_pl+" Competition and round "+round2_pl+" Team2 vs Goals Histogram Chart")
        st.plotly_chart(fig12)
    if(game2_pl == 'Select' and round2_pl == 'Select' and match2_pl == 'Select' and date2_pl == 'Select above first'):
        st.subheader("Please Select for Details")
    elif(game2_pl != 'Select' and round2_pl == 'Select' and match2_pl == 'Select' and date2_pl == 'Select'):
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
        st.subheader("You Selected " + game2_pl+" .Select more for Results")
    elif(game2_pl == 'Select' and round2_pl != 'Select' and match2_pl == 'Select' and date2_pl == 'Select'):
        st.subheader("Reuslt for " + round2_pl + " .Select more")
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
    elif(game2_pl == 'Select' and round2_pl == 'Select' and match2_pl != 'Select' and date2_pl == 'Select'):
        st.subheader("Result for match " +match2_pl)
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
    elif(game2_pl != 'Select' and round2_pl != 'Select' and match2_pl == 'Select' and date2_pl == 'Select'):
        st.subheader("In " + game2_pl + " Competition Match round is " +round2_pl)
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
    elif(match2_pl != 'Select' and date2_pl == 'Select'):
        st.subheader("Result Match "+match2_pl )
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
    elif(match2_pl != 'Select' and date2_pl != 'Select'):
        st.subheader("Result for Match " +match2_pl+" played on " +date2_pl)
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
    else:
        st.subheader("Here's your Result")
        game = helper.game_info1(df_game1,game2_pl,round2_pl,match2_pl,date2_pl)
        st.table(game)
    
    pie1 = helper.pie_chart1(df_pie,match2_pl,date2_pl)
    pie2 = helper.pie_chart2(df_pie,match2_pl,date2_pl)
    if(match2_pl != 'Select' and date2_pl != 'Select'):
        st.subheader("Chart of Goals in Match (" + match2_pl +")")
        fig = px.pie(names = pie1,values = pie2)
        st.plotly_chart(fig)
        st_lottie(lottie_finish5,height=250,width=400)
    elif(match2_pl != 'Select' and date2_pl == 'Select'):
        st.subheader("Please select Date for Goals Chart of Teams")
    else:
        st.subheader("Please select Match and Date for Goals Chart of Teams")
if user_menu == "Analysis for Competition":
    st.title("Players Performance in Competitions")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Competitions')
        st.header('42')
    with col2:
        st.header('Players')
        st.header('16689')
    with col3:
        st_lottie(lottie_coding,height=180,width=200)
    League_pl = preprocess.comp1(d_comp)
    lea_pl = st.sidebar.selectbox("Select League Name",League_pl)
    na_pl = preprocess.comp_name(d_comp,lea_pl)
    name_pl = st.sidebar.selectbox("Select Player",na_pl)

    def com_hist_goals1(df,player):
        fig1 = px.histogram(df[df['player_name'] == player],y = 'League_name',x = 'goals',color = 'League_name',title= "Goals Graph of ("+player+") in all Tournament he played")
        return fig1
    def com_hist_goals2(df,player):
        fig2 = px.histogram(df[df['player_name'] == player],y = 'League_name',x = 'assists',color = 'League_name',title= "Assits Graph of ("+player+") in all Tournament he played")
        return fig2
    def com_hist_goals3(df,player):
        fig3 = px.histogram(df[df['player_name'] == player],y = 'League_name',x = 'yellow_cards',color = 'League_name',title= "Yellow Card Graph of ("+player+") in all Tournament he played")
        return fig3
    def com_hist_goals4(df,player):
        fig4 = px.histogram(df[df['player_name'] == player],y = 'League_name',x = 'red_cards',color = 'League_name',title= "Red Card Graph of ("+player+") in all Tournament he played")
        return fig4
    if(name_pl =='Select' and lea_pl == 'Select'):
        st.subheader("Please Select from sidebar for Data")
    if(name_pl != 'Select' and lea_pl == 'Select'):
        st.subheader("Details of Player (" +name_pl+") in all Tournaments")
        comp = helper.competition_info(d_comp,name_pl,lea_pl)
        st.table(comp)
    if(name_pl == 'Select' and lea_pl != 'Select'):
        st.subheader("Details of all Players participated in league (" +lea_pl+")")
        comp = helper.competition_info(d_comp,name_pl,lea_pl)
        st.table(comp)
    if(name_pl != 'Select' and lea_pl != 'Select'):
        st.subheader("Details of Player ("+name_pl+") participated in league (" +lea_pl+")")
        comp = helper.competition_info(d_comp,name_pl,lea_pl)
        st.table(comp)
    st_lottie(lottie_coding2,height=250,width=400)
    if (name_pl == 'Select'):
        st.subheader("Please Select for Player Name for Performance Chart")
    if(name_pl != 'Select'):
        st.plotly_chart(com_hist_goals1(d_comp,name_pl))
        st.plotly_chart(com_hist_goals2(d_comp,name_pl))
        st.plotly_chart(com_hist_goals3(d_comp,name_pl))
        st.plotly_chart(com_hist_goals4(d_comp,name_pl))
        st_lottie(lottie_finish5,height=250,width=400)
