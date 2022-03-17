create table if not exists genre (
	id serial primary key,
	genre_name varchar(80) not null unique
);
create table if not exists musician (
	id serial primary key,
	musician_name varchar(200) not null unique,
	genre_id integer references genre(id)
);
create table if not exists albums (
	id serial primary key,
	album_name text not null,
	release_date date not null,
	musician_id integer references musician(id)
);
create table if not exists tracks (
	id serial primary key,
	track_name text not null,
	duration time not null,
	album_id integer references albums(id)
);
