# LineupLab
A predictive NBA matchup analyzer using a novel Convolutional Neural Network model to forecast win probabilities by analyzing team lineups, player performance, and historical statistics, leveraging lineup consistency and player-specific weighting for enhanced accuracy.

By treating each lineup as a 'kernel' in the CNN, the model captures hierarchical relationships among players and team structures, applying weights to players based on time spent in-game and team consistency metrics. The model also incorporates a unique weighting system that adjusts for lineup stability, with higher importance assigned to consistent lineups. Player performance metrics are normalized, allowing the CNN to identify intricate patterns that contribute to game-winning probabilities. With this approach, the model provides a dynamic win/loss prediction percentage that accounts for individual and team-level contributions, enabling insights into the effects of varying lineups and strategic rotations. This model represents an innovative application of CNNs, typically used in computer vision, to sports analytics by interpreting player and team data in a structured, relational format akin to image features.
