# virus

## Project Proposal

Andrew Pan

### Goals

The main idea of this project is to program a Neato to hijack wireless sessions of other Neatos and begin issuing commands to them, ultimately creating and coordinating a swarm.  Throughout the course of this project, I hope to analyze and deconstruct the message formats sent between ROS nodes on a network and spoof them to overwrite intended messages from a normal actor on the network.  I also hope to determine ways to coordinate a swarm of Neatos to move in tandem and organize layouts. For this project, an MVP would be to use a Neato to connect to another Neato and issue a movement command.  As a stretch goal, the Neato would be able to transmit the slave node source code to robots in its swarm, which would then also attempt to hijack further Neatos.  Additionally, coordinating a swarm to move in a meaningful or humorous manner would be a stretch goal as well.

### Rough Timeline

11/16: Have basic wireless connection to a free Neato from a ROS node
11/30: Issuing commands and coordinating multiple slave Neatos from a master node
12/7: Code injection into slaved Neatos
12/11: Refinement and cleanup
12/14: Presentation Prepared

### Risks

The biggest risks for my project stem from the actual implementations of ROS message delivery and receipt at a low level.  I have no prior knowledge of any potential security protocols built into ROS networks, so each additional layer of security will significantly increase the amount of work I will have to put in to wireless network research.  Beyond that, I do not have a concrete idea of what sort of swarm coordination I want to implement, but I will hopefully come up with a reasonably scoped concept when I reach the coordination phase of my project.

### YOGA

The first of my learning goals for this assignment is to create an effective strategy for organizing movements of multiple actors in a network.  I plan on issuing movements from a master node, but accounting for the movements of a potentially arbitrary number of components appeals to me as both an interesting and potentially challenging goal.  This goal also allows for a large amount of flexibility in terms of further directions I can take it, and as an MVP I would aim to simply have the swarm move from one point another in a formation.  Further additions to this goal haven't been scoped yet, but can easily include challenges such as creating shapes or navigating around objects together.

My next learning goal is to work with hijacking network communications.  I have previously worked with UDP and TCP connections and transferringg data following BitTorrent protocols and I've done a fair bit of learning regarding penetration testing, but I haven't actually attempted to assume the role of a bad actor from a relatively low-level approach.  I hope to gain experience in working with network communications which can in turn inform me of how some security protocols could effectively serve to thwart network attacks.

My last learning goal is to hopefully work with code injection.  I find it very interesting to overwrite an existing process with an injected code segment, having been on the receiving end before, and would like to better understand what's happening at a fundamental level.  This goal is dependent on how much progress I make in other sections of the project, but ideally I would be able to inject a function into the code running on a robot given knowledge of said robot's processes beforehand.