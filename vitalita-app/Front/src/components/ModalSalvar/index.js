import React, {useState} from 'react'
import {View, Text, Button, Modal, Stylesheet} from 'react-native'
import styles from "./style";

export default function(){

    const [visivel,setVisivel] = useState(false)

    // const mudaState = ()  =>{
    //     setVisivel(!visivel);
    // };

    return(
        <View style={styles.modalContainer}>

            <Modal 
            transparent={true}
            visible={true}
           >

             <View>
                <Text style={styles.textoModalSalvar}>Currículo salvo!</Text>
                <Button style={styles.botaoModalSalvar}
                title="Fechar">
                 onPress={()=>
                 {setVisivel(false)}}   
                </Button>
             </View>   

            </Modal>

        </View>
    );

}