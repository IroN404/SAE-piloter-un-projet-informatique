# Documentation d'utilisation du code ToDoList

Ce code est une application de liste de tâches simple créée avec PyQt5, une bibliothèque Python pour le développement d'interfaces graphiques. L'application permet à l'utilisateur d'ajouter des tâches à une liste, en spécifiant diverses informations telles que l'étiquette, la tâche elle-même, le statut, la priorité, la personne responsable, la date de début et la date butoir. De plus, il y a une option pour marquer les tâches comme terminées. L'interface utilisateur de l'application offre également un mode jour/nuit, où le fond de l'application et le logo changent de couleur en fonction du mode sélectionné.

## Utilisation de l'application

1. **Lancement de l'application**:
   - L'application est lancée en exécutant le script Python. Assurez-vous d'avoir PyQt5 installé.

2. **Interface principale**:
   - Une fenêtre principale s'ouvre avec un logo en haut à gauche et un bouton "Ajouter une Tache" en haut à droite.

3. **Ajout d'une tâche**:
   - Cliquez sur le bouton "Ajouter une Tache" pour ajouter une nouvelle tâche à la liste. Une nouvelle section de saisie de tâche apparaît en dessous de la précédente.

   - Vous pouvez remplir les champs suivants pour chaque tâche :
     - **Étiquette** : Ajoutez une étiquette pour la tâche.
     - **Tâche** : Saisissez la description de la tâche.
     - **Statut** : Sélectionnez le statut de la tâche parmi les options "En cours" ou "En attente".
     - **Priorité** : Sélectionnez la priorité de la tâche parmi les options "P1", "P2", ou "P3".
     - **Personne** : Ajoutez la personne responsable de la tâche.
     - **Date de début** : Sélectionnez la date de début de la tâche.
     - **Date butoir** : Sélectionnez la date butoir de la tâche.
     - **Tâche finie** : Cochez cette case si la tâche est terminée.

4. **Changement de mode jour/nuit**:
   - Cliquez sur le logo en haut à gauche pour basculer entre le mode jour et le mode nuit. Le fond de l'application et le logo changeront de couleur en conséquence.

5. **Validation des champs**:
   - Appuyez sur "Entrée" après avoir saisi les informations dans chaque champ pour les valider. Les informations saisies seront affichées sous forme d'étiquettes et le champ de saisie sera supprimé.

6. **Modification du statut et de la priorité**:
   - Si vous sélectionnez une option dans le menu déroulant "Statut" ou "Priorité", cela sera également affiché sous forme d'étiquette avec une couleur associée.

7. **Marquer une tâche comme terminée**:
   - Cochez la case "Tâche finie" pour marquer une tâche comme terminée. La date actuelle sera affichée à la place de la case cochée.

8. **Fermeture de l'application**:
   - Vous pouvez fermer l'application en cliquant sur le bouton de fermeture de la fenêtre.

C'est tout ce qu'il y a à savoir pour utiliser cette application ToDoList. Elle vous permet de gérer votre liste de tâches de manière simple et intuitive tout en offrant une option de personnalisation avec le mode jour/nuit.
