// ignore_for_file: camel_case_types

import 'package:mysql1/mysql1.dart';

//settings do mysql
//10.0.2.2 é o host do emulador
class mysql {
  static String host = '10.0.2.2', user = 'root', db = 'db_extcomp';
  static int port = 3306;
  mysql();
  //estabelecer a conexão
  Future<MySqlConnection> getConnection() async {
    var settings =
        ConnectionSettings(host: host, port: port, user: user, db: db);
    return await MySqlConnection.connect(settings);
  }
}
