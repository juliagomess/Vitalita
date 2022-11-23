// ignore_for_file: non_constant_identifier_names, prefer_const_constructors, must_call_super, sized_box_for_whitespace, camel_case_types, prefer_const_constructors_in_immutables, use_key_in_widget_constructors, avoid_unnecessary_containers, prefer_final_fields

import 'dart:convert';
import 'dart:developer';
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:vitalitaapp/mysql.dart';
import 'package:crypto/crypto.dart';
import 'package:youtube_player_flutter/youtube_player_flutter.dart';

// classe para recebe informação de associado
class Associado {
  final int ID;
  final String foto;
  final String nome;
  final bool pcd;

  const Associado({
    required this.ID,
    required this.foto,
    required this.nome,
    required this.pcd,
  });
}

// classe para receber informação de cursos, eventos, jogos, vagas de emprego e videoaulas
class Dados {
  final String logo;
  final String titulo;
  final String URL;
  final DateTime data_exp;
  final String descricao;

  const Dados({
    required this.logo,
    required this.titulo,
    required this.URL,
    required this.data_exp,
    required this.descricao,
  });
}

// class para receber informação de currículo
class Curriculo {
  final String instituicao;
  final String cursoExtra;
  final String empresaTrabalhada;
  final String cargoOcupado;
  final String laudo;

  const Curriculo({
    required this.instituicao,
    required this.cursoExtra,
    required this.empresaTrabalhada,
    required this.cargoOcupado,
    this.laudo = '',
  });
}

late Associado associado;
bool logged = false;

// abre URL no browser
_launchURLBrowser(url) async {
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}

void main() {
  runApp(MaterialApp(
    home: Login(),
  ));
}

double space = 15;
Color maincolor = Color(0xFF25623F);
Color buttonColor = Color(0xFF17a2b8);
TextStyle txtButtonStyle = TextStyle(color: buttonColor, fontSize: 16);
ButtonStyle smallButtonStyle = ButtonStyle(
    backgroundColor: MaterialStateProperty.all<Color>(maincolor),
    shape: MaterialStateProperty.all<RoundedRectangleBorder>(
        RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(18.0),
            side: BorderSide(color: Colors.white))));

// tela de login
class Login extends StatefulWidget {
  const Login({Key? key}) : super(key: key);

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final email = TextEditingController();
  final senha = TextEditingController();

  String warn = "";
  Widget _body = Container();
  @override
  void initState() {
    setState(() {
      _body = mainbody();
    });
  }

