import { StyleSheet, Text, View } from "react-native";
import Title from "../components/Title";
import Form from "../components/Formulario";

export default function Login() {
  return (
    <View style={styles.container}>
      <Title />
      <Form />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "flex-start",
  },
});
