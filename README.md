# Proof Read this read me guy

# Site for logging your shows #
Back-End for the site made to log shows
### Tech used #
* Javascript
* AJAX
* Mongoose/MongoDB
* Passport
* bcrypt
* Django

### API Documentation


## Tasks

Terminal commands available to use all are prefaced with `npm run`

| Command                | Effect                                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| `server (serve, s)`  | Starts a development server with `nodemon` that automatically refreshes when you change something.            |
| `test`             | Runs automated tests.                                                                                           |
| `debug-server` | Starts the server in debug mode, which will print lots of extra info about what's happening inside the app.         |
| `start`            | Runs the server with a non-refreshing instance (no nodemon)                                                     |
| `debug-server`     | debugs server issues?                                                                                           |

## API

Scripts are included in [`curl-scripts`](curl-scripts) to test built-in actions.


### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up`             | `users#signup`    |
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/` | `users#changepw`  |
| DELETE | `/sign-out/`        | `users#signout`   |


#### POST /sign-up

Request:

```sh
curl --include --request POST http://localhost:4741/sign-up \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "an@example.email",
      "password": "an example password",
      "password_confirmation": "an example password"
    }
  }'
```

```sh
curl-scripts/auth/sign-up.sh
```

Response:

```md
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8

{
  "user": {
    "id": 1,
    "email": "an@example.email"
  }
}
```

#### POST /sign-in

Request:

```sh
curl --include --request POST http://localhost:4741/sign-in \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "an@example.email",
      "password": "an example password"
    }
  }'
```

```sh
curl-scripts/auth/sign-in.sh
```

Response:

```md
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "user": {
    "id": 1,
    "email": "an@example.email",
    "token": "33ad6372f795694b333ec5f329ebeaaa"
  }
}
```

#### PATCH /change-password/

Request:

```sh
curl --include --request PATCH http://localhost:4741/change-password/ \
  --header "Authorization: Bearer $TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "passwords": {
      "old": "an example password",
      "new": "super sekrit"
    }
  }'
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/auth/change-password.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

#### DELETE /sign-out/

Request:

```sh
curl --include --request DELETE http://localhost:4741/sign-out/ \
  --header "Authorization: Bearer $TOKEN"
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/auth/sign-out.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/shows`             | `shows#index`    |
| GET   | `/shows`             | `shows#get`    |
| PATCH  | `/shows/:id`         | `shows#update`  |
| DELETE | `/shows/:id`        | `shows#destroy`   |


#### POST /sign-up

Request:

```sh
curl --include "http://localhost:4741/shows" \

echo
```

```sh
curl-scripts/shows/index.sh
```


#### POST /shows

Request:

```sh
curl 'http://localhost:4741/shows' \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data '{
    "show": {
      "title": "'"${TITLE}"'",
      "director": "'"${DIRECTOR}"'",
      "rating": "'"${RATING}"'",
      "releaseDate": "'"${RELEASEDATE}"'",
      "description": "'"${DESC}"'"
    }
  }'

echo

```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa TITLE="avatar or smn" DIRECTOR="steven shpielberg i think" curl-scripts/shows/update.sh
```

Response:

```md
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "show": {
    "id": 53ad637ff795634b334ec5g329ebdfd,
    "title": "avatar or smn",
    "director": "steven shpielberd i think"
    "rating": null,
    "releaseDate": "null",
    "description": "null"
  }
}
```

#### PATCH /shows/:id

Request:

```sh
curl "http://localhost:4741/shows/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data '{
    "show": {
      "title": "'"${TITLE}"'",
      "director": "'"${DIRECTOR}"'",
      "rating": "'"${RATING}"'",
      "releaseDate": "'"${RELEASEDATE}"'",
      "description": "'"${DESC}"'"
    }
  }'

echo

```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa id=53ad637ff795634b334ec5g329ebdfd TITLE="not avatar or smn" DIRECTOR="not steven shpielberg i think" curl-scripts/shows/update.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

#### DELETE /shows/:id

Request:

```sh
curl "http://localhost:4741/shows/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Bearer ${TOKEN}" \

echo
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/shows/destroy.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

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
Went digital with this Wireframe, my physical ones didn't turn out that well so

![ERD](https://media.git.generalassemb.ly/user/32482/files/1f9c4a80-500f-11eb-8f30-08e2292b5a98)


### Future Plans, Problems to solve #

* Add personal user show list
* Add features to allow for dynamic show adding to that list
* Add features to allow for dynamic show removal from that list
* Stylize the Site
* add user reviews