  Widget mainbody() {
    return Scaffold(
      body: SingleChildScrollView(
        physics: ClampingScrollPhysics(),
        padding: EdgeInsets.symmetric(vertical: 40, horizontal: 20),
        child: ConstrainedBox(
          constraints: BoxConstraints(
            minWidth: 100,
            minHeight: 100,
          ),
          child: IntrinsicHeight(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisSize: MainAxisSize.max,
              children: [
                Expanded(
                    flex: 4,
                    child: Image(
                        image: AssetImage('assets/logo.png'))), //logo do app
                Expanded(
                    flex: 1,
                    child: Container(
                        width: 500,
                        padding: EdgeInsets.all(15),
                        color: maincolor,
                        child: Text("Login",
                            textAlign: TextAlign.center,
                            style: TextStyle(
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                                color: Colors.white)))),
                SizedBox(
                  height: 20,
                ),
                Expanded(
                  flex: 1,
                  child: TextField(
                    controller: email,
                    decoration:
                        InputDecoration(labelText: "e-mail"), //input de email
                  ),
                ),
                SizedBox(
                  height: 15,
                ),
                Expanded(
                  flex: 1,
                  child: TextField(
                    controller: senha,
                    decoration:
                        InputDecoration(labelText: "senha"), //input de senha
                    obscureText: true,
                  ),
                ),
                Expanded(
                    flex: 1,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        TextButton(
                          onPressed: () => showDialog<String>(
                            context: context,
                            builder: (BuildContext context) => AlertDialog(
                              title: const Text(
                                  'Recuperar acesso'), // botão e pop-up de esqueci a senha
                              content: const Text(
                                  'Para recuperar sua conta, basta contatar um admnistrador'),
                              actions: <Widget>[
                                TextButton(
                                  onPressed: () => Navigator.pop(context, 'OK'),
                                  child: const Text('OK'),
                                ),
                              ],
                            ),
                          ),
                          child: Text(
                            "esqueci a senha",
                            style: txtButtonStyle,
                          ),
                        ),
                        TextButton(
                          onPressed: () => showDialog<String>(
                            context: context,
                            builder: (BuildContext context) => AlertDialog(
                              //botão e pop-up de não tenho conta
                              title: const Text('Criar conta'),
                              content: const Text(
                                  'O acesso só é permitido a associados e colaboradores, se deseja acesso contate um orgão responsável'),
                              actions: <Widget>[
                                TextButton(
                                  onPressed: () {
                                    _launchURLBrowser(
                                        'https://www.extcomp.com/');
                                    Navigator.pop(context, 'Contato');
                                  },
                                  child: const Text('Contato'),
                                ),
                                TextButton(
                                  onPressed: () => Navigator.pop(context, 'OK'),
                                  child: const Text('OK'),
                                ),
                              ],
                            ),
                          ),
                          child: Text(
                            "não tenho conta",
                            style: txtButtonStyle,
                          ),
                        )
                      ],
                    )),
                Expanded(
                    flex: 1,
                    child: Container(
                      height: 8,
                      child: ElevatedButton(
                        //botão de login
                        style: smallButtonStyle,
                        onPressed: () {
                          if (email.text != '' && senha.text != '')
                            logintry();
                          else {
                            showDialog<String>(
                              context: context,
                              builder: (BuildContext context) => AlertDialog(
                                title: const Text('campos vazios'),
                                content: const Text('Preencha todos os campos'),
                                actions: <Widget>[
                                  TextButton(
                                    onPressed: () =>
                                        Navigator.pop(context, 'OK'),
                                    child: const Text('OK'),
                                  ),
                                ],
                              ),
                            );
                          }
                        },
                        child: Text("entrar",
                            style: TextStyle(
                                fontSize: 24,
                                fontWeight: FontWeight.bold,
                                color: Colors.white)),
                      ),
                    ))
              ],
            ),
          ),
        ),
      ),
    );
  }

  void logintry() {
    // função de login
    var db = mysql();
    final senha_hash = sha256.convert(utf8.encode(senha.text));
    db.getConnection().then((conn) {
      conn.query(
          'select id, nome, foto, pcd from associado where email = ? and senha_hash = ?',
          [email.text, senha_hash.toString()]).then((results) {
        if (results.isNotEmpty) {
          bool spec;
          if (results.first[3] == 0)
            spec = false;
          else
            spec = true;

          associado = Associado(
              ID: results.first[0],
              nome: results.first[1],
              foto: results.first[2],
              pcd: spec);
          logged = true;
          Navigator.of(context).popUntil((route) => route.isFirst);
          Navigator.pushReplacement(context,
              MaterialPageRoute(builder: (BuildContext context) => Home()));
        } else {
          showDialog<String>(
            context: context,
            builder: (BuildContext context) => AlertDialog(
              title: const Text('usuário não encontrado'),
              content: const Text('Preencha corretamente os campos abaixo'),
              actions: <Widget>[
                TextButton(
                  onPressed: () => Navigator.pop(context, 'OK'),
                  child: const Text('OK'),
                ),
              ],
            ),
          );
        }
        conn.close();
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }
}

// tela principal, cada botão pra uma tela (falta videoaula e curriculo)
class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    void logoff() {
      // função de logoff
      associado = const Associado(ID: -1, foto: '', nome: '', pcd: false);
      logged = false;
      Navigator.of(context).popUntil((route) => route.isFirst);
      Navigator.pushReplacement(context,
          MaterialPageRoute(builder: (BuildContext context) => Login()));
    }

    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        leading: TextButton(
          child: Text(
            "sair",
            style: txtButtonStyle,
          ),
          onPressed: () => showDialog<String>(
            context: context,
            builder: (BuildContext context) => AlertDialog(
              // botão de logoff
              title: const Text('Desconectar'),
              content: const Text('Tem certeza que deseja desconectar?'),
              actions: <Widget>[
                TextButton(
                  onPressed: () => logoff(),
                  child: const Text('Sim'),
                ),
                TextButton(
                  onPressed: () => Navigator.pop(context, 'OK'),
                  child: const Text('Não'),
                ),
              ],
            ),
          ),
        ),
        title: Text('Vitalita: Aluno'),
        centerTitle: true,
      ),
      body: ListView(
        padding: EdgeInsets.all(12),
        children: [
          Container(
            height: 100,
            child: ElevatedButton(
              //botão para a tela de cursos
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(maincolor),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                      RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18.0),
                          side: BorderSide(color: Colors.black)))),
              onPressed: () => Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const cursospage())),
              child: Text(
                'CURSOS',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                ),
              ),
            ),
          ),
          SizedBox(height: space),
          Container(
            height: 100,
            child: ElevatedButton(
              //botão para a tela de eventos
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(maincolor),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                      RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18.0),
                          side: BorderSide(color: Colors.black)))),
              onPressed: () => Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const eventospage())),
              child: Text(
                'EVENTOS',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                ),
              ),
            ),
          ),
          SizedBox(height: space),
          Container(
            height: 100,
            child: ElevatedButton(
              //botão para a tela de jogos
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(maincolor),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                      RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18.0),
                          side: BorderSide(color: Colors.black)))),
              onPressed: () => Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const jogospage())),
              child: Text(
                'JOGOS',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                ),
              ),
            ),
          ),
          SizedBox(height: space),
          Container(
            height: 100,
            child: ElevatedButton(
              //botão para a tela de vagas de emprego
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(maincolor),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                      RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18.0),
                          side: BorderSide(color: Colors.black)))),
              onPressed: () => Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const vagaspage())),
              child: Text(
                'VAGAS DE EMPREGO',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                ),
              ),
            ),
          ),
          SizedBox(height: space),
          Container(
            height: 100,
            child: ElevatedButton(
              //botão para a tela de videoaulas
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(maincolor),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                      RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18.0),
                          side: BorderSide(color: Colors.black)))),
              onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => const videoaulaspage())),
              child: Text(
                'VIDEOAULAS',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                ),
              ),
            ),
          ),
          SizedBox(height: space),
          Container(
            height: 100,
            child: ElevatedButton(
              //botão para a tela de curriculo
              style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(maincolor),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                      RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18.0),
                          side: BorderSide(color: Colors.black)))),
              onPressed: () => Navigator.push(context,
                  MaterialPageRoute(builder: (context) => const curriculo())),
              child: Text(
                'CURRÍCULO',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 35,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

//tela de curriculo
class curriculo extends StatefulWidget {
  const curriculo({Key? key}) : super(key: key);

  @override
  State<curriculo> createState() => _curriculoState();
}

class _curriculoState extends State<curriculo> {
  final inst = TextEditingController();
  final cursos = TextEditingController();
  final empresas = TextEditingController();
  final cargos = TextEditingController();

  var db = mysql();
  Widget buttons = Container();
  late Curriculo curriculo;
  bool canEdit = false;
  bool resumeCreated = false;
  bool specialNeeds = false;

  Widget _body = CircularProgressIndicator();

  //deletar curriculo
  deleteResume() async {
    await db.getConnection().then((conn) {
      conn.query('delete from curriculo where associado_id = ?',
          [associado.ID]).then((value) {
        conn.close();
        inst.text = '';
        cursos.text = '';
        empresas.text = '';
        cargos.text = '';
        resumeCreated = false;
        setState(() {
          canEdit = false;
          buttons = startEditting();
          _body = mainCurriculo();
        });
      });
    });
  }

  //salvar/atualizar curriculo
  handleResume() async {
    await db.getConnection().then((conn) {
      String sql;
      log(resumeCreated.toString());
      if (resumeCreated) {
        log("curriculo atualizado");
        sql =
            'update curriculo set instituicao_ensino = ?, curso_extra = ?, empresa_trabalhada = ?, cargo_ocupado = ? where associado_id = ?';
      } else {
        log("novo curriculo");
        sql =
            'insert into curriculo (instituicao_ensino, curso_extra,empresa_trabalhada,cargo_ocupado, associado_id) values (?,?,?,?,?)';
      }
      conn.query(sql, [
        curriculo.instituicao,
        curriculo.cursoExtra,
        curriculo.empresaTrabalhada,
        curriculo.cargoOcupado,
        associado.ID
      ]).then((value) => conn.close());
    });
  }

  //botão para começar a editar
  Widget startEditting() {
    return Container(
      alignment: Alignment.center,
      child: ElevatedButton(
        style: smallButtonStyle,
        onPressed: (() => setState(() {
              canEdit = true;
              buttons = finishEditting();
              _body = mainCurriculo();
            })),
        child: Text("Editar"),
      ),
    );
  }

  //botões para terminar de editar
  Widget finishEditting() {
    return Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
      ElevatedButton(
        //salvar
        style: smallButtonStyle,
        onPressed: (() {
          if (inst.text != '' &&
              cursos.text != '' &&
              empresas.text != '' &&
              cargos.text != '') {
            curriculo = Curriculo(
                instituicao: inst.text,
                cursoExtra: cursos.text,
                empresaTrabalhada: empresas.text,
                cargoOcupado: cargos.text);
            handleResume().then((value) {
              resumeCreated = true;
              showDialog<String>(
                //popup q curriculo foi salvo
                context: context,
                builder: (BuildContext context) => AlertDialog(
                  title: const Text('Currículo registrado'),
                  content: const Text('Currículo registrado com sucesso!'),
                  actions: <Widget>[
                    TextButton(
                      onPressed: () => Navigator.pop(context, 'ok'),
                      child: const Text('OK'),
                    ),
                  ],
                ),
              );
              setState(() {
                canEdit = false;
                buttons = startEditting();
                _body = mainCurriculo();
              });
            });
          } else {
            showDialog<String>(
              //popup q curriculo foi salvo
              context: context,
              builder: (BuildContext context) => AlertDialog(
                title: const Text('Campos vazios '),
                content: const Text('Preencha todos os campos'),
                actions: <Widget>[
                  TextButton(
                    onPressed: () => Navigator.pop(context, 'ok'),
                    child: const Text('OK'),
                  ),
                ],
              ),
            );
          }
        }),
        child: Text("Salvar"),
      ),
      ElevatedButton(
        //deletar
        style: smallButtonStyle,
        onPressed: (() {
          if (resumeCreated) //check if can delete
          {
            //popup de confirmação
            showDialog<String>(
              context: context,
              builder: (BuildContext context) => AlertDialog(
                title: const Text('Deletar currículo'),
                content:
                    const Text('Tem certeza que deseja deletar seu currículo?'),
                actions: <Widget>[
                  TextButton(
                    onPressed: () {
                      Navigator.pop(context, 'não');
                      deleteResume();
                    },
                    child: const Text('Sim'),
                  ),
                  TextButton(
                    onPressed: () => Navigator.pop(context, 'não'),
                    child: const Text('Não'),
                  ),
                ],
              ),
            );
          } else {
            showDialog<String>(
              context: context,
              builder: (BuildContext context) => AlertDialog(
                title: const Text('Currículo não encontrado'),
                content: const Text('Não há currículo registrado nessa conta'),
                actions: <Widget>[
                  TextButton(
                    onPressed: () => Navigator.pop(context, 'ok'),
                    child: const Text('OK'),
                  ),
                ],
              ),
            ); // pop up nothing to delete
          }
        }),
        child: Text("Deletar"),
      ),
      ElevatedButton(
        //cancelar
        style: smallButtonStyle,
        onPressed: (() {
          showDialog<String>(
            //popup de confirmação
            context: context,
            builder: (BuildContext context) => AlertDialog(
              title: const Text('Cancelar'),
              content: const Text(
                  'Tem certeza que deseja cancelar? Suas alterações não serão salvas'),
              actions: <Widget>[
                TextButton(
                  onPressed: () {
                    if (resumeCreated) //revert to clear or old data if resume exists
                    {
                      inst.text = curriculo.instituicao;
                      cursos.text = curriculo.cursoExtra;
                      empresas.text = curriculo.empresaTrabalhada;
                      cargos.text = curriculo.cargoOcupado;
                    } else {
                      inst.text = '';
                      cursos.text = '';
                      empresas.text = '';
                      cargos.text = '';
                    }

                    setState(() {
                      canEdit = false;
                      buttons = startEditting();
                      _body = mainCurriculo();
                    });
                    Navigator.pop(context, 'sim');
                  },
                  child: const Text('Sim'),
                ),
                TextButton(
                    onPressed: () => Navigator.pop(context, 'Não'),
                    child: const Text('Não'))
              ],
            ),
          );
        }),
        child: Text("Cancelar"),
      )
    ]);
  }

  @override
  void initState() {
    specialNeeds = associado.pcd;
    //checar se curriculo existe
    db.getConnection().then((conn) {
      conn.query(
          'select instituicao_ensino, curso_extra, empresa_trabalhada, cargo_ocupado from curriculo where associado_id = ?',
          [associado.ID.toString()]).then((results) {
        if (results.isNotEmpty) {
          //se existe
          var x = results.first;
          resumeCreated = true;
          curriculo = Curriculo(
              instituicao: x[0],
              cursoExtra: x[1],
              empresaTrabalhada: x[2],
              cargoOcupado: x[3]);
          setState(() {
            inst.text = curriculo.instituicao;
            cursos.text = curriculo.cursoExtra;
            empresas.text = curriculo.empresaTrabalhada;
            cargos.text = curriculo.cargoOcupado;
            canEdit = false;
            buttons = startEditting();
            _body = mainCurriculo();
          });
        } else {
          //se não existe
          resumeCreated = false;
          setState(() {
            canEdit = true;
            buttons = finishEditting();
            _body = mainCurriculo();
          });
        }
        conn.close();
      });
    });
  }

  Widget mainCurriculo() {
    return Scaffold(
        appBar: AppBar(backgroundColor: maincolor, title: Text("Curriculo")),
        body: SingleChildScrollView(
          padding: EdgeInsets.symmetric(vertical: 20, horizontal: 20),
          child: ConstrainedBox(
            constraints: BoxConstraints(
              minWidth: 100,
              minHeight: 100,
            ),
            child: IntrinsicHeight(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                mainAxisSize: MainAxisSize.max,
                children: [
                  Expanded(
                      flex: 1,
                      child: Container(
                        alignment: Alignment.center,
                        color: maincolor,
                        child: const Text("Preencha os campos:",
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 30,
                            )),
                      )),
                  Expanded(
                    //instituições
                    flex: 3,
                    child: TextField(
                      controller: inst,
                      enabled: canEdit,
                      decoration:
                          InputDecoration(labelText: "instituições de ensino"),
                    ),
                  ),
                  Expanded(
                    //cursos
                    flex: 3,
                    child: TextField(
                      controller: cursos,
                      enabled: canEdit,
                      decoration: InputDecoration(labelText: "Cursos extras"),
                    ),
                  ),
                  Expanded(
                    //empresas
                    flex: 3,
                    child: TextField(
                      controller: empresas,
                      enabled: canEdit,
                      decoration:
                          InputDecoration(labelText: "empresas trabalhadas"),
                    ),
                  ),
                  Expanded(
                    //cargos
                    flex: 3,
                    child: TextField(
                      controller: cargos,
                      enabled: canEdit,
                      decoration: InputDecoration(labelText: "cargos ocupados"),
                    ),
                  ),
                  Expanded(flex: 3, child: buttons) //botões
                ],
              ),
            ),
          ),
        ));
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }
}

