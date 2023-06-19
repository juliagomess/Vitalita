const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
const sha256 = require('sha256'); //encriptar senha

const bodyParser = require('body-parser');
const cors = require('cors');

const fs = require('fs');

app.use(cors());
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

let port = process.env.port || 3000;

const mysql = require('mysql');

const con = mysql.createConnection({
    host: 'localhost', // O host do banco. Ex: localhost
    user: 'root', // Um usuário do banco. Ex: user 
    password: '', // A senha do usuário. Ex: user123
    database: 'db_extcomp' // A base de dados a qual a aplicação irá se conectar, deve ser a mesma onde foi executado o Código 1. Ex: node_mysql
});

const assetsDir = './front/assets/logo/'
const mediaDir = '../Vitalita Web/sistematrabalhista/src/media/'

function base64_encode(file) {
    // read binary data
    var bitmap = fs.readFileSync(mediaDir+file);
    // convert binary data to base64 encoded string
    return new Buffer(bitmap).toString('base64');
}

function copiarArquivo(srcDir,destDir) {
    fs.copyFileSync(mediaDir+srcDir,assetsDir+destDir);
}

con.connect((err) => {
    if (err) {
        console.log('Erro connecting to database...', err)
        return
    }
    console.log('Connection established!')
});

var idUser;

app.post('/login', async(req,res) => {
    con.query('SELECT * FROM associado  WHERE email = ?', [req.body.emailUser], (err, rows) => {
        if (err) throw err
    
        if(rows[0] != undefined) {
            let senhaHash = sha256(req.body.senhaUser)
            let senhaBD = rows[0].senha_hash;
            if(senhaBD == senhaHash) {
                console.log('Entrou ');
                idUser = rows[0].id;
                res.json({login: 0});
            }
            else {
                console.log('Senha incorreta');
                res.json({login: 1});
            }    
        }
        else {
            console.log('Este usuário não existe');
            res.json({login: 2});
        }   
    })
});

app.get('/curriculo', async(req,res) => {

    console.log(idUser);

    con.query('SELECT * FROM curriculo WHERE associado_id = ?', idUser, (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) { //curriculo ja existe, atualiza
            res.json({instituicao: rows[0].instituicao_ensino,
                      cursos: rows[0].curso_extra,
                      empresas: rows[0].empresa_trabalhada,
                      cargos: rows[0].cargo_ocupado
            });
        } else { //currculo não existe, cadastra
            res.json({instituicao: "",
                      cursos: "",
                      empresas: "",
                      cargos: ""
            });
        }
    }); 
});

app.post('/create', async(req,res) => {
    let inst = req.body.instituicaoUser;
    let curso = req.body.cursosUser;
    let emp = req.body.empresasUser;
    let cargo = req.body.cargosUser;

    con.query('SELECT * FROM curriculo WHERE associado_id = ?', idUser, (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) { //curriculo ja existe, atualiza
            con.query('UPDATE curriculo SET instituicao_ensino = ?, curso_extra = ?, empresa_trabalhada = ?, cargo_ocupado = ? WHERE associado_id = ?',
                [inst,curso,emp,cargo,idUser], (err, rows) => {
                    if (err) throw err

                    console.log('Currículo atualizado com sucesso');
                    
                });
        } else { //currculo não existe, cadastra
            con.query('INSERT INTO curriculo(associado_id, instituicao_ensino, curso_extra, empresa_trabalhada, cargo_ocupado) VALUES (?, ?, ?, ?, ?)',
                [idUser,inst,curso,emp,cargo], (err, rows) => {
                    if (err) throw err

                    console.log('Currículo cadastrado com sucesso');
                    
                })
        }
        
    });    
});

app.get('/delete', async(req,res) => {

    con.query('DELETE FROM curriculo WHERE associado_id = ?',idUser, (err, rows) => {
        if (err) throw err

        console.log('Currículo deletado com sucesso');
        
    })
});

app.get('/cursos', async(req,res) => {

    con.query('SELECT * FROM curso', (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {

            for(let i=0;true;i++){
                if(rows[i]==undefined)
                    break
                else {
                    rows[i].logo = base64_encode(rows[i].logo)
                    // copiarArquivo(rows[i].logo,'curso/curso'+ rows[i].id + '.png');
                }
            }

            res.json({cursos: rows});
        } else {
            res.json({cursos: []});
        }
        
    });
});

app.post('/buscaCurso', async(req,res) => {
    con.query("SELECT * FROM curso WHERE titulo LIKE ?",([req.body.filtroBusca]+'%'), (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {
            res.json({cursos: rows});
        } else {
            console.log("nada");
            res.json({cursos: []});
        }
    });    
});

