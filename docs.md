# NBA Players API Docs

Just a quick FYI this API only contains players andd stats as of the 2025-2026 NBA season.

## Search by Player Name

You can search a player by their name with a GET request to the following route:
`/name/{first name here}/{last name here}/`

So for instance, you could send a GET request to `/name/LeBron/James` and you would get back:

```json
[
  {
    "Name": "LeBron James",
    "Debut": 2004,
    "Final": 2025,
    "Position": "['Forward', 'Guard']",
    "Height": 81,
    "Weight": 250.0,
    "Birthday": "December 30, 1984",
    "School": null,
    "HOF": false,
    "Active": true,
    "G": 1562,
    "PTS": 27.0,
    "TRB": 7.5,
    "AST": 7.4,
    "FG%": 50.6,
    "FG3%": 34.9,
    "FT%": 73.7,
    "eFG%": 54.8,
    "PER": 26.9,
    "WS": 271.4
  }
]
```

## Search Active Players

You can view players who are actively playing in the NBA by searching at the following route `/active-players/{amount}` where amount is how many players you want to view. If amount is left blank it will show all active players while if amount where for example 10 it will only show 10 active players.
Here is an example on a get request route to view 5 active NBA players:
`/active-players/5` and this GET request will return:

```json
[
  {
    "Name": "Precious Achiuwa",
    "Debut": 2021,
    "Final": 2025,
    "Position": "['Forward']",
    "Height": 80,
    "Weight": 225.0,
    "Birthday": "September 19, 1999",
    "School": "['Memphis']",
    "HOF": false,
    "Active": true,
    "G": 320,
    "PTS": 7.6,
    "TRB": 5.7,
    "AST": 1.0,
    "FG%": 48.4,
    "FG3%": 30.4,
    "FT%": 60.6,
    "eFG%": 51.4,
    "PER": 14.0,
    "WS": 11.8
  },
  {
    "Name": "Steven Adams",
    "Debut": 2014,
    "Final": 2025,
    "Position": "['Center']",
    "Height": 83,
    "Weight": 265.0,
    "Birthday": "July 20, 1993",
    "School": "['Pitt']",
    "HOF": false,
    "Active": true,
    "G": 764,
    "PTS": 8.8,
    "TRB": 8.0,
    "AST": 1.5,
    "FG%": 58.6,
    "FG3%": 5.9,
    "FT%": 53.3,
    "eFG%": 58.6,
    "PER": 17.1,
    "WS": 61.6
  },
  {
    "Name": "Bam Adebayo",
    "Debut": 2018,
    "Final": 2025,
    "Position": "['Center', 'Forward']",
    "Height": 81,
    "Weight": 255.0,
    "Birthday": "July 18, 1997",
    "School": "['Kentucky']",
    "HOF": false,
    "Active": true,
    "G": 567,
    "PTS": 15.7,
    "TRB": 8.9,
    "AST": 3.6,
    "FG%": 53.7,
    "FG3%": 31.4,
    "FT%": 75.6,
    "eFG%": 54.5,
    "PER": 19.8,
    "WS": 57.6
  },
  {
    "Name": "Ochai Agbaji",
    "Debut": 2023,
    "Final": 2025,
    "Position": "['Guard']",
    "Height": 77,
    "Weight": 215.0,
    "Birthday": "April 20, 2000",
    "School": "['Kansas']",
    "HOF": false,
    "Active": true,
    "G": 201,
    "PTS": 7.9,
    "TRB": 2.9,
    "AST": 1.2,
    "FG%": 45.0,
    "FG3%": 35.3,
    "FT%": 73.4,
    "eFG%": 54.0,
    "PER": 9.8,
    "WS": 4.5
  },
  {
    "Name": "Santi Aldama",
    "Debut": 2022,
    "Final": 2025,
    "Position": "['Forward']",
    "Height": 83,
    "Weight": 224.0,
    "Birthday": "January 10, 2001",
    "School": "['Loyola (MD)']",
    "HOF": false,
    "Active": true,
    "G": 235,
    "PTS": 9.8,
    "TRB": 5.2,
    "AST": 1.9,
    "FG%": 45.9,
    "FG3%": 34.5,
    "FT%": 69.2,
    "eFG%": 54.6,
    "PER": 14.3,
    "WS": 12.2
  }
]
```

## Top Scoring Players

