import { StyleSheet, Text, View, Button, TouchableOpacity } from "react-native";
import { CheckBox } from "react-native-btr";
import React, { useState, useEffect } from "react";
import Icons from "react-native-vector-icons/FontAwesome";
import { useNavigation } from "@react-navigation/native";
import { CommonActions } from "@react-navigation/native";
import styles from "./style";

export default function App(props) {
  const navigation = useNavigation(); //vai fazer a navegação funcionar

  return (
    <TouchableOpacity
      style={styles.containerHome}
      onPress={() => {
        navigation.navigate(props.screen);
      }}
    >
      <Icons name={props.icon} size={60} color={"#FFF"} />
      <Text style={styles.text}>{props.text}</Text>
    </TouchableOpacity>
  );
}