// tela da lista dos cursos
class cursospage extends StatefulWidget {
  const cursospage({Key? key}) : super(key: key);

  @override
  State<cursospage> createState() => _cursospageState();
}

class _cursospageState extends State<cursospage> {
  Widget _body = CircularProgressIndicator();

  @override
  void initState() {
    LoadCursos();
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }

  LoadCursos() {
    //busca cursos no bd
    List<Dados> dados = [];
    var db = mysql();
    db.getConnection().then((conn) {
      conn
          .query('select logo, titulo, url,  data_exp, descricao from curso')
          .then((results) {
        for (var x in results) {
          dados.add(Dados(
              logo: x[0],
              titulo: x[1],
              URL: x[2],
              data_exp: x[3],
              descricao: x[4].toString()));
          print(x[0]);
        }
        conn.close();
        setState(() => _body = maincursos(dados));
      });
    });
  }

  Widget maincursos(List<Dados> dados) {
    //monta os cursos na lista
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text('Vitalita: Cursos'),
        centerTitle: true,
      ),
      body: ListView(
        padding: EdgeInsets.all(12),
        children: DadosWidget(context, dados, "Curso"),
      ),
    );
  }
}

// tela da lista dos eventos
class eventospage extends StatefulWidget {
  const eventospage({Key? key}) : super(key: key);

