import pandas as pd
import numpy as np

# df_club_h = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\clubs.csv")
# df_competition = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\competitions.csv")
# df_game_event = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\game_events.csv")
# df_game = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\games.csv")
# df_player_valuation = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\player_valuations.csv")
# df_players = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\players.csv")
# df_appearances = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\appearances.csv")
# df_club_games_h = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\club_games.csv")

def fetch_goals1(df_new_p,host,names):
    if host == 'All Data' and names == 'All Data':
        temp1_df = df_new_p
        # temp2_df = df1
    if host != 'All Data' and names == 'All Data':
        temp1_df = df_new_p
        # temp2_df = df4[df4['hosting'] == host] 
    if host == 'All Data' and names != 'All Data':
        temp1_df = df_new_p[df_new_p['name'] == names]
        # temp2_df = df1[df1['name'] == names]
    if host !='All Data' and names != 'All Data':
        temp1_df = df_new_p[df_new_p['name'] == names]
        # temp2_df = df4[(df4['name'] == names) & (df4['hosting'] == host)]
    temp1_df.rename(columns = {'name':'Name','squad_size':'Squad Size','stadium_name':'Stadium Name','net_transfer_record':'Net Transfer Record','average_age':'Average Age','foreigners_number':'Foreigners Players','national_team_players':'National Team Player'},inplace  = True)
    temp1_df['Squad Size'] = temp1_df['Squad Size'].astype('int')
    temp1_df['Average Age'] = temp1_df['Average Age'].astype('int')
    temp1_df['Foreigners Players'] = temp1_df['Foreigners Players'].astype('int')
    temp1_df['National Team Player'] = temp1_df['National Team Player'].astype('int')
    return temp1_df
def fetch_goals2(df4,df1,host,names):
    if host == 'All Data' and names == 'All Data':
        temp2_df = df1
    if host != 'All Data' and names == 'All Data':
        temp2_df = df4[df4['hosting'] == host] 
    if host == 'All Data' and names != 'All Data':
        temp2_df = df1[df1['name'] == names]
    if host !='All Data' and names != 'All Data':
        temp2_df = df4[(df4['name'] == names) & (df4['hosting'] == host)]
    temp2_df.rename(columns = {'hosting':'Hosting','is_win' : 'Total Wins','name' : 'Name','own_goals' : 'Total Goals','opponent_goals':'Total Opponent Goals'},inplace = True)
    temp2_df['Total Goals'] = temp2_df['Total Goals'].astype('int')
    temp2_df['Total Wins'] = temp2_df['Total Wins'].astype('int')
    temp2_df['Total Opponent Goals'] = temp2_df['Total Opponent Goals'].astype('int')
    return temp2_df
def goal_tally(df_club_h,df_club_games_h):
    df_club_n = df_club_h.merge(df_club_games_h,on = 'club_id',how = 'inner')
    dfff = df_club_n.drop(['coach_name','total_market_value','url'],axis = 'columns')
    df1 = dfff.groupby(['name']).sum()[['is_win','own_goals','opponent_goals'
]].sort_values(['is_win'],ascending = False).reset_index()
    
    df_club_new1 = df_club_h.merge(df_club_games_h,on = 'club_id',how = 'inner')
    df_p = df_club_new1.groupby(['name','squad_size','stadium_name','net_transfer_record','average_age','foreigners_number','national_team_players']).sum()[['is_win'
]].sort_values(['is_win'],ascending = False).reset_index()
   
    # df_new_p = df_p.drop(['is_win'],axis='columns')
    df2 = df1.merge(df_p,on = 'name',how = 'inner')
    df3 = df2.drop(['squad_size','stadium_name','net_transfer_record','average_age','foreigners_number','national_team_players','is_win_x'],axis = 'columns')
    df3.rename(columns = {'is_win_y' : 'Total Wins','name' : 'Name','own_goals' : 'Total Goals','opponent_goals':'Total Opponent Goals'},inplace = True)
    return df3
