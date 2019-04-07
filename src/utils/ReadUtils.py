'''
Utilities to help read and parse input data.

todo: docs
todo: type hints
'''

'''
Schema:
Date (YYYY-MM-DD)
Team 1 (prefixed by '@' if played at home)
Team 1's score
Team 2 (prefixed by '@' if played at home)
Team 2's score
Flags: P=playoff, F=forfeit, S=stricken, E=exhibition, O?=overtime
Note: may include game title or venue information

todo: docs
todo: it'd be nice to have an example URL of where this input is
'''
def read_in_massey_game_data(filename):
    with open(filename, 'r') as f:
        raw_data = [row for row in f]

    return raw_data

'''
todo: docs
todo: rule of 30 refactor
'''
def clean_massey_raw_line(line):
    clean_line = []
    split_line = line.split(' ')

    line_offset = 0
    for i in range(len(split_line)):
        try:
            thing = split_line[i + line_offset]
        except IndexError:
            print "Index error"
            print split_line
            print i
            print line_offset
            raise RuntimeError()


        if thing: # this isn't empty so it's useful info
            # ugh this is hacky as shit
            if len(clean_line) == 0:
                # you found the date
                clean_line.append(thing)
            elif len(clean_line) == 1:
                # team 1 can have multiple space-delimited columns
                school_name = thing
                offset = 1
                next_thing = split_line[i+offset + line_offset]
                while next_thing and next_thing[0] in VALID_SCHOOL_NAME_CHARS:
                    school_name += next_thing
                    offset += 1
                    next_thing = split_line[i+offset+line_offset]
                line_offset += offset - 1
                clean_line.append(school_name)
            elif len(clean_line) == 2:
                # score 1
                clean_line.append(thing)
            elif len(clean_line) == 3:
                # team 2 is same as team 1
                # team 1 can have multiple space-delimited columns
                school_name = thing
                offset = 1
                next_thing = split_line[i+offset + line_offset]
                while next_thing and next_thing[0] in VALID_SCHOOL_NAME_CHARS:
                    school_name += next_thing
                    offset += 1
                    next_thing = split_line[i+offset+line_offset]
                line_offset += offset - 1
                clean_line.append(school_name)
            elif len(clean_line) == 4:
                # score 2
                clean_line.append(thing)
            else:
                # check to make sure the last thing is a score
                if clean_line[-1][0] not in string.digits:
                    raise RuntimeError("The last item in a row wasn't a score?", clean_line)
                return clean_line
    # this line should neber execute
    raise RuntimeError("Got to a point in clean_massey_raw_line that we shouldn't have.", clean_line, "\n", line)

'''
Schema:
days since 1-1-0000
YYYYMMDD
team1 index (zero if a non-conference team)
homefield1 (1=home, -1=away, 0=neutral)
score1
team2 index (zero if a non-conference team)
homefield2 (1=home, -1=away, 0=neutral)
score2

todo: docs
todo: this is unused in the old stuff. what is this?
'''
def read_clean_games_data(filename):
    games = []
    with open(filename, 'r') as f:
        games = [row.split('\t') for row in f]

    # the last one is a newline
    clean_games = [[int(datapoint.strip()) for datapoint in game] for game in games[:-1]]

    return clean_games

'''
Parse the massey team names csv into a dict of {team_id -> team_name}

todo: docs
todo: this is unused in the old stuff. what is this?
'''
def parse_teams(filename):
    raw_teams = []
    with open(filename, 'r') as f:
        raw_teams = [row for row in f]

    if len(raw_teams) > 1:
        raise RuntimeError("there were line breaks in the teams file")

    split_teams = raw_teams[0].split(' ')
    parsed_teams = {}

    # this is so shitty
    # len(split_teams)-1 because the last thing is /r/n
    for i in range(0, len(split_teams)-1, 2):
        raw_team_id = split_teams[i]
        team_name = split_teams[i+1]
        team_id = int(raw_team_id.strip()[:-1])
        parsed_teams[team_id] = team_name

    return parsed_teams

'''
todo: docs
todo: type hints
todo: surely this can be done better
'''
def make_game_from_line(line):
    team_1 = line[GAME_DATA_SCHEMA['team 1']]
    team_2 = line[GAME_DATA_SCHEMA['team 2']]
    score_1 = line[GAME_DATA_SCHEMA['team 1 score']]
    score_2 = line[GAME_DATA_SCHEMA['team 2 score']]
    date = line[GAME_DATA_SCHEMA['date']]

    location = 1
    if team_2.startswith('@'):
        location = 2
        team_2 = team_2[1:]
    elif team_1.startswith('@'):
        team_1 = team_1[1:]
    else:
        location = 0

    return Game(team_1, team_2, int(score_1), int(score_2), location, date)