  @override
  State<eventospage> createState() => _eventospageState();
}

class _eventospageState extends State<eventospage> {
  Widget _body = CircularProgressIndicator();

  @override
  void initState() {
    LoadEventos();
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }

  LoadEventos() {
    //busca eventos no bd
    List<Dados> dados = [];
    var db = mysql();
    db.getConnection().then((conn) {
      conn
          .query('select logo, titulo, url,  data_exp, descricao from evento')
          .then((results) {
        for (var x in results) {
          dados.add(Dados(
              logo: x[0],
              titulo: x[1],
              URL: x[2],
              data_exp: x[3],
              descricao: x[4].toString()));
          print(x[0]);
        }
        conn.close();
        setState(() => _body = maineventos(dados));
      });
    });
  }

  Widget maineventos(List<Dados> dados) {
    //monta eventos na lista
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text('Vitalita: Eventos'),
        centerTitle: true,
      ),
      body: ListView(
        padding: EdgeInsets.all(12),
        children: DadosWidget(context, dados, "Evento"),
      ),
    );
  }
}

// tela da lista das vagas
class vagaspage extends StatefulWidget {
  const vagaspage({Key? key}) : super(key: key);

  @override
  State<vagaspage> createState() => _vagaspageState();
}

class _vagaspageState extends State<vagaspage> {
  Widget _body = CircularProgressIndicator();

