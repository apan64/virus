# H4x0r Virus

## An attempt to make the lives of others slightly more bothersome

The main idea of this project is to program a Neato to hijack wireless sessions of other Neatos and begin issuing commands to them, ultimately creating and coordinating a swarm.  As ROS implementations assume that systems will be running on a closed network, there is not much in terms of security protocols that have been built into communications between components in a ROS network, leaving many vulnerabilities open if a bad actor manages to gain access to a network.  As a general overview, this project consists of a primary running node that issues commands to a single Neato while scanning the network for other potential Neatos.  Upon finding a machine, it attempts to launch a node on said machine through a threaded subprocess and adds the machine to its stored network of Neatos.  Once a Neato has been added to the network, it receives commands from the master node which can range from simple movements to coordinated ones.

## Project Stories

### Story 1

Given that network projects typically require some knowledge of the system one is working with, so far I have spent the majority of my time researching the specific implementation details of ROS messages and communications in an attempt to discern areas where I could insert my own project work.  For me, this also involved learning more about the specifics of how ROS is implemented as well as reading through the written drivers for the Neatos we use in class as our robots.  At this point I now have enough information to begin writing code to connect to Neatos, starting with creating a network of Neatos by launching nodes on available ones and hopefully working my way up to connecting to Neatos already in use.

### Story 2

I am currently working on connecting to multiple Neatos simultaneously, but have run into a host of problems.  I tried multiple approaches to this issue such as making calls within a running ROS node to launch new nodes on Neatos, but have met a number of walls due to the way that the Neato drivers are implemented.  I also have tried my hand at intercepting information being sent to and from Neatos, though attempts to extract data directly from these communications have been difficult.  As a result, I have worked on directly editing the drivers and launch files for the Neatos but have still ran into issues due to not fully understanding subsequent systems and nodes that are launched through these files.  I have managed to edit these files to enable my machine to connect to multiple Neatos simultaneously, but cannot necessarily issue commands to these Neatos simultaneously without either running into socket errors or losing sensor data.