def player_info1(p_name,p_country,c_club,df1):
    if p_name == 'Select' and p_country == 'Select' and c_club == 'Select':
        p_temp1 = None
    if p_name != 'Select' and p_country == 'Select' and c_club == 'Select':
        p_temp1 = df1[df1['player_name'] == p_name]
        
    if p_name == 'Select' and p_country != 'Select' and c_club == 'Select':
        p_temp1 = df1[df1['country_of_citizenship_x'] == p_country]
        
    if p_name == 'Select' and p_country == 'Select' and c_club != 'Select':
        p_temp1 = df1[df1['current_club_name'] == c_club]
        
    if p_name != 'Select' and p_country != 'Select' and c_club == 'Select':
        
        p_temp1 = df1[df1['player_name'] == p_name]
    if p_name != 'Select' and p_country == 'Select' and c_club != 'Select':
        p_temp1 = df1[df1['player_name'] == p_name]
       
    if p_name == 'Select' and p_country != 'Select' and c_club != 'Select':
        p_temp1 = df1[(df1['country_of_citizenship_x'] == p_country) & (df1['current_club_name'] == c_club)]
    if p_name != 'Select' and p_country != 'Select' and c_club != 'Select':
        p_temp1 = df1[df1['player_name'] == p_name]
        
    return p_temp1

def player_info2(p_name,p_country,c_club,df2):
    if p_name == 'Select' and p_country == 'Select' and c_club == 'Select':
        p_temp2 = None
    if p_name != 'Select' and p_country == 'Select' and c_club == 'Select':
        
        p_temp2 = df2[df2['player_name'] == p_name]
    if p_name == 'Select' and p_country != 'Select' and c_club == 'Select':
        
        p_temp2 = df2[df2['country_of_citizenship_x'] == p_country]
    if p_name == 'Select' and p_country == 'Select' and c_club != 'Select':
       
        p_temp2 = df2[df2['current_club_name'] == c_club]
    if p_name != 'Select' and p_country != 'Select' and c_club == 'Select':
        
        p_temp2 = df2[df2['player_name'] == p_name]
    if p_name != 'Select' and p_country == 'Select' and c_club != 'Select':
       
        p_temp2 = df2[(df2['player_name'] == p_name) & (df2['current_club_name'] == c_club)]
    if p_name == 'Select' and p_country != 'Select' and c_club != 'Select':
        
        p_temp2 = df2[(df2['country_of_citizenship_x'] == p_country) & (df2['current_club_name'] == c_club)]
    if p_name != 'Select' and p_country != 'Select' and c_club != 'Select':
        
        p_temp2 = df2[df2['player_name'] == p_name]
    return p_temp2

