import { StyleSheet, Text, View, TextInput, TouchableOpacity,ScrollView } from "react-native";
import AvisoSemConteudo from "../components/SemConteudo";
import HeaderNavigacao from "../components/HeaderNavigacao"; 
import AcessoSecao from "../components/AcessarSecao";
import { useEffect, useState } from "react";
import config from "../../config/config.json";
import stylesFilter from "../components/InputDeFiltro/style"
import Icons from "react-native-vector-icons/FontAwesome";


export default function Videoaulas() {
  const [allVideoaulas, setAllVideoaulas] = useState(fetch(config.urlRootNode + "videoaulas")
  .then((res) => res.json())
   .then((json) =>{
   setAllVideoaulas(json.videoaulas)}));
  const [filtro, setFiltro] = useState("");



 async function busca() {
  let req = await fetch(config.urlRootNode + "buscaVideoaula", {
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
    .then((data) => setAllVideoaulas(data.videoaulas));
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
          <Icons name="search" size={25} color="orange"/>
          </TouchableOpacity>
        </View>
        
        {
         allVideoaulas.length > 0 ? (
          <ScrollView style={styles.scroll}>
           <View style={styles.contentArea}> 
         {   allVideoaulas.map(item => (
              <AcessoSecao titulo={item.titulo} url={item.url} descricao={item.descricao} dataExp={item.data_exp}  back="VideoAulas" img={item.logo}/>
           ))}
       </View>
       </ScrollView>
       )   :   <AvisoSemConteudo text="videoaulas" />
       }
  
    
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
  }, contentArea: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "95%",
    flexWrap: "wrap",
  
  },
  scroll:{
    width:"100%",
    marginLeft:15
  }
});
