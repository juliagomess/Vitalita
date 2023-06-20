import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  ScrollView,
} from "react-native";
import AvisoSemConteudo from "../components/SemConteudo";
import HeaderNavigacao from "../components/HeaderNavigacao";
import AcessoSecao from "../components/AcessarSecao";
import { useEffect, useState } from "react";
import config from "../../config/config.json";
import stylesFilter from "../components/InputDeFiltro/style";
import Icons from "react-native-vector-icons/FontAwesome";

export default function Jogos() {
  const [allJogos, setAllJogos] = useState([]);
  const [filtro, setFiltro] = useState("");

  useEffect(() => {
    fetch(config.urlRootNode + "jogos")
      .then((res) => res.json())
      .then((json) => setAllJogos(json.jogos));
  }, []);

  async function busca() {
    let req = await fetch(config.urlRootNode + "buscaJogo", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        filtroBusca: filtro,
      }),
    })
      .then((res) => res.json())
      .then((data) => setAllJogos(data.jogos));
  }

  return (
    <View style={styles.container}>
      <HeaderNavigacao back="Home" />
      <View style={stylesFilter.FilterArea}>
        <TextInput
          style={stylesFilter.formFilter}
          placeholder="Faça uma pesquisa"
          onChangeText={(text) => setFiltro(text)}
        />
        <TouchableOpacity onPress={busca}>
          <Icons name="search" size={25} color="orange" />
        </TouchableOpacity>
      </View>

      {allJogos.length > 0 ? (
        <ScrollView style={styles.scroll}>
          <View style={styles.contentArea}>
            {allJogos.map((item) => (
              <AcessoSecao
                titulo={item.titulo}
                url={item.url}
                descricao={item.descricao}
                dataExp={item.data_exp}
                back="Jogos"
                img={item.logo}
              />
            ))}
          </View>
        </ScrollView>
      ) : (
        <AvisoSemConteudo text="jogos" />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#FFF",
    alignItems: "center",
    justifyContent: "flex-start",
    marginTop: 30,
  },
  contentArea: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "95%",
    flexWrap: "wrap",
  },
  scroll: {
    width: "100%",
    marginLeft: 15,
  },
});
