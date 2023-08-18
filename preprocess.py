import pandas as pd

# df_club_p = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\clubs.csv")
# df_competition = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\competitions.csv")
# df_game_event = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\game_events.csv")
# df_game = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\games.csv")
# df_player_valuation = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\player_valuations.csv")
# df_players = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\players.csv")
# df_appearances = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\appearances.csv")
# df_club_games_p = pd.read_csv("C:\\Users\\Gyanendra\\Desktop\\files\\club_games.csv")

# def preprocessor():
#     df_club_new1 = df_club_p.merge(df_club_games_p,on = 'club_id',how = 'inner')
#     df_p = df_club_new1.groupby(['name','squad_size','stadium_name','net_transfer_record','average_age','foreigners_number','national_team_players']).sum()[['is_win'
# ]].sort_values(['is_win'],ascending = False).reset_index()

#     df_new_p = df_p.drop(['is_win'],axis='columns')
#     df_new_p.rename(columns = {'name':'Name','squad_size':'Squad Size','stadium_name':'Stadium Size','net_transfer_record':'Net Transfer Record','average_age':'Average Age','foreigners_number':'Foreigners Players','national_team_players':'National Team Player'},inplace  = True)
#     return df_new_p

# def club():
#     df_club_new1 = df_club_p.merge(df_club_games_p,on = 'club_id',how = 'inner')
#     df_p = df_club_new1.groupby(['name','squad_size','stadium_name','net_transfer_record','average_age','foreigners_number','national_team_players','hosting']).sum()[['is_win'
# ]].sort_values(['is_win'],ascending = False).reset_index()
   
#     df_new_p1 = df_p.drop(['is_win'],axis='columns')
#     club_name = df_new_p1['name'].unique().tolist()
#     club_name.insert(0,'All Data')
#     host_m = df_new_p1['hosting'].unique().tolist()
#     host_m.insert(0,'All Data')
#     return club_name,host_m
def player1(df):
    country_pl = df['country_of_citizenship_x'].unique().tolist()
    country_pl.insert(0,'Select')
    return country_pl
def player2(df,countpl):
    if(countpl == 'Select'):
        club_pl = df['current_club_name'].unique().tolist()
        club_pl.insert(0,'Select')
    if(countpl != 'Select'):
        club_pl = df[df['country_of_citizenship_x'] == countpl]['current_club_name'].unique().tolist()
        club_pl.insert(0,'Select')
    return club_pl
def player3(df,countpl,clu_pl):
    if(countpl != 'Select' and clu_pl == 'Select'):
        name_pl = df[df['country_of_citizenship_x'] == countpl]['player_name'].unique().tolist()
        name_pl.insert(0,'Select')
    if(countpl == 'Select' and clu_pl == 'Select'):
        # name_pl = df['player_name'].unique().tolist()
        name_pl=['Select above first']
        # name_pl.insert(0,"Select above first")
    if(countpl == 'Select' and clu_pl != 'Select'):
        name_pl = df[df['current_club_name'] == clu_pl]['player_name'].unique().tolist()
        name_pl.insert(0,'Select')
    if(countpl != 'Select' and clu_pl != 'Select'):
        name_pl = df[(df['country_of_citizenship_x'] == countpl) & (df['current_club_name'] == clu_pl)]['player_name'].unique().tolist()
        name_pl.insert(0,'Select')
    return name_pl

        
def game1(df1):
    game_pl = df1['competition_type'].unique().tolist()
    game_pl.insert(0,'Select')
    return game_pl
def game2(df1,g_p):
    if g_p == 'Select':
        round_pl = df1['round'].unique().tolist()
        round_pl.insert(0,'Select')
    if g_p != 'Select':
        round_pl = df1[df1['competition_type'] == g_p]['round'].unique().tolist()
        round_pl.insert(0,'Select')
    return round_pl
def game3(df1,g_p,r_p):
    if(g_p == 'Select' and r_p == 'Select'):
        match_pl = df1['Football_Match'].unique().tolist()
        match_pl.insert(0,'Select')
    if(g_p != 'Select' and r_p == 'Select'):
        match_pl = df1[df1['competition_type'] == g_p]['Football_Match'].unique().tolist()
        match_pl.insert(0,'Select')
    if(g_p == 'Select' and r_p != 'Select'):
        match_pl = df1[df1['round'] == r_p]['Football_Match'].unique().tolist()
        match_pl.insert(0,'Select')
    if(g_p != 'Select' and r_p != 'Select'):
        match_pl = df1[(df1['competition_type'] == g_p)&(df1['round'] == r_p)]['Football_Match'].unique().tolist()
        match_pl.insert(0,'Select')
    return match_pl
def game4(df1,g_p,r_p,m_p):
    if(g_p == 'Select' and r_p == 'Select' and m_p == 'Select'):
        # date_pl = df1['date'].unique().tolist()
        # date_pl.insert(0,'Select')
        date_pl = ['Select above first']
    if(g_p != 'Select' and r_p == 'Select' and m_p == 'Select'):
        date_pl = df1[df1['competition_type'] == g_p]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    if(g_p != 'Select' and r_p != 'Select' and m_p == 'Select'):
        date_pl = df1[(df1['competition_type'] == g_p)&(df1['round'] == r_p)]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    if(g_p == 'Select' and r_p != 'Select' and m_p == 'Select'):
        date_pl = df1[df1['round'] == g_p]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    if(g_p == 'Select' and r_p != 'Select' and m_p != 'Select'):
        date_pl = df1[(df1['round'] == r_p)&(df1['Football_Match'] == m_p)]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    if(g_p != 'Select' and r_p == 'Select' and m_p != 'Select'):
        date_pl = df1[(df1['competition_type'] == g_p) & (df1['Football_Match'] == m_p)]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    if(g_p != 'Select' and r_p != 'Select' and m_p != 'Select'):
        date_pl = df1[(df1['competition_type'] == g_p) & (df1['round'] == r_p) & (df1['Football_Match'] == m_p)]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    if(g_p == 'Select' and r_p == 'Select' and m_p != 'Select'):
        date_pl = df1[(df1['Football_Match'] == m_p)]['date'].unique().tolist()
        date_pl.insert(0,'Select')
    return date_pl
def game_line1(df,c_t,r_t):
    line1 = df[(df['competition_type'] == c_t) & (df['round'] == r_t)]
    line2 = line1.sort_values(['home_club_goals'],ascending = False).reset_index()
    return line2
def game_line2(df,c_t,r_t):
    line1 = df[(df['competition_type'] == c_t) & (df['round'] == r_t)]
    # line2 = line1.sort_values(['away_club_goals'],ascending = True).reset_index()
    return line1
def comp1(df):
    leag_n = df['League_name'].unique().tolist()
    leag_n.insert(0,"Select")
    return leag_n
def comp_name(df,name):
    if name == 'Select':
        name_n = df['player_name'].unique().tolist()
        name_n.insert(0,"Select")
    if name != 'Select':
        name_n = df[df['League_name'] == name]['player_name'].unique().tolist()
        name_n.insert(0,'Select')
    return name_n