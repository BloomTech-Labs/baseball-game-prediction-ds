'''Access point for prediction model'''

import json
import pickle

from flask import Flask, jsonify, request

model = pickle.load(open('cat_pickle.pkl', 'rb'))

app = Flask(__name__)

#Drop API route for access 
@app.route('/', mathods=['POST'])

def prediction():
    """Take in user input from site and run prediction against trained model
    format of api call must be json containing in order:
    date                               int64
    game_num                           int64
    day_of_week                        string
    visiting_team                      string
    visiting_team_league               string
    visiting_game_num                  int64
    home_team                          string
    home_team_league                   string
    home_team_game_num                 int64
    day_night                          string
    park_id                            string
    visiting_manager_name              string
    home_manager_name                  string
    visiting_starting_pitcher_name     string
    home_starting_pitcher_name         string
    visiting_1_name                    string
    visiting_1_pos                     int64
    visiting_2_name                    string
    visiting_2_pos                     int64
    visiting_3_name                    string
    visiting_3_pos                     int64
    visiting_4_name                    string
    visiting_4_pos                     int64
    visiting_5_name                    string
    visiting_5_pos                     int64
    visiting_6_name                    string
    visiting_6_pos                     int64
    visiting_7_name                    string
    visiting_7_pos                     int64
    visiting_8_name                    string
    visiting_8_pos                     int64
    visiting_9_name                    string
    visiting_9_pos                     int64
    home_1_name                        string
    home_1_pos                         int64
    home_2_name                        string
    home_2_pos                         int64
    home_3_name                        string
    home_3_pos                         int64
    home_4_name                        string
    home_4_pos                         int64
    home_5_name                        string
    home_5_pos                         int64
    home_6_name                        string
    home_6_pos                         int64
    home_7_name                        string
    home_7_pos                         int64
    home_8_name                        string
    home_8_pos                         int64
    home_9_name                        string
    home_9_pos                         int64
    """
# Get input values from request
    data = request.get_json(force=True)
# Wrangle data to pass model input standards
    data_in = json.loads(data)
    game = list(data_in.values())
    