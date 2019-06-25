package com.example.appmotorista

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_notification.*

class NotificationActivity : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_notification)

//        buttonRotaSelecionada.setOnClickListener { buttonRotaSelecionadaClick() }
        buttonIniciaRota.setOnClickListener { buttonRotaClick() }

    }

    private fun buttonRotaSelecionadaClick() {
        //tvPontoFinal.text = etPontoFinal.text.toString()
    }

    private fun buttonRotaClick() {

        val nomeIda = etNomeIda.text.toString()
        val nomeVolta = etNomeVolta.text.toString()

        val intent = Intent(this,RotaIniciada::class.java)
        intent.putExtra("nomeIda", nomeIda)
        intent.putExtra("nomeVolta", nomeVolta)
        intent.putExtra("nomeAtual", nomeIda)
        startActivity(intent)
    }
}