  @override
  void initState() {
    Loadvagas();
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }

  Loadvagas() {
    //busca vagas no bd
    List<Dados> dados = [];
    var db = mysql();
    db.getConnection().then((conn) {
      conn
          .query('select logo, titulo, url,  data_exp, descricao from vaga')
          .then((results) {
        for (var x in results) {
          dados.add(Dados(
              logo: x[0],
              titulo: x[1],
              URL: x[2],
              data_exp: x[3],
              descricao: x[4].toString()));
          print(x[0]);
        }
        conn.close();
        setState(() => _body = mainvagas(dados));
      });
    });
  }

  Widget mainvagas(List<Dados> dados) {
    //monta vagas na lista
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text('Vitalita: vagas'),
        centerTitle: true,
      ),
      body: ListView(
        padding: EdgeInsets.all(12),
        children: DadosWidget(context, dados, "Vaga"),
      ),
    );
  }
}

// tela da lista dos jogos
class jogospage extends StatefulWidget {
  const jogospage({Key? key}) : super(key: key);

  @override
  State<jogospage> createState() => _jogospageState();
}

class _jogospageState extends State<jogospage> {
  Widget _body = CircularProgressIndicator();

  @override
  void initState() {
    Loadjogos();
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }

  Loadjogos() {
    //busca jogos no bd
    List<Dados> dados = [];
    var db = mysql();
    db.getConnection().then((conn) {
      conn
          .query('select logo, titulo, url, descricao from jogo')
          .then((results) {
        for (var x in results) {
          dados.add(Dados(
              logo: x[0],
              titulo: x[1],
              URL: x[2],
              data_exp: DateTime(0, 0, 0),
              descricao: x[3].toString()));
          print(x[0]);
        }
        conn.close();
        setState(() => _body = mainjogos(dados));
      });
    });
  }

  Widget mainjogos(List<Dados> dados) {
    //monta jogos na lista
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text('Vitalita: jogos'),
        centerTitle: true,
      ),
      body: ListView(
        padding: EdgeInsets.all(12),
        children: jogosDadosWidget(context, dados),
      ),
    );
  }
}

// tela da lista de videoaulas
class videoaulaspage extends StatefulWidget {
  const videoaulaspage({Key? key}) : super(key: key);

  @override
  State<videoaulaspage> createState() => _videoaulaspageState();
}

class _videoaulaspageState extends State<videoaulaspage> {
  Widget _body = CircularProgressIndicator();

  @override
  void initState() {
    Loadvideoaulas();
  }

  @override
  Widget build(BuildContext context) {
    return _body;
  }

