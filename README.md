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
