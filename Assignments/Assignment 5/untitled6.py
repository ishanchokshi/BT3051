# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1suR74MWPwR_c9BMFl9zRnkg43RW1ZHDI
"""

import numpy as np 
import matplotlib.pyplot as plt
from numpy import random
import networkx as nx

def get_leaders(G):
	return sorted(G.nodes, key = G.degree, reverse=True)[:6]

SocialGraph = nx.barabasi_albert_graph(60, 2, 42)
Leaders = get_leaders(SocialGraph)
Trump_Card = 59;

# You are given SocialGraph which reflects the social network of the 60 participants.
# Six chosen leaders are given to you as a list using variable called 'Leaders'

# Add any functions required

def select_members(member_list,members_selected,n_members_selected,teams,leader,flag):
    """Selection of team members """
    leaders_node = []

    team_members = list(random.choice(member_list, size = n_members_selected,replace = False)) #Select the team members at random
    members_selected = members_selected + team_members #Number of members selected for each team
    if(flag==0): #Flag = 0 implies Selection of friends (immediate neighbors)
        teams[leader] = team_members #Assigning the members to the respective teams
    else: #Flag = 1 implies selection of second neighbors and remaining members
        teams[leader] = teams[leader] + team_members #Assigning the members to the respective teams
    return teams,members_selected

def Form_Teams(G, Leaders): # Copy this function from the previous subquestion
    """ Form six teams each consisting of 10 individuals """
    teams = {i:[0 for i in range(10)] for i in Leaders}
    """ Add your code here """

    leader_order = random.permutation(Leaders) #Randomly assign the order in which the leaders will select team members
    selected = []
    members_selected = []
    #Selecting the friends first
    for leader in leader_order:
        flag = 0 #A flag which informs whether it is the selection of immediate neighbors, or the selection of second neighbors and remaining members
        leader_neighbors = [i for i in G.neighbors(leader) if i not in members_selected if i not in Leaders] #Return list of immediate neighbors for each leader
        n_members_selected = min(9,len(leader_neighbors)) #Determines how many team members will be selected for each team
        teams, members_selected = select_members(leader_neighbors,members_selected,n_members_selected,teams,leader,flag) #Return the list of members in the team

    #Selecting the friends of friends (second neighbors)
    for leader in leader_order:
        flag = 1
        second_neighbors = [i for neighbor in G.neighbors(leader) for i in G.neighbors(neighbor) if i not in members_selected if i not in Leaders] #Return list of second neighbors for each leader
        n_members_selected = min(9 - len(teams[leader]), len(second_neighbors)) #Determines how many team members will be selected for each team
        teams, members_selected = select_members(second_neighbors,members_selected,n_members_selected,teams,leader,flag) #Return the list of members in the team

    #Select the remaining members
    for leader in leader_order:
        flag = 1
        members_remaining = [i for i in G if i not in members_selected if i not in Leaders] #Return list of members that haven't been selected yet
        n_members_selected = min(9 - len(teams[leader]), len(members_remaining)) #Determines how many team members will be selected for each team
        teams, members_selected = select_members(members_remaining,members_selected,n_members_selected,teams,leader,flag) #Return the list of members in the team
    for i in teams.keys():
        teams[i] = [i] + teams[i] #Add the team leader to the list of team members in each team
    
    return teams

def Tug_of_war_Trump_Card(Teams, Trump_Card): # Update this function from your previous subquestion
    """ Tug of war round. Each team has equal chance of winning. Returns three winning teams."""
    """ Add your code here """

    leaders_winners = list(random.choice(Leaders, (3,2),replace = False)) #Assign teams as pairs for the tug of war
    Winning_Teams = []
    for i in leaders_winners:
        if(Trump_Card in Teams[i[0]] or Trump_Card in Teams[i[1]]): #Check if the Trump card is in any one of the teams 
            if(Trump_Card in Teams[i[0]]): #Assign the probabilty of selecting the team as winner to 0.9 for the team which has the trump card
                Winning_Teams = Winning_Teams + list(random.choice(i,1,replace=False,p = [0.9, 0.1])) 
            else:
                Winning_Teams = Winning_Teams + list(random.choice(i,1,replace=False,p = [0.1, 0.9])) 
        else:
            Winning_Teams = Winning_Teams + list(random.choice(i,1,replace=False,p = [0.5, 0.5])) #Assign the probabilty of selecting any one of the teams as winner to 0.5 if none of them have the trump card
    
    return Winning_Teams

def simulate_Trump_Card(G, Leaders): # Copy this function from the previous subquestion with appropriate modifications
    """ Simulate the scenario multiple times """
    probabilities_of_winning = {i:0.2 for i in G.nodes}
    """ Modify the code as required """
    simulations = 0
    for i in range(10000):
        Teams = Form_Teams(G,Leaders)
        Winners = Tug_of_war_Trump_Card(Teams, Trump_Card) 
        # Update the probabilites
        players_won = [] #List of players who won
        simulations = simulations + 1
        for i in Winners:
            players_won = players_won + Teams[i]
        for i in G.nodes():
            if(i not in players_won):
                probabilities_of_winning[i] = (probabilities_of_winning[i]* (simulations-1))/simulations #Probability updated if the player has lost
            else:
                probabilities_of_winning[i] = (probabilities_of_winning[i]* (simulations-1)+1)/simulations #Probability updated if the player has won

    return probabilities_of_winning

win_probabilities = simulate_Trump_Card(SocialGraph,Leaders)
print(win_probabilities)