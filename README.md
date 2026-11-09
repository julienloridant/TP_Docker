# Exercice 3 – Prise en main de Docker

## 1. Vérifier la version de Docker

**Commande :**
```bash
docker --version
```

**Résultat :**
```text
Docker version 29.9.2, build a82e528
```

## 2. Lister les images disponibles sur la machine

**Commande :**
```bash
docker images
```

**Résultat :**
```text
IMAGE                    ID             DISK USAGE   CONTENT SIZE   EXTRA
chromadb/chroma:latest   1e0b73a187a2        826MB          176MB    U
hello-world:latest       c567b231f656       25.9kB         9.49kB    U
```

L'image `chromadb/chroma` est utilisée dans le cadre d'un projet personnel.

## 3. Télécharger une image depuis Docker Hub

**Commande :**
```bash
docker pull hello-world
```

**Résultat :**
```text
Using default tag: latest
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```

L'image `hello-world` a été téléchargée avec succès depuis Docker Hub.

## 4. Exécuter un conteneur à partir de l'image

**Commande :**
```bash
docker run hello-world
```

Le conteneur s'exécute et affiche un message de bienvenue confirmant le bon fonctionnement de Docker.

## 5. Lister les conteneurs en cours d'exécution

**Commande :**
```bash
docker ps
```

Aucun conteneur `hello-world` n'apparaît dans la liste, car son exécution est terminée après l'affichage du message.

## 6. Lister tous les conteneurs (actifs et arrêtés)

**Commande :**
```bash
docker ps -a
```

**Résultat :**
```text
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS                      PORTS     NAMES
0d0f90390fa2   hello-world       "/hello"                 2 minutes ago    Exited (0) 2 minutes ago              wizardly_almeida
691925339fd6   hello-world       "/hello"                 7 minutes ago    Exited (0) 7 minutes ago              loving_pascal
2cac4c507662   chromadb/chroma   "dumb-init -- chroma…"   9 minutes ago    Exited (0) 9 minutes ago              goofy_goodall
5564067fde83   hello-world       "/hello"                 12 minutes ago   Exited (0) 12 minutes ago             boring_blackburn
7ae1f8d0e1be   chromadb/chroma   "dumb-init -- chroma…"   4 days ago       Exited (0) 4 days ago                 chroma
```

On constate que plusieurs conteneurs sont arrêtés (`Exited (0)`). Cela signifie qu'ils se sont terminés correctement.

## 7. Supprimer un conteneur

**Commande :**
```bash
docker rm loving_pascal
```

Le conteneur est supprimé en utilisant son nom (`loving_pascal`).

Ce nom a été généré automatiquement par Docker lors de la création du conteneur. Il est également possible d'utiliser son identifiant (`CONTAINER ID`).

## 8. Supprimer une image

**Commande :**
```bash
docker rmi hello-world
```

**Résultat :**
```text
Untagged: hello-world:latest
Deleted: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
```

L'image `hello-world` a été supprimée de la machine.




## 4. Exercice : Création d'un serveur web avec Docker

**1. Téléchargement de l'image officielle Nginx :**

```bash
docker pull nginx
```

Résultat :
```text
Using default tag: latest
latest: Pulling from library/nginx
6d2e43921e9e: Pull complete
37fb86c2a767: Pull complete
bbb080c71d50: Pull complete
1962e1ff75b4: Pull complete
512ac5e7ce8e: Pull complete
1724c05f72c6: Pull complete
7cb4701ce7cd: Pull complete
4582dace95e2: Download complete
d2c7e31f04a3: Download complete
Digest: sha256:165ddde8751e75a1c907d24ef10d9f6deb08b57e0fe56caf67512486aff76d82
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
```

**2. Lancement d'un conteneur Nginx en arrière-plan :**

```bash
docker run -d -p 8080:80 --name mon_nginx nginx
```

→ Démarrage d'un serveur web accessible sur http://localhost:8080.

Résultat :
```text
3d3329f7512e87b12930b1f3e6b0a0a9e7444475198ced0c0679d47224886312
```

**3. Vérification de l'activité du conteneur :**

```bash
docker ps
```

Résultat :
```text
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                     NAMES
3d3329f7512e   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx
```

**4. Accès à la page par défaut de Nginx depuis le navigateur :**

Adresse : http://localhost:8080

**5. Arrêt du conteneur :**

```bash
docker stop mon_nginx
```

Résultat :
```text
mon_nginx
```