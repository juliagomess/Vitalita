import { StyleSheet, Text, View } from "react-native";
import Title from "../components/Title";
import FormAlterarSenha from "../components/AlterarSenha";
import HeaderNavegacao from "../components/HeaderNavigacao";

export default function Login() {
  return (
    <View style={styles.container}>

      <HeaderNavegacao back="Home"/>
      <FormAlterarSenha />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    marginTop: 30,
    backgroundColor: "#FFF",
  },
});
