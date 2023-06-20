import { StyleSheet, Text, View } from "react-native";
import Icons from "react-native-vector-icons/FontAwesome";
import styles from "./style";

export default function App(props) {
  return (
    <View style={styles.Container}>
      <Text style={styles.title}>Aviso</Text>
      <Icons name="close" size={100} color={"#FA0303"} />
      <Text style={styles.subTitulo}>
        Ainda não existem {props.text} disponíveis
      </Text>
    </View>
  );
}
