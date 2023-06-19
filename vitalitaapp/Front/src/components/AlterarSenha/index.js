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
  import Icons from "react-native-vector-icons/FontAwesome";
  import ModalSalvar from "../ModalSalvar";
  import { useNavigation } from "@react-navigation/native";
  
  export default function App() {
   
  const [senhaAtual, setSenhaAtual] = useState("");
  const [novaSenha, setNovaSenha] = useState("");
  const [confirmaSenha, setConfirmaSenha] = useState("");
  const [hidePassword, setHidePassoword] = useState(true);
  const [data, setData] = useState(null);
  const navigation = useNavigation(); 

    function handlePressPassword(){
        if(novaSenha == confirmaSenha) {
            if(novaSenha != senhaAtual) {
                UpdatePassword();
            } else {
                alert('Nova senha não pode ser igual a senha antiga!');
            }
        } else {
            alert('Senhas não são equivalentes!')
        }
    }

    async function UpdatePassword() {
        let req = await fetch(config.urlRootNode + "alteraSenha", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            senhaUser: senhaAtual,
            novaSenhaUser: novaSenha,
          }),
        })
        .then((res) => res.json())
        .then((data) => setData(data.alteraSenha));
      }

      if(data == 0) {
        setData(null)
        setSenhaAtual("");
        setNovaSenha("");
        setConfirmaSenha("");
        alert('Senha alterada com sucesso!');
      } else if(data == 1) {
        setData(null)
        alert('Senha incorreta');
      }

  
    return (
      <View style={styles.container}>


        <Text style={styles.Title}>Alterar Senha</Text>

        <View>
            <Text style={styles.label}>Senha atual</Text>
            <View style={styles.passwordArea}>
            
            <TextInput
              style={styles.formPassword}
              placeholder="Digite sua senha atual"
              value={senhaAtual}
              onChangeText={(text) => setSenhaAtual(text)}
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
        </View>
       
  
        <View>
            <Text style={styles.label}>Nova senha</Text>
            <View style={styles.passwordArea}>
            
            <TextInput
              style={styles.formPassword}
              placeholder="Digite uma nova senha"
              value={novaSenha}
              onChangeText={(text) => setNovaSenha(text)}
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
        </View>        
  
        <View>
            <Text style={styles.label}>Confirme sua senha</Text>
            <View style={styles.passwordArea}>
            
            <TextInput
              style={styles.formPassword}
              placeholder="Confirme sua nova senha"
              value={confirmaSenha}
              onChangeText={(text) => setConfirmaSenha(text)}
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
        </View>
  
  
        <View style={styles.viewButtons}>
  
          <TouchableOpacity style={styles.save} onPress={handlePressPassword} >
            <Text style={styles.textAlterar}>Alterar</Text>
          </TouchableOpacity>

        </View>
      </View>
    );
  }
  