  Loadvideoaulas() {
    //busca videoaulas no bd
    List<Dados> dados = [];
    var db = mysql();
    db.getConnection().then((conn) {
      conn
          .query('select logo, titulo, url, descricao from videoaula')
          .then((results) {
        for (var x in results) {
          dados.add(Dados(
              logo: x[0],
              titulo: x[1],
              URL: x[2],
              data_exp: DateTime(0, 0, 0),
              descricao: x[3].toString()));
          print(x[0]);
        }
        conn.close();
        setState(() => _body = mainvideoaulas(dados));
      });
    });
  }

  Widget mainvideoaulas(List<Dados> dados) {
    //monta videoaulas na lista
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text('Vitalita: videoaulas'),
        centerTitle: true,
      ),
      body: ListView(
        padding: EdgeInsets.all(12),
        children: videoDadosWidget(context, dados),
      ),
    );
  }
}

// monta a lista de dados (cursos, eventos, e vagas)
List<Widget> DadosWidget(BuildContext context, List<Dados> dados, String tipo) {
  List<Widget> cursos = [];
  for (int I = 0; I < dados.length; I++) {
    cursos.add(
      Container(
          color: maincolor,
          height: 200,
          child: Column(
            children: [
              Expanded(
                  //logo
                  flex: 5,
                  child: Image.network(
                      "http://10.0.2.2:8000/extcomp/associado/media/" +
                          dados[I].logo,
                      loadingBuilder: (context, child, loadingProgress) {
                    if (loadingProgress == null) return child;
                    return const SizedBox(
                        height: 100,
                        width: 100,
                        child: Center(child: CircularProgressIndicator()));
                  }, errorBuilder: (context, exception, stackTrace) {
                    return Column(
                      children: const [
                        Expanded(
                            flex: 5,
                            child: Image(
                              image: AssetImage("assets/placeholder.png"),
                            )),
                        Expanded(
                            flex: 1,
                            child: Text("imagem não disponível",
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 12,
                                )))
                      ],
                    );
                  })),
              Expanded(
                  //titulo
                  flex: 2,
                  child: Center(
                      child: Text(
                    dados[I].titulo,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 30,
                    ),
                  ))),
              Expanded(
                  //botão para acessar
                  flex: 2,
                  child: Container(
                    width: 200,
                    child: ElevatedButton(
                      style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all<Color>(buttonColor),
                          shape:
                              MaterialStateProperty.all<RoundedRectangleBorder>(
                                  RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10.0),
                          ))),
                      onPressed: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => DadosPage(dados[I], tipo))),
                      child: Text(
                        "Acessar",
                        style: TextStyle(
                          fontSize: 25,
                        ),
                      ),
                    ),
                  )),
            ],
          )),
    );
    cursos.add(SizedBox(height: space));
  }
  return cursos;
}

// monta a lista de jogos
List<Widget> jogosDadosWidget(BuildContext context, List<Dados> dados) {
  List<Widget> cursos = [];
  for (int I = 0; I < dados.length; I++) {
    cursos.add(
      Container(
          color: maincolor,
          height: 200,
          child: Column(
            children: [
              Expanded(
                  //logo
                  flex: 5,
                  child: Image.network(
                      "http://10.0.2.2:8000/extcomp/associado/media/" +
                          dados[I].logo,
                      loadingBuilder: (context, child, loadingProgress) {
                    if (loadingProgress == null) return child;
                    return const SizedBox(
                        height: 100,
                        width: 100,
                        child: Center(child: CircularProgressIndicator()));
                  }, errorBuilder: (context, exception, stackTrace) {
                    return Column(
                      children: const [
                        Expanded(
                            flex: 5,
                            child: Image(
                              image: AssetImage("assets/placeholder.png"),
                            )),
                        Expanded(
                            flex: 1,
                            child: Text("imagem não disponível",
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 12,
                                )))
                      ],
                    );
                  })),
              Expanded(
                  //titulo
                  flex: 2,
                  child: Center(
                      child: Text(
                    dados[I].titulo,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 30,
                    ),
                  ))),
              Expanded(
                  //botão para acessar
                  flex: 2,
                  child: Container(
                    width: 200,
                    child: ElevatedButton(
                      style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all<Color>(buttonColor),
                          shape:
                              MaterialStateProperty.all<RoundedRectangleBorder>(
                                  RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10.0),
                          ))),
                      onPressed: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => jogoDadosPage(dados[I]))),
                      child: Text(
                        "Acessar",
                        style: TextStyle(
                          fontSize: 25,
                        ),
                      ),
                    ),
                  )),
            ],
          )),
    );
    cursos.add(SizedBox(height: space));
  }
  return cursos;
}

