# Baseball Game Outcome Prediction API

## What is it

The Baseball Game Outcome Prediction API allows users to run a powerful machine learning prediction model with a simple request to an API. Using machine learning and historic Major League Baseball data results in an accuracy of 53%. Packaging this power into an API allows the user to make a request with the details of a game and recieve accurate results of the outcome.

## Main Features

Here are some details of the API

* Restful API
* Accepts post requests
* Outputs winning team prediction
* Utilizes Flask And Heroku
* Built with Python

## Where to access the API 

The Endpoint to access the prediction model API is available here:
[Game Prediction](https://baseball-game-predictor.herokuapp.com/)

## Interacting with the API

To interact with the API please send a post request to the endpoint url listed above.
The format of the post request should be a json string formatted and containing the values profiled below.

```json
{
    "date": 20080612
    ,   "game_num": 0
    ,   "day_of_week": "Thu"
    ,   "visiting_team": "MIN"
    ,   "visiting_team_league": "AL"
    ,   "visiting_game_num": 67
    ,   "home_team": "CLE"
    ,   "home_team_league": "AL"
    ,   "home_team_game_num": 67
    ,   "day_night": "N"
    ,   "park_id": "CLE08"
    ,   "visiting_manager_name": "Ron Gardenhire"
    ,   "home_manager_name": "Eric Wedge"
    ,   "visiting_starting_pitcher_name": "Livan Hernandez"
    ,   "home_starting_pitcher_name": "Aaron Laffey"
    ,   "visiting_1_name": "Carlos Gomez"
    ,   "visiting_1_pos": 8
    ,   "visiting_2_name": "Alexi Casilla"
    ,   "visiting_2_pos": 4
    ,   "visiting_3_name": "Joe Mauer"
    ,   "visiting_3_pos": 2
    ,   "visiting_4_name": "Justin Morneau"
    ,   "visiting_4_pos": 3
    ,   "visiting_5_name": "Michael Cuddyer"
    ,   "visiting_5_pos": 9
    ,   "visiting_6_name": "Jason Kubel"
    ,   "visiting_6_pos": 7
    ,   "visiting_7_name": "Craig Monroe"
    ,   "visiting_7_pos": 10
    ,   "visiting_8_name": "Brendan Harris"
    ,   "visiting_8_pos": 6
    ,   "visiting_9_name": "Matt Macri"
    ,   "visiting_9_pos": 5
    ,   "home_1_name": "Grady Sizemore"
    ,   "home_1_pos": 8
    ,   "home_2_name": "Jamey Carroll"
    ,   "home_2_pos": 4
    ,   "home_3_name": "Ben Francisco"
    ,   "home_3_pos": 7
    ,   "home_4_name": "Ryan Garko"
    ,   "home_4_pos": 3
    ,   "home_5_name": "David Dellucci"
    ,   "home_5_pos": 10
    ,   "home_6_name": "Jhonny Peralta"
    ,   "home_6_pos": 6
    ,   "home_7_name": "Shin-Soo Choo"
    ,   "home_7_pos": 9
    ,   "home_8_name": "Casey Blake"
    ,   "home_8_pos": 5
    ,   "home_9_name": "Kelly Shoppach"
    ,   "home_9_pos": 2
}
```

The return for this request will be a json string as shown below

```json
{
    'Winning team': 'CLE'
}
```
