# Open space organizer
This project contains an algorithm that randomly assign people to a spot in the openspace.

The default setup of the open space is 6 tables of 4 seats → 24 seats.

# Workflow

## High level flow chart:

```mermaid
graph TD;
    A[read_input_file]-->B[create 6 tables with 4 seats];
    B-->C[randomize the list]
    C-->D[for every person in names];
    D-->E{Table.has_free_spots};
    E-- True --> G[NO MORE TABLES FREE];
    E-- No --> F[YES];
    F-->H[Openspace.organize];

```


## Flow chart of the organize algorithm:

```mermaid
graph TD;
    A{is table nr == 6} -- YES --> B[OUT OF TABLES]
    B --> X[END]
    A -- NO --> C[seatnr + 1]
    C --> D{is seat nr == 4}
    D -- NO --> E[seatnr + 1]
    D -- YES --> F[OUT OF SEATS]
    F --> A
    E --> G[Seat.set_occupant]
```


# Installation



# Usage

The program reads data from a txt file that contains all the names of people in the openspace. The program then randomly assigns each person to a spot in the openspace.


# Timeline



# Personal situation

This project was made as an assignment in the BeCode course: Data AI operator.


### to cover in this README file:
(Visuals)
(Contributors)

