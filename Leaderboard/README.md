# Prediction Leaderboard

### Concept:
The main idea behind the Leaderboard is to allow users to compete with one another and our model. Essentially, for a given time period, we want to rank-order the predictive accuracy of our users and our model. Because the baseball season is already over at the time of this writing however, we will simply document our approach to building this and let the next team take a stab at implementing it.

### Implementation: 
Our application's back-end is built using `Node.js` and so it'll be easiest to design our Leaderboard accordingly. Using the existing structure, we would have to expand our Firebase database to:
1) Include a field for *User Predictions* (for each game in a season, a user can submit a prediction or abstain)
2) Include a field for *Model Predictions* (same as above but for our model's predictions)
2) Include *Game Outcomes* (so as the season progresses each game's outcome is logged and stored)
3) Compare the Outcomes and Predictions together to calculate Accuracy for each user and our model.


### Measuring Accuracy:
```

```
