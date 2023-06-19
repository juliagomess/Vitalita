import {
  View,
  Text,
  StyleSheet,
  TextInput,
  Button,
  TouchableOpacity,
} from "react-native";
import React, { useState, useEffect } from "react";
import config from "../../../config/config.json";
import styles from "./style";
import Modal from 'react-native-modal';
import ModalSalvar from "../ModalSalvar";
import { useNavigation } from "@react-navigation/native";

export default function App() {
  const [instituicao, setInstituicao] = useState("");
  const [empresas, setEmpresas] = useState("");
  const [cursos, setCursos] = useState("");
  const [cargos, setCargos] = useState("");
  const [data, setData] = useState(null);
  const navigation = useNavigation(); 

  useEffect(() => {
    fetch(config.urlRootNode + "curriculo")
      .then((res) => res.json())
      .then((json) => setInstituicao(json.instituicao));
    fetch(config.urlRootNode + "curriculo")
      .then((res) => res.json())
      .then((json) => setEmpresas(json.empresas));
    fetch(config.urlRootNode + "curriculo")
      .then((res) => res.json())
      .then((json) => setCursos(json.cursos));
    fetch(config.urlRootNode + "curriculo")
      .then((res) => res.json())
      .then((json) => setCargos(json.cargos));
  }, []);

  const handlePressSave = ()=>{
    if(instituicao == "" && empresas == "" && cursos == "" && cargos == "") {
      alert("Não é possível salvar um currículo vazio")
    } else {
      createCV();
      alert("Currículo Salvo!");
    }
  };

  const handlePressDelete = ()=>{
    eraseCV();
    setInstituicao("");
    setCargos("");
    setCursos("");
    setEmpresas("");
    alert("Currículo Apagado!");
  };

  async function createCV() {
    let req = await fetch(config.urlRootNode + "create", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        instituicaoUser: instituicao,
        empresasUser: empresas,
        cursosUser: cursos,
        cargosUser: cargos,
      }),
    });
  }

  async function eraseCV() {
    fetch(config.urlRootNode + "delete");
  }

  return (
    <View style={styles.container}>

      <Text style={styles.Title}>Currículo</Text>

      <View>
        <Text style={styles.label}>Instituição de Ensino</Text>
        <TextInput
          style={styles.input}
          placeholder="Digite o nome da sua instituição de ensino"
          onChangeText={setInstituicao}
          value={instituicao}
        />
      </View>

      <View>
        <Text style={styles.label}>Empresas Trabalhadas</Text>
        <TextInput
          style={styles.input}
          placeholder="Digite o nome das empresas em que trabalhou"
          onChangeText={setEmpresas}
          value={empresas}

        />
      </View>

      <View>
        <Text style={styles.label}>Cursos Extras</Text>
        <TextInput
          style={styles.input}
          placeholder="Digite o nome dos cursos extras que fez"
          onChangeText={setCursos}
          value={cursos}

        />
      </View>

      <View>
        <Text style={styles.label}>Cargos Ocupados</Text>
        <TextInput
          style={styles.input}
          placeholder="Digite os cargos que ocupou"
          onChangeText={setCargos}
          value={cargos}

        />
      </View>

      <View style={styles.viewButtons}>
       

        <TouchableOpacity style={styles.delete} onPress={handlePressDelete}>
          <Text style={styles.textDelete}>Deletar</Text>
        </TouchableOpacity>


        <TouchableOpacity style={styles.save} onPress={handlePressSave}>
          <Text style={styles.textSave}>Salvar</Text>
        </TouchableOpacity>
    
      </View>
    </View>
  );
}