app.get('/eventos', async(req,res) => {

    con.query('SELECT * FROM evento', (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {

            for(let i=0;true;i++){
                if(rows[i]==undefined)
                    break
                else {
                    rows[i].logo = base64_encode(rows[i].logo)
                    // copiarArquivo(rows[i].logo,'evento/evento'+ rows[i].id + '.png');
                }
            }

            res.json({eventos: rows});
        } else {
            res.json({eventos: []});
        }
        
    });
});

app.post('/buscaEvento', async(req,res) => {
    console.log(req.body.filtroBusca)
    con.query("SELECT * FROM evento WHERE titulo LIKE ?",([req.body.filtroBusca]+'%'), (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {
            console.log(rows);
            res.json({eventos: rows});
        } else {
            console.log("nada");
            res.json({eventos: []});
        }
    });    
});

app.get('/jogos', async(req,res) => {

    con.query('SELECT * FROM jogo', (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {

            for(let i=0;true;i++){
                if(rows[i]==undefined)
                    break
                else {
                    rows[i].logo = base64_encode(rows[i].logo)
                    // copiarArquivo(rows[i].logo,'jogo/jogo'+ rows[i].id + '.png');
                }
            }
            res.json({jogos: rows});
        } else {
            res.json({jogos: []});
        }
        
    });
});

app.post('/buscaJogo', async(req,res) => {
    con.query("SELECT * FROM jogo WHERE titulo LIKE ?",([req.body.filtroBusca]+'%'), (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {
            res.json({jogos: rows});
        } else {
            console.log("nada");
            res.json({jogos: []});
        }
    });    
});

app.get('/videoaulas', async(req,res) => {

    con.query('SELECT * FROM videoaula', (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {

            for(let i=0;true;i++){
                if(rows[i]==undefined)
                    break
                else {
                    rows[i].logo = base64_encode(rows[i].logo)
                    // copiarArquivo(rows[i].logo,'videoaula/videoaula'+ rows[i].id + '.png');
                }
            }

            res.json({videoaulas: rows});
        } else {
            res.json({videoaulas: []});
        }
        
    });
});

app.post('/buscaVideoaula', async(req,res) => {
    con.query("SELECT * FROM videoaula WHERE titulo LIKE ?",([req.body.filtroBusca]+'%'), (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {
            res.json({videoaulas: rows});
        } else {
            console.log("nada");
            res.json({videoaulas: []});
        }
    });    
});

app.get('/vagas', async(req,res) => {

    con.query('SELECT * FROM vaga', (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {

            for(let i=0;true;i++){
                if(rows[i]==undefined)
                    break
                else {
                    rows[i].logo = base64_encode(rows[i].logo)
                    // copiarArquivo(rows[i].logo,'vaga/vaga'+ rows[i].id + '.png');
                }
            }

            res.json({vagas: rows});
        } else {
            res.json({vagas: []});
        }
        
    });
});

app.post('/buscaVaga', async(req,res) => {
    con.query("SELECT * FROM vaga WHERE titulo LIKE ?",([req.body.filtroBusca]+'%'), (err, rows) => {
        if (err) throw err

        if(rows[0] != undefined) {
            res.json({vagas: rows});
        } else {
            console.log("nada");
            res.json({vagas: []});
        }
    });    
});

app.post('/alteraSenha', async(req,res) => {
    con.query('SELECT * FROM associado  WHERE id = ?', idUser, (err, rows) => {
        if (err) throw err
    
        if(rows[0] != undefined) {
            let senhaHash = sha256(req.body.senhaUser)
            let senhaBD = rows[0].senha_hash;
            if(senhaBD == senhaHash) {
                console.log('Pode alterar senha');
                let novaSenha = sha256(req.body.novaSenhaUser);

                con.query('UPDATE associado SET senha_hash = ? where id = ?', [novaSenha,idUser], (err, rows) => {
                    if (err) throw err

                    console.log('Senha alterada com sucesso');
                    res.json({alteraSenha: 0});
                });
                
            } else {
                console.log('Senha incorreta');
                res.json({alteraSenha: 1});
            }    
        } else {
            console.log('Este usuário não existe');
            res.json({alteraSenha: 1});
        }   
    })
});

app.listen(port, (req,res) => {
    console.log('Servidor rodando');
});

// con.end((err) => {
//     if(err) {
//         console.log('Erro to finish connection...', err)
//         return 
//     }
//     console.log('The connection was finish...')
// })
