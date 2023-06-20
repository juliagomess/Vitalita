import { StyleSheet } from "react-native";

export default styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#FFF",
    rowGap: 20,
    width:330
  },

  label: {
    fontSize: 12.5,
  },
  input: {
    borderRadius: 10,
    borderWidth: 1,
    borderColor: "grey",
    padding: 7,
    height: 52,
    
  },

  save: {
    backgroundColor: "orange",
    padding: 8,
    borderRadius: 8,
    width: "30%",
  },

  viewInput:{
  },

  textAlterar: {
    color: "#FFF",
    textAlign: "center",
    fontSize:16
  },

  viewButtons: {
    flexDirection: "row",
    columnGap: 10,
    marginTop: 40,
    justifyContent: "space-between",
  },
  Title: {
    fontSize: 25,
    color: "orange",
    fontWeight: "bold",
    textAlign:"center"
  },
  passwordArea:{
    flexDirection:"row",
    borderWidth: 1,
    borderColor: "grey",
    height: 52,
    padding:5,
    borderRadius: 10,
    alignItems: "center",
  },
  formPassword: {
    width: "88%",
  },
 
});