// monta a lista de videoaulas
List<Widget> videoDadosWidget(BuildContext context, List<Dados> dados) {
  List<Widget> cursos = [];
  for (int I = 0; I < dados.length; I++) {
    cursos.add(
      Container(
          color: maincolor,
          height: 200,
          child: Column(
            children: [
              Expanded(
                  //logo
                  flex: 5,
                  child: Image.network(
                      "http://10.0.2.2:8000/extcomp/associado/media/" +
                          dados[I].logo,
                      loadingBuilder: (context, child, loadingProgress) {
                    if (loadingProgress == null) return child;
                    return const SizedBox(
                        height: 100,
                        width: 100,
                        child: Center(child: CircularProgressIndicator()));
                  }, errorBuilder: (context, exception, stackTrace) {
                    return Column(
                      children: const [
                        Expanded(
                            flex: 5,
                            child: Image(
                              image: AssetImage("assets/placeholder.png"),
                            )),
                        Expanded(
                            flex: 1,
                            child: Text("imagem não disponível",
                                style: TextStyle(
                                  color: Colors.black,
                                  fontSize: 12,
                                )))
                      ],
                    );
                  })),
              Expanded(
                  //titulo
                  flex: 2,
                  child: Center(
                      child: Text(
                    dados[I].titulo,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 30,
                    ),
                  ))),
              Expanded(
                  //botão para acessar
                  flex: 2,
                  child: Container(
                    width: 200,
                    child: ElevatedButton(
                      style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all<Color>(buttonColor),
                          shape:
                              MaterialStateProperty.all<RoundedRectangleBorder>(
                                  RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10.0),
                          ))),
                      onPressed: () => Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => videoaulaPage(dados[I]))),
                      child: const Text(
                        "Acessar",
                        style: TextStyle(
                          fontSize: 25,
                        ),
                      ),
                    ),
                  )),
            ],
          )),
    );
    cursos.add(SizedBox(height: space));
  }
  return cursos;
}

// tela pra curso, evento ou vaga individual
class DadosPage extends StatelessWidget {
  DadosPage(this.c, this.tipo);

  final Dados c;
  final String tipo;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text(tipo + ": " + c.titulo),
        centerTitle: true,
      ),
      body: Center(
          child: Column(children: [
        Expanded(
            //logo
            flex: 4,
            child: Image.network(
                "http://10.0.2.2:8000/extcomp/associado/media/" + c.logo,
                loadingBuilder: (context, child, loadingProgress) {
              if (loadingProgress == null) return child;
              return const SizedBox(
                  height: 100,
                  width: 100,
                  child: Center(child: CircularProgressIndicator()));
            }, errorBuilder: (context, exception, stackTrace) {
              return Column(
                children: const [
                  Expanded(
                      flex: 5,
                      child: Image(
                        image: AssetImage("assets/placeholder.png"),
                      )),
                  Expanded(
                      flex: 1,
                      child: Text("imagem não disponível",
                          style: TextStyle(
                            color: Colors.black,
                            fontSize: 12,
                          )))
                ],
              );
            })),
        Expanded(
          flex: 6,
          child: Container(
            child: Column(children: [
              Expanded(
                  //titulo
                  flex: 1,
                  child: Container(
                    color: maincolor,
                    alignment: Alignment.center,
                    child: Text(
                      c.titulo,
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 36,
                      ),
                    ),
                  )),
              Expanded(
                  //descrição
                  flex: 5,
                  child: SingleChildScrollView(
                      padding: EdgeInsets.symmetric(horizontal: 2.0),
                      child: Text(
                        c.descricao,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 25,
                        ),
                      ))),
              Expanded(
                  // data de expiração
                  flex: 1,
                  child: Container(
                      color: maincolor,
                      alignment: Alignment.center,
                      child: Text(
                        "Data de expiração: " +
                            c.data_exp.day.toString() +
                            "/" +
                            c.data_exp.month.toString() +
                            "/" +
                            c.data_exp.year.toString(),
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 22,
                        ),
                      ))),
            ]),
          ),
        ),
        Expanded(
            //botão para abrir url
            flex: 2,
            child: Container(
              padding: EdgeInsets.all(10),
              child: ElevatedButton(
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all<Color>(buttonColor),
                    shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                        RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(18.0),
                            side: BorderSide(color: Colors.white)))),
                onPressed: () => _launchURLBrowser(c.URL),
                child: Text(
                  "Entrar",
                  style: TextStyle(
                    fontSize: 30,
                  ),
                ),
              ),
            ))
      ])),
    );
  }
}

// tela pra jogo individual
class jogoDadosPage extends StatelessWidget {
  jogoDadosPage(this.c);

  final Dados c;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text("Jogo: " + c.titulo),
        centerTitle: true,
      ),
      body: Center(
          child: Column(children: [
        Expanded(
            //logo
            flex: 4,
            child: Image.network(
                "http://10.0.2.2:8000/extcomp/associado/media/" + c.logo,
                loadingBuilder: (context, child, loadingProgress) {
              if (loadingProgress == null) return child;
              return const SizedBox(
                  height: 100,
                  width: 100,
                  child: Center(child: CircularProgressIndicator()));
            }, errorBuilder: (context, exception, stackTrace) {
              return Column(
                children: const [
                  Expanded(
                      flex: 5,
                      child: Image(
                        image: AssetImage("assets/placeholder.png"),
                      )),
                  Expanded(
                      flex: 1,
                      child: Text("imagem não disponível",
                          style: TextStyle(
                            color: Colors.black,
                            fontSize: 12,
                          )))
                ],
              );
            })),
        Expanded(
          flex: 6,
          child: Container(
            child: Column(children: [
              Expanded(
                  //titulo
                  flex: 1,
                  child: Container(
                    color: maincolor,
                    alignment: Alignment.center,
                    child: Text(
                      c.titulo,
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 36,
                      ),
                    ),
                  )),
              Expanded(
                  // descrição
                  flex: 5,
                  child: SingleChildScrollView(
                      padding: EdgeInsets.symmetric(horizontal: 2.0),
                      child: Text(
                        c.descricao,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 25,
                        ),
                      ))),
            ]),
          ),
        ),
        Expanded(
            //botão para abrir url
            flex: 2,
            child: Container(
              padding: EdgeInsets.all(10),
              child: ElevatedButton(
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all<Color>(buttonColor),
                    shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                        RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(18.0),
                            side: BorderSide(color: Colors.white)))),
                onPressed: () => _launchURLBrowser(c.URL),
                child: Text(
                  "Entrar",
                  style: TextStyle(
                    fontSize: 30,
                  ),
                ),
              ),
            ))
      ])),
    );
  }
}

