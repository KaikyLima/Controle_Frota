-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-04-11 22:47:53 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE ctengate (
    id                INTEGER NOT NULL,
    dtengate          DATE NOT NULL,
    dtdesengate       DATE,
    veiculo_idveiculo INTEGER NOT NULL,
    nrfrota           INTEGER NOT NULL,
    nrconjunto        INTEGER NOT NULL
);

ALTER TABLE ctengate ADD CONSTRAINT ctengate_pk PRIMARY KEY ( id );

CREATE TABLE ctvinculo (
    id                    INTEGER NOT NULL,
    dtvinculo             DATE NOT NULL,
    dtdesvinculo          DATE,
    motorista_idmotorista INTEGER NOT NULL,
    veiculo_idveiculo     INTEGER NOT NULL,
    nrfrota               INTEGER NOT NULL
);

ALTER TABLE ctvinculo ADD CONSTRAINT ctvinculo_pk PRIMARY KEY ( id );

CREATE TABLE despesas (
    cod               INTEGER NOT NULL,
    tpgastos          VARCHAR2(100 CHAR) NOT NULL,
    dtemissao         DATE NOT NULL,
    nrnota            CHAR(10 CHAR) NOT NULL,
    valor             FLOAT NOT NULL,
    observacao        VARCHAR2(300 CHAR),
    veiculo_idveiculo INTEGER NOT NULL,
    fornecedor_cod    INTEGER NOT NULL
);

ALTER TABLE despesas ADD CONSTRAINT despesas_pk PRIMARY KEY ( cod );

CREATE TABLE fornecedor (
    cod          INTEGER NOT NULL,
    cnpj         CHAR(14) NOT NULL,
    nmfornecedor VARCHAR2(200 CHAR) NOT NULL
);

ALTER TABLE fornecedor ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( cod );

ALTER TABLE fornecedor ADD CONSTRAINT fornecedor__un UNIQUE ( cnpj );

CREATE TABLE funcionario (
    nrmatricula     INTEGER NOT NULL,
    nmfuncionario   VARCHAR2(100 CHAR) NOT NULL,
    dsfuncao        VARCHAR2(100 CHAR) NOT NULL,
    dtadmissao      DATE NOT NULL,
    pessoa_idpessoa INTEGER NOT NULL
);

ALTER TABLE funcionario ADD CONSTRAINT funcionario_pk PRIMARY KEY ( nrmatricula );

CREATE TABLE motorista (
    idmotorista             INTEGER NOT NULL,
    nmmotorista             VARCHAR2(100 CHAR) NOT NULL,
    funcionario_nrmatricula INTEGER NOT NULL,
    tpsituacao              VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE motorista ADD CONSTRAINT motorista_pk PRIMARY KEY ( idmotorista );

CREATE TABLE pessoa (
    idpessoa     INTEGER NOT NULL,
    nmpessoa     VARCHAR2(100 CHAR) NOT NULL,
    nrcpf        CHAR(11 CHAR) NOT NULL,
    dtnascimento DATE NOT NULL
);

ALTER TABLE pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( idpessoa );

ALTER TABLE pessoa ADD CONSTRAINT pessoa__un UNIQUE ( nrcpf );

CREATE TABLE veiculo (
    idveiculo         INTEGER NOT NULL,
    nrplaca           CHAR(7 CHAR) NOT NULL,
    dsmodelo          VARCHAR2(100 CHAR) NOT NULL,
    tptracao          VARCHAR2(40 CHAR) NOT NULL,
    nrrenavam         CHAR(11 CHAR) NOT NULL,
    dtaquisicao       DATE NOT NULL,
    nrfrota           INTEGER,
    nrconjunto        INTEGER,
    nrchassi          VARCHAR2(17 CHAR) NOT NULL,
    tpcombustivel     VARCHAR2(100 CHAR),
    anoveic           INTEGER NOT NULL,
    dsmarca           VARCHAR2(100 CHAR) NOT NULL,
    qteixo            INTEGER NOT NULL,
    veiculo_idveiculo INTEGER,
    tpveiculo         VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE veiculo ADD CONSTRAINT veiculo_pk PRIMARY KEY ( idveiculo );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo__un UNIQUE ( nrplaca,
                                        nrrenavam,
                                        nrchassi );

ALTER TABLE ctengate
    ADD CONSTRAINT ctengate_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

ALTER TABLE ctvinculo
    ADD CONSTRAINT ctvinculo_motorista_fk FOREIGN KEY ( motorista_idmotorista )
        REFERENCES motorista ( idmotorista );

ALTER TABLE ctvinculo
    ADD CONSTRAINT ctvinculo_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

ALTER TABLE despesas
    ADD CONSTRAINT despesas_fornecedor_fk FOREIGN KEY ( fornecedor_cod )
        REFERENCES fornecedor ( cod );

ALTER TABLE despesas
    ADD CONSTRAINT despesas_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

ALTER TABLE funcionario
    ADD CONSTRAINT funcionario_pessoa_fk FOREIGN KEY ( pessoa_idpessoa )
        REFERENCES pessoa ( idpessoa );

ALTER TABLE motorista
    ADD CONSTRAINT motorista_funcionario_fk FOREIGN KEY ( funcionario_nrmatricula )
        REFERENCES funcionario ( nrmatricula );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

CREATE SEQUENCE ctengate_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctengate_id_trg BEFORE
    INSERT ON ctengate
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := ctengate_id_seq.nextval;
END;
/

CREATE SEQUENCE ctvinculo_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctvinculo_id_trg BEFORE
    INSERT ON ctvinculo
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := ctvinculo_id_seq.nextval;
END;
/

CREATE SEQUENCE funcionario_nrmatricula_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER funcionario_nrmatricula_trg BEFORE
    INSERT ON funcionario
    FOR EACH ROW
    WHEN ( new.nrmatricula IS NULL )
BEGIN
    :new.nrmatricula := funcionario_nrmatricula_seq.nextval;
END;
/

CREATE SEQUENCE motorista_idmotorista_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER motorista_idmotorista_trg BEFORE
    INSERT ON motorista
    FOR EACH ROW
    WHEN ( new.idmotorista IS NULL )
BEGIN
    :new.idmotorista := motorista_idmotorista_seq.nextval;
END;
/

CREATE SEQUENCE pessoa_idpessoa_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER pessoa_idpessoa_trg BEFORE
    INSERT ON pessoa
    FOR EACH ROW
    WHEN ( new.idpessoa IS NULL )
BEGIN
    :new.idpessoa := pessoa_idpessoa_seq.nextval;
END;
/

CREATE SEQUENCE veiculo_idveiculo_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER veiculo_idveiculo_trg BEFORE
    INSERT ON veiculo
    FOR EACH ROW
    WHEN ( new.idveiculo IS NULL )
BEGIN
    :new.idveiculo := veiculo_idveiculo_seq.nextval;
END;
/



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             8
-- CREATE INDEX                             0
-- ALTER TABLE                             19
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           6
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          6
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
