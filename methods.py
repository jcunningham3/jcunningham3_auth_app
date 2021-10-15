import requests

# GOAL
# Build the user's team from fantasy premier league
# Compare the user's current team to the best team
# Analyze the user's current team and make transfer suggestions
# create an interactive experience for the user by adding features such as chatting and monthly awards
team = {
    'picks': '',
    'player_data': '',
    'personal_data': '',
    'classic_league': '',
    'team_info': [
        {
            'id': 1,
            'name': 'Arsenal',
            'colors': '#EF0107',
            'logo': '\static\img\logos\ars.png',
            'jersey': '\static\img\jerseys\shirt_3-66_ars.webp',
            'jersey_goal': '\static\img\jerseys\arsg.webp'
        },
        {
            'id': 2,
            'name': 'Aston Villa',
            'colors': '#670E36',
            'logo': '\static\img\logos\logo_avl.png',
            'jersey': '\static\img\jerseys\shirt_7-66_avl.webp',
            'jersey_goal': '\static\img\jerseys\keeper_avl.webp'
        },
        {
            'id': 3,
            'name': 'Brentford',
            'colors': '#e30613',
            'logo': '\static\img\logos\logo_bre.png',
            'jersey': '\static\img\jerseys\jersey_bre.webp',
            'jersey_goal': '\static\img\jerseys\keeper_bre.webp'
        },
        {
            'id': 4,
            'name': 'Brigton Hove Albion',
            'colors': '#0057B8',
            'logo': '\static\img\logos\logo_bha.png',
            'jersey': '\static\img\jerseys\shirt_36-66_bha.webp',
            'jersey_goal': '\static\img\jerseys\shirt_90_1-66_bur_g.webp'
        },
        {
            'id': 5,
            'name': 'Burnley',
            'colors': '#6C1D45',
            'logo': '\static\img\logos\bur.png',
            'jersey': '\static\img\jerseys\shirt_90-66_bur.webp',
            'jersey_goal': '\static\img\jerseys\shirt_90_1-66_burg.webp'
        },
        {
            'id': 6,
            'name': 'Chelsea',
            'colors': '#034694',
            'logo': '\static\img\logos\che.png',
            'jersey': '\static\img\jerseys\che.webp',
            'jersey_goal': '\static\img\jerseys\cheg.webp',
        },
        {
            'id': 7,
            'name': 'Crystal Palace',
            'colors': '#1B458F',
            'logo': '\static\img\logos\cry.png',
            'jersey': '\static\img\jerseys\cry.webp',
            'jersey_goal': '\static\img\jerseys\cryg.webp'
        },
        {
            'id': 8,
            'name': 'Everton',
            'colors': '#003399',
            'logo': '\static\img\logos\eve.png',
            'jersey': '\static\img\jerseys\eve.webp',
            'jersey_goal': '\static\img\jerseys\eveg.webp'
        },
        {
            'id': 9,
            'name': 'Leicester City',
            'colors': '#003090',
            'logo': '\static\img\logos\lei.png',
            'jersey': '\static\img\jerseys\lei.webp',
            'jersey_goal': '\static\img\jerseys\leig.webp'
        },
        {
            'id': 10,
            'name': 'Leeds United',
            'colors': '#FFCD00',
            'logo': '\static\img\logos\lee.png',
            'jersey': '\static\img\jerseys\lee.webp',
            'jersey_goal': '\static\img\jerseys\leeg.webp'
        },
        {
            'id': 11,
            'name': 'Liverpool',
            'colors': '#C8102E',
            'logo': '\static\img\logos\liv.png',
            'jersey': '\static\img\jerseys\liv.webp',
            'jersey_goal': '\static\img\jerseys\livg.webp'
        },
        {
            'id': 12,
            'name': 'Manchester City',
            'colors': '#6CABDD',
            'logo': '\static\img\logos\mcy.png',
            'jersey': '\static\img\jerseys\mci.webp',
            'jersey_goal': '\static\img\jerseys\mcig.webp'
        },
        {
            'id': 13,
            'name': 'Manchester United',
            'colors': '#DA291C',
            'logo': '\static\img\logos\mnu.png',
            'jersey': '\static\img\jerseys\mun.webp',
            'jersey_goal': '\static\img\jerseys\mung.webp'
        },
        {
            'id': 14,
            'name': 'Newcastle United',
            'colors': '#41B6E6',
            'logo': '\static\img\logos\logo_new.png',
            'jersey': '\static\img\jerseys\shirt_4-66_new.webp',
            'jersey_goal': '\static\img\jerseys\newg.webp'
        },
        {
            'id': 15,
            'name': 'Norwich City',
            'colors': '#00A650',
            'logo': '\static\img\logos\nor.png',
            'jersey': '\static\img\jerseys\nor.webp',
            'jersey_goal': '\static\img\jerseys\norg.webp'
        },
        {
            'id': 16,
            'name': 'Southampton',
            'colors': '#D71920',
            'logo': '\static\img\logos\sou.png',
            'jersey': '\static\img\jerseys\sou.webp',
            'jersey_goal': '\static\img\jerseys\soug.webp'
        },
        {
            'id': 17,
            'name': 'Tottenham',
            'colors': '#132257',
            'logo': 'static\img\logos\logo_tot.png',
            'jersey': '\static\img\jerseys\shirt_6-66_tot.webp',
            'jersey_goal': '\static\img\jerseys\keeper_tot.webp'
        },
        {
            'id': 18,
            'name': 'Watford',
            'colors': '#FBEE23',
            'logo': '\static\img\logos\wat.png',
            'jersey': '\static\img\jerseys\wat.webp',
            'jersey_goal': '\static\img\jerseys\watg.webp'
        },
        {
            'id': 19,
            'name': 'West Ham United',
            'colors': '#4F0E0E',
            'logo': '\static\img\logos\whu.png',
            'jersey': '\static\img\jerseys\whu.webp',
            'jersey_goal': '\static\img\jerseys\whug.webp'
        },
        {
            'id': 20,
            'name': 'Wolverhampton',
            'colors': '#F9B208',
            'logo': '\static\img\logos\wol.png',
            'jersey': '\static\img\jerseys\wol.webp',
            'jersey_goal': '\static\img\jerseys\wolg.webp'
        }
    ]
}

# use this endpoint('https://fantasy.premierleague.com/api/my-team/' + team_id + '/') to get
# the user's team
# this method requires the user's email, password, and team id from fantaasy premier league
def get_users_basic_team(email, password, team_id):

    team_id = str(team_id)

    # put the cookies received in session to be remembered
    session = requests.session()

    # url needed to make the post request
    url = 'https://users.premierleague.com/accounts/login/'

    # data needed for the post request
    payload = {
     'password': password,
     'login': email,
     'redirect_uri': 'https://fantasy.premierleague.com/a/login',
     'app': 'plfpl-web'
    }
    session.post(url, data=payload)

    # Get response sent with authorization cookies
    res = session.get('https://fantasy.premierleague.com/api/my-team/' + team_id + '/')

    # setting the response to a var called 'data' and making the response json
    data = res.json()

    return data

# use this endpoint('https://fantasy.premierleague.com/api/bootstrap-static/') to get all the footballer's data
# the data from here will be used in combination with the get_users_team to gain access to names and other important stats
# as well as wether or not game weeks have started and ended
def get_all_footballers():
    res = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = res.json()
    return data

# use this endpoint('https://fantasy.premierleague.com/api/entry/' + team_id + '/') to get the user's
# personal info like their team name, points, and more importantly their league info as well as other info
# this method requires the user's team id
def get_users_personal_info(team_id):
    team_id = str(team_id)
    res = requests.get('https://fantasy.premierleague.com/api/entry/' + team_id + '/')
    data = res.json()
    return data
    
# use this endpoint('https://fantasy.premierleague.com/api/leagues-classic/'+ id + '/standings/') to get
# the users classic league information like who plays in the classic league. This info will be used
# for things like league standings.
# This method requires the user's  league id
def get_classic_league(id):
    id = str(id)
    res = requests.get('https://fantasy.premierleague.com/api/leagues-classic/'+ id + '/standings/')
    data = res.json()
    return data

