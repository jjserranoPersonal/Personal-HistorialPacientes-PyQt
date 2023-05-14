drop database historial_pacientes; #Eliminar base de datos 
drop table historial; #Eliminar Tabla
truncate paciente;
truncate historial;
#---------------------
use historial_pacientes;
SELECT * FROM usuarios;
SELECT * FROM paciente;
SELECT * FROM historial;
insert into usuarios (usuario,password) values 
('jserrano','123456');
#----------------------------------------------------------------------------------
#Creacion de base de  datos historial_pacientes
#----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS paciente (id INTEGER PRIMARY KEY AUTOINCREMENT,
					identificacion VARCHAR(50) UNIQUE NOT NULL,
					nombres VARCHAR(100) NOT NULL, 
					apellidos VARCHAR(100) NOT NULL,
                    direccion VARCHAR(200),
                    correo VARCHAR(100),
                    telefono VARCHAR(50),
                    fechaNacimiento date,
                    sexo VARCHAR(1),
                    transfusiones VARCHAR(2),
                    peso VARCHAR(20),
                    talla VARCHAR(20),
                    habitosToxicos VARCHAR(300),
                    alergiaMedicamentos VARCHAR(300),
                    vacunacion VARCHAR(300),
                    app VARCHAR(300),
                    apf VARCHAR(300),
                    nombreAcompanante VARCHAR(200),
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
                    		
CREATE TABLE IF NOT EXISTS historial (id INTEGER PRIMARY KEY AUTOINCREMENT,
					pacienteId INT NOT NULL,
					estado VARCHAR(1000), 
					hea VARCHAR(1000), 
                    impDiagnostica VARCHAR(1000), 
                    conductaSeguir VARCHAR(1000), 
                    motivoConsulta VARCHAR(1000), 
                    temperatura VARCHAR(20), 
                    tensionArterial VARCHAR(20), 
                    freCardiaca VARCHAR(20), 
                    freRespiratoria VARCHAR(20), 
                    oxigenacion VARCHAR(20), 
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
                    FOREIGN KEY (pacienteId) REFERENCES paciente (id));    
                    
 CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,
					usuario VARCHAR(50) UNIQUE NOT NULL, 
					password VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);             
                    
                    
                  
                  