You can view the players who scored the most PPG with a GET request at route `/players/top/pts/{amount}` if you leave amount empty it will show all players sorted by the top players if you give amount a number lets say 10 it will show the top 10 scoring players.
Here is an example on a GET request you can make to show the top 3 scoring players:
`players/top/pts/3` this will return:

```json
[
  {
    "Name": "Michael Jordan",
    "Debut": 1985,
    "Final": 2003,
    "Position": "['Guard', 'Forward']",
    "Height": 78,
    "Weight": 198.0,
    "Birthday": "February 17, 1963",
    "School": "['UNC']",
    "HOF": true,
    "Active": false,
    "G": 1072,
    "PTS": 30.1,
    "TRB": 6.2,
    "AST": 5.3,
    "FG%": 49.7,
    "FG3%": 32.7,
    "FT%": 83.5,
    "eFG%": 50.9,
    "PER": 27.9,
    "WS": 214.0
  },
  {
    "Name": "Wilt Chamberlain",
    "Debut": 1960,
    "Final": 1973,
    "Position": "['Center']",
    "Height": 85,
    "Weight": 275.0,
    "Birthday": "August 21, 1936",
    "School": "['Kansas']",
    "HOF": true,
    "Active": false,
    "G": 1045,
    "PTS": 30.1,
    "TRB": 22.9,
    "AST": 4.4,
    "FG%": 54.0,
    "FG3%": null,
    "FT%": 51.1,
    "eFG%": null,
    "PER": 26.2,
    "WS": 247.3
  },
  {
    "Name": "Luka Dončić",
    "Debut": 2019,
    "Final": 2025,
    "Position": "['Guard', 'Forward']",
    "Height": 78,
    "Weight": 230.0,
    "Birthday": "February 28, 1999",
    "School": null,
    "HOF": false,
    "Active": true,
    "G": 450,
    "PTS": 28.6,
    "TRB": 8.6,
    "AST": 8.2,
    "FG%": 46.8,
    "FG3%": 35.0,
    "FT%": 75.1,
    "eFG%": 54.2,
    "PER": 25.5,
    "WS": 57.1
  }
]
```

## View All Players

To see all players and there stats you can go to `players/{amount}` if you leave amount empty than you will see every player who has ever played in the NBA until the 2025-2026 NBA season otherwise you will only see the amount of players that you enter when you press amount.
For example if you send a GET request to route `players/3` than you will see 3 random players and it will return

```json
[
  {
    "Name": "A.C. Green",
    "Debut": 1986,
    "Final": 2001,
    "Position": "['Forward', 'Center']",
    "Height": 81,
    "Weight": 220.0,
    "Birthday": "October 4, 1963",
    "School": "['Oregon State']",
    "HOF": false,
    "Active": false,
    "G": 1278,
    "PTS": 9.6,
    "TRB": 7.4,
    "AST": 1.1,
    "FG%": 49.4,
    "FG3%": 25.4,
    "FT%": 73.4,
    "eFG%": 50.1,
    "PER": 14.4,
    "WS": 99.5
  },
  {
    "Name": "A.J. Bramlett",
    "Debut": 2000,
    "Final": 2000,
    "Position": "['Center']",
    "Height": 82,
    "Weight": 227.0,
    "Birthday": "January 10, 1977",
    "School": "['Arizona']",
    "HOF": false,
    "Active": false,
    "G": 8,
    "PTS": 1.0,
    "TRB": 2.8,
    "AST": 0.0,
    "FG%": 19.0,
    "FG3%": null,
    "FT%": null,
    "eFG%": 19.0,
    "PER": -0.4,
    "WS": -0.2
  },
  {
    "Name": "A.J. English",
    "Debut": 1991,
    "Final": 1992,
    "Position": "['Guard']",
    "Height": 75,
    "Weight": 175.0,
    "Birthday": "July 11, 1967",
    "School": "['Virginia Union University']",
    "HOF": false,
    "Active": false,
    "G": 151,
    "PTS": 9.9,
    "TRB": 2.1,
    "AST": 2.1,
    "FG%": 43.5,
    "FG3%": 13.8,
    "FT%": 77.8,
    "eFG%": 43.8,
    "PER": 11.6,
    "WS": 1.1
  }
]
```

## Report an Issue

If you would like to report an issue it is preferd you do so through github but if you would like to do so with the api feel free to do so.

If you send the followin json code in a post request to `/report_issue`

```json
{
  "issue": "## issue is blah blah blah"
}
```

and the server responds with

```json
{ "status": "success", "message": "Issue recorded" }
```

than you have successfully sent an issue
