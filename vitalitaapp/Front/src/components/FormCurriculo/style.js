import { StyleSheet } from "react-native";

export default styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#FFF",
    rowGap: 20,
    marginTop: 20,
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
  Title: {
    fontSize: 25,
    color: "orange",
    fontWeight: "bold",
    textAlign:"center"
  },

  save: {
    backgroundColor: "#09E020",
    padding: 8,
    borderRadius: 8,
    width: "40%",
  },

  delete: {
    backgroundColor: "#FA0303",
    borderRadius: 8,
    width: "40%",
    padding: 8,
  },


  textDelete: {
    color: "#FFF",
    textAlign: "center",
    fontSize:16
  },

  textSave: {
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
});
