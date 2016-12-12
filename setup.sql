
create table games (
    player_id integer not null,  -- "id" in fpl data
    game_id integer not null,    -- "event_id"
    assists integer not null,
    attempted_passes integer not null,
    big_chances_created integer not null,
    big_chances_missed integer not null,
    bonus integer not null,
    bps integer not null,
    clean_sheets integer not null,
    clearances_blocks_interceptions integer not null,
    completed_passes integer not null,
    -- creativity "0.0",
    dribbles integer not null,
    -- ea_index integer not null,
    errors_leading_to_goal integer not null,
    errors_leading_to_goal_attempt integer not null,
    fixture integer not null,
    fouls integer not null,
    goals_conceded integer not null,
    goals_scored integer not null,
    -- ict_index "0.0",
    -- id 1,
    -- influence "0.0",
    key_passes integer not null,
    -- kickoff_time "2016-08-14T15:00:00Z",
    -- kickoff_time_formatted "14 Aug 16:00",
    loaned_in integer not null,
    loaned_out integer not null,
    minutes integer not null,
    offside integer not null,
    open_play_crosses integer not null,
    opponent_team integer not null,
    own_goals integer not null,
    penalties_conceded integer not null,
    penalties_missed integer not null,
    penalties_saved integer not null,
    recoveries integer not null,
    red_cards integer not null,
    gameweek integer not null,
    saves integer not null,
    total_selected_by integer not null,  -- "selected"
    tackled integer not null,            -- Difference?
    tackles integer not null,
    target_missed integer not null,
    away_score integer not null,         -- "team_a_score"
    home_score integer not null,         -- "team_h_score"
    -- threat "0.0",
    total_points integer not null,
    transfers_balance integer not null,  -- Needed? Just difference of in and out
    transfers_in integer not null,
    transfers_out integer not null,
    value integer not null,
    was_home boolean not null,
    winning_goals integer not null,
    yellow_cards integer not null
);
