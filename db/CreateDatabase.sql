USE toDoList_SQL

CREATE TABLE tarefas (
	id integer not null auto_increment,
	titulo varchar(100),
	estado varchar(100),
	PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO tarefas (titulo, estado) VALUES ('Estudar Python', 'Pendente');
INSERT INTO tarefas (titulo, estado) VALUES ('Fazer exercícios de Flask', 'Concluída');
INSERT INTO tarefas (titulo, estado) VALUES ('Preparar apresentação', 'Em andamento');