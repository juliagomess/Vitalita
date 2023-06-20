import {
  StyleSheet,
  Text,
  TextInput,
  View,
  Button,
  TouchableOpacity,
} from "react-native";
import { CheckBox } from "react-native-btr";
import React, { useState, useEffect } from "react";
import config from "../../../config/config.json";
import Icons from "react-native-vector-icons/FontAwesome";
import { useNavigation } from "@react-navigation/native";
import { CommonActions } from "@react-navigation/native";
import ButtonEsqueciSenha from "../ButtonEsqueciSenha";
import styles from "./style";

export default function App() {
  const navigation = useNavigation(); //vai fazer a navegação funcionar
  const [email, setEmail] = useState(null);
  const [senha, setSenha] = useState(null);
  const [hidePassword, setHidePassoword] = useState(true);
  const [data, setData] = useState(null);

  const handlePressLogin = ()=>{
    loginUser();
  };

  async function loginUser() {
    let req = await fetch(config.urlRootNode + "login", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        emailUser: email,
        senhaUser: senha,
      }),
    })
      .then((res) => res.json())
      .then((data) => setData(data.login));
  }

  if (data == 0) {
    setEmail("");
    setSenha("");
    setData(null);
    navigation.dispatch(
      CommonActions.navigate({
        name: "Home",
      })
    );
  } else if(data == 1) {
    setData(null);
    alert("Senha incorreta!");
  } else if(data == 2) {
    setData(null);
    alert("Esse email não foi cadastrado!");
  }

  return (
    <View style={styles.formContainer}>
      <View style={styles.form}>
        <Text style={styles.formLabel}>Email</Text>
        <TextInput
          style={styles.formInput}
          placeholder="Preencha este campo com o seu e-mail"
          value={email}
          onChangeText={(text) => setEmail(text)}
        />
        <Text style={styles.formLabel}>Senha</Text>
        <View style={styles.passwordArea}>
          <TextInput
            style={styles.formPassword}
            placeholder="Preencha este campo com a sua senha"
            value={senha}
            onChangeText={(text) => setSenha(text)}
            secureTextEntry={hidePassword}
          />
          <TouchableOpacity
            onPress={() => {
              setHidePassoword(!hidePassword);
            }}
            style={styles.eyeIcon}
          >
            {hidePassword ? (
              <Icons name="eye" color="#000" size={25} />
            ) : (
              <Icons name="eye-slash" color="#000" size={25} />
            )}
          </TouchableOpacity>
        </View>

        {/* <Text style={styles.noShare}>
          Não compartilhe este campo com ninguém
        </Text> */}
        {/* <Text style={styles.semConta}>
          Sem conta? Entre em contato com o órgão responsável
        </Text> */}

        <View style={styles.containerEsqueciSenha}>
          {/* <TouchableOpacity style={styles.esqueciSenha} screen="Forget">Esqueci minha senha!</TouchableOpacity> */}
          {/* <Forget /> */}
          <ButtonEsqueciSenha screen="EsqueciSenha"></ButtonEsqueciSenha>
        </View>
        <Button title="Entrar" color="#FFA500" onPress={handlePressLogin} />
      </View>
    </View>
  );
}
