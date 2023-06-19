import { StyleSheet, Text, View, Button, TouchableOpacity } from "react-native";
import React, { useState, useEffect } from "react";
import Icons from "react-native-vector-icons/FontAwesome";
import { useNavigation } from "@react-navigation/native";
import { CommonActions } from "@react-navigation/native";
import styles from "./style";

export default function App(props) {
  const navigation = useNavigation(); //vai fazer a navegação funcionar

  return (
    <TouchableOpacity
      onPress={() => {
        navigation.navigate(props.screen);
      }}
    >
      <Text style={styles.esqueciSenha}>Esqueci minha senha!</Text>
    </TouchableOpacity>
  );
}
