package com.example.appusuario

import android.os.Bundle
import android.os.PersistableBundle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import com.example.appmotorista.R
import kotlinx.android.synthetic.main.activity_notification.*
import kotlinx.android.synthetic.main.activity_rotainiciada.*
import org.json.JSONObject
import java.net.URL
import java.util.concurrent.Executors

class RotaIniciada : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_rotainiciada)

        buttonLocalizacaoMudou.setOnClickListener { buttonLocalizacaoMudouClick() }

    }

    private fun buttonLocalizacaoMudouClick() {
        sendData()
    }

    private fun sendData() {

        val baseUrl = "http://muriloceolin.pythonanywhere.com/"
        val barra = "/"
        val complemento = "usuario"
        val latitude = etLatitude.text.toString()
        val longitude = etLongitude.text.toString()
        val onibus = etOnibus.text.toString()
        val localizacao = buttonLocalizacaoMudou.text.toString()
        val username = "segundo"//intent.extras.getString("username")

        Executors.newSingleThreadExecutor().execute(){

            val json = URL("${baseUrl}${localizacao}${barra}${complemento}${barra}${username}${barra}${latitude}${barra}${longitude}${barra}${onibus}").readText()
            val resp = JSONObject(json)
            val resultado = listOf(resp.get("resp")) //resp

            tvResposta.text = resultado.get(0).toString()
//            if (resultado.get(0).toString() == "Usuario aguardando no ponto")
//            {
//                Log.i("HOLA",resultado.get(0).toString() )
//                tvResposta.text = resultado.get(0).toString()
//
//            }
////            else if(resultado.get(0).toString() == "Usuarios Juntos")
////            {
////                //Limpa da Lista
////                Log.i("HOLA","Usuarios caminhando juntos")
////            }
//            else
//            {
//                //Adiciona na lista
//                Log.i("HOLA",resultado.get(0).toString())
//                tvResposta.text = resultado.get(0).toString()
//            }


        }

    }
}