# Setup

## Setting Up Docker
If you already have Docker Engine and Docker Compose (or Docker Desktop, which covers both) installed and setup properly, you may skip this step.

The first step is to setup Docker on your machine, as it's used to run the container the webapp runs in. Visit (here)[https://www.docker.com/products/docker-desktop/] and follow the instructions to setup Docker Desktop on your machine. That takes care of Docker Compose and Docker Engine. Test this is functioning properly by starting up the Hello World container as the instructions prescribe.

## Clone the Repo
The next step is to clone this repository onto your machine. To do this, follow (this guide)[https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository] by github to clone a repository, on the NoodleMaps repository (here)[https://github.com/olincollege/noodlemaps].

## Start It Up
All your setup is complete! To start the Noodlemaps server locally, navigate to `/noodlemaps/src` and run the command `docker compose up` in the terminal to start the service. If all goes well you should get about 12 lines of output in your terminal containing the line `Running on http://172.30.0.2:5000`. Navigate to that link to access the webapp! Please refer to `using-the-form` for further interaction (starting from the "Enter Your Data" section).

## Shut It Down
It's good practice to fully shut down your containers when you're done with them. To do this, run `ctrl-c` in the terminal window where you ran the compose up command and let the container spin down (this takes about ten seconds).

## If You Edit
If you work on anything within the container and want to spin up a container with those edits, you'll have to run `docker compose up --build` instead. This takes a little longer to run but rebuilds the container, reflecting your changes.