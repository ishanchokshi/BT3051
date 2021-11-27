import numpy as np 
import matplotlib.pyplot as plt
from numpy import random
import networkx as nx

def select_members(member_list,members_selected,n_members_selected,teams,leader,flag):
    """Selection of team members """
    leaders_node = []

    team_members = list(random.choice(member_list, size = n_members_selected,replace = False))
    members_selected = members_selected + team_members
    if(flag==0):
        teams[leader] = team_members
    else:
        teams[leader] = teams[leader] + team_members
    return teams,members_selected

def get_leaders(G):
	return sorted(G.nodes, key = G.degree, reverse=True)[:6]

SocialGraph = nx.barabasi_albert_graph(60, 2, 42)
Leaders = get_leaders(SocialGraph)
Trump_Card = 59;

# You are given SocialGraph which reflects the social network of the 60 participants.
# Six chosen leaders are given to you as a list using variable called 'Leaders'

# Add any functions required

def Form_Teams(G, Leaders): # Copy this function from the previous subquestion
    """ Form six teams each consisting of 10 individuals """
    teams = {i:[0 for i in range(10)] for i in Leaders}
    """ Add your code here """
    leader_order = random.permutation(Leaders)
    selected = []
    members_selected = []
    for leader in leader_order:
        flag = 0
        leader_neighbors = [i for i in G.neighbors(leader) if i not in members_selected if i not in Leaders]
        n_members_selected = min(9,len(leader_neighbors))
        teams, members_selected = select_members(leader_neighbors,members_selected,n_members_selected,teams,leader,flag)

  #Get second neighbors
    for leader in leader_order:
        flag = 1
        second_neighbors = [i for neighbor in G.neighbors(leader) for i in G.neighbors(neighbor) if neighbor in teams[leader] if i not in members_selected if i not in Leaders ]
        n_members_selected = min(9 - len(teams[leader]), len(second_neighbors))
        teams, members_selected = select_members(second_neighbors,members_selected,n_members_selected,teams,leader,flag)

  #Select the remaining members
    for leader in leader_order:
        flag = 1
        members_remaining = [i for i in G if i not in members_selected if i not in Leaders]
        n_members_selected = min(9 - len(teams[leader]), len(members_remaining))
        teams, members_selected = select_members(members_remaining,members_selected,n_members_selected,teams,leader,flag)
    for i in teams.keys():
        teams[i] = [i] + teams[i]
    return teams
    

def Tug_of_war_Trump_Card(Teams, Trump_Card): # Update this function from your previous subquestion
    """ Tug of war round. Each team has equal chance of winning. Returns three winning teams."""
    """ Add your code here """
    leaders_winners = list(random.choice(Leaders, (3,2),replace = False))
    leaders_list = []
    p = []
    Winning_Teams = []
    for i in leaders_winners:
        if(Trump_Card in Teams[i[0]] or Trump_Card in Teams[i[1]]):
            if(Trump_Card in Teams[i[0]]):
                Winning_Teams = Winning_Teams + list(random.choice(i,1,replace=False,p = [0.9, 0.1]))
            else:
                Winning_Teams = Winning_Teams + list(random.choice(i,1,replace=False,p = [0.1, 0.9])) 
        else:
            Winning_Teams = Winning_Teams + list(random.choice(i,1,replace=False,p = [0.5, 0.5]))
        # leaders_list = leaders_list + [i[0],i[1]]
    # Winning_Teams = list(random.choice(leaders_list,3,replace=False,p = p))

    return Winning_Teams

def simulate_Trump_Card(G, Leaders): # Copy this function from the previous subquestion with appropriate modifications
    """ Simulate the scenario multiple times """
    probabilities_of_winning = {i:0.2 for i in G.nodes}
    """ Modify the code as required """
    games = 0
    for i in range(10000):
        games = games + 1
        Teams = Form_Teams(G,Leaders)
        Winners = Tug_of_war_Trump_Card(Teams, Trump_Card) 
        # Update the probabilites
        players_won = []
        for i in Winners:
            players_won = players_won + Teams[i]
        for i in G:
            if(i not in players_won):
                probabilities_of_winning[i] = (probabilities_of_winning[i]* (games-1))/games
            else:
                probabilities_of_winning[i] = (probabilities_of_winning[i]* (games-1)+1)/games


    return probabilities_of_winning

Winning = simulate_Trump_Card(SocialGraph,Leaders)
print(Winning)