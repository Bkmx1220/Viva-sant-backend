# VivaSanté API Specification v1.0

## Informations générales

* Version : 1.0
* Backend : Django 5 + Django REST Framework
* Authentification : JWT
* Base URL (Développement) : `http://127.0.0.1:8000/api/`

---

# Authentification

## POST /auth/register/

Créer un compte utilisateur.

### Requête

```json
{
  "first_name": "Jean",
  "last_name": "Dupont",
  "email": "jean@example.com",
  "password": "Password123!"
}
```

### Réponse

```json
{
  "message": "Compte créé avec succès"
}
```

---

## POST /auth/login/

Connexion.

### Requête

```json
{
  "email": "jean@example.com",
  "password": "Password123!"
}
```

### Réponse

```json
{
  "access": "...",
  "refresh": "...",
  "user": {
    "id": 1,
    "first_name": "Jean",
    "last_name": "Dupont",
    "email": "jean@example.com"
  }
}
```

---

## POST /auth/refresh/

Renouveler le token.

---

## POST /auth/logout/

Déconnexion.

---

# Utilisateur

## GET /users/me/

Retourne le profil connecté.

---

# Dashboard

## GET /dashboard/

Retourne :

* Score santé
* Calories
* Eau
* Pas
* Activité

---

# Nutrition

## POST /nutrition/analyze/

Analyse IA d'un repas.

Entrée :

* image

Retour :

* Calories
* Protéines
* Lipides
* Glucides
* Recommandations

---

## GET /nutrition/history/

Historique des repas.

---

# Coach IA

## POST /ai/chat/

Chat avec l'assistant santé.

---

# Activité

## GET /activity/

Historique.

## POST /activity/

Ajouter une activité.

---

# Profil

## GET /profile/

Profil utilisateur.

## PUT /profile/

Modifier le profil.

---

# Notifications

## GET /notifications/

Liste.

## PUT /notifications/{id}/

Marquer comme lue.
