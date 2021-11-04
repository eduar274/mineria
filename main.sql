create table articulos(
    id varchar(15) primary key,
    nombre_categoria varchar(80),
    precio_avg varchar(80),
    rating_avg decimal(6,2)
)

create table reviews(
    id varchar(10) primary key,
    titulo varchar(50),
    comentario varchar(500),
    rating_avg decimal(6,2),
    fecha varchar(30),
    id_articulo varchar(15),
    CONSTRAINT FK_articulo FOREIGN KEY (id_articulo)
    REFERENCES articulos(id) 
)