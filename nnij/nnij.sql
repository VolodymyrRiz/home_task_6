-- Table: groups_nnij
DROP TABLE IF EXISTS groups_nnij;
CREATE TABLE groups_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ VARCHAR(3) UNIQUE NOT NULL
);

-- Table: students_nnij
DROP TABLE IF EXISTS students_nnij;
CREATE TABLE students_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR(30) UNIQUE NOT NULL,
    groups_nnij_id INTEGER,
    FOREIGN KEY (groups_nnij_id) REFERENCES groups_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: teachers_nnij
DROP TABLE IF EXISTS teachers_nnij;
CREATE TABLE teachers_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher VARCHAR(5) UNIQUE NOT NULL,
    groups_nnij_id INTEGER,
    FOREIGN KEY (groups_nnij_id) REFERENCES groups_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: subjects_nnij
DROP TABLE IF EXISTS subjects_nnij;
CREATE TABLE subjects_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_ VARCHAR(5) UNIQUE NOT NULL,
    teachers_nnij_id INTEGER,
    FOREIGN KEY (teachers_nnij_id) REFERENCES teachers_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: marks_nnij
DROP TABLE IF EXISTS marks_nnij;
CREATE TABLE marks_nnij (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    students_nnij_id INTEGER,
    subjects_nnij_id INTEGER,
    mark INTEGER,
    FOREIGN KEY (students_nnij_id) REFERENCES students_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    FOREIGN KEY (subjects_nnij_id) REFERENCES subjects_nnij (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
