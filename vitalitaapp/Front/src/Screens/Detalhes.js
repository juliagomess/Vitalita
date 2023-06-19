import { FlatList, StyleSheet, Text, View, TextInput, TouchableOpacity,ScrollView,Image, Button, Linking } from "react-native";
import Icons from "react-native-vector-icons/FontAwesome";
import { useEffect, useState } from "react";
import config from "../../config/config.json";
import { useNavigation } from "@react-navigation/native";
import HeaderNavigacao from "../components/HeaderNavigacao";
import style from "../components/SemConteudo/style";

export default function Detalhes(props) {
  
  const base64Image = 'data:image/jpeg;base64,' + props.route.params.img

  const handlePress = () => {
    Linking.openURL(props.route.params.url);
  };

  return (
    <View style={styles.container}>
      
    <HeaderNavigacao back={props.route.params.back}></HeaderNavigacao>
    <Image style={styles.imagemDetalhes} source={{uri:base64Image}} />
    <Text style={styles.textoDetalhes}>{props.route.params.titulo}</Text>
    <Text style={styles.textoDetalhes}>{props.route.params.descricao}</Text>

    <TouchableOpacity style={styles.botaoDetalhes} onPress={handlePress}>
      <Text style={styles.textoBotao}>Acessar</Text>      
    </TouchableOpacity>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#FFF",
    marginTop: 30,
    justifyContent: "flex-start",
    alignItems: "center",
  },
  textoDetalhes: {
    marginTop: 20,
    padding: 10,
    gap: 10,
    color: "black",
    fontWeight: "bold",
    justifyContent: "center",
    textAlign: "center",
  },
  
  imagemDetalhes: {
    height: "30%",
    width: "58%", 
  },

  botaoDetalhes: {
    justifyContent: "center",
    alignItems: "center",
    marginTop: 10,
    borderRadius: 20,
    backgroundColor: "orange",
    width: "55%",
  },

  textoBotao: {
    padding: 18,
    color: "#fff",
    fontWeight: "bold",
    fontSize: 18,
  },
});
