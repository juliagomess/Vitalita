import { StyleSheet } from "react-native";

export default styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "flex-start",
    backgroundColor: "#FFF",
    paddingTop: 30,
    rowGap: 10,
  },

  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 16,
    textAlign: "center",
  },

  label: {
    fontSize: 12.5,
    marginTop: 16,
  },

  input: {
    borderRadius: 10,
    borderWidth: 1,
    borderColor: "grey",
    padding: 7,
    height: 52,
  },

  viewButtons: {
    flexDirection: "row",
    columnGap: 10,
    marginTop: 40,
    justifyContent: "flex-start",
  },

  alterar: {
    backgroundColor: "#09E020",
    padding: 8,
    borderRadius: 8,
    width: "30%",
  },

  textAlterar: {
    color: "#FFF",
    textAlign: "center",
  },
});
