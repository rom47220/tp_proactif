# 🧠 Sensibilisation par la pratique — TP Sécurité Proactive

Ce projet complète la première partie du TP en ajoutant une dimension **pédagogique et interactive** autour des vulnérabilités web les plus courantes.  
L’objectif est de **renforcer la compréhension** des attaques et contre-mesures via un **quiz** et un **mini CTF** hébergé sur une plateforme dédiée.

---

## 📝 Objectifs pédagogiques

- ✅ Identifier et comprendre les principales vulnérabilités web (SQLi, XSS, Command Injection, etc.)  
- ✅ Sensibiliser aux bonnes pratiques de développement sécurisé  
- ✅ Mettre en place des activités interactives pour tester et ancrer les connaissances

---

## 📊 1️⃣ Quiz interactif (Kahoot)

Un **quiz de 10 questions** a été conçu pour sensibiliser les participants aux risques et bonnes pratiques.  
Il mélange des QCM et des questions Vrai/Faux couvrant :

- Injection SQL  
- XSS réfléchi  
- Headers HTTP de sécurité  
- Command injection  
- Bonnes pratiques DevSecOps (CodeQL, Dependabot…)

👉 **Lien du quiz** : [👉 Accéder au Kahoot](https://kahoot.it/)  
*(remplacer par le lien public de ton quiz une fois publié)*

---

## 🏁 2️⃣ Mini CTF — Capture The Flag

Un mini CTF a été mis en place pour permettre aux participants de **mettre en pratique leurs connaissances** en exploitant des vulnérabilités réelles dans un environnement contrôlé.

### ⚔️ **Challenges inclus** :
| Nom du challenge             | Type de vulnérabilité      | Objectif |
|------------------------------|-----------------------------|----------|
| 🐍 `sql_injection_basic`     | Injection SQL              | Extraire un flag en exploitant une requête vulnérable |
| 📤 `malicious_upload`       | Upload de fichier          | Obtenir une webshell en uploadant un fichier interdit |
| 💥 `command_injection_ping` | Exécution de commande      | Obtenir un flag en exploitant un formulaire ping vulnérable |

👉 Chaque challenge expose une vulnérabilité courante et illustre une **erreur fréquente de développement**.

---

## 🧰 3️⃣ Plateforme CTF

Les challenges sont hébergés sur la plateforme [**CTFd**](https://github.com/CTFd/CTFd), déployée localement pour l’occasion.

- 🌐 Accès : `http://<adresse-ctfd>`  
- 👤 Compte participant : `student / student`  
- 📌 3 flags à trouver pour compléter le CTF