//tela para videoaula individual
class videoaulaPage extends StatefulWidget {
  videoaulaPage(this.c);

  final Dados c;

  @override
  State<videoaulaPage> createState() => _videoaulaPageState(c);
}

class _videoaulaPageState extends State<videoaulaPage> {
  _videoaulaPageState(this.c);

  final Dados c;

  Widget player = CircularProgressIndicator();

  //variaveis do player de vídeo (ainda não entendi 100%)
  late YoutubePlayerController _controller;
  late TextEditingController _idController;
  late TextEditingController _seekToController;
  late PlayerState _playerState;
  late YoutubeMetaData _videoMetaData;
  double _volume = 100;
  bool _muted = false;
  bool _isPlayerReady = false;

  //transforma url para ID
  String getVideoID(String url) {
    url = url.replaceAll("https://www.youtube.com/watch?v=", "");
    url = url.replaceAll("https://m.youtube.com/watch?v=", "");
    return url;
  }

  @override
  void initState() {
    super.initState();
    //controlador do player
    _controller = YoutubePlayerController(
      initialVideoId: getVideoID(c.URL),
      flags: const YoutubePlayerFlags(
        mute: false,
        autoPlay: true,
        disableDragSeek: false,
        loop: false,
        isLive: false,
        forceHD: false,
        enableCaption: true,
      ),
    )..addListener(listener);
    _idController = TextEditingController();
    _seekToController = TextEditingController();
    _videoMetaData = const YoutubeMetaData();
    _playerState = PlayerState.unknown;
  }

// ainda não entendi 100% oq listener, deactivate e dispose fazem
  void listener() {
    if (_isPlayerReady && mounted && !_controller.value.isFullScreen) {
      setState(() {
        _playerState = _controller.value.playerState;
        _videoMetaData = _controller.metadata;
      });
    }
  }

  @override
  void deactivate() {
    _controller.pause();
    super.deactivate();
  }

  @override
  void dispose() {
    _controller.dispose();
    _idController.dispose();
    _seekToController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return page();
  }

  Widget page() {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: maincolor,
        title: Text("Videoaula: " + c.titulo),
        centerTitle: true,
      ),
      body: Center(
          child: Column(children: [
        Expanded(
            // logo
            flex: 4,
            child: Image.network(
                "http://10.0.2.2:8000/extcomp/associado/media/" + c.logo,
                loadingBuilder: (context, child, loadingProgress) {
              if (loadingProgress == null) return child;
              return const SizedBox(
                  height: 100,
                  width: 100,
                  child: Center(child: CircularProgressIndicator()));
            }, errorBuilder: (context, exception, stackTrace) {
              return Column(
                children: const [
                  Expanded(
                      flex: 5,
                      child: Image(
                        image: AssetImage("assets/placeholder.png"),
                      )),
                  Expanded(
                      flex: 1,
                      child: Text("imagem não disponível",
                          style: TextStyle(
                            color: Colors.black,
                            fontSize: 12,
                          )))
                ],
              );
            })),
        Expanded(
          flex: 7,
          child: Container(
            child: Column(children: [
              Expanded(
                  //titulo
                  flex: 1,
                  child: Container(
                    color: maincolor,
                    alignment: Alignment.center,
                    child: Text(
                      c.titulo,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 36,
                      ),
                    ),
                  )),
              Expanded(
                  //player de video
                  flex: 6,
                  child: YoutubePlayer(
                    controller: _controller,
                    showVideoProgressIndicator: true,
                    progressIndicatorColor: maincolor,
                  )),
              Expanded(
                  //descrição
                  flex: 2,
                  child: SingleChildScrollView(
                      padding: EdgeInsets.symmetric(horizontal: 2.0),
                      child: Text(
                        c.descricao,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 25,
                        ),
                      ))),
            ]),
          ),
        ),
        Expanded(
            //botão para acessar url
            flex: 1,
            child: Container(
              padding: EdgeInsets.all(10),
              child: ElevatedButton(
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all<Color>(buttonColor),
                    shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                        RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ))),
                onPressed: () => _launchURLBrowser(c.URL),
                child: Text(
                  "Abrir no browser",
                  style: TextStyle(
                    fontSize: 26,
                  ),
                ),
              ),
            ))
      ])),
    );
  }
}
