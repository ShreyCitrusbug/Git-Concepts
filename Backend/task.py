import random

organizer_choice_flag: bool = True  # flag to keep adding teams
teams_list: list = []
days: list = []
venues: list = ["Perth", "MCG", "Brisbane", "Sydney"]
while organizer_choice_flag == True:
    teams: str = input("Enter the name of the team : \n")
    teams_list.append(teams)
    organizer_choice = input(
        "\nPress any key to continue adding\nPress N if done adding teams\n"
    ).lower()
    if organizer_choice == "n":
        organizer_choice_flag = False
print(teams_list)

# Loop to create a list for total days the tournament will last including semi-finals and finals
for i in range(1, int((len(teams_list) * (len(teams_list) - 1)) / 2) + 1):
    days.append(f"Day{i}")
days.extend(
    f"Day {int((len(teams_list) * (len(teams_list) - 1))/2)+2}",
    f"Day {int((len(teams_list) * (len(teams_list) - 1))/2)+3}",
    f"Day {int((len(teams_list) * (len(teams_list) - 1))/2)+5}",
)
# Creating a list for randomly chosen venues from a given list of venues
venue_list: list = []
for i in range(1, int((len(teams_list) * (len(teams_list) - 1)) / 2) + 1):
    venue_list.append(random.choice(venues))
semis: str = input("\nWhere to carry out semi finals : \n")
finals: str = input("\nWhere to carry out  finals: \n")
venue_list.extend(semis, semis, finals)


# Creating the day and venue pair to know which venue will be for which day
match_venues: dict = {k: v for (k, v) in zip(days, venue_list)}

# Creating a list of teams who will match up against each other as per the rules
matches: list = []
for i in range(len(teams_list)):
    for j in range(i, len(teams_list)):
        if i == j:
            continue
        else:
            matches.append((teams_list[i], teams_list[j]))

group_stage_days: list = days[
    0 : len(days) - 3
]  # Choosing total days for group stage (excluding knockouts)
shuffled_teams: list = matches.copy()

random.shuffle(shuffled_teams)  # Shuffling the matched teams bracket

# Creating a bracket such that no team play on consecutive days
group_stage_bracket: list = []
left_out_teams: list = []
for i in range(len(shuffled_teams)):
    if i == 0:
        group_stage_bracket.append(shuffled_teams[i])
    else:
        if (
            shuffled_teams[i][0] in group_stage_bracket[-1]
            or shuffled_teams[i][1] in group_stage_bracket[-1]
        ):
            left_out_teams.append(shuffled_teams[i])
        else:
            group_stage_bracket.append(shuffled_teams[i])

for item in left_out_teams:
    for i in range(1, len(group_stage_bracket)):
        if (
            item[0] in group_stage_bracket[i - 1]
            or item[1] in group_stage_bracket[i - 1]
            or item[0] in group_stage_bracket[i]
            or item[1] in group_stage_bracket[i]
        ):
            continue
        else:
            group_stage_bracket.insert(i, item)
            break


# Creating the final bracket for teams with proper "V/S" string
final_group_bracket: list = []
for item in group_stage_bracket:
    final_group_bracket.append(f"{item[0].upper()} V/S {item[1].upper()}")

# Creating the final dictionary for the day and the matches and the venues
final_schedule: dict = dict(zip(days, list(zip(final_group_bracket, venue_list))))

# Added the semi-finals and finals to the dictionary
final_schedule.update(
    {
        f"Day {int((len(teams_list) * (len(teams_list) - 1))/2)+2}": (
            "SF1 : TBD VS TBD",
            "Perth",
        )
    },
    {
        f"Day {int((len(teams_list) * (len(teams_list) - 1))/2)+3}": (
            "SF2 : TBD VS TBD",
            "Perth",
        )
    },
    {
        f"Day {int((len(teams_list) * (len(teams_list) - 1))/2)+5}": (
            "Finals : Winner SF1 V/S Winner SF2",
            "MCG",
        )
    },
)


# FINAL SCHEDULE
print(final_schedule)
