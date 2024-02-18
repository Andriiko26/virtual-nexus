## Technologys
<div align="center">
	<table>
		<tr>
			<td><code><img width="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" alt="HTML" title="HTML"/></code></td>
			<td><code><img width="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" alt="CSS" title="CSS"/></code></td>
			<td><code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code></td>
			<td><code><img width="50" src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" alt="Django" title="Django"/></code></td>
			<td><code><img width="50" src="https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png" alt="PostgreSQL" title="PostgreSQL"/></code></td>
		</tr>
	</table>
</div>

# Social media
It's only beck-end part so I took all the front-end from ChatGPT

## Futures
Posts:
- View all posts
- Adding your post with tags
- Commenting posts
- Like post
- Searching for an article
- Markdown is supported
- Edit post
- Pagination of posts on one page
- Deleting posts

Users:
- Change your username.
- Adding a profile photo
- Adding a description to your profile

API:
- Get all posts
- Creating your own
- Like post and get like counter
- Commenting posts and get list of comments
- Searching posts

## Endpoints
- List of posts: `api/v1/`
- Search for posts `search/`
- Detail of post: `api/v1/id`
- Like post: `api/v1/id/like`
- List of comments: `api/v1/id/comments`
- Add a comment: `api/v1/id/comments/create`
- Get token: `api/v1/token`
- Create post: `api/v1/create/`

## To run it on your machine
Clone the ropository: `git clone https://github.com/Maksim325/virtual-nexus.git`

Go to directory: `cd "virtual nexus"`

Create virtual environment and activate it: `python -m venv venv`, `venv\Scripts\activate` 

Or if you in Linux: `source venv\bin\activate`

Install requariments: `pip install -r requariments.txt`

Go to project directory and run server: `cd virual_nexus_project`, `python manage.py runserver`

## Envsroment
Setup all this enviroment
```
#django
SECRET_KEY=
DEBUG=
PRODUCT=

#postgree
NAME=
USER=
PASSWORD=
HOST=
PORT=

#email
DEFAULT_FROM_EMAIL=

#pagination
API_PAGINATION=
POST_PAGINATION=
```

## If you find a bug
Contact me: garvatmaksim@gmail.com