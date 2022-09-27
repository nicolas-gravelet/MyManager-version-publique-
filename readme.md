# MyManager - version publique

## Utilisation
`$> docker-compose build && docker-compose up`

## Description
MyManager est une application web permettant à l'utilisateur de gérer différentes choses.
Elle est pour l'instant constituée de 3 parties :

 - Media Manager
 
Gestion de la médiathèque personnelle de l'utilisateur (s'adaptant aux films et séries en DVD et blu-ray aussi bien qu'aux jeux vidéos)

- Career Manager

Aide à la recherche d'emploi/stage/alternance permettant à l'utilisateur de constituer un tableau avec l'ensemble des offres auxquelles il a pu postuler, pour lui faciliter le suivi des processus de recrutement. Il a également accès à différentes plateformes de recrutement via cet espace.

- Rent Manager

 Gestion locative axée pour les utilisateurs de plateformes de style Aibnb. Permet de répertorier les informations sur les locataires et leur séjour afin de faciliter certaines démarches (notamment la déclaration de revenus locatifs)

## Panneau de configuration (en développement)
Cette application, aujourd'hui en développement, possède également un panneau de configuration composé de parties (pour l'instant)

- Paramètres RentManager

Permet de configurer l'accès à une annonce Airbnb pour permettre à l'utilisateur de la modifier rapidement via le site d'Airbnb (si l'utilisateur passe par cette plateforme pour sa location), mais également de rentrer le prix du loyer quotidien (permettant le calcul automatique du prix total lors de la saisie des dates du séjour)

- Etat des services

Permet de vérifier la liaison au serveur back-end et à ses différentes fonctionnalités, ainsi que la connexion à Internet

## Technologies utilisées
### Containerisation
Docker et docker-compose

### Front-end
JavaScript (framework Vue.js)

### Back-end
Python (framework Django [DRF])