def game_info1(df1,g_pl,r_pl,m_pl,d_pl):
    if g_pl == 'Select' and r_pl == 'Select' and m_pl == 'Select' and d_pl == 'Select':
        g_temp = None
    if g_pl != 'Select' and r_pl == 'Select' and m_pl == 'Select' and d_pl == 'Select':
        # g_temp = df1[df1['competition_type'] == g_pl]
        g_temp = None
    if g_pl == 'Select' and r_pl != 'Select' and m_pl == 'Select' and d_pl == 'Select':
        g_temp = df1[df1['round'] == r_pl]
    if g_pl == 'Select' and r_pl != 'Select' and m_pl != 'Select' and d_pl == 'Select':
        g_temp = df1[(df1['Football_Match'] == m_pl) & (df1['round'] == r_pl)]
    if g_pl != 'Select' and r_pl != 'Select' and m_pl == 'Select' and d_pl == 'Select':
        g_temp = df1[(df1['competition_type'] == g_pl) & (df1['round'] == r_pl)]
    if g_pl != 'Select' and r_pl != 'Select' and m_pl != 'Select' and d_pl == 'Select':
        g_temp = df1[(df1['competition_type'] == g_pl) & (df1['round'] == r_pl) & (df1['Football_Match'] == m_pl)]
    if g_pl != 'Select' and r_pl != 'Select' and m_pl != 'Select' and d_pl != 'Select':
        g_temp = df1[(df1['competition_type'] == g_pl) & (df1['round'] == r_pl) & (df1['Football_Match'] == m_pl) & (df1['date'] == d_pl)]
    if g_pl == 'Select' and r_pl == 'Select' and m_pl != 'Select' and d_pl == 'Select':
        g_temp = df1[df1['Football_Match'] == m_pl]
    if g_pl == 'Select' and r_pl == 'Select' and m_pl == 'Select' and d_pl != 'Select':
        g_temp = df1[df1['round'] == d_pl]
    if g_pl != 'Select' and r_pl == 'Select' and m_pl != 'Select' and d_pl == 'Select':
        g_temp = df1[(df1['Football_Match'] == m_pl) & (df1['competition_type'] == g_pl)]
    if g_pl != 'Select' and r_pl == 'Select' and m_pl == 'Select' and d_pl != 'Select':
        g_temp = df1[(df1['competition_type'] == g_pl) & (df1['date'] == d_pl)]
    if g_pl == 'Select' and r_pl == 'Select' and m_pl != 'Select' and d_pl != 'Select':
        g_temp = df1[(df1['Football_Match'] == m_pl) & (df1['date'] == d_pl)]
    if g_pl != 'Select' and r_pl != 'Select' and m_pl == 'Select' and d_pl != 'Select':
        g_temp = df1[(df1['competition_type'] == g_pl) & (df1['round'] == r_pl) & (df1['date'] == d_pl)]
    if g_pl == 'Select' and r_pl != 'Select' and m_pl != 'Select' and d_pl != 'Select':
        g_temp = df1[(df1['date'] == d_pl) & (df1['round'] == r_pl) & (df1['Football_Match'] == m_pl)]
    if g_pl != 'Select' and r_pl == 'Select' and m_pl != 'Select' and d_pl != 'Select':
        g_temp = df1[(df1['competition_type'] == g_pl) & (df1['date'] == d_pl) & (df1['Football_Match'] == m_pl)]
    return g_temp
def pie_chart1(df,match,date):
    Teams = np.array(df[(df["Football_Match"] == match) & (df['date'] == date)]['home_club_name'])
    Teams = np.append(Teams,df[(df["Football_Match"] == match) & (df['date'] == date)]['away_club_name'])
    return Teams
def pie_chart2(df,match,date):
    value =  np.array([df[(df["Football_Match"] == match) & (df['date'] == date)]['home_club_goals']])
    value = np.append(value,df[(df["Football_Match"] == match) & (df['date'] == date)]['away_club_goals'])
    return value
def pl_pie(df,name,country):
    stats = np.array(df[(df['player_name'] == name) & (df['country_of_citizenship_x'] == country)]['Total Assist'])
    stat = np.append(stats,df[(df['player_name'] == name) & (df['country_of_citizenship_x'] == country)]['Total Red Card'])
    sta = np.append(stat,df[(df['player_name'] == name) & (df['country_of_citizenship_x'] == country)]['Total Yellow Card'])
    st = np.append(sta,df[(df['player_name'] == name) & (df['country_of_citizenship_x'] == country)]['Total Goals'])           
    return st
def pl_pie_Club(df,name):
    stats = np.array(df[df['name'] == name]['is_win'])
    stat = np.append(stats,df[df['name'] == name]['own_goals'])
    sta = np.append(stat,df[df['name'] == name]['opponent_goals'])
    return sta
def pl_pie_club1(df,name,d_f):
    stats = np.array(df[(df['name'] == name) & (df['hosting'] == d_f)]['is_win'])
    stats = np.append(stats,df[(df['name'] == name) & (df['hosting'] == d_f)]['own_goals'])
    stats = np.append(stats,df[(df['name'] == name) & (df['hosting'] == d_f)]['opponent_goals'])
    return stats
def competition_info(df,name,l_name):
    if(name != "Select" and l_name == 'Select'):
        temp = df[df['player_name'] == name]
    if(name != 'Select' and l_name != 'Select'):
        temp = df[(df['League_name'] == l_name) & (df['player_name'] == name)]
    if(name == 'Select' and l_name != 'Select'):
        temp = df[df['League_name'] == l_name]
    return temp
