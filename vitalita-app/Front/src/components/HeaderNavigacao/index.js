import { StyleSheet, Text, TouchableOpacity, View } from "react-native";
import styles from "./style";
import Icons from "react-native-vector-icons/FontAwesome";
import { useNavigation } from "@react-navigation/native";
import { useEffect, useState } from "react";

export default function HeaderNavigacao(props) {
  const navigation = useNavigation(); //vai fazer a navegação funcionar
  const [dropdownOpen, setDropdownOpen] = useState(false); //dropdownMenu


  return (
    <View style={styles.navigationContainer}>
      <TouchableOpacity
        onPress={() => {
          navigation.navigate(props.back);
        }}
      >
        <Icons
          style={styles.btnNav}
          name="chevron-left"
          size={35}
          color="orange"
        />
      </TouchableOpacity> 
      <TouchableOpacity
      style={styles.btnNav}
      >
        <Icons
          style={styles.btnNavUser}
          name="user-circle"
          size={35}
          color="orange"
        />
        
      </TouchableOpacity>
    </View>
  );
}
