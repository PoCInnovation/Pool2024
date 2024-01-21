# PoC Software Pool 2023 - Day 02 - noSQL

**Day purposes**

✔️ Perform basic NoSQL queries, emphasizing MongoDB as a practical example.

✔️ Explore NoSQL database management tools.

✔️ Grasp the fundamentals of NoSQL databases, with a focus on MongoDB.

## Introduction

During the [day 01](../../day01), you learned a programming language to 
develop software. But a software isn't only composed of a hundred thousand
lines of code, it's common to use external tools to take in charge a specific
task. 😉<br>
For example, you can use [Prometheus](https://prometheus.io)/[Grafana](https://grafana.com) to monitor your app, [Kafka](https://kafka.apache.org) as a queue or a [database](https://en.wikipedia.org/wiki/Database) to store huge amount of data...

### What's a database?

It's an organized space where you can store pieces of information.
Each time you need a permanent storage, for example, to store users, you will
need a database.<br>
It has many usage and ways, the most popular is [SQL database](https://en.wikipedia.org/wiki/SQL) or 
also called [relational database](https://en.wikipedia.org/wiki/Relational_database). However, today, we will delve into the world of [NoSQL databases](https://en.wikipedia.org/wiki/NoSQL), and more specifically, [document databases](https://en.wikipedia.org/wiki/Document-oriented_database) like [MongoDB](https://en.wikipedia.org/wiki/MongoDB).

### Type of database

Today we will learn document database but other exists:

- [Relational](https://en.wikipedia.org/wiki/Relational_database)
- [Graph](https://en.wikipedia.org/wiki/Graph_database)
- [Column](https://en.wikipedia.org/wiki/Column-oriented_DBMS)
- [Key/Value](https://en.wikipedia.org/wiki/Key–value_database)
- [Search Engine](https://en.wikipedia.org/wiki/Database_search_engine)
- [Multi model](https://en.wikipedia.org/wiki/Multi-model_database)

> You can find more information about databases in this [post](https://fireship.io/lessons/top-seven-database-paradigms/) 😄

## Requirements

There are many tools to manage a database. We give you the choice between
[DataGrip](https://www.jetbrains.com/datagrip/) and [Compass IDE](https://www.mongodb.com/products/tools/compass).

> We recommend DataGrip for its powerful UX and easy adoption 😉

In the folder [resources](./resources), you will find a file named 
[database.json](./resources/database.json) to generate a new database
with artists and musics 🎵

Here's a schema of our data:
![Artists database](../../../.github/assets/software/software_bdd.png)

In document databases, data is stored into a [document](https://www.mongodb.com/docs/manual/core/document/) where each information is stored in an object as a [field-and-value](https://www.mongodb.com/docs/manual/core/document/).

You won't be using traditional relations as in a relational database, where you create [relationships](https://hasura.io/learn/database/postgresql/core-concepts/6-postgresql-relationships/) between tables 😄. Instead, in a document database, you have the flexibility to either [embed](https://www.mongodb.com/basics/embedded-mongodb) related data directly within a document or use [references](https://www.mongodb.com/docs/manual/reference/database-references/) to establish connections between documents.

> 💡 You can find more information about MongoDB concepts [here](https://www.mongodb.com/basics).

> These concepts are important, if you are lost don't hesitate to ask the staff for help they'll be happy to help you understand 😜

### DataGrip

> If you don't want to use DataGrip, move to the [Compass IDE](#compass-ide) setup.

First, download DataGrip using the [Jetbrains Toolbox](https://www.jetbrains.com/toolbox-app/).

You can use [docker](https://www.docker.com) to run a [MongoDB](https://www.mongodb.com/) 
database and [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/) to run the script to fill the documents

```shell
docker run -d \
  --name poc-mongo-db \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=pass \
  -v db:/var/lib/mongodb/data \
  mongo:latest
```

```shell
npm run start
## or
yarn start
```

> If you can't manage to connect to your database, try changing the POSTGRES_USER parameter to something else and reloading your container using ``docker rm``.

> Don't worry about this command for now, you will learn docker during day04 👀

Start DataGrip and create a new `Data Source` of type `MongoDB`.

Before entering the information chose the authentication method `User & Password`
<br>
Here's the information to fill in the form:
- Database name: `admin`
- Username: `admin`
- Password: `pass`
- Host: `localhost`
- Port: `27017`

> 💡 You will certainly have to download the MongoDB driver on your first connection.

Below you have an example of configuration:
![DataGrip configuration](../../../.github/assets/software/software_postresql_connection.png)


After applying the configuration, you should see a new data source in the left panel of DataGrip.

Verify that you have something similar to the example below:
![DataGrip data source](../../../.github/assets/software/software_postgresql_result.png)

> You can look a [these steps](https://www.jetbrains.com/help/datagrip/mongodb.html)
> if you encounter an issue during the configuration.

### Compass IDE

> This is a official IDE by MongoDB for MongoDB

- Go to [MongoDB Compass](https://www.mongodb.com/try/download/compass).
- Click on `Platform` and select `Ubuntu`.
- Click on `Download`.
- Go to your `Downloads/` folder.
- Execute this command: <br>
    ```sudo dpkg -i mongodb-compass_1.41.0_amd64.deb```
- Open compass from you applications

You should get the following result

![sql ide online result](../../../.github/assets/software/software_bdd_compass.png)

## Step 0 - Setup
### 📑 Description:
If you correctly followed the requirements, you should have a database
ready to use 😍

### 📌 Tasks:
You will just need to create a new directory in your pool repository to
submit your work:
```shell
mkdir -p day02
```

This day is composed of two parts, so for now you will push your work in the directory `SQL` 😉
```shell
mkdir -p day02/SQL
```

Create a file `queries.md` in which you will write every query you make to keep a trace:
```shell
touch queries.md
```

## Step 1 - Basics
### 📑 Description:
Your database is ready to run your first requests 🥳

The goal of this step is to understand how to read data in a database using
[SQL](https://en.wikipedia.org/wiki/SQL).

Let's try to get some information from the table `artists`.

### 📌 Tasks:
Write 3 queries to :
- Retrieve **all** the information contained in the `artists` table.
- Retrieve **only** `name` and `genre` from the table `artists`.
- Retrieve the list of all `artists` of `genre` `hip-hop/rap`.

### 📚 Documentation:
> See how to [read data in SQL](https://sql.sh/cours/select) or in [PostgreSQL](https://www.postgresql.org/docs/9.5/sql-select.html).

## Step 2 - Relations
### 📑 Description:
As we said before, a relational database is perfect to handle data with 
multiple relations between them.

### 📌 Tasks:
Let's write 3 new queries to link information from tables:
- Retrieve `name` from `artists` and `musics`.<br>
You must specify the name of your result column with `artists_names` and `musics_names`.
- Retrieve all `artist` who singed in the music `We Are The World`.<br>
Those artists must be sorted in `descending` order according to their number of fans.
- Retrieve all the `musics` from `Booba`.<br>
They must be sorted in `alphabetical` order.

### 📚 Documentation:
> See [how to sort data](https://docs.postgresql.fr/9.2/queries-order.html)
> and [join in SQL](https://sql.sh/cours/jointures).

## Step 3 - CRUD
### 📑 Description:
Yesterday, you programmed the CRUD of a resource, let's learn how to do it using SQL 💪

### 📌 Tasks:
Write 3 queries to:
- Add a new `artist` with his `id` set to `100`.
- Delete all musics that have the `Gold` `certification`.
- Add the music `Take What You Want` to the `artists` you previously created.

> ⚠️ `artists` and `musics` are linked using a relationship table, you
> will maybe need to do 2 queries to delete records.

### 📚 Documentation:
> See how [create](https://www.w3schools.com/sql/sql_insert.asp) or 
> [delete](https://www.w3schools.com/sql/sql_delete.asp) data in SQL.

## Step 4 - Good counts make good friends
### 📑 Description:
You've learned the basics, let's see more advanced features with pre-processing SQL functions 🧐

### 📚 Documentation
You will use functions to [count elements](https://www.w3schools.com/sql/sql_count_avg_sum.asp) directly from SQL.

> 💡 Databases are faster than any programming language (except C) so if you can pre-process your data in your query, do it.

### 📌 Tasks:
Write 4 new queries to:
- Count the number of `artists`
- Count the number of `artists` in each `genre`.
- Count the number of `musics` sorted by their certification and displayed in ascending order.
- Count the number of `musics` of each `artists`, sorted by their certification and 
displayed in ascending order.

> ⚠️ Be sure you never count the same music two time.

> You'll certainly need to [group element in SQL](https://www.w3schools.com/sql/sql_groupby.asp) 😉

## Step 5 - Rap Game
### 📑 Description:
You have certainly noticed, there are several kind of musics related to rap: 
the `rap` and `hip-hop/rap`.

We would like to organize a concert with all the rappers in our database, but
for that, we need a list of them.
### 📌 Tasks:
Write a query that retrieve all the rappers in the database, sorted in 
descending order by their fans' number.
### 📚 Documentation:
> 💡 You'll maybe need to [manipulate string](https://www.tutorialspoint.com/sql/sql-string-functions.htm) 
> and [cast data](https://www.w3schools.com/sql/func_sqlserver_cast.asp). 

## To go further

Congratulation, you now have solid knowledge in SQL 🎉

Here are some links for the most courageous among you:

- [Organize your database with schemas](https://www.postgresql.org/docs/14/ddl-schemas.html)
- [Create your own PostgreSQL function](https://www.postgresql.org/docs/14/xfunc-sql.html)
- [Automate task with triggers](https://www.postgresql.org/docs/14/trigger-definition.html)
- [Improve query performance](https://www.postgresql.org/docs/14/performance-tips.html)

<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn logo">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram logo"
>
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter logo">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord logo">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white" alt="Website logo">
    </a>
</p>

> 🚀 Don't hesitate to follow us on our different networks, and put a star 🌟 on `PoC's` repositories.
