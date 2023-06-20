import {
  View,
  Text,
  StyleSheet,
  TextInput,
  Button,
  TouchableOpacity,
} from "react-native";
import React, { useState, useEffect } from "react";
import styles from "./style";

//import config from "../../config/config.json";

export default function () {
  const [emailCadastrado, setEmailCadastrado] = useState("");
  const [novaSenha, setNovaSenha] = useState("");
  const [confirmaSenha, setConfirmaSenha] = useState("");

  // async function changePassword() {
  //     let req = await fetch(config.urlRootNode + "change", {
  //       method: "POST",
  //       headers: {
  //         "Accept": "application/json",
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({
  //         email: emailCadastrado,
  //         newPassword: novaSenha,
  //         confirmPassword: confirmaSenha,
  //       }),
  //     });
  //   }
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Esqueci minha senha</Text>

      <View>
        <Text style={styles.label}>E-mail</Text>
        <TextInput
          style={styles.input}
          placeholder="Digite seu e-mail já cadastrado"
          onChangeText={setEmailCadastrado}
          value={emailCadastrado}
        />
      </View>

      <View>
        <Text style={styles.label}>Nova senha</Text>
        <TextInput
          style={styles.input}
          placeholder="Digite sua nova senha"
          // onChangeText={setNovaSenha}
          value={novaSenha}
        />
      </View>

      <View>
        <Text style={styles.label}>Confirme a nova senha</Text>
        <TextInput
          style={styles.input}
          placeholder="Confirme sua senha"
          // onChangeText={setConfirmaSenha}
          value={confirmaSenha}
        />
      </View>

      <View style={styles.viewButtons}>
        <TouchableOpacity style={styles.alterar}>
          <Text style={styles.textAlterar}>Alterar senha</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}
