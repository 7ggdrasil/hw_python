create table if not exists Genre (
	genre_name varchar(100) primary key
);

create table if not exists Mus (
	id serial primary key,
	mus_name varchar(200) not null
);

create table if not exists MusGenre (
	mus_id int references Mus(id),
	genre_name varchar(100) references Genre(genre_name),
	constraint PK primary key(mus_id, genre_name)
);

create table if not exists Albums (
	id serial primary key,
	album_name text not null,
	release_date date not null,
	music_id int references Mus(id)
);

create table if not exists Tracks (
	id serial primary key,
	track_name text not null unique,
	duration time not null,
	track_id int unique references Albums(id)
);

create table if not exists TrackCollections (
	track_collection_name text not null,
	release_date date not null,
	track_id int references Tracks(id)
);