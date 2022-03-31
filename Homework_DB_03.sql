create table if not exists Mus (
	id serial primary key,
	mus_name varchar(200) not null
);

create table if not exists Genre (
	id serial primary key,
	genre_name varchar(100) unique
);

create table if not exists MusGenre (
	mus_id int references Mus(id),
	genre_id int references Genre(id),
	constraint PK primary key(mus_id, genre_id)
);

create table if not exists Albums (
	id serial primary key,
	album_name text not null,
	release_date date not null
);

create table if not exists MusAlbums (
	mus_id int references  Mus(id),
	album_id int references Albums(id),
	constraint MA primary key(mus_id, album_id)
);

create table if not exists Tracks (
	id serial primary key,
	track_name text not null unique,
	duration time not null,
	track_id int references Albums(id)
);

create table if not exists Collection (
	id serial  primary key,
	track_collection_name text not null,
	release_date date not null	
);

create table if not exists TrackCollection (
	track_id int references Tracks(id),
	collect_id int references  Collection(id),
	constraint TC primary key(track_id, collect_id)	
);