# put all the data from the 4 endpoints together to create the user's profile
user_profile = {
    'team_name': 'incoming data is coming from a source being looped over',
    'fav_team': 'incoming data is coming from a source being looped over',
    'fav_team_id': 'incoming data is coming from a source being looped over',
    'fav_team_logo': 'incoming data is coming from a source being looped over',
    'fav_team_colors': 'incoming data is coming from a source being looped over',
    'fav_team_jersey': 'incoming data is coming from a source being looped over',
    'fav_team_jersey_goal': 'incoming data is coming from a source being looped over',
    'overall_points': 'incoming data is coming from a source being looped over',
    'overall_rank': 'incoming data is coming from a source being looped over',
    'gameweek_points': 'incoming data is coming from a source being looped over',
    'gameweek_rank': 'incoming data is coming from a source being looped over',
    'classic_league_id': 0,
    'classic_league_name': 'incoming data is coming from a source being looped over',
    'classic_league_rank': 0,
    'classic_league_rank_previous': 0,

    #USERS PLAYER 1/15
    'p1_chance_of_playing_next_round': '',
    'p1_chance_of_playing_this_round': '',
    'p1_cost_change_event': '',
    'p1_cost_change_event_fall': '',
    'p1_cost_change_start': '',
    'p1_cost_change_start_fall': '',
    'p1_dreamteam_count': '',
    'p1_element_type': '',
    'p1_event_points': '',
    'p1_first_name': '',
    'p1_form': '',
    'p1_player_id': '',
    'p1_in_dreamteam': '',
    'p1_now_cost': '',
    'p1_photo': '',
    'p1_points_per_game': '',
    'p1_second_name':'',
    'p1_selected_by_percent':'',
    'p1_special':'',
    'p1_squad_number':'',
    'p1_status':'',
    'p1_team':'',
    'p1_team_code':'',
    'p1_total_points':'',
    'p1_value_form':'',
    'p1_value_season':'',
    'p1_web_name':'',
    'p1_minutes':'',
    'p1_goals_scored':'',
    'p1_assists':'',
    'p1_clean_sheets':'',
    'p1_own_goals':'',
    'p1_penalties_saved':'',
    'p1_goals_conceded':'',
    'p1_penalties_missed':'',
    'p1_yellow_cards':'',
    'p1_red_cards':'',
    'p1_saves':'',
    'p1_bonus':'',
    'p1_bps':'',
    'p1_team_jersey':'',
    'p1_team_logo':'',
    'p1_team_colors':'',
    'p1_team_name':'',

    #USERS PLAYER 2/15
    'p2_chance_of_playing_next_round': '',
    'p2_chance_of_playing_this_round': '',
    'p2_cost_change_event': '',
    'p2_cost_change_event_fall': '',
    'p2_cost_change_start': '',
    'p2_cost_change_start_fall': '',
    'p2_dreamteam_count': '',
    'p2_element_type': '',
    'p2_event_points': '',
    'p2_first_name': '',
    'p2_form': '',
    'p2_player_id': '',
    'p2_in_dreamteam': '',
    'p2_now_cost': '',
    'p2_photo': '',
    'p2_points_per_game': '',
    'p2_second_name':'',
    'p2_selected_by_percent':'',
    'p2_special':'',
    'p2_squad_number':'',
    'p2_status':'',
    'p2_team':'',
    'p2_team_code':'',
    'p2_total_points':'',
    'p2_value_form':'',
    'p2_value_season':'',
    'p2_web_name':'',
    'p2_minutes':'',
    'p2_goals_scored':'',
    'p2_assists':'',
    'p2_clean_sheets':'',
    'p2_goals_conceded':'',
    'p2_own_goals':'',
    'p2_penalties_saved':'',
    'p2_penalties_missed':'',
    'p2_yellow_cards':'',
    'p2_red_cards':'',
    'p2_saves':'',
    'p2_bonus':'',
    'p2_bps':'',
    'p2_team_jersey':'',
    'p2_team_logo':'',
    'p2_team_colors':'',
    'p2_team_name':'',

    'p3_chance_of_playing_next_round': '',
    'p3_chance_of_playing_this_round': '',
    'p3_cost_change_event': '',
    'p3_cost_change_event_fall': '',
    'p3_cost_change_start': '',
    'p3_cost_change_start_fall': '',
    'p3_dreamteam_count': '',
    'p3_element_type': '',
    'p3_event_points': '',
    'p3_first_name': '',
    'p3_form': '',
    'p3_player_id': '',
    'p3_in_dreamteam': '',
    'p3_now_cost': '',
    'p3_photo': '',
    'p3_points_per_game': '',
    'p3_second_name':'',
    'p3_selected_by_percent':'',
    'p3_special':'',
    'p3_squad_number':'',
    'p3_status':'',
    'p3_team':'',
    'p3_team_code':'',
    'p3_total_points':'',
    'p3_value_form':'',
    'p3_value_season':'',
    'p3_web_name':'',
    'p3_minutes':'',
    'p3_goals_scored':'',
    'p3_assists':'',
    'p3_clean_sheets':'',
    'p3_goals_conceded':'',
    'p3_own_goals':'',
    'p3_penalties_saved':'',
    'p3_penalties_missed':'',
    'p3_yellow_cards':'',
    'p3_red_cards':'',
    'p3_saves':'',
    'p3_bonus':'',
    'p3_bps':'',
    'p3_team_jersey':'',
    'p3_team_logo':'',
    'p3_team_colors':'',
    'p3_team_name':'',

    'p4_chance_of_playing_next_round': '',
    'p4_chance_of_playing_this_round': '',
    'p4_cost_change_event': '',
    'p4_cost_change_event_fall': '',
    'p4_cost_change_start': '',
    'p4_cost_change_start_fall': '',
    'p4_dreamteam_count': '',
    'p4_element_type': '',
    'p4_event_points': '',
    'p4_first_name': '',
    'p4_form': '',
    'p4_player_id': '',
    'p4_in_dreamteam': '',
    'p4_now_cost': '',
    'p4_photo': '',
    'p4_points_per_game': '',
    'p4_second_name':'',
    'p4_selected_by_percent':'',
    'p4_special':'',
    'p4_squad_number':'',
    'p4_status':'',
    'p4_team':'',
    'p4_team_code':'',
    'p4_total_points':'',
    'p4_value_form':'',
    'p4_value_season':'',
    'p4_web_name':'',
    'p4_minutes':'',
    'p4_goals_scored':'',
    'p4_assists':'',
    'p4_clean_sheets':'',
    'p4_goals_conceded':'',
    'p4_own_goals':'',
    'p4_penalties_saved':'',
    'p4_penalties_missed':'',
    'p4_yellow_cards':'',
    'p4_red_cards':'',
    'p4_saves':'',
    'p4_bonus':'',
    'p4_bps':'',
    'p4_team_jersey':'',
    'p4_team_logo':'',
    'p4_team_colors':'',
    'p4_team_name':'',

    'p5_chance_of_playing_next_round': '',
    'p5_chance_of_playing_this_round': '',
    'p5_cost_change_event': '',
    'p5_cost_change_event_fall': '',
    'p5_cost_change_start': '',
    'p5_cost_change_start_fall': '',
    'p5_dreamteam_count': '',
    'p5_element_type': '',
    'p5_event_points': '',
    'p5_first_name': '',
    'p5_form': '',
    'p5_player_id': '',
    'p5_in_dreamteam': '',
    'p5_now_cost': '',
    'p5_photo': '',
    'p5_points_per_game': '',
    'p5_second_name':'',
    'p5_selected_by_percent':'',
    'p5_special':'',
    'p5_squad_number':'',
    'p5_status':'',
    'p5_team':'',
    'p5_team_code':'',
    'p5_total_points':'',
    'p5_value_form':'',
    'p5_value_season':'',
    'p5_web_name':'',
    'p5_minutes':'',
    'p5_goals_scored':'',
    'p5_assists':'',
    'p5_clean_sheets':'',
    'p5_goals_conceded':'',
    'p5_own_goals':'',
    'p5_penalties_saved':'',
    'p5_penalties_missed':'',
    'p5_yellow_cards':'',
    'p5_red_cards':'',
    'p5_saves':'',
    'p5_bonus':'',
    'p5_bps':'',
    'p5_team_jersey':'',
    'p5_team_logo':'',
    'p5_team_colors':'',
    'p5_team_name':'',

    'p6_chance_of_playing_next_round': '',
    'p6_chance_of_playing_this_round': '',
    'p6_cost_change_event': '',
    'p6_cost_change_event_fall': '',
    'p6_cost_change_start': '',
    'p6_cost_change_start_fall': '',
    'p6_dreamteam_count': '',
    'p6_element_type': '',
    'p6_event_points': '',
    'p6_first_name': '',
    'p6_form': '',
    'p6_player_id': '',
    'p6_in_dreamteam': '',
    'p6_now_cost': '',
    'p6_photo': '',
    'p6_points_per_game': '',
    'p6_second_name':'',
    'p6_selected_by_percent':'',
    'p6_special':'',
    'p6_squad_number':'',
    'p6_status':'',
    'p6_team':'',
    'p6_team_code':'',
    'p6_total_points':'',
    'p6_value_form':'',
    'p6_value_season':'',
    'p6_web_name':'',
    'p6_minutes':'',
    'p6_goals_scored':'',
    'p6_assists':'',
    'p6_clean_sheets':'',
    'p6_goals_conceded':'',
    'p6_own_goals':'',
    'p6_penalties_saved':'',
    'p6_penalties_missed':'',
    'p6_yellow_cards':'',
    'p6_red_cards':'',
    'p6_saves':'',
    'p6_bonus':'',
    'p6_bps':'',
    'p6_team_jersey':'',
    'p6_team_logo':'',
    'p6_team_colors':'',
    'p6_team_name':'',

    'p7_chance_of_playing_next_round': '',
    'p7_chance_of_playing_this_round': '',
    'p7_cost_change_event': '',
    'p7_cost_change_event_fall': '',
    'p7_cost_change_start': '',
    'p7_cost_change_start_fall': '',
    'p7_dreamteam_count': '',
    'p7_element_type': '',
    'p7_event_points': '',
    'p7_first_name': '',
    'p7_form': '',
    'p7_player_id': '',
    'p7_in_dreamteam': '',
    'p7_now_cost': '',
    'p7_photo': '',
    'p7_points_per_game': '',
    'p7_second_name':'',
    'p7_selected_by_percent':'',
    'p7_special':'',
    'p7_squad_number':'',
    'p7_status':'',
    'p7_team':'',
    'p7_team_code':'',
    'p7_total_points':'',
    'p7_value_form':'',
    'p7_value_season':'',
    'p7_web_name':'',
    'p7_minutes':'',
    'p7_goals_scored':'',
    'p7_assists':'',
    'p7_clean_sheets':'',
    'p7_goals_conceded':'',
    'p7_own_goals':'',
    'p7_penalties_saved':'',
    'p7_penalties_missed':'',
    'p7_yellow_cards':'',
    'p7_red_cards':'',
    'p7_saves':'',
    'p7_bonus':'',
    'p7_bps':'',
    'p7_team_jersey':'',
    'p7_team_logo':'',
    'p7_team_colors':'',
    'p7_team_name':'',

    'p8_chance_of_playing_next_round': '',
    'p8_chance_of_playing_this_round': '',
    'p8_cost_change_event': '',
    'p8_cost_change_event_fall': '',
    'p8_cost_change_start': '',
    'p8_cost_change_start_fall': '',
    'p8_dreamteam_count': '',
    'p8_element_type': '',
    'p8_event_points': '',
    'p8_first_name': '',
    'p8_form': '',
    'p8_player_id': '',
    'p8_in_dreamteam': '',
    'p8_now_cost': '',
    'p8_photo': '',
    'p8_points_per_game': '',
    'p8_second_name':'',
    'p8_selected_by_percent':'',
    'p8_special':'',
    'p8_squad_number':'',
    'p8_status':'',
    'p8_team':'',
    'p8_team_code':'',
    'p8_total_points':'',
    'p8_value_form':'',
    'p8_value_season':'',
    'p8_web_name':'',
    'p8_minutes':'',
    'p8_goals_scored':'',
    'p8_assists':'',
    'p8_clean_sheets':'',
    'p8_goals_conceded':'',
    'p8_own_goals':'',
    'p8_penalties_saved':'',
    'p8_penalties_missed':'',
    'p8_yellow_cards':'',
    'p8_red_cards':'',
    'p8_saves':'',
    'p8_bonus':'',
    'p8_bps':'',
    'p8_team_jersey':'',
    'p8_team_logo':'',
    'p8_team_colors':'',
    'p8_team_name':'',

    'p9_chance_of_playing_next_round': '',
    'p9_chance_of_playing_this_round': '',
    'p9_cost_change_event': '',
    'p9_cost_change_event_fall': '',
    'p9_cost_change_start': '',
    'p9_cost_change_start_fall': '',
    'p9_dreamteam_count': '',
    'p9_element_type': '',
    'p9_event_points': '',
    'p9_first_name': '',
    'p9_form': '',
    'p9_player_id': '',
    'p9_in_dreamteam': '',
    'p9_now_cost': '',
    'p9_photo': '',
    'p9_points_per_game': '',
    'p9_second_name':'',
    'p9_selected_by_percent':'',
    'p9_special':'',
    'p9_squad_number':'',
    'p9_status':'',
    'p9_team':'',
    'p9_team_code':'',
    'p9_total_points':'',
    'p9_value_form':'',
    'p9_value_season':'',
    'p9_web_name':'',
    'p9_minutes':'',
    'p9_goals_scored':'',
    'p9_assists':'',
    'p9_clean_sheets':'',
    'p9_goals_conceded':'',
    'p9_own_goals':'',
    'p9_penalties_saved':'',
    'p9_penalties_missed':'',
    'p9_yellow_cards':'',
    'p9_red_cards':'',
    'p9_saves':'',
    'p9_bonus':'',
    'p9_bps':'',
    'p9_team_jersey':'',
    'p9_team_logo':'',
    'p9_team_colors':'',
    'p9_team_name':'',

    'p10_chance_of_playing_next_round': '',
    'p10_chance_of_playing_this_round': '',
    'p10_cost_change_event': '',
    'p10_cost_change_event_fall': '',
    'p10_cost_change_start': '',
    'p10_cost_change_start_fall': '',
    'p10_dreamteam_count': '',
    'p10_element_type': '',
    'p10_event_points': '',
    'p10_first_name': '',
    'p10_form': '',
    'p10_player_id': '',
    'p10_in_dreamteam': '',
    'p10_now_cost': '',
    'p10_photo': '',
    'p10_points_per_game': '',
    'p10_second_name':'',
    'p10_selected_by_percent':'',
    'p10_special':'',
    'p10_squad_number':'',
    'p10_status':'',
    'p10_team':'',
    'p10_team_code':'',
    'p10_total_points':'',
    'p10_value_form':'',
    'p10_value_season':'',
    'p10_web_name':'',
    'p10_minutes':'',
    'p10_goals_scored':'',
    'p10_assists':'',
    'p10_clean_sheets':'',
    'p10_goals_conceded':'',
    'p10_own_goals':'',
    'p10_penalties_saved':'',
    'p10_penalties_missed':'',
    'p10_yellow_cards':'',
    'p10_red_cards':'',
    'p10_saves':'',
    'p10_bonus':'',
    'p10_bps':'',
    'p10_team_jersey':'',
    'p10_team_logo':'',
    'p10_team_colors':'',
    'p10_team_name':'',

    'p11_chance_of_playing_next_round': '',
    'p11_chance_of_playing_this_round': '',
    'p11_cost_change_event': '',
    'p11_cost_change_event_fall': '',
    'p11_cost_change_start': '',
    'p11_cost_change_start_fall': '',
    'p11_dreamteam_count': '',
    'p11_element_type': '',
    'p11_event_points': '',
    'p11_first_name': '',
    'p11_form': '',
    'p11_player_id': '',
    'p11_in_dreamteam': '',
    'p11_now_cost': '',
    'p11_photo': '',
    'p11_points_per_game': '',
    'p11_second_name':'',
    'p11_selected_by_percent':'',
    'p11_special':'',
    'p11_squad_number':'',
    'p11_status':'',
    'p11_team':'',
    'p11_team_code':'',
    'p11_total_points':'',
    'p11_value_form':'',
    'p11_value_season':'',
    'p11_web_name':'',
    'p11_minutes':'',
    'p11_goals_scored':'',
    'p11_assists':'',
    'p11_clean_sheets':'',
    'p11_goals_conceded':'',
    'p11_own_goals':'',
    'p11_penalties_saved':'',
    'p11_penalties_missed':'',
    'p11_yellow_cards':'',
    'p11_red_cards':'',
    'p11_saves':'',
    'p11_bonus':'',
    'p11_bps':'',
    'p11_team_jersey':'',
    'p11_team_logo':'',
    'p11_team_colors':'',
    'p11_team_name':'',

    'p12_chance_of_playing_next_round': '',
    'p12_chance_of_playing_this_round': '',
    'p12_cost_change_event': '',
    'p12_cost_change_event_fall': '',
    'p12_cost_change_start': '',
    'p12_cost_change_start_fall': '',
    'p12_dreamteam_count': '',
    'p12_element_type': '',
    'p12_event_points': '',
    'p12_first_name': '',
    'p12_form': '',
    'p12_player_id': '',
    'p12_in_dreamteam': '',
    'p12_now_cost': '',
    'p12_photo': '',
    'p12_points_per_game': '',
    'p12_second_name':'',
    'p12_selected_by_percent':'',
    'p12_special':'',
    'p12_squad_number':'',
    'p12_status':'',
    'p12_team':'',
    'p12_team_code':'',
    'p12_total_points':'',
    'p12_value_form':'',
    'p12_value_season':'',
    'p12_web_name':'',
    'p12_minutes':'',
    'p12_goals_scored':'',
    'p12_assists':'',
    'p12_clean_sheets':'',
    'p12_goals_conceded':'',
    'p12_own_goals':'',
    'p12_penalties_saved':'',
    'p12_penalties_missed':'',
    'p12_yellow_cards':'',
    'p12_red_cards':'',
    'p12_saves':'',
    'p12_bonus':'',
    'p12_bps':'',
    'p12_team_jersey':'',
    'p12_team_logo':'',
    'p12_team_colors':'',
    'p12_team_name':'',

    'p13_chance_of_playing_next_round': '',
    'p13_chance_of_playing_this_round': '',
    'p13_cost_change_event': '',
    'p13_cost_change_event_fall': '',
    'p13_cost_change_start': '',
    'p13_cost_change_start_fall': '',
    'p13_dreamteam_count': '',
    'p13_element_type': '',
    'p13_event_points': '',
    'p13_first_name': '',
    'p13_form': '',
    'p13_player_id': '',
    'p13_in_dreamteam': '',
    'p13_now_cost': '',
    'p13_photo': '',
    'p13_points_per_game': '',
    'p13_second_name':'',
    'p13_selected_by_percent':'',
    'p13_special':'',
    'p13_squad_number':'',
    'p13_status':'',
    'p13_team':'',
    'p13_team_code':'',
    'p13_total_points':'',
    'p13_value_form':'',
    'p13_value_season':'',
    'p13_web_name':'',
    'p13_minutes':'',
    'p13_goals_scored':'',
    'p13_assists':'',
    'p13_clean_sheets':'',
    'p13_goals_conceded':'',
    'p13_own_goals':'',
    'p13_penalties_saved':'',
    'p13_penalties_missed':'',
    'p13_yellow_cards':'',
    'p13_red_cards':'',
    'p13_saves':'',
    'p13_bonus':'',
    'p13_bps':'',
    'p13_team_jersey':'',
    'p13_team_logo':'',
    'p13_team_colors':'',
    'p13_team_name':'',

    'p14_chance_of_playing_next_round': '',
    'p14_chance_of_playing_this_round': '',
    'p14_cost_change_event': '',
    'p14_cost_change_event_fall': '',
    'p14_cost_change_start': '',
    'p14_cost_change_start_fall': '',
    'p14_dreamteam_count': '',
    'p14_element_type': '',
    'p14_event_points': '',
    'p14_first_name': '',
    'p14_form': '',
    'p14_player_id': '',
    'p14_in_dreamteam': '',
    'p14_now_cost': '',
    'p14_photo': '',
    'p14_points_per_game': '',
    'p14_second_name':'',
    'p14_selected_by_percent':'',
    'p14_special':'',
    'p14_squad_number':'',
    'p14_status':'',
    'p14_team':'',
    'p14_team_code':'',
    'p14_total_points':'',
    'p14_value_form':'',
    'p14_value_season':'',
    'p14_web_name':'',
    'p14_minutes':'',
    'p14_goals_scored':'',
    'p14_assists':'',
    'p14_clean_sheets':'',
    'p14_goals_conceded':'',
    'p14_own_goals':'',
    'p14_penalties_saved':'',
    'p14_penalties_missed':'',
    'p14_yellow_cards':'',
    'p14_red_cards':'',
    'p14_saves':'',
    'p14_bonus':'',
    'p14_bps':'',
    'p14_team_jersey':'',
    'p14_team_logo':'',
    'p14_team_colors':'',
    'p14_team_name':'',

    'p15_chance_of_playing_next_round': '',
    'p15_chance_of_playing_this_round': '',
    'p15_cost_change_event': '',
    'p15_cost_change_event_fall': '',
    'p15_cost_change_start': '',
    'p15_cost_change_start_fall': '',
    'p15_dreamteam_count': '',
    'p15_element_type': '',
    'p15_event_points': '',
    'p15_first_name': '',
    'p15_form': '',
    'p15_player_id': '',
    'p15_in_dreamteam': '',
    'p15_now_cost': '',
    'p15_photo': '',
    'p15_points_per_game': '',
    'p15_second_name':'',
    'p15_selected_by_percent':'',
    'p15_special':'',
    'p15_squad_number':'',
    'p15_status':'',
    'p15_team':'',
    'p15_team_code':'',
    'p15_total_points':'',
    'p15_value_form':'',
    'p15_value_season':'',
    'p15_web_name':'',
    'p15_minutes':'',
    'p15_goals_scored':'',
    'p15_assists':'',
    'p15_clean_sheets':'',
    'p15_goals_conceded':'',
    'p15_own_goals':'',
    'p15_penalties_saved':'',
    'p15_penalties_missed':'',
    'p15_yellow_cards':'',
    'p15_red_cards':'',
    'p15_saves':'',
    'p15_bonus':'',
    'p15_bps':'',
    'p15_team_jersey':'',
    'p15_team_logo':'',
    'p15_team_colors':'',
    'p15_team_name':'',

    'roster': [],
    'leagues': [],
    'transfers': {
        'cost': '',
        'made': '',
        'bank': '',
        'value': ''
    },
    'gameweek': ''
}

# put all the functions together and differnet data pieces of the endpoints to create a user's profile
# import this method to app.py
def create_profile(email, password, team_id):
    team['picks'] = get_users_basic_team(email, password, team_id)
    team['player_data'] = get_all_footballers()
    team['personal_data'] = get_users_personal_info(team_id)

    # get the user's leagues
    for league in team['personal_data']['leagues']['classic']:
        # this league is the user's classic league
        if league['league_type'] == 'x':
            classic_id = league['id']
            team['classic_league'] = get_classic_league(classic_id)
            user_profile['leagues'].append(league)

    # these leagues are general leagues
    for league in team['personal_data']['leagues']['classic']:
        if league['name'] == 'Overall' or league['name'] == 'NBC Sports League':
            user_profile['leagues'].append(league)

    # user's personal info
    user_profile['team_name'] = team['personal_data']['name']

    for team_details in team['team_info']:
        if team['personal_data']['favourite_team'] == team_details['id']:
            user_profile['fav_team'] = team_details['name']
            user_profile['fav_team_id'] = team_details['id']
            user_profile['fav_team_logo'] = team_details['logo']
            user_profile['fav_team_colors'] = team_details['colors']
            user_profile['fav_team_jersey'] = team_details['jersey']
            user_profile['fav_team_jersey_goal'] = team_details['jersey_goal']
            user_profile['overall_points'] = team['personal_data']['summary_overall_points']
            user_profile['overall_rank'] = team['personal_data']['summary_overall_rank']
            user_profile['gameweek_points'] = team['personal_data']['summary_event_points']
            user_profile['gameweek_rank'] = team['personal_data']['summary_event_rank']
            for league in team['personal_data']['leagues']['classic']:
                if league['league_type'] == 'x':
                    user_profile['classic_league_id'] = league['id']
                    user_profile['classic_league_name'] = league['name']
                    user_profile['classic_league_rank'] = league['entry_rank']
                    user_profile['classic_league_rank_previous'] = league['entry_last_rank']

    # checking player transfer status
    user_profile['transfers']['cost'] = team['picks']['transfers']['cost']
    user_profile['transfers']['made'] = team['picks']['transfers']['made']
    user_profile['transfers']['bank'] = team['picks']['transfers']['bank']
    user_profile['transfers']['value'] = team['picks']['transfers']['value']

    # user's player picks info
    for users_pick in team['picks']['picks']:
        for player in team['player_data']['elements']:

            # users pick position 1
            if users_pick['element'] == player['id'] and users_pick['position'] == 1:
                user_profile['p1_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p1_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p1_cost_change_event'] = player['cost_change_event']
                user_profile['p1_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p1_cost_change_start'] = player['cost_change_start']
                user_profile['p1_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p1_dreamteam_count'] = player['dreamteam_count']
                user_profile['p1_element_type'] = player['element_type']
                user_profile['p1_event_points'] = player['event_points']
                user_profile['p1_first_name'] = player['first_name']
                user_profile['p1_form'] = player['form']
                user_profile['p1_player_id'] = player['id']
                user_profile['p1_in_dreamteam'] = player['in_dreamteam']
                user_profile['p1_now_cost'] = player['now_cost']
                user_profile['p1_photo'] = player['photo']
                user_profile['p1_points_per_game'] = player['points_per_game']
                user_profile['p1_second_name'] = player['second_name']
                user_profile['p1_selected_by_percent'] = player['now_cost']
                user_profile['p1_special'] = player['special']
                user_profile['p1_squad_number'] = player['squad_number']
                user_profile['p1_status'] = player['status']
                user_profile['p1_team'] = player['team']
                user_profile['p1_team_code'] = player['team_code']
                user_profile['p1_total_points'] = player['total_points']
                user_profile['p1_value_form'] = player['value_form']
                user_profile['p1_value_season'] = player['value_season']
                user_profile['p1_web_name'] = player['web_name']
                user_profile['p1_minutes'] = player['minutes']
                user_profile['p1_goals_scored'] = player['goals_scored']
                user_profile['p1_assists'] = player['assists']
                user_profile['p1_clean_sheets'] = player['clean_sheets']
                user_profile['p1_goals_conceded'] = player['goals_conceded']
                user_profile['p1_own_goals'] = player['own_goals']
                user_profile['p1_penalties_saved'] = player['penalties_saved']
                user_profile['p1_penalties_missed'] = player['penalties_missed']
                user_profile['p1_yellow_cards'] = player['yellow_cards']
                user_profile['p1_red_cards'] = player['red_cards']
                user_profile['p1_saves'] = player['saves']
                user_profile['p1_bonus'] = player['bonus']
                user_profile['p1_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p1_team_jersey'] = team_details['jersey_goal']
                        user_profile['p1_team_logo'] = team_details['logo']
                        user_profile['p1_team_colors'] = team_details['colors']
                        user_profile['p1_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 2
            if users_pick['element'] == player['id'] and users_pick['position'] == 2:
                user_profile['p2_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p2_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p2_cost_change_event'] = player['cost_change_event']
                user_profile['p2_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p2_cost_change_start'] = player['cost_change_start']
                user_profile['p2_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p2_dreamteam_count'] = player['dreamteam_count']
                user_profile['p2_element_type'] = player['element_type']
                user_profile['p2_event_points'] = player['event_points']
                user_profile['p2_first_name'] = player['first_name']
                user_profile['p2_form'] = player['form']
                user_profile['p2_player_id'] = player['id']
                user_profile['p2_in_dreamteam'] = player['in_dreamteam']
                user_profile['p2_now_cost'] = player['now_cost']
                user_profile['p2_photo'] = player['photo']
                user_profile['p2_points_per_game'] = player['points_per_game']
                user_profile['p2_second_name'] = player['second_name']
                user_profile['p2_selected_by_percent'] = player['now_cost']
                user_profile['p2_special'] = player['special']
                user_profile['p2_squad_number'] = player['squad_number']
                user_profile['p2_status'] = player['status']
                user_profile['p2_team'] = player['team']
                user_profile['p2_team_code'] = player['team_code']
                user_profile['p2_total_points'] = player['total_points']
                user_profile['p2_value_form'] = player['value_form']
                user_profile['p2_value_season'] = player['value_season']
                user_profile['p2_web_name'] = player['web_name']
                user_profile['p2_minutes'] = player['minutes']
                user_profile['p2_goals_scored'] = player['goals_scored']
                user_profile['p2_assists'] = player['assists']
                user_profile['p2_clean_sheets'] = player['clean_sheets']
                user_profile['p2_goals_conceded'] = player['goals_conceded']
                user_profile['p2_own_goals'] = player['own_goals']
                user_profile['p2_penalties_saved'] = player['penalties_saved']
                user_profile['p2_penalties_missed'] = player['penalties_missed']
                user_profile['p2_yellow_cards'] = player['yellow_cards']
                user_profile['p2_red_cards'] = player['red_cards']
                user_profile['p2_saves'] = player['saves']
                user_profile['p2_bonus'] = player['bonus']
                user_profile['p2_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p2_team_jersey'] = team_details['jersey']
                        user_profile['p2_team_logo'] = team_details['logo']
                        user_profile['p2_team_colors'] = team_details['colors']
                        user_profile['p2_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 3
            if users_pick['element'] == player['id'] and users_pick['position'] == 3:
                user_profile['p3_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p3_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p3_cost_change_event'] = player['cost_change_event']
                user_profile['p3_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p3_cost_change_start'] = player['cost_change_start']
                user_profile['p3_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p3_dreamteam_count'] = player['dreamteam_count']
                user_profile['p3_element_type'] = player['element_type']
                user_profile['p3_event_points'] = player['event_points']
                user_profile['p3_first_name'] = player['first_name']
                user_profile['p3_form'] = player['form']
                user_profile['p3_player_id'] = player['id']
                user_profile['p3_in_dreamteam'] = player['in_dreamteam']
                user_profile['p3_now_cost'] = player['now_cost']
                user_profile['p3_photo'] = player['photo']
                user_profile['p3_points_per_game'] = player['points_per_game']
                user_profile['p3_second_name'] = player['second_name']
                user_profile['p3_selected_by_percent'] = player['now_cost']
                user_profile['p3_special'] = player['special']
                user_profile['p3_squad_number'] = player['squad_number']
                user_profile['p3_status'] = player['status']
                user_profile['p3_team'] = player['team']
                user_profile['p3_team_code'] = player['team_code']
                user_profile['p3_total_points'] = player['total_points']
                user_profile['p3_value_form'] = player['value_form']
                user_profile['p3_value_season'] = player['value_season']
                user_profile['p3_web_name'] = player['web_name']
                user_profile['p3_minutes'] = player['minutes']
                user_profile['p3_goals_scored'] = player['goals_scored']
                user_profile['p3_assists'] = player['assists']
                user_profile['p3_clean_sheets'] = player['clean_sheets']
                user_profile['p3_goals_conceded'] = player['goals_conceded']
                user_profile['p3_own_goals'] = player['own_goals']
                user_profile['p3_penalties_saved'] = player['penalties_saved']
                user_profile['p3_penalties_missed'] = player['penalties_missed']
                user_profile['p3_yellow_cards'] = player['yellow_cards']
                user_profile['p3_red_cards'] = player['red_cards']
                user_profile['p3_saves'] = player['saves']
                user_profile['p3_bonus'] = player['bonus']
                user_profile['p3_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p3_team_jersey'] = team_details['jersey']
                        user_profile['p3_team_logo'] = team_details['logo']
                        user_profile['p3_team_colors'] = team_details['colors']
                        user_profile['p3_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 4
            if users_pick['element'] == player['id'] and users_pick['position'] == 4:
                user_profile['p4_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p4_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p4_cost_change_event'] = player['cost_change_event']
                user_profile['p4_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p4_cost_change_start'] = player['cost_change_start']
                user_profile['p4_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p4_dreamteam_count'] = player['dreamteam_count']
                user_profile['p4_element_type'] = player['element_type']
                user_profile['p4_event_points'] = player['event_points']
                user_profile['p4_first_name'] = player['first_name']
                user_profile['p4_form'] = player['form']
                user_profile['p4_player_id'] = player['id']
                user_profile['p4_in_dreamteam'] = player['in_dreamteam']
                user_profile['p4_now_cost'] = player['now_cost']
                user_profile['p4_photo'] = player['photo']
                user_profile['p4_points_per_game'] = player['points_per_game']
                user_profile['p4_second_name'] = player['second_name']
                user_profile['p4_selected_by_percent'] = player['now_cost']
                user_profile['p4_special'] = player['special']
                user_profile['p4_squad_number'] = player['squad_number']
                user_profile['p4_status'] = player['status']
                user_profile['p4_team'] = player['team']
                user_profile['p4_team_code'] = player['team_code']
                user_profile['p4_total_points'] = player['total_points']
                user_profile['p4_value_form'] = player['value_form']
                user_profile['p4_value_season'] = player['value_season']
                user_profile['p4_web_name'] = player['web_name']
                user_profile['p4_minutes'] = player['minutes']
                user_profile['p4_goals_scored'] = player['goals_scored']
                user_profile['p4_assists'] = player['assists']
                user_profile['p4_clean_sheets'] = player['clean_sheets']
                user_profile['p4_goals_conceded'] = player['goals_conceded']
                user_profile['p4_own_goals'] = player['own_goals']
                user_profile['p4_penalties_saved'] = player['penalties_saved']
                user_profile['p4_penalties_missed'] = player['penalties_missed']
                user_profile['p4_yellow_cards'] = player['yellow_cards']
                user_profile['p4_red_cards'] = player['red_cards']
                user_profile['p4_saves'] = player['saves']
                user_profile['p4_bonus'] = player['bonus']
                user_profile['p4_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p4_team_jersey'] = team_details['jersey']
                        user_profile['p4_team_logo'] = team_details['logo']
                        user_profile['p4_team_colors'] = team_details['colors']
                        user_profile['p4_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 5
            if users_pick['element'] == player['id'] and users_pick['position'] == 5:
                user_profile['p5_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p5_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p5_cost_change_event'] = player['cost_change_event']
                user_profile['p5_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p5_cost_change_start'] = player['cost_change_start']
                user_profile['p5_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p5_dreamteam_count'] = player['dreamteam_count']
                user_profile['p5_element_type'] = player['element_type']
                user_profile['p5_event_points'] = player['event_points']
                user_profile['p5_first_name'] = player['first_name']
                user_profile['p5_form'] = player['form']
                user_profile['p5_player_id'] = player['id']
                user_profile['p5_in_dreamteam'] = player['in_dreamteam']
                user_profile['p5_now_cost'] = player['now_cost']
                user_profile['p5_photo'] = player['photo']
                user_profile['p5_points_per_game'] = player['points_per_game']
                user_profile['p5_second_name'] = player['second_name']
                user_profile['p5_selected_by_percent'] = player['now_cost']
                user_profile['p5_special'] = player['special']
                user_profile['p5_squad_number'] = player['squad_number']
                user_profile['p5_status'] = player['status']
                user_profile['p5_team'] = player['team']
                user_profile['p5_team_code'] = player['team_code']
                user_profile['p5_total_points'] = player['total_points']
                user_profile['p5_value_form'] = player['value_form']
                user_profile['p5_value_season'] = player['value_season']
                user_profile['p5_web_name'] = player['web_name']
                user_profile['p5_minutes'] = player['minutes']
                user_profile['p5_goals_scored'] = player['goals_scored']
                user_profile['p5_assists'] = player['assists']
                user_profile['p5_clean_sheets'] = player['clean_sheets']
                user_profile['p5_goals_conceded'] = player['goals_conceded']
                user_profile['p5_own_goals'] = player['own_goals']
                user_profile['p5_penalties_saved'] = player['penalties_saved']
                user_profile['p5_penalties_missed'] = player['penalties_missed']
                user_profile['p5_yellow_cards'] = player['yellow_cards']
                user_profile['p5_red_cards'] = player['red_cards']
                user_profile['p5_saves'] = player['saves']
                user_profile['p5_bonus'] = player['bonus']
                user_profile['p5_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p5_team_jersey'] = team_details['jersey']
                        user_profile['p5_team_logo'] = team_details['logo']
                        user_profile['p5_team_colors'] = team_details['colors']
                        user_profile['p5_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 6
            if users_pick['element'] == player['id'] and users_pick['position'] == 6:
                user_profile['p6_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p6_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p6_cost_change_event'] = player['cost_change_event']
                user_profile['p6_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p6_cost_change_start'] = player['cost_change_start']
                user_profile['p6_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p6_dreamteam_count'] = player['dreamteam_count']
                user_profile['p6_element_type'] = player['element_type']
                user_profile['p6_event_points'] = player['event_points']
                user_profile['p6_first_name'] = player['first_name']
                user_profile['p6_form'] = player['form']
                user_profile['p6_player_id'] = player['id']
                user_profile['p6_in_dreamteam'] = player['in_dreamteam']
                user_profile['p6_now_cost'] = player['now_cost']
                user_profile['p6_photo'] = player['photo']
                user_profile['p6_points_per_game'] = player['points_per_game']
                user_profile['p6_second_name'] = player['second_name']
                user_profile['p6_selected_by_percent'] = player['now_cost']
                user_profile['p6_special'] = player['special']
                user_profile['p6_squad_number'] = player['squad_number']
                user_profile['p6_status'] = player['status']
                user_profile['p6_team'] = player['team']
                user_profile['p6_team_code'] = player['team_code']
                user_profile['p6_total_points'] = player['total_points']
                user_profile['p6_value_form'] = player['value_form']
                user_profile['p6_value_season'] = player['value_season']
                user_profile['p6_web_name'] = player['web_name']
                user_profile['p6_minutes'] = player['minutes']
                user_profile['p6_goals_scored'] = player['goals_scored']
                user_profile['p6_assists'] = player['assists']
                user_profile['p6_clean_sheets'] = player['clean_sheets']
                user_profile['p6_goals_conceded'] = player['goals_conceded']
                user_profile['p6_own_goals'] = player['own_goals']
                user_profile['p6_penalties_saved'] = player['penalties_saved']
                user_profile['p6_penalties_missed'] = player['penalties_missed']
                user_profile['p6_yellow_cards'] = player['yellow_cards']
                user_profile['p6_red_cards'] = player['red_cards']
                user_profile['p6_saves'] = player['saves']
                user_profile['p6_bonus'] = player['bonus']
                user_profile['p6_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p6_team_jersey'] = team_details['jersey']
                        user_profile['p6_team_logo'] = team_details['logo']
                        user_profile['p6_team_colors'] = team_details['colors']
                        user_profile['p6_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 7
            if users_pick['element'] == player['id'] and users_pick['position'] == 7:
                user_profile['p7_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p7_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p7_cost_change_event'] = player['cost_change_event']
                user_profile['p7_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p7_cost_change_start'] = player['cost_change_start']
                user_profile['p7_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p7_dreamteam_count'] = player['dreamteam_count']
                user_profile['p7_element_type'] = player['element_type']
                user_profile['p7_event_points'] = player['event_points']
                user_profile['p7_first_name'] = player['first_name']
                user_profile['p7_form'] = player['form']
                user_profile['p7_player_id'] = player['id']
                user_profile['p7_in_dreamteam'] = player['in_dreamteam']
                user_profile['p7_now_cost'] = player['now_cost']
                user_profile['p7_photo'] = player['photo']
                user_profile['p7_points_per_game'] = player['points_per_game']
                user_profile['p7_second_name'] = player['second_name']
                user_profile['p7_selected_by_percent'] = player['now_cost']
                user_profile['p7_special'] = player['special']
                user_profile['p7_squad_number'] = player['squad_number']
                user_profile['p7_status'] = player['status']
                user_profile['p7_team'] = player['team']
                user_profile['p7_team_code'] = player['team_code']
                user_profile['p7_total_points'] = player['total_points']
                user_profile['p7_value_form'] = player['value_form']
                user_profile['p7_value_season'] = player['value_season']
                user_profile['p7_web_name'] = player['web_name']
                user_profile['p7_minutes'] = player['minutes']
                user_profile['p7_goals_scored'] = player['goals_scored']
                user_profile['p7_assists'] = player['assists']
                user_profile['p7_clean_sheets'] = player['clean_sheets']
                user_profile['p7_goals_conceded'] = player['goals_conceded']
                user_profile['p7_own_goals'] = player['own_goals']
                user_profile['p7_penalties_saved'] = player['penalties_saved']
                user_profile['p7_penalties_missed'] = player['penalties_missed']
                user_profile['p7_yellow_cards'] = player['yellow_cards']
                user_profile['p7_red_cards'] = player['red_cards']
                user_profile['p7_saves'] = player['saves']
                user_profile['p7_bonus'] = player['bonus']
                user_profile['p7_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p7_team_jersey'] = team_details['jersey']
                        user_profile['p7_team_logo'] = team_details['logo']
                        user_profile['p7_team_colors'] = team_details['colors']
                        user_profile['p7_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 8
            if users_pick['element'] == player['id'] and users_pick['position'] == 8:
                user_profile['p8_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p8_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p8_cost_change_event'] = player['cost_change_event']
                user_profile['p8_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p8_cost_change_start'] = player['cost_change_start']
                user_profile['p8_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p8_dreamteam_count'] = player['dreamteam_count']
                user_profile['p8_element_type'] = player['element_type']
                user_profile['p8_event_points'] = player['event_points']
                user_profile['p8_first_name'] = player['first_name']
                user_profile['p8_form'] = player['form']
                user_profile['p8_player_id'] = player['id']
                user_profile['p8_in_dreamteam'] = player['in_dreamteam']
                user_profile['p8_now_cost'] = player['now_cost']
                user_profile['p8_photo'] = player['photo']
                user_profile['p8_points_per_game'] = player['points_per_game']
                user_profile['p8_second_name'] = player['second_name']
                user_profile['p8_selected_by_percent'] = player['now_cost']
                user_profile['p8_special'] = player['special']
                user_profile['p8_squad_number'] = player['squad_number']
                user_profile['p8_status'] = player['status']
                user_profile['p8_team'] = player['team']
                user_profile['p8_team_code'] = player['team_code']
                user_profile['p8_total_points'] = player['total_points']
                user_profile['p8_value_form'] = player['value_form']
                user_profile['p8_value_season'] = player['value_season']
                user_profile['p8_web_name'] = player['web_name']
                user_profile['p8_minutes'] = player['minutes']
                user_profile['p8_goals_scored'] = player['goals_scored']
                user_profile['p8_assists'] = player['assists']
                user_profile['p8_clean_sheets'] = player['clean_sheets']
                user_profile['p8_goals_conceded'] = player['goals_conceded']
                user_profile['p8_own_goals'] = player['own_goals']
                user_profile['p8_penalties_saved'] = player['penalties_saved']
                user_profile['p8_penalties_missed'] = player['penalties_missed']
                user_profile['p8_yellow_cards'] = player['yellow_cards']
                user_profile['p8_red_cards'] = player['red_cards']
                user_profile['p8_saves'] = player['saves']
                user_profile['p8_bonus'] = player['bonus']
                user_profile['p8_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p8_team_jersey'] = team_details['jersey']
                        user_profile['p8_team_logo'] = team_details['logo']
                        user_profile['p8_team_colors'] = team_details['colors']
                        user_profile['p8_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 9
            if users_pick['element'] == player['id'] and users_pick['position'] == 9:
                user_profile['p9_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p9_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p9_cost_change_event'] = player['cost_change_event']
                user_profile['p9_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p9_cost_change_start'] = player['cost_change_start']
                user_profile['p9_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p9_dreamteam_count'] = player['dreamteam_count']
                user_profile['p9_element_type'] = player['element_type']
                user_profile['p9_event_points'] = player['event_points']
                user_profile['p9_first_name'] = player['first_name']
                user_profile['p9_form'] = player['form']
                user_profile['p9_player_id'] = player['id']
                user_profile['p9_in_dreamteam'] = player['in_dreamteam']
                user_profile['p9_now_cost'] = player['now_cost']
                user_profile['p9_photo'] = player['photo']
                user_profile['p9_points_per_game'] = player['points_per_game']
                user_profile['p9_second_name'] = player['second_name']
                user_profile['p9_selected_by_percent'] = player['now_cost']
                user_profile['p9_special'] = player['special']
                user_profile['p9_squad_number'] = player['squad_number']
                user_profile['p9_status'] = player['status']
                user_profile['p9_team'] = player['team']
                user_profile['p9_team_code'] = player['team_code']
                user_profile['p9_total_points'] = player['total_points']
                user_profile['p9_value_form'] = player['value_form']
                user_profile['p9_value_season'] = player['value_season']
                user_profile['p9_web_name'] = player['web_name']
                user_profile['p9_minutes'] = player['minutes']
                user_profile['p9_goals_scored'] = player['goals_scored']
                user_profile['p9_assists'] = player['assists']
                user_profile['p9_clean_sheets'] = player['clean_sheets']
                user_profile['p9_goals_conceded'] = player['goals_conceded']
                user_profile['p9_own_goals'] = player['own_goals']
                user_profile['p9_penalties_saved'] = player['penalties_saved']
                user_profile['p9_penalties_missed'] = player['penalties_missed']
                user_profile['p9_yellow_cards'] = player['yellow_cards']
                user_profile['p9_red_cards'] = player['red_cards']
                user_profile['p9_saves'] = player['saves']
                user_profile['p9_bonus'] = player['bonus']
                user_profile['p9_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p9_team_jersey'] = team_details['jersey']
                        user_profile['p9_team_logo'] = team_details['logo']
                        user_profile['p9_team_colors'] = team_details['colors']
                        user_profile['p9_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 10
            if users_pick['element'] == player['id'] and users_pick['position'] == 10:
                user_profile['p10_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p10_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p10_cost_change_event'] = player['cost_change_event']
                user_profile['p10_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p10_cost_change_start'] = player['cost_change_start']
                user_profile['p10_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p10_dreamteam_count'] = player['dreamteam_count']
                user_profile['p10_element_type'] = player['element_type']
                user_profile['p10_event_points'] = player['event_points']
                user_profile['p10_first_name'] = player['first_name']
                user_profile['p10_form'] = player['form']
                user_profile['p10_player_id'] = player['id']
                user_profile['p10_in_dreamteam'] = player['in_dreamteam']
                user_profile['p10_now_cost'] = player['now_cost']
                user_profile['p10_photo'] = player['photo']
                user_profile['p10_points_per_game'] = player['points_per_game']
                user_profile['p10_second_name'] = player['second_name']
                user_profile['p10_selected_by_percent'] = player['now_cost']
                user_profile['p10_special'] = player['special']
                user_profile['p10_squad_number'] = player['squad_number']
                user_profile['p10_status'] = player['status']
                user_profile['p10_team'] = player['team']
                user_profile['p10_team_code'] = player['team_code']
                user_profile['p10_total_points'] = player['total_points']
                user_profile['p10_value_form'] = player['value_form']
                user_profile['p10_value_season'] = player['value_season']
                user_profile['p10_web_name'] = player['web_name']
                user_profile['p10_minutes'] = player['minutes']
                user_profile['p10_goals_scored'] = player['goals_scored']
                user_profile['p10_assists'] = player['assists']
                user_profile['p10_clean_sheets'] = player['clean_sheets']
                user_profile['p10_goals_conceded'] = player['goals_conceded']
                user_profile['p10_own_goals'] = player['own_goals']
                user_profile['p10_penalties_saved'] = player['penalties_saved']
                user_profile['p10_penalties_missed'] = player['penalties_missed']
                user_profile['p10_yellow_cards'] = player['yellow_cards']
                user_profile['p10_red_cards'] = player['red_cards']
                user_profile['p10_saves'] = player['saves']
                user_profile['p10_bonus'] = player['bonus']
                user_profile['p10_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p10_team_jersey'] = team_details['jersey']
                        user_profile['p10_team_logo'] = team_details['logo']
                        user_profile['p10_team_colors'] = team_details['colors']
                        user_profile['p10_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 11
            if users_pick['element'] == player['id'] and users_pick['position'] == 11:
                user_profile['p11_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p11_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p11_cost_change_event'] = player['cost_change_event']
                user_profile['p11_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p11_cost_change_start'] = player['cost_change_start']
                user_profile['p11_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p11_dreamteam_count'] = player['dreamteam_count']
                user_profile['p11_element_type'] = player['element_type']
                user_profile['p11_event_points'] = player['event_points']
                user_profile['p11_first_name'] = player['first_name']
                user_profile['p11_form'] = player['form']
                user_profile['p11_player_id'] = player['id']
                user_profile['p11_in_dreamteam'] = player['in_dreamteam']
                user_profile['p11_now_cost'] = player['now_cost']
                user_profile['p11_photo'] = player['photo']
                user_profile['p11_points_per_game'] = player['points_per_game']
                user_profile['p11_second_name'] = player['second_name']
                user_profile['p11_selected_by_percent'] = player['now_cost']
                user_profile['p11_special'] = player['special']
                user_profile['p11_squad_number'] = player['squad_number']
                user_profile['p11_status'] = player['status']
                user_profile['p11_team'] = player['team']
                user_profile['p11_team_code'] = player['team_code']
                user_profile['p11_total_points'] = player['total_points']
                user_profile['p11_value_form'] = player['value_form']
                user_profile['p11_value_season'] = player['value_season']
                user_profile['p11_web_name'] = player['web_name']
                user_profile['p11_minutes'] = player['minutes']
                user_profile['p11_goals_scored'] = player['goals_scored']
                user_profile['p11_assists'] = player['assists']
                user_profile['p11_clean_sheets'] = player['clean_sheets']
                user_profile['p11_goals_conceded'] = player['goals_conceded']
                user_profile['p11_own_goals'] = player['own_goals']
                user_profile['p11_penalties_saved'] = player['penalties_saved']
                user_profile['p11_penalties_missed'] = player['penalties_missed']
                user_profile['p11_yellow_cards'] = player['yellow_cards']
                user_profile['p11_red_cards'] = player['red_cards']
                user_profile['p11_saves'] = player['saves']
                user_profile['p11_bonus'] = player['bonus']
                user_profile['p11_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p11_team_jersey'] = team_details['jersey']
                        user_profile['p11_team_logo'] = team_details['logo']
                        user_profile['p11_team_colors'] = team_details['colors']
                        user_profile['p11_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 12
            if users_pick['element'] == player['id'] and users_pick['position'] == 12:
                user_profile['p12_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p12_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p12_cost_change_event'] = player['cost_change_event']
                user_profile['p12_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p12_cost_change_start'] = player['cost_change_start']
                user_profile['p12_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p12_dreamteam_count'] = player['dreamteam_count']
                user_profile['p12_element_type'] = player['element_type']
                user_profile['p12_event_points'] = player['event_points']
                user_profile['p12_first_name'] = player['first_name']
                user_profile['p12_form'] = player['form']
                user_profile['p12_player_id'] = player['id']
                user_profile['p12_in_dreamteam'] = player['in_dreamteam']
                user_profile['p12_now_cost'] = player['now_cost']
                user_profile['p12_photo'] = player['photo']
                user_profile['p12_points_per_game'] = player['points_per_game']
                user_profile['p12_second_name'] = player['second_name']
                user_profile['p12_selected_by_percent'] = player['now_cost']
                user_profile['p12_special'] = player['special']
                user_profile['p12_squad_number'] = player['squad_number']
                user_profile['p12_status'] = player['status']
                user_profile['p12_team'] = player['team']
                user_profile['p12_team_code'] = player['team_code']
                user_profile['p12_total_points'] = player['total_points']
                user_profile['p12_value_form'] = player['value_form']
                user_profile['p12_value_season'] = player['value_season']
                user_profile['p12_web_name'] = player['web_name']
                user_profile['p12_minutes'] = player['minutes']
                user_profile['p12_goals_scored'] = player['goals_scored']
                user_profile['p12_assists'] = player['assists']
                user_profile['p12_clean_sheets'] = player['clean_sheets']
                user_profile['p12_goals_conceded'] = player['goals_conceded']
                user_profile['p12_own_goals'] = player['own_goals']
                user_profile['p12_penalties_saved'] = player['penalties_saved']
                user_profile['p12_penalties_missed'] = player['penalties_missed']
                user_profile['p12_yellow_cards'] = player['yellow_cards']
                user_profile['p12_red_cards'] = player['red_cards']
                user_profile['p12_saves'] = player['saves']
                user_profile['p12_bonus'] = player['bonus']
                user_profile['p12_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p12_team_jersey'] = team_details['jersey_goal']
                        user_profile['p12_team_logo'] = team_details['logo']
                        user_profile['p12_team_colors'] = team_details['colors']
                        user_profile['p12_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 13
            if users_pick['element'] == player['id'] and users_pick['position'] == 13:
                user_profile['p13_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p13_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p13_cost_change_event'] = player['cost_change_event']
                user_profile['p13_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p13_cost_change_start'] = player['cost_change_start']
                user_profile['p13_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p13_dreamteam_count'] = player['dreamteam_count']
                user_profile['p13_element_type'] = player['element_type']
                user_profile['p13_event_points'] = player['event_points']
                user_profile['p13_first_name'] = player['first_name']
                user_profile['p13_form'] = player['form']
                user_profile['p13_player_id'] = player['id']
                user_profile['p13_in_dreamteam'] = player['in_dreamteam']
                user_profile['p13_now_cost'] = player['now_cost']
                user_profile['p13_photo'] = player['photo']
                user_profile['p13_points_per_game'] = player['points_per_game']
                user_profile['p13_second_name'] = player['second_name']
                user_profile['p13_selected_by_percent'] = player['now_cost']
                user_profile['p13_special'] = player['special']
                user_profile['p13_squad_number'] = player['squad_number']
                user_profile['p13_status'] = player['status']
                user_profile['p13_team'] = player['team']
                user_profile['p13_team_code'] = player['team_code']
                user_profile['p13_total_points'] = player['total_points']
                user_profile['p13_value_form'] = player['value_form']
                user_profile['p13_value_season'] = player['value_season']
                user_profile['p13_web_name'] = player['web_name']
                user_profile['p13_minutes'] = player['minutes']
                user_profile['p13_goals_scored'] = player['goals_scored']
                user_profile['p13_assists'] = player['assists']
                user_profile['p13_clean_sheets'] = player['clean_sheets']
                user_profile['p13_goals_conceded'] = player['goals_conceded']
                user_profile['p13_own_goals'] = player['own_goals']
                user_profile['p13_penalties_saved'] = player['penalties_saved']
                user_profile['p13_penalties_missed'] = player['penalties_missed']
                user_profile['p13_yellow_cards'] = player['yellow_cards']
                user_profile['p13_red_cards'] = player['red_cards']
                user_profile['p13_saves'] = player['saves']
                user_profile['p13_bonus'] = player['bonus']
                user_profile['p13_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p13_team_jersey'] = team_details['jersey']
                        user_profile['p13_team_logo'] = team_details['logo']
                        user_profile['p13_team_colors'] = team_details['colors']
                        user_profile['p13_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 14
            if users_pick['element'] == player['id'] and users_pick['position'] == 14:
                user_profile['p14_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p14_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p14_cost_change_event'] = player['cost_change_event']
                user_profile['p14_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p14_cost_change_start'] = player['cost_change_start']
                user_profile['p14_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p14_dreamteam_count'] = player['dreamteam_count']
                user_profile['p14_element_type'] = player['element_type']
                user_profile['p14_event_points'] = player['event_points']
                user_profile['p14_first_name'] = player['first_name']
                user_profile['p14_form'] = player['form']
                user_profile['p14_player_id'] = player['id']
                user_profile['p14_in_dreamteam'] = player['in_dreamteam']
                user_profile['p14_now_cost'] = player['now_cost']
                user_profile['p14_photo'] = player['photo']
                user_profile['p14_points_per_game'] = player['points_per_game']
                user_profile['p14_second_name'] = player['second_name']
                user_profile['p14_selected_by_percent'] = player['now_cost']
                user_profile['p14_special'] = player['special']
                user_profile['p14_squad_number'] = player['squad_number']
                user_profile['p14_status'] = player['status']
                user_profile['p14_team'] = player['team']
                user_profile['p14_team_code'] = player['team_code']
                user_profile['p14_total_points'] = player['total_points']
                user_profile['p14_value_form'] = player['value_form']
                user_profile['p14_value_season'] = player['value_season']
                user_profile['p14_web_name'] = player['web_name']
                user_profile['p14_minutes'] = player['minutes']
                user_profile['p14_goals_scored'] = player['goals_scored']
                user_profile['p14_assists'] = player['assists']
                user_profile['p14_clean_sheets'] = player['clean_sheets']
                user_profile['p14_goals_conceded'] = player['goals_conceded']
                user_profile['p14_own_goals'] = player['own_goals']
                user_profile['p14_penalties_saved'] = player['penalties_saved']
                user_profile['p14_penalties_missed'] = player['penalties_missed']
                user_profile['p14_yellow_cards'] = player['yellow_cards']
                user_profile['p14_red_cards'] = player['red_cards']
                user_profile['p14_saves'] = player['saves']
                user_profile['p14_bonus'] = player['bonus']
                user_profile['p14_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p14_team_jersey'] = team_details['jersey']
                        user_profile['p14_team_logo'] = team_details['logo']
                        user_profile['p14_team_colors'] = team_details['colors']
                        user_profile['p1_team_name'] = team_details['name']
                user_profile['roster'].append(player)

            # users pick position 15
            if users_pick['element'] == player['id'] and users_pick['position'] == 15:
                user_profile['p15_chance_of_playing_next_round'] = player['chance_of_playing_next_round']
                user_profile['p15_chance_of_playing_this_round'] = player['chance_of_playing_this_round']
                user_profile['p15_cost_change_event'] = player['cost_change_event']
                user_profile['p15_cost_change_event_fall'] =player['cost_change_event_fall']
                user_profile['p15_cost_change_start'] = player['cost_change_start']
                user_profile['p15_cost_change_start_fall'] = player['cost_change_start_fall']
                user_profile['p15_dreamteam_count'] = player['dreamteam_count']
                user_profile['p15_element_type'] = player['element_type']
                user_profile['p15_event_points'] = player['event_points']
                user_profile['p15_first_name'] = player['first_name']
                user_profile['p15_form'] = player['form']
                user_profile['p15_player_id'] = player['id']
                user_profile['p15_in_dreamteam'] = player['in_dreamteam']
                user_profile['p15_now_cost'] = player['now_cost']
                user_profile['p15_photo'] = player['photo']
                user_profile['p15_points_per_game'] = player['points_per_game']
                user_profile['p15_second_name'] = player['second_name']
                user_profile['p15_selected_by_percent'] = player['now_cost']
                user_profile['p15_special'] = player['special']
                user_profile['p15_squad_number'] = player['squad_number']
                user_profile['p15_status'] = player['status']
                user_profile['p15_team'] = player['team']
                user_profile['p15_team_code'] = player['team_code']
                user_profile['p15_total_points'] = player['total_points']
                user_profile['p15_value_form'] = player['value_form']
                user_profile['p15_value_season'] = player['value_season']
                user_profile['p15_web_name'] = player['web_name']
                user_profile['p15_minutes'] = player['minutes']
                user_profile['p15_goals_scored'] = player['goals_scored']
                user_profile['p15_assists'] = player['assists']
                user_profile['p15_clean_sheets'] = player['clean_sheets']
                user_profile['p15_goals_conceded'] = player['goals_conceded']
                user_profile['p15_own_goals'] = player['own_goals']
                user_profile['p15_penalties_saved'] = player['penalties_saved']
                user_profile['p15_penalties_missed'] = player['penalties_missed']
                user_profile['p15_yellow_cards'] = player['yellow_cards']
                user_profile['p15_red_cards'] = player['red_cards']
                user_profile['p15_saves'] = player['saves']
                user_profile['p15_bonus'] = player['bonus']
                user_profile['p15_bps'] = player['bps']
                for team_details in team['team_info']:
                    if player['team'] == team_details['id']:
                        user_profile['p15_team_jersey'] = team_details['jersey']
                        user_profile['p15_team_logo'] = team_details['logo']
                        user_profile['p15_team_colors'] = team_details['colors']
                        user_profile['p15_team_name'] = team_details['name']
                user_profile['roster'].append(player)

    # get gameweek
    for current_gameweek in team['player_data']['events']:
        if current_gameweek['finished'] == True:
            gameweek =  current_gameweek['id']
    user_profile['gameweek'] = "Gameweek " + str(gameweek)


# methods to sort players for roster route
# filter total_points
def sort_by_total_points(e):
    return e['total_points']

# filter event_points
def sort_by_event_points(e):
    return e['event_points']

# filter points_per_game
def sort_by_points_per_game(e):
    return float(e['points_per_game'])

# filter form
def sort_by_form(e):
    return float(e['form'])

# filter minutes
def sort_by_minutes(e):
    return e['minutes']

# filter price
def sort_by_price(e):
    return float(e['now_cost'] * 0.1)


# sort roster by total points
def organize_by_total_points():
    user_profile['roster'].sort(key=sort_by_total_points, reverse=True)
    return user_profile['roster']

# sort roster by gameweek points
def organize_by_event_points():
    user_profile['roster'].sort(key=sort_by_event_points, reverse=True)
    return user_profile['roster']

# sort roster by points per game
def organize_by_points_per_game():
    user_profile['roster'].sort(key=sort_by_points_per_game, reverse=True)
    return user_profile['roster']

# sort roster by form
def organize_by_form():
    user_profile['roster'].sort(key=sort_by_form, reverse=True)
    return user_profile['roster']

# sort roster by minutes
def organize_by_minutes():
    user_profile['roster'].sort(key=sort_by_minutes, reverse=True)
    return user_profile['roster']

# sort roster by price
def organize_by_price():
    user_profile['roster'].sort(key=sort_by_price, reverse=True)
    return user_profile['roster']
