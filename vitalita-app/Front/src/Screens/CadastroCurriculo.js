import { StyleSheet, Text, View } from "react-native";
import FormCurriculo from "../components/FormCurriculo";
import HeaderNavigacao from "../components/HeaderNavigacao";

export default function CadastroCurriculo() {
  return (
    <View style={styles.container}>
      <HeaderNavigacao back="Home"></HeaderNavigacao>
      <FormCurriculo />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "flex-start",
    marginTop: 30,
  },
});
