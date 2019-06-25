package com.example.appmotorista

import android.os.Bundle
import android.os.PersistableBundle
import android.support.v7.app.AppCompatActivity
import android.util.Log
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
        val complemento = "motorista"
        val latitude = etLatitude.text.toString()
        val longitude = etLongitude.text.toString()
        val latiSaida = "29"
        val longiSaida = "50"
        val latiDestino = "32"
        val longiDestino = "51"
        val localizacao = buttonLocalizacaoMudou.text.toString()
        val username = "primeiro"//intent.extras.getString("username")

        val nomeIda = intent.getStringExtra("nomeIda")
        val nomeVolta = intent.getStringExtra("nomeVolta")
        val nomeAtual = intent.getStringExtra("nomeAtual")

        Executors.newSingleThreadExecutor().execute(){

            //URL ANTIGA: /localizacao/motorista/<usernameApp>/<latitude>/<longitude>

            ///localizacao/motorista/<usernameApp>/<latitude>/<longitude>/<latiSaida>/<longiSaida>/<latiDestino>/<longiDestino>/
            // <nomeIda>/<nomeVolta>/<nomeAtual>
            val json = URL("${baseUrl}${localizacao}${barra}${complemento}${barra}${username}${barra}${latitude}${barra}${longitude}${barra}" +
                    "${latiSaida}${barra}${longiSaida}${barra}${latiDestino}${barra}${longiDestino}${barra}${nomeIda}${barra}${nomeVolta}${barra}${nomeAtual}").readText()
            val resp = JSONObject(json)
            val resultado = listOf(resp.get("result")) //resp

            tvResposta.text = resultado.get(0).toString()

            if (resultado.get(0).toString() == "Usuario esperando no ponto")
            {
                Log.i("HOLA",resultado.get(0).toString() )
//                tvResposta.text = resultado.get(0).toString()

            }
        }

    }
}