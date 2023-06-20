import { StyleSheet, Text, View } from "react-native";
import Title from "./src/components/Title";
import Form from "./src/components/Formulario";
import CadastroCurriculo from "./src/Screens/CadastroCurriculo";
import { NavigationContainer, StackRouter } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Cursos from "./src/Screens/Cursos";
import Login from "./src/Screens/Login";
import Home from "./src/Screens/Home";
import Eventos from "./src/Screens/Eventos";
import Jogos from "./src/Screens/Jogos";
import Vagas from "./src/Screens/Vagas";
import VideoAulas from "./src/Screens/Videoaulas";
import EsqueciSenha from "./src/Screens/EsqueciSenha";
import Detalhes from "./src/Screens/Detalhes";
import AlterarSenha from "./src/Screens/AlterarSenha";
const stack = createNativeStackNavigator();

function MyStack() {
  return (
    <stack.Navigator>
      <stack.Screen
        name="Login"
        component={Login}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="EsqueciSenha"
        component={EsqueciSenha}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="Home"
        component={Home}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="CadastroCurriculo"
        component={CadastroCurriculo}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="Cursos"
        component={Cursos}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="Eventos"
        component={Eventos}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="Jogos"
        component={Jogos}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="Vagas"
        component={Vagas}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="VideoAulas"
        component={VideoAulas}
        options={{ headerShown: false }}
      />
       <stack.Screen
        name="Detalhes"
        component={Detalhes}
        options={{ headerShown: false }}
      />
      <stack.Screen
        name="AlterarSenha"
        component={AlterarSenha}
        options={{ headerShown: false }}
      />



    </stack.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <MyStack />
    </NavigationContainer>
  );
}
