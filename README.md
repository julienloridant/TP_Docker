Exercice 3 : 
1. Vérifiez la version de Docker :
docker --version

Résultat : 
Docker version 29.9.2, build a82e528


2. Listez les images disponibles sur votre machine :
docker images

IMAGE                    ID             DISK USAGE   CONTENT SIZE   EXTRA
chromadb/chroma:latest   1e0b73a187a2        826MB          176MB    U     -> projet perso
hello-world:latest       c567b231f656       25.9kB         9.49kB    U   


3. Téléchargez une image depuis Docker Hub :
docker pull hello-world

Using default tag: latest
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest



4. Exécutez un conteneur à partir de l'image :
docker run hello-world



5. Listez les conteneurs en cours d'exécution :
docker ps
Ici pas de hello-world actif car il a fini d'afficher son texte 


6. Listez tous les conteneurs (actifs et stoppés) :
docker ps -a
→ Affiche tout l’historique des conteneurs.
7. Supprimez un conteneur :
docker rm <ID_conteneur>
8. Supprimez une image :
docker rmi <ID_image>