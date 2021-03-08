# Site for logging your shows #
Back-End for the site made to log shows
### Tech used #
* Python
* Axios
* Passport
* bcrypt
* Django
* Postgresql

### API Documentation


## Tasks

Terminal commands available to use all are prefaced with `python *python route* `

| Command                | Effect                                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| `manage.py runserver )`  | Starts the server         |
| `makemigrations`             | Makes modifications Models   |
| `migrate` | Applies the modifications from the migrations        |

## API

Scripts are included in [`curl-scripts`](curl-scripts) to test built-in actions.


### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up`             | `users#signup`    |
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/` | `users#changepw`  |
| DELETE | `/sign-out/`        | `users#signout`   |

### Shows

| Action | Verb | URI Pattern |
| ----------- | ----------- | ----------- |
| POST | Create | `/shows`
| GET | Index | `/shows`
| GET | Show | `/shows/:id`
| PATCH | Update | `/shows/:id`
| DELETE | Delete | `/shows/:id`

### Planning and Organization #
1. Created ERD and user stories.
2. Created auth routes
3. Created show routes
4. Handle front-end
### User Stories #

* I want to be able to sign up
* I want to be able to sign-in
* I want to be able to change my password
* I want to be able to sign-out
* I want to be able to add a show to my watched shows
* I want to be able to see who made the show
* I want to be able to see when the show came out
* I want to be able to see a description of the show
* I want to be able to write about the shows I've seen
* I want to be able to search from a list of shows already stored

### Wireframes #
More relations to come

![ERD](https://media.git.generalassemb.ly/user/32482/files/1f9c4a80-500f-11eb-8f30-08e2292b5a98)


### Future Plans, Problems to solve #

* Add personal user show list
* Add features to allow for dynamic show adding to that list
* Add features to allow for dynamic show removal from that list
* Stylize the Site
* add user